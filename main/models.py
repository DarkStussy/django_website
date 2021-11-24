from django.db import models


class Feedback(models.Model):
    name = models.CharField('Name', max_length=20)
    email = models.EmailField()
    message = models.TextField('Message')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
