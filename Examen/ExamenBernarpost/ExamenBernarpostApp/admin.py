from django.contrib import admin
from .models import Usuarios
from .models import Posts
from .models import Planes

# Register your models here.

admin.site.register(Usuarios)

admin.site.register(Posts)

admin.site.register(Planes)
