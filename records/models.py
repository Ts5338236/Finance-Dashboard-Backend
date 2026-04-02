from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from decimal import Decimal

class FinancialRecord(models.Model):
    TYPE_CHOICES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )
    
    CATEGORY_CHOICES = (
        ('salary', 'Salary'),
        ('food', 'Food'),
        ('rent', 'Rent'),
        ('utilities', 'Utilities'),
        ('transport', 'Transport'),
        ('entertainment', 'Entertainment'),
        ('health', 'Health'),
        ('other', 'Other'),
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='records')
    amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.type} - {self.amount}"

    class Meta:
        ordering = ['-date', '-created_at']
