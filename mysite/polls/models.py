from django.db import models

class ListaCSV(models.Model):
    headword = models.CharField(max_length=100)
    first_attestation_example_md = models.CharField(max_length=900)

    def __str__(self):
        return self.headword
