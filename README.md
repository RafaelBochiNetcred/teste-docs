# Test Docs - Netcred API

Projeto Django/DRF para validar uma estrategia de documentacao da Netcred API com paginas Markdown estaticas, schema OpenAPI automatico e Redocly.

## Objetivo

- Gerar schema OpenAPI 3 com `drf-spectacular`.
- Publicar um portal Redocly com paginas estaticas e referencia OpenAPI automatica.
- Documentar o recurso de Webhook com campos, eventos suportados, exemplos, headers de entrega e respostas de erro/sucesso.
- Ocultar do schema publico endpoints auxiliares ou campos internos que nao devem ser consumidos por integradores.

## Como rodar

### API Django

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

URLs principais:

- API: `http://127.0.0.1:8000/api/webhooks/`
- OpenAPI schema: `http://127.0.0.1:8000/api/schema/`
- ReDoc: `http://127.0.0.1:8000/api/docs/`
- Swagger UI, apenas com `DEBUG=True`: `http://127.0.0.1:8000/api/docs/swagger/`

### Portal Redocly

Entre na pasta isolada do portal e instale as dependencias Node:

```bash
cd redocly-docs
npm install
```

Gere o schema OpenAPI usado pelo Redocly:

```bash
npm run docs:openapi
```

Valide a configuracao e o schema:

```bash
npm run docs:check-config
npm run docs:lint
```

Abra uma pre-visualizacao local do portal:

```bash
npm run docs:preview
```

O Redocly usa somente a pasta `redocly-docs/`:

- `redocly-docs/redocly.yaml`: configuracao principal do projeto.
- `redocly-docs/sidebars.yaml`: navegacao lateral das paginas estaticas e da referencia.
- `redocly-docs/docs/postman/`: paginas Markdown importadas da collection Postman.
- `redocly-docs/openapi/openapi.yaml`: schema gerado automaticamente pelo `drf-spectacular`.

## Endpoints do prototipo

- `GET /api/webhooks/`: lista assinaturas.
- `POST /api/webhooks/`: cria uma assinatura.
- `GET /api/webhooks/{id}/`: detalha uma assinatura.
- `PATCH /api/webhooks/{id}/`: atualiza parcialmente uma assinatura.
- `DELETE /api/webhooks/{id}/`: remove uma assinatura.
- `POST /api/webhooks/{id}/ping/`: simula o envio de uma notificacao de ping.

O app tambem possui `/api/companies/` e `/api/teste/` para facilitar testes locais.
Com `DEBUG=True`, o schema mostra todos os endpoints.
Com `DEBUG=False`, o schema publico mostra apenas as actions marcadas como documentadas.

## Como configurar no Redocly

No Reunite/Redocly, conecte este repositorio e configure `redocly-docs/` como a pasta raiz do portal. Assim o Redocly nao tenta importar o projeto Django inteiro.

Para paginas estaticas, adicione arquivos `.md` e referencie-os no `sidebars.yaml` ou no `navbar` do `redocly.yaml`.

Para referencia automatica, mantenha o job de build gerando `openapi/openapi.yaml` antes do deploy:

```bash
python ../manage.py spectacular --file openapi/openapi.yaml --validate
```

No `redocly.yaml`, a API fica registrada assim:

```yaml
apis:
  netcred@v1:
    root: ./openapi/openapi.yaml
```
