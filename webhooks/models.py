from django.core import validators
from django.db import models


class WebhookURLField(models.URLField):
    default_validators = [
        validators.URLValidator(schemes=["http", "https", "awssqs", "gcpubsub"])
    ]


class Company(models.Model):
    name = models.CharField(max_length=255)
    marketplace_id = models.CharField(max_length=64, blank=True, default="")

    class Meta:
        verbose_name = "company"
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name


class Webhook(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    target_url = WebhookURLField(max_length=255)
    is_active = models.BooleanField(default=True)
    secret_key = models.CharField(max_length=255, blank=True, default="")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="webhooks")
    mask_user_agent = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
            ("ping_webhook", "Can ping webhook"),
        ]
        ordering = ["-created", "-id"]

    def __str__(self):
        return self.name or f"Webhook #{self.pk}"


class WebhookEvent(models.Model):
    class WebhookEventType(models.TextChoices):
        ANY = "ANY", "Any event"
        CHARGE_CREATE = "CHARGE_CREATE", "Charge created"
        CHARGE_UPDATE = "CHARGE_UPDATE", "Charge updated"
        CHARGE_VOID = "CHARGE_VOID", "Charge voided"
        TRANSACTION_CREATE = "TRANSACTION_CREATE", "Transaction created"
        TRANSACTION_CAPTURE = "TRANSACTION_CAPTURE", "Transaction captured"
        TRANSACTION_EXPIRED = "TRANSACTION_EXPIRED", "Transaction expired"
        TRANSACTION_UPDATE = "TRANSACTION_UPDATE", "Transaction updated"
        TRANSACTION_VOID = "TRANSACTION_VOID", "Transaction voided"
        TRANSACTION_REFUND = "TRANSACTION_REFUND", "Transaction refunded"
        TRANSACTION_DISPUTE = "TRANSACTION_DISPUTE", "Transaction disputed"
        TRANSACTION_AUTHORIZE = "TRANSACTION_AUTHORIZE", "Transaction authorized"
        PAYMENT_PROFILE_TOKENIZE = "PAYMENT_PROFILE_TOKENIZE", "Payment profile tokenized"
        PAYMENT_PROFILE_UPDATE = "PAYMENT_PROFILE_UPDATE", "Payment profile updated"
        PAYMENT_PROFILE_DELETE = "PAYMENT_PROFILE_DELETE", "Payment profile deleted"
        PAYMENT_PROFILE_EXPIRING = "PAYMENT_PROFILE_EXPIRING", "Payment profile close to expiry"
        WEBHOOK_PING = "WEBHOOK_PING", "Webhook ping"

    webhook = models.ForeignKey(Webhook, related_name="events", on_delete=models.CASCADE)
    event_type = models.CharField(
        choices=WebhookEventType.choices,
        max_length=128,
        db_index=True,
    )

    class Meta:
        unique_together = ("webhook", "event_type")
        ordering = ["event_type"]

    def __str__(self):
        return self.event_type
