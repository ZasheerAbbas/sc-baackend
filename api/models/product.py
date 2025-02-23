from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
     

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', related_name='+', blank=True, null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey('User', related_name='+', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
