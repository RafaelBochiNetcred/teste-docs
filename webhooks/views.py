from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .docs import (
    WEBHOOK_DESTROY_SCHEMA,
    WEBHOOK_LIST_SCHEMA,
    WEBHOOK_PARTIAL_UPDATE_SCHEMA,
    WEBHOOK_PING_SCHEMA,
    WEBHOOK_RETRIEVE_SCHEMA,
)
from .models import Company, Webhook, WebhookEvent
from .schema import documented_endpoint
from .serializers import CompanySerializer, WebhookSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """Endpoint auxiliar para cadastrar empresas no prototipo local."""

    queryset = Company.objects.all().order_by("name")
    serializer_class = CompanySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "marketplace_id"]
    ordering_fields = ["id", "name", "marketplace_id"]


@extend_schema(tags=["Webhooks"])
class WebhookViewSet(viewsets.ModelViewSet):
    queryset = Webhook.objects.select_related(
        "company").prefetch_related("events")
    serializer_class = WebhookSerializer
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        "id": ["exact"],
        "is_active": ["exact"],
        "target_url": ["icontains"],
        "mask_user_agent": ["exact"],
        "company_id": ["exact", "in"],
        "company__marketplace_id": ["exact", "in"],
        "events__event_type": ["exact", "in"],
    }
    search_fields = ["name", "target_url", "company__name"]
    ordering_fields = [
        "id",
        "created",
        "company_id",
        "company__name",
        "name",
        "target_url",
        "is_active",
    ]

    @documented_endpoint
    @extend_schema(**WEBHOOK_LIST_SCHEMA)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @documented_endpoint
    @extend_schema(**WEBHOOK_RETRIEVE_SCHEMA)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @documented_endpoint
    @extend_schema(**WEBHOOK_PARTIAL_UPDATE_SCHEMA)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @documented_endpoint
    @extend_schema(**WEBHOOK_DESTROY_SCHEMA)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @documented_endpoint
    @extend_schema(**WEBHOOK_PING_SCHEMA)
    @action(detail=True, methods=["post"])
    def ping(self, request, pk=None):
        webhook = self.get_object()
        event = WebhookEvent.WebhookEventType.WEBHOOK_PING
        result = (
            f"Ping notification sent successfully to {webhook.target_url} "
            f"with event {event}."
        )
        return Response({"result": result, "status_code": "200"}, status=status.HTTP_200_OK)


class TesteViewSet(viewsets.ModelViewSet):
    queryset = Webhook.objects.select_related(
        "company").prefetch_related("events")
    serializer_class = WebhookSerializer
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]
