from drf_spectacular.utils import OpenApiResponse

from webhooks.serializers import WebhookErrorSerializer


WEBHOOK_DESTROY_SCHEMA = {
    "summary": "Remove uma assinatura de webhook",
    "description": (
        "Exclui definitivamente a assinatura e seus eventos vinculados. Apos a "
        "remocao, novas notificacoes deixam de ser enviadas para a URL configurada."
    ),
    "responses": {
        204: OpenApiResponse(description="Assinatura removida com sucesso."),
        404: OpenApiResponse(
            response=WebhookErrorSerializer,
            description="Assinatura nao encontrada.",
        ),
    },
}
