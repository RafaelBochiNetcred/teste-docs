from drf_spectacular.utils import OpenApiExample, OpenApiResponse

from webhooks.serializers import (
    WebhookErrorSerializer,
    WebhookSerializer,
    WebhookValidationErrorSerializer,
)


WEBHOOK_PARTIAL_UPDATE_SCHEMA = {
    "summary": "Atualiza parcialmente uma assinatura de webhook",
    "description": (
        "Atualiza os campos enviados. Quando `events` e informado, a lista "
        "anterior de eventos assinados e substituida pela nova lista."
    ),
    "examples": [
        OpenApiExample(
            "Ativar webhook e trocar eventos",
            value={
                "is_active": True,
                "events": ["ANY"],
            },
            request_only=True,
        )
    ],
    "responses": {
        200: OpenApiResponse(
            response=WebhookSerializer,
            description="Assinatura atualizada com sucesso.",
        ),
        400: OpenApiResponse(
            response=WebhookValidationErrorSerializer,
            description="Erro de validacao dos campos enviados.",
        ),
        404: OpenApiResponse(
            response=WebhookErrorSerializer,
            description="Assinatura nao encontrada.",
        ),
    },
}
