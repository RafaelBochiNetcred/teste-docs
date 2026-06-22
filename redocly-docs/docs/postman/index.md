# Visao geral

Este projeto demonstra uma documentacao Redocly combinando paginas Markdown com uma referencia OpenAPI gerada pelo Django REST Framework e drf-spectacular.

## Estrutura da documentacao

- [Por onde comecar](por-onde-comecar/index.md)
- [Autenticacao](autenticacao/index.md)
- [Webhook](webhook/index.md)
- [Referencia da API](../../openapi/openapi.yaml)

## Referencias da API

O schema OpenAPI e gerado automaticamente a partir das views do Django. Com `DEBUG=False`, entram no schema publico apenas as actions marcadas com `@documented_endpoint`.

As interfaces de API ficam disponiveis no projeto Django:

- OpenAPI: `/api/schema/`
- ReDoc: `/api/docs/`
- Swagger UI: `/api/docs/swagger/`
