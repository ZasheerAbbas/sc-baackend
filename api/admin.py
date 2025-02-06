from django.contrib import admin
from api.models import *
# Register your models here.


admin.site.register(Document)
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(Logs)
