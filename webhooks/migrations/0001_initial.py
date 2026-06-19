from django.db import migrations, models
import django.core.validators
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("marketplace_id", models.CharField(blank=True, default="", max_length=64)),
            ],
            options={
                "verbose_name": "company",
                "verbose_name_plural": "companies",
            },
        ),
        migrations.CreateModel(
            name="Webhook",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "target_url",
                    models.URLField(
                        max_length=255,
                        validators=[
                            django.core.validators.URLValidator(
                                schemes=["http", "https", "awssqs", "gcpubsub"]
                            )
                        ],
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("secret_key", models.CharField(blank=True, default="", max_length=255)),
                ("mask_user_agent", models.BooleanField(default=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="webhooks",
                        to="webhooks.company",
                    ),
                ),
            ],
            options={
                "permissions": [("ping_webhook", "Can ping webhook")],
                "ordering": ["-created", "-id"],
            },
        ),
        migrations.CreateModel(
            name="WebhookEvent",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "event_type",
                    models.CharField(
                        choices=[
                            ("ANY", "Any event"),
                            ("CHARGE_CREATE", "Charge created"),
                            ("CHARGE_UPDATE", "Charge updated"),
                            ("CHARGE_VOID", "Charge voided"),
                            ("TRANSACTION_CREATE", "Transaction created"),
                            ("TRANSACTION_CAPTURE", "Transaction captured"),
                            ("TRANSACTION_EXPIRED", "Transaction expired"),
                            ("TRANSACTION_UPDATE", "Transaction updated"),
                            ("TRANSACTION_VOID", "Transaction voided"),
                            ("TRANSACTION_REFUND", "Transaction refunded"),
                            ("TRANSACTION_DISPUTE", "Transaction disputed"),
                            ("TRANSACTION_AUTHORIZE", "Transaction authorized"),
                            ("PAYMENT_PROFILE_TOKENIZE", "Payment profile tokenized"),
                            ("PAYMENT_PROFILE_UPDATE", "Payment profile updated"),
                            ("PAYMENT_PROFILE_DELETE", "Payment profile deleted"),
                            ("PAYMENT_PROFILE_EXPIRING", "Payment profile close to expiry"),
                            ("WEBHOOK_PING", "Webhook ping"),
                        ],
                        db_index=True,
                        max_length=128,
                    ),
                ),
                (
                    "webhook",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="events",
                        to="webhooks.webhook",
                    ),
                ),
            ],
            options={
                "ordering": ["event_type"],
                "unique_together": {("webhook", "event_type")},
            },
        ),
    ]
