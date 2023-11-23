from rest_framework import serializers
from .models import Club, Player, Coach, Result, Fixture, League


class PlayerSerializer(serializers.ModelSerializer):
    club = serializers.StringRelatedField()
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'field_name', 'position', 'club']


class ClubSerializer(serializers.ModelSerializer):
    coach = serializers.StringRelatedField()
    players = PlayerSerializer(many=True)

    class Meta:
        model = Club
        fields = ['name', 'founded', 'coach', 'players']

        
class CoachSerializer(serializers.ModelSerializer):
    club = serializers.StringRelatedField()
    class Meta:
        model = Coach
        fields = ['first_name', 'last_name', 'club']
        
    
class ResultSerializer(serializers.ModelSerializer):
    home_team = serializers.StringRelatedField()
    away_team = serializers.StringRelatedField()
    class Meta:
        model = Result
        fields = ['date', 'home_team', 'away_team', 'home_team_goals', 'away_team_goals']
        
    
class FixtureSerializer(serializers.ModelSerializer):
    home_team = serializers.StringRelatedField()
    away_team = serializers.StringRelatedField()
    class Meta:
        model = Fixture
        fields = ['date', 'home_team', 'away_team']
        

class LeagueSerializer(serializers.ModelSerializer):
    clubs = ClubSerializer(many=True)
    results = ResultSerializer(many=True)
    fixtures = FixtureSerializer(many=True)
    
    class Meta:
        model = League
        fields = ['name', 'clubs', 'results', 'fixtures']