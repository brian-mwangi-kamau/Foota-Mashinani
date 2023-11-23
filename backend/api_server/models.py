from django.db import models


class Club(models.Model):
    club_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    founded = models.CharField(max_length=10)
    coach = models.ForeignKey('Coach', on_delete=models.SET_NULL, null=True, blank=True, related_name='coach')
    players = models.ManyToManyField('Player', blank=True, related_name='players')
    leagues = models.ManyToManyField('League', blank=True, related_name='players')
    

    def save(self, *args, **kwargs):
        super().save(using='default', *args, **kwargs)
        
    def __str__(self):
        return f"{self.name}"
    

class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    field_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    club = models.ForeignKey('Club', on_delete=models.CASCADE, blank=True)
    
    def save(self, *args, **kwargs):
        super().save(using='default', *args, **kwargs)

    def __str__(self):
        return f"{self.field_name}"
    

class Coach(models.Model):
    coach_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    club = models.ForeignKey('Club', on_delete=models.CASCADE, related_name='coached_club', blank=True)
    
    def save(self, *args, **kwargs):
        super().save(using='default', *args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name_plural = "Coaches"
    

class Result(models.Model):
    result_id = models.AutoField(primary_key=True)
    date = models.DateField()
    home_team = models.ForeignKey('Club', related_name='result_home_team', on_delete=models.CASCADE)
    away_team = models.ForeignKey('Club', related_name='result_away_team', on_delete=models.CASCADE)
    home_team_goals = models.PositiveIntegerField()
    away_team_goals = models.PositiveIntegerField()
    
    def save(self, *args, **kwargs):
        super().save(using='default', *args, **kwargs)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} - {self.date}"
    

class Fixture(models.Model):
    fixture_id = models.AutoField(primary_key=True)
    date = models.DateField()
    home_team = models.ForeignKey('Club', related_name='fixture_home_team', on_delete=models.CASCADE)
    away_team = models.ForeignKey('Club', related_name='fixture_away_team', on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        super().save(using='default', *args, **kwargs)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} - {self.date}"
    
    

class League(models.Model):
    league_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    league_description = models.TextField(max_length=500)
    clubs = models.ManyToManyField('Club', blank=True, related_name='clubs')
    results = models.ManyToManyField('Result', blank=True, related_name='results')
    fixtures = models.ManyToManyField('Fixture', blank=True, related_name='fixtures')
    
    def save(self, *args, **kwargs):
        super().save(using='default', *args, **kwargs)
    
    def __str__(self):
        return f"{self.name}"