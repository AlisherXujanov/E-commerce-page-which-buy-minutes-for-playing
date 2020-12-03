from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone

CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear')
)


LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    stert_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


EASY = 2
NORMAL = 1
ADVANCED = 0.5
MINUTE_CHOICES = (
    (ADVANCED, 'Advanced (30-sek)'), (NORMAL,
                                      'Normal (1min)'), (EASY, 'Easy (2min)'),
)


class Timer(models.Model):
    name = models.CharField(max_length=50, default="")
    difficulty = models.FloatField(
        default=NORMAL, choices=MINUTE_CHOICES, help_text="How Clever And Fast You Are?")
    started_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('quiz')
