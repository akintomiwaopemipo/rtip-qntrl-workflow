#!/usr/bin/env bash

set -e

# Load .env
set -a
source .env
set +a

AUTH_URL="https://accounts.zoho.com/oauth/v2/auth?scope=${QNTRL_SCOPE}&client_id=${QNTRL_CLIENT_ID}&response_type=code&access_type=offline&redirect_uri=${QNTRL_REDIRECT_URI}&prompt=consent"


echo ""
echo "Open this URL in browser:"
echo ""
echo "$AUTH_URL"
echo ""
echo "After approving, paste the 'code' parameter here:"
read -r AUTH_CODE

echo ""
echo "Requesting refresh token..."
echo ""

curl -sSX POST "https://accounts.zoho.com/oauth/v2/token" \
  -d "grant_type=authorization_code" \
  -d "client_id=${QNTRL_CLIENT_ID}" \
  -d "client_secret=${QNTRL_CLIENT_SECRET}" \
  -d "redirect_uri=${QNTRL_REDIRECT_URI}" \
  -d "code=${AUTH_CODE}" | python -m json.tool

echo ""