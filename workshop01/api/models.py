from django.db import models
# from django.contrib.auth.models import User

class Job(models.Model):
    STATUS_CHOICES = (
        ('published', 'PUBLISHED'),
        ('expired', 'EXPIRED'),
    )

    PRICE_TYPE_CHOICES = (
        ('fixed', 'FIXED'),
        ('negotiable', 'NEGOTIABLE'),
    )

    PRICE_UNIT_CHOICES = (
        ('unit', 'UNIT'),
        ('million', 'MILLION'),
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    likeCount = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pricePreview = models.CharField(max_length=50)
    priceType = models.CharField(max_length=20, choices=PRICE_TYPE_CHOICES)
    priceUnit = models.CharField(max_length=10, choices=PRICE_UNIT_CHOICES)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    category = models.CharField(max_length=100)
    specs = models.JSONField(null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-createdAt']

