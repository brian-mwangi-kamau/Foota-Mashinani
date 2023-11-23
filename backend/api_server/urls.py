from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClubViewset, PlayerViewset, CoachViewset, ResultViewset, FixtureViewset, LeagueViewset

router = DefaultRouter()
router.register(r'v1/clubs', ClubViewset, basename='club')
router.register(r'v1/players', PlayerViewset, basename='player')
router.register(r'v1/coaches', CoachViewset, basename='coach')
router.register(r'v1/results', ResultViewset, basename='results')
router.register(r'v1/fixtures', FixtureViewset, basename='fixtures')
router.register(r'v1/league', LeagueViewset, basename='league')



urlpatterns = [
    path('', include(router.urls)),
]
