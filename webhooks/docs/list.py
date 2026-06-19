from drf_spectacular.utils import OpenApiExample, OpenApiParameter, OpenApiResponse

from webhooks.serializers import WebhookSerializer


WEBHOOK_LIST_SCHEMA = {
    "summary": "Lista assinaturas de webhook",
    "description": (
        "Retorna as assinaturas cadastradas. Permite filtrar por empresa, "
        "status, URL de destino e eventos assinados. Use este endpoint para "
        "auditar quais destinos estao configurados para receber notificacoes."
    ),
    "parameters": [
        OpenApiParameter(
            name="events__event_type__in",
            description="Filtra webhooks que assinam um ou mais eventos separados por virgula.",
            required=False,
            type=str,
        ),
    ],
    "responses": {
        200: OpenApiResponse(
            response=WebhookSerializer,
            description="Lista paginada de assinaturas de webhook.",
            examples=[
                OpenApiExample(
                    "Lista paginada",
                    value={
                        "count": 1,
                        "next": None,
                        "previous": None,
                        "results": [
                            {
                                "id": 10,
                                "name": "ERP Financeiro",
                                "target_url": (
                                    "https://integrador.example.com/netcred/webhooks"
                                ),
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
                            }
                        ],
                    },
                    response_only=True,
                )
            ],
        )
    },
}
