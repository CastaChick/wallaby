echo 'SHEET_KEY=$SHEET_KEY' >> .env
echo 'API_TOKEN=$API_TOKEN' >> .env

mkdir env
touch env/account_key.json
echo '{
  "type": "$ACCOUNT_TYPE",
  "project_id": "$PROJECT_ID",
  "private_key_id": "$PRIVATE_KEY_ID",
  "private_key": "$PRIVATE_KEY",
  "client_email": "$CLIENT_EMAIL",
  "client_id": "$CLIENT_ID",
  "auth_uri": "$AUTH_URI",
  "token_uri": "$TOKEN_URI",
  "auth_provider_x509_cert_url": "$AUTH_PROVIDER",
  "client_x509_cert_url": "$CLIENT_URL"
}' >> env/account_key.json
