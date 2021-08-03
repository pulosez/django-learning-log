from django.db import models


class Topic(models.Model):
    """Тема, яку вивчає користувач."""
    text = models.CharField(
        max_length=200,
    )
    date_added = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        """Повернути рядкове представлення моделі."""
        return self.text

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'


class Entry(models.Model):
    """Якась конкретна інформація до цієї теми."""
    topic = models.ForeignKey(
        'learning_logs.Topic',
        on_delete=models.CASCADE,
    )

    text = models.TextField()
    date_added = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        """Повернути представлення моделі у string."""
        return f"{self.text[:50]}..."

    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'
