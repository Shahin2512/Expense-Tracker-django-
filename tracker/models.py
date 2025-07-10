from django.db import models


CATEGORY_CHOICES = [
    ('Food', 'Food'),
    ('Transport', 'Transport'),
    ('Entertainment', 'Entertainment'),
    ('Bills', 'Bills'),
    ('Other', 'Other'),
]

class Expense(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField()

    def __str__(self):
        return f"{self.title} - ₹{self.amount}"
# Create your models here.
