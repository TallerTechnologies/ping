from django.contrib import admin
from ping.models import Team, Match, Championship, Player, Journey
admin.site.autodiscover()


map(admin.site.register, [Team, Match, Championship, Player, Journey])


