# Redocly API Docs Example

Projeto de exemplo para documentar uma API Django REST Framework com:

- schema OpenAPI gerado por `drf-spectacular`;
- ReDoc em `/api/docs/`;
- Swagger UI em `/api/docs/swagger/`;
- portal Redocly com paginas Markdown e referencia OpenAPI;
- filtro para publicar no OpenAPI apenas actions marcadas com `@documented_endpoint` quando `DEBUG=False`.

## Atualizando schemas

Sempre que alterar views, serializers, filtros ou schemas:

```bash
cd redocly-docs
npm run docs:openapi
```

Esse comando gera:

- `openapi/openapi.yaml` com `DJANGO_DEBUG=False`;
- `openapi/webhooks.yaml` a partir da tag `Webhooks`;
- `openapi/company.yaml` a partir da tag `Company`, usando `DJANGO_DEBUG=True`.

## Adicionando uma pagina Markdown

1. Crie o arquivo dentro de `redocly-docs/docs/`.

Exemplo:

```text
redocly-docs/docs/minha-pagina.md
```

2. Adicione no `redocly-docs/sidebars.yaml`:

```yaml
- page: docs/minha-pagina.md
  label: Minha pagina
```

Para pagina filha, coloque dentro de um `group`.

## Adicionando uma nova view ao OpenAPI

1. Registre a view no router:

```python
router.register("charges", ChargeViewSet, basename="charge")
```

2. Marque as actions que devem aparecer no schema publico:

```python
@documented_endpoint
@extend_schema(tags=["Charges"])
def list(self, request, *args, **kwargs):
    return super().list(request, *args, **kwargs)
```

3. Gere os schemas:

```bash
cd redocly-docs
npm run docs:openapi
```

Com `DEBUG=False`, apenas actions com `@documented_endpoint` entram no schema publico.

## Criando uma referencia separada por tag

1. Garanta que a view usa uma tag:

```python
@extend_schema(tags=["Charges"])
```

2. Adicione a geracao no script `docs:openapi` em `redocly-docs/package.json`:

```bash
python3 ../scripts/split_openapi_by_tag.py openapi/openapi.yaml Charges openapi/charges.yaml
```

3. Registre em `redocly-docs/redocly.yaml`:

```yaml
apis:
  charges@v1:
    root: ./openapi/charges.yaml
```

4. Adicione no `redocly-docs/sidebars.yaml`:

```yaml
- page: openapi/charges.yaml
  label: Charges
```

Depois disso, futuras alteracoes ficam automatizadas pelo `npm run docs:openapi`.
