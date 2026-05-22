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

Set-Location $PSScriptRoot

gcloud config set project $ProjectId | Out-Null

gcloud run deploy $ServiceName `
  --source . `
  --region $Region `
  --project $ProjectId `
  --allow-unauthenticated `
  --platform managed `
  --port 8080

$serviceUrl = gcloud run services describe $ServiceName --region $Region --project $ProjectId --format "value(status.url)"
Write-Host "Deploy Success: $serviceUrl" -ForegroundColor Green
