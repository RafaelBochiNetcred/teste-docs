from drf_spectacular.utils import OpenApiExample, OpenApiResponse

from webhooks.serializers import WebhookErrorSerializer, WebhookPingResponseSerializer


WEBHOOK_PING_SCHEMA = {
    "summary": "Envia ping para uma assinatura de webhook",
    "description": (
        "Simula o envio de uma notificacao de ping para validar se o destino "
        "configurado esta apto a receber payloads. No projeto real esta acao "
        "chama a task `send_webhook_request`; aqui retornamos uma resposta "
        "deterministica para documentacao e testes locais. A chamada de webhook "
        "gerada pelo ping usa os mesmos headers documentados no recurso."
    ),
    "responses": {
        200: OpenApiResponse(
            response=WebhookPingResponseSerializer,
            description="Ping simulado com sucesso.",
        ),
        404: OpenApiResponse(
            response=WebhookErrorSerializer,
            description="Assinatura nao encontrada.",
        ),
    },
    "examples": [
        OpenApiExample(
            "Ping enviado",
            value={
                "result": "Ping notification sent successfully!",
                "status_code": "200",
            },
            response_only=True,
        )
    ],
}
