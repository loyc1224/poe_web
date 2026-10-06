param(
    [string]$ProjectId = "udata-gcp-1",
    [string]$Region = "asia-east1",
    [string]$ServiceName = "poe-python-web"
)

$ErrorActionPreference = "Stop"

Write-Host "=== Cloud Run Deploy ===" -ForegroundColor Cyan
Write-Host "Project: $ProjectId"
Write-Host "Region : $Region"
Write-Host "Service: $ServiceName"

Set-Location (Split-Path -Parent $PSScriptRoot)

python -m unittest discover -s tests -v
if ($LASTEXITCODE -ne 0) { throw "Site tests failed; deployment stopped." }

$validationReport = Join-Path $env:TEMP "poe-web-predeploy-validation.json"
python scripts/validate_site.py --report $validationReport
if ($LASTEXITCODE -ne 0) { throw "Browser feature validation failed; deployment stopped." }

$configuration = gcloud run services describe $ServiceName --region $Region --project $ProjectId --format=json | ConvertFrom-Json
if ($LASTEXITCODE -ne 0) { throw "Cannot inspect production configuration; deployment stopped." }
$configuredNames = @($configuration.spec.template.spec.containers[0].env | Where-Object {
  $_.value -or $_.valueFrom.secretKeyRef
} | ForEach-Object { $_.name })
if ($configuredNames -notcontains "STRATEGY_PASSWORD" -or
  ($configuredNames -notcontains "FLASK_SECRET_KEY" -and $configuredNames -notcontains "SECRET_KEY")) {
  throw "Production strategy password or stable session secret is missing; deployment stopped."
}

gcloud config set project $ProjectId | Out-Null
if ($LASTEXITCODE -ne 0) { throw "Cannot select Google Cloud project." }

gcloud run deploy $ServiceName `
  --source . `
  --region $Region `
  --project $ProjectId `
  --allow-unauthenticated `
  --platform managed `
  --port 8080
if ($LASTEXITCODE -ne 0) { throw "Cloud Run deployment failed." }

$serviceUrl = gcloud run services describe $ServiceName --region $Region --project $ProjectId --format "value(status.url)"
if ($LASTEXITCODE -ne 0) { throw "Cannot read deployed service URL." }
$readiness = Invoke-RestMethod "$serviceUrl/health/ready"
if ($readiness.status -ne "ok") { throw "Deployed service is not ready." }
python scripts/validate_site.py --base-url $serviceUrl --report (Join-Path $env:TEMP "poe-web-postdeploy-validation.json")
if ($LASTEXITCODE -ne 0) { throw "Deployment finished, but live feature verification failed." }
Write-Host "Deploy Success: $serviceUrl" -ForegroundColor Green
