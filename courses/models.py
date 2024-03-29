from django.db import models
from profiles.models import AcceptedCrypto


class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=10000, blank=True)
    geolocation = models.CharField(max_length=150, blank=True)
    accepted_cryptos = models.ManyToManyField(AcceptedCrypto, related_name="accepted_cryptos")

    def __str__(self):
        return self.title

    def get_accepted_cryptos(self):
        return [(accepted_crypto.code, accepted_crypto.name) for accepted_crypto in self.accepted_cryptos.all]
