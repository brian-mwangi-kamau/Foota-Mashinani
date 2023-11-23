from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Club, Player, Coach, Result, Fixture, League
from .serializers import ClubSerializer, PlayerSerializer, CoachSerializer, ResultSerializer, FixtureSerializer, LeagueSerializer
from .permissions import ReadOnlyPermission, APIKeyPermission 

# pylint: disable=no-member
class ClubViewset(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = [ReadOnlyPermission, IsAuthenticated, APIKeyPermission] 


class PlayerViewset(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [ReadOnlyPermission, IsAuthenticated, APIKeyPermission]
    
    
class CoachViewset(viewsets.ModelViewSet):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
    permission_classes = [ReadOnlyPermission, IsAuthenticated, APIKeyPermission]
    

class ResultViewset(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [ReadOnlyPermission, IsAuthenticated, APIKeyPermission]
    
    
class FixtureViewset(viewsets.ModelViewSet):
    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer
    permission_classes = [ReadOnlyPermission, IsAuthenticated, APIKeyPermission]
    

class LeagueViewset(viewsets.ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    permission_classes = [ReadOnlyPermission, IsAuthenticated, APIKeyPermission]
    
