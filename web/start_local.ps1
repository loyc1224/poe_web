param(
    [Parameter(Mandatory=$true)]
    [string]$ClientId,

    [string]$RedirectUri = "",

    [string]$BindHost = "127.0.0.1",

    [int]$Port = 5000
)

$ErrorActionPreference = "Stop"

Set-Location $PSScriptRoot

if ([string]::IsNullOrWhiteSpace($RedirectUri)) {
    $RedirectUri = "http://$BindHost`:$Port/callback"
}

$env:POE_TW_CLIENT_ID = $ClientId
$env:POE_TW_REDIRECT_URI = $RedirectUri

Write-Host "POE_TW_CLIENT_ID=$($env:POE_TW_CLIENT_ID)"
Write-Host "POE_TW_REDIRECT_URI=$($env:POE_TW_REDIRECT_URI)"
Write-Host "Starting Flask on $BindHost`:$Port ..."

python -c "from app import app; app.run(host='$BindHost', port=$Port, debug=True, threaded=True)"
