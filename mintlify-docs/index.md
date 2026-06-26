---
title: Visao geral
description: Estrutura da documentacao da API Netcred.
---

# Visao geral

Este projeto demonstra uma documentacao Mintlify combinando paginas Markdown com uma referencia OpenAPI gerada pelo Django REST Framework e drf-spectacular.

## Estrutura da documentacao

- [Por onde comecar](/por-onde-comecar)
- [Autenticacao](/autenticacao)
- [Webhook](/webhook)
- [Referencia da API](/api-reference)

## Referencias da API

O schema OpenAPI e gerado automaticamente a partir das views do Django. Com `DEBUG=False`, entram no schema publico apenas as actions marcadas com `@documented_endpoint`.

As interfaces de API ficam disponiveis no projeto Django:

- OpenAPI: `/api/schema/`
- ReDoc: `/api/docs/`
- Swagger UI: `/api/docs/swagger/`
