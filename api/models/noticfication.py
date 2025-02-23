from django.db import models

class Notification(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='notifications')
    container = models.ForeignKey('Container', on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', related_name='+', blank=True, null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey('User', related_name='+', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name