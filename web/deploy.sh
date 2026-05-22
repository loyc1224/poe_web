#!/bin/bash
set -e

PROJECT_ID="udata-gcp-1"
REGION="asia-east1"
SERVICE_NAME="poe-python-web"

echo "=== Cloud Run Deploy ==="
echo "Project: ${PROJECT_ID}"
echo "Region : ${REGION}"
echo "Service: ${SERVICE_NAME}"

cd "$(dirname "$0")"

gcloud config set project "${PROJECT_ID}"

gcloud run deploy "${SERVICE_NAME}" \
  --source . \
  --region "${REGION}" \
  --project "${PROJECT_ID}" \
  --allow-unauthenticated \
  --platform managed \
  --port 8080

gcloud run services describe "${SERVICE_NAME}" --region "${REGION}" --project "${PROJECT_ID}" --format='value(status.url)'
