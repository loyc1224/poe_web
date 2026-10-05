param(
    [Parameter(Mandatory = $true)]
    [string]$BucketName,

    [Parameter(Mandatory = $true)]
    [string]$RuntimeServiceAccount,

    [string]$ProjectId = "udata-gcp-1",
    [string]$Region = "asia-east1",
    [string]$ServiceName = "poe-python-web",
    [string]$SchedulerJobName = "poe-tw-currency-refresh"
)

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

$bucketUri = "gs://$BucketName"
& gcloud config set project $ProjectId | Out-Null
if ($LASTEXITCODE -ne 0) { throw "無法設定 Google Cloud 專案" }

& gcloud services enable storage.googleapis.com cloudscheduler.googleapis.com --project $ProjectId
if ($LASTEXITCODE -ne 0) { throw "無法啟用 Cloud Storage / Cloud Scheduler API" }

& gcloud storage buckets describe $bucketUri --project $ProjectId *> $null
if ($LASTEXITCODE -ne 0) {
    & gcloud storage buckets create $bucketUri --project $ProjectId --location $Region --uniform-bucket-level-access
    if ($LASTEXITCODE -ne 0) { throw "建立 Cloud Storage bucket 失敗" }
}

& gcloud storage buckets add-iam-policy-binding $bucketUri --member "serviceAccount:$RuntimeServiceAccount" --role "roles/storage.objectUser" --project $ProjectId
if ($LASTEXITCODE -ne 0) { throw "無法授予 Cloud Run 服務帳號資料集存取權" }

$randomBytes = New-Object byte[] 32
[System.Security.Cryptography.RandomNumberGenerator]::Create().GetBytes($randomBytes)
$refreshToken = [Convert]::ToBase64String($randomBytes).TrimEnd('=').Replace('+', '-').Replace('/', '_')

& gcloud run services update $ServiceName --project $ProjectId --region $Region --service-account $RuntimeServiceAccount --update-env-vars "TW_CURRENCY_BUCKET=$BucketName,TW_CURRENCY_REFRESH_TOKEN=$refreshToken"
if ($LASTEXITCODE -ne 0) { throw "Cloud Run environment update failed" }

$urlFormat = "value(status.url)"
$serviceUrl = (& gcloud run services describe $ServiceName --project $ProjectId --region $Region "--format=$urlFormat").Trim()
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($serviceUrl)) { throw "無法取得 Cloud Run URL" }

$refreshUrl = "$serviceUrl/api/tw-pricer/refresh"
$schedulerArgs = @(
    "--project", $ProjectId,
    "--location", $Region,
    "--schedule", "15 * * * *",
    "--time-zone", "Asia/Taipei",
    "--uri", $refreshUrl,
    "--http-method", "POST",
    "--update-headers", "X-Refresh-Token=$refreshToken",
    "--attempt-deadline", "180s"
)

& gcloud scheduler jobs describe $SchedulerJobName --project $ProjectId --location $Region *> $null
if ($LASTEXITCODE -eq 0) {
    & gcloud scheduler jobs update http $SchedulerJobName @schedulerArgs
} else {
    & gcloud scheduler jobs create http $SchedulerJobName @schedulerArgs
}
if ($LASTEXITCODE -ne 0) { throw "建立或更新每小時行情排程失敗" }

$headers = @{ "X-Refresh-Token" = $refreshToken }
Invoke-RestMethod -Method Post -Uri $refreshUrl -Headers $headers -TimeoutSec 120 | Out-Null
Write-Host "Dataset initialized; Cloud Scheduler runs hourly."