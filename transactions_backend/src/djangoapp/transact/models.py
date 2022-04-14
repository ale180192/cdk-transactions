from django.db import models
from uuid import uuid4


class Company(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False
    )
    name = models.CharField(max_length=64, unique=True)
    status = models.BooleanField(default=True)

class Transaction(models.Model):
    class Status(models.TextChoices):
        CLOSED = "CLOSED"
        REVERSED = "REVERSED"
        PENDING = "PENDING"

    id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False
    )
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE, null=False)
    price = models.DecimalField(
        max_digits=19, decimal_places=2
    )
    status = models.CharField(
        max_length=8,
        choices=Status.choices,
        default=Status.PENDING
    )
    approved = models.BooleanField(default=False)
    charged = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

