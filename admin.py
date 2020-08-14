from django.contrib import admin
from .models import user
from loginapp.models import user,resetpassword
admin.site.register(user)
admin.site.register(resetpassword)
