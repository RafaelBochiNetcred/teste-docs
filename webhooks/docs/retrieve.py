from drf_spectacular.utils import OpenApiExample, OpenApiResponse

from webhooks.serializers import WebhookErrorSerializer, WebhookSerializer


WEBHOOK_RETRIEVE_SCHEMA = {
    "summary": "Detalha uma assinatura de webhook",
    "description": (
        "Retorna configuracoes, empresa vinculada e eventos assinados. A chave "
        "secreta nao e exposta na resposta publica."
    ),
    "responses": {
        200: OpenApiResponse(
            response=WebhookSerializer,
            description="Assinatura encontrada.",
        ),
        404: OpenApiResponse(
            response=WebhookErrorSerializer,
            description="Assinatura nao encontrada.",
            examples=[
                OpenApiExample(
                    "Nao encontrado",
                    value={"detail": "Not found."},
                    response_only=True,
                )
            ],
        ),
    },
}
