from django.contrib import admin
from .models import Club, Player, Coach, Result, Fixture, League

admin.site.register(Club)
admin.site.register(Coach)
admin.site.register(Player)
admin.site.register(Result)
admin.site.register(Fixture)
admin.site.register(League)