from django.contrib import admin
from .models import Noticias
from .models import Clothing
from .models import Environment
from .models import Health
from .models import Transport
from .models import Game
from .models import Supplies
from .models import Post
admin.site.register(Noticias)
admin.site.register(Clothing)
admin.site.register(Environment)
admin.site.register(Health)
admin.site.register(Transport)
admin.site.register(Game)
admin.site.register(Supplies)
admin.site.register(Post)
# Register your models here.
