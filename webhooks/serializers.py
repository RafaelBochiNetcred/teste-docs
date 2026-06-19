from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from .models import Company, Webhook, WebhookEvent


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "marketplace_id"]
        extra_kwargs = {
            "name": {
                "help_text": "Nome da empresa vinculada a uma ou mais assinaturas de webhook."
            },
            "marketplace_id": {
                "help_text": "Identificador externo da empresa no marketplace, quando existir."
            },
        }


class WebhookEventSerializer(serializers.ModelSerializer):
    event_type = serializers.ChoiceField(
        choices=WebhookEvent.WebhookEventType.choices,
        help_text="Tipo de evento que dispara o envio de notificacao para o webhook.",
    )

    class Meta:
        model = WebhookEvent
        fields = ["id", "event_type"]


class WebhookSerializer(serializers.ModelSerializer):
    events = serializers.ListField(
        child=serializers.ChoiceField(
            choices=WebhookEvent.WebhookEventType.choices),
        write_only=True,
        help_text=(
            "Lista de eventos que a assinatura deve receber. Use ANY para receber todos os eventos disponíveis"
        ),
    )
    subscribed_events = serializers.SerializerMethodField(
        help_text="Eventos atualmente vinculados a assinatura."
    )
    company_name = serializers.CharField(
        source="company.name",
        read_only=True,
        help_text="Nome da empresa vinculada ao webhook.",
    )

    class Meta:
        model = Webhook
        fields = [
            "id",
            "name",
            "target_url",
            "events",
            "subscribed_events",
            "company",
            "company_name",
            "is_active",
            "secret_key",
            "mask_user_agent",
            "created",
            "modified",
        ]
        read_only_fields = ["id", "company_name",
                            "subscribed_events", "created", "modified"]
        extra_kwargs = {
            "name": {
                "help_text": "Nome opcional para identificar a assinatura de webhook."
            },
            "target_url": {
                "help_text": (
                    "URL que recebera o payload do evento. Sao aceitos os esquemas "
                    "http, https, awssqs e gcpubsub."
                )
            },
            "company": {
                "help_text": "ID da empresa dona da assinatura de webhook."
            },
            "is_active": {
                "help_text": "Define se a assinatura esta ativa e apta a receber notificacoes."
            },
            "secret_key": {
                "help_text": (
                    "Chave usada para assinar o payload enviado ao integrador. "
                    "No ambiente real, deve ser armazenada e exibida com cuidado."
                ),
                "write_only": True,
                "required": False,
            },
            "mask_user_agent": {
                "help_text": "Define se o user agent padrao deve ser mascarado no envio."
            },
        }

    @extend_schema_field(serializers.ListField(child=serializers.CharField()))
    def get_subscribed_events(self, webhook):
        return list(webhook.events.values_list("event_type", flat=True))

    def create(self, validated_data):
        events = validated_data.pop("events")
        webhook = Webhook.objects.create(**validated_data)
        self._replace_events(webhook, events)
        return webhook

    def update(self, instance, validated_data):
        events = validated_data.pop("events", None)
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()

        if events is not None:
            self._replace_events(instance, events)

        return instance

    def _replace_events(self, webhook, events):
        webhook.events.all().delete()
        WebhookEvent.objects.bulk_create(
            WebhookEvent(webhook=webhook, event_type=event) for event in events
        )


class WebhookPingResponseSerializer(serializers.Serializer):
    result = serializers.CharField(
        help_text="Mensagem informando se a notificacao de ping foi simulada com sucesso."
    )
    status_code = serializers.CharField(
        help_text="Codigo de status associado a simulacao do ping."
    )


class WebhookErrorSerializer(serializers.Serializer):
    detail = serializers.CharField(
        help_text=(
            "Mensagem de erro retornada quando a requisicao nao pode ser processada "
            "ou o recurso solicitado nao existe."
        )
    )


class WebhookValidationErrorSerializer(serializers.Serializer):
    field_name = serializers.ListField(
        child=serializers.CharField(),
        help_text=(
            "Lista de mensagens de validacao agrupadas por campo. O nome real do "
            "campo aparece como chave no payload retornado pela API."
        ),
    )
