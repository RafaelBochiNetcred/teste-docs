#!/usr/bin/env bash
set -euo pipefail

mkdir -p openapi
python manage.py spectacular --file openapi/openapi.yaml --validate

if command -v redocly >/dev/null 2>&1; then
  redocly lint netcred@v1
else
  echo "OpenAPI gerado em openapi/openapi.yaml."
  echo "Instale as dependencias Node com 'npm install' para executar 'redocly lint' e 'redocly preview'."
fi
