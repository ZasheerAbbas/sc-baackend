from django.db import models


# def get_file_path(self, filename):
#     return f'petitions/{self.petition.pk}/{filename}'

def get_file_path(self, filename):
    return f'files/{self.pk}/{filename}'

class Document(models.Model):
    path = models.FileField(upload_to=get_file_path)
    #petition = models.ForeignKey('Petition', related_name='documents', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.path.name}'
