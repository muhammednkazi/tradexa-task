# in this file we register the databases classes/tables that we have created in models.py
# only after registering it can be displayed in the database.


from django.contrib import admin
from .models import user,posts


# Register your models here.
admin.site.register(user)
admin.site.register(posts)