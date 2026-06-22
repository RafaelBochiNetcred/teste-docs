# Redocly API Docs Example

Projeto de exemplo para documentar uma API Django REST Framework com:

- schema OpenAPI gerado por `drf-spectacular`;
- ReDoc em `/api/docs/`;
- Swagger UI em `/api/docs/swagger/`;
- portal Redocly com paginas Markdown e referencia OpenAPI;
- filtro para publicar no OpenAPI apenas actions marcadas com `@documented_endpoint` quando `DEBUG=False`.

## Como rodar a API

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

URLs principais:

- OpenAPI: `http://127.0.0.1:8000/api/schema/`
- ReDoc: `http://127.0.0.1:8000/api/docs/`
- Swagger UI: `http://127.0.0.1:8000/api/docs/swagger/`

## DEBUG e schema publico

Com `DEBUG=False`, o hook `webhooks.schema_hooks.only_documented_endpoints` remove do OpenAPI tudo que nao estiver marcado com `@documented_endpoint`.

Exemplo:

```python
@documented_endpoint
@extend_schema(**WEBHOOK_LIST_SCHEMA)
def list(self, request, *args, **kwargs):
    return super().list(request, *args, **kwargs)
```

Para ligar o modo debug:

```bash
DJANGO_DEBUG=True python manage.py runserver
```

No modo debug, o schema mostra todos os endpoints registrados. A rota auxiliar de empresas, `/api/companies/`, tambem fica disponivel apenas nesse modo.

## Como rodar o Redocly

```bash
cd redocly-docs
npm install
npm run docs:openapi
npm run docs:preview
```

Arquivos principais:

- `redocly-docs/redocly.yaml`: configuracao do portal.
- `redocly-docs/sidebars.yaml`: menu lateral.
- `redocly-docs/index.md`: pagina inicial.
- `redocly-docs/docs/`: paginas Markdown.
- `redocly-docs/openapi/openapi.yaml`: schema usado pela referencia da API.

## Paginas mantidas

- Inicio
- Visao geral
- Por onde comecar
- Autenticacao
- Webhook, incluindo suas paginas filhas
- Referencia da API
