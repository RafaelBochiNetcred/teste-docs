from drf_spectacular.utils import OpenApiExample, OpenApiResponse

from webhooks.serializers import (
    WebhookSerializer,
    WebhookValidationErrorSerializer,
)


WEBHOOK_CREATE_SCHEMA = {
    "summary": "Cria uma assinatura de webhook",
    "description": (
        "Cria uma nova assinatura vinculada a empresa informada. A lista de "
        "eventos e obrigatoria e aceita apenas valores definidos em "
        "`WebhookEventType`. Informe `secret_key` quando o integrador precisar "
        "validar a assinatura enviada no header `X-Netcred-Signature`."
    ),
    "responses": {
        201: OpenApiResponse(
            response=WebhookSerializer,
            description="Assinatura criada com sucesso.",
            examples=[
                OpenApiExample(
                    "Webhook criado",
                    value={
                        "id": 10,
                        "name": "ERP Financeiro",
                        "target_url": "https://integrador.example.com/netcred/webhooks",
                        "subscribed_events": [
                            "CHARGE_CREATE",
                            "TRANSACTION_CAPTURE",
                        ],
                        "company": 1,
                        "company_name": "Empresa Exemplo",
                        "is_active": True,
                        "mask_user_agent": False,
                        "created": "2026-06-19T10:00:00-03:00",
                        "modified": "2026-06-19T10:00:00-03:00",
                    },
                    response_only=True,
                )
            ],
        ),
        400: OpenApiResponse(
            response=WebhookValidationErrorSerializer,
            description="Erro de validacao dos campos enviados.",
            examples=[
                OpenApiExample(
                    "Evento invalido",
                    value={"events": ['"UNKNOWN_EVENT" is not a valid choice.']},
                    response_only=True,
                )
            ],
        ),
    },
    "examples": [
        OpenApiExample(
            "Criar webhook HTTPS",
            value={
                "name": "ERP Financeiro",
                "target_url": "https://integrador.example.com/netcred/webhooks",
                "events": ["CHARGE_CREATE", "TRANSACTION_CAPTURE"],
                "company": 1,
                "is_active": True,
                "secret_key": "minha-chave-secreta",
                "mask_user_agent": False,
            },
            request_only=True,
        )
    ],
}
