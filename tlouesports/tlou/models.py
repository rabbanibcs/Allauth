from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea, NumberInput
from django.utils.text import slugify
from django.utils.html import strip_tags
import math
from django.db.models.signals import post_save


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=400)
    image = models.ImageField(upload_to="media/News")
    Description = RichTextField()
    time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class userdtl(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bpass = models.CharField(max_length=50, default="")
    add1 = models.CharField(max_length=500, default="")
    add2 = models.CharField(max_length=500, default="")
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=50, default="")
    zipcode = models.IntegerField(default=0)
    tpass = models.CharField(max_length=500, default="")
    psn = models.CharField(max_length=500, default="")
    xbl = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.user.username


class Games(models.Model):
    Name = models.CharField(max_length=400)
    image = models.ImageField(upload_to="media/Games")
    time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return self.Name


class Ladders(models.Model):
    Name = models.CharField(max_length=400)
    game = models.ForeignKey(Games, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to="media/Ladders")
    console = models.CharField(max_length=100)
    maxmembers = models.CharField(default="11", max_length=20)
    region = models.CharField(max_length=100)
    season = models.IntegerField(default=0)
    teams = models.IntegerField(default=0)
    matches_played = models.IntegerField(default=0)
    rules = RichTextField()
    playoff_info = RichTextField()
    time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return self.Name


class Banner(models.Model):
    Heading = models.CharField(max_length=400)
    content = RichTextField()
    time = models.DateTimeField(null=False)
    image = models.ImageField(upload_to="media/Banner", null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.Heading


class sliders(models.Model):
    Heading = models.CharField(max_length=400)
    SubHeading = models.CharField(max_length=400, null=True)
    link = models.CharField(max_length=400, default="#")
    image = models.ImageField(upload_to="media/Sliders", null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.Heading


class Social(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=400, default="#")
    faicon = models.CharField(max_length=100, default="fa-facebook")

    def __str__(self):
        return self.name


class image(models.Model):
    title = models.CharField(max_length=400)
    image = models.ImageField(upload_to="media/Sliders", null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class team(models.Model):
    Name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/Teams", null=True, blank=True)
    ladder = models.ForeignKey(Ladders, on_delete=models.DO_NOTHING, null=True, blank=True)
    Win = models.IntegerField(default=0)
    Lose = models.IntegerField(default=0)
    Trophies = models.IntegerField(default=0)
    Member1 = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="Member1", null=True, blank=True)
    Member2 = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="Member2", null=True, blank=True)
    Member3 = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="Member3", null=True, blank=True)
    Member4 = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="Member4", null=True, blank=True)
    Member5 = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="Member5", null=True, blank=True)
    Member6 = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="Member6", null=True, blank=True)
    Member7 = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="Member7", null=True, blank=True)
    Member8 = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="Member8", null=True, blank=True)
    Member9 = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="Member9", null=True, blank=True)
    Member10 = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="Member10", null=True, blank=True)
    Member11 = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="Member11", null=True, blank=True)
    Member12 = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="Member12", null=True, blank=True)
    Member13 = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="Member13", null=True, blank=True)
    Member14 = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="Member14", null=True, blank=True)
    Member15 = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="Member15", null=True, blank=True)

    # two fields created for points and crown
    points = models.PositiveIntegerField(default=1200)
    crown = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + '_' + self.Name + '_' + str(self.crown)

    # method for calculating points after each game
    @staticmethod
    def elo_rating(team1, team2, a): # takes two team objects, a=1 means team1 wins
        # collects each team's point before game
        t1 = team1.points
        t2 = team2.points
        # sets value of K if team1 wins
        if a == 1:
            if t1 < 1500:
                K = 50
            elif 1500 <= t1 < 1800:
                K = 40
            elif t1 >= 1800:
                K = 25
        # sets value of K if team2 wins
        else:
            if t2 < 1500:
                K = 50
            elif 1500 <= t2 < 1800:
                K = 40
            elif t2 >= 1800:
                K = 25

        team2_expected_points = 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (t1 - t2) / 400))
        team1_expected_points = 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (t2 - t1) / 400))
        # points after game
        if a == 1:
            New_t1 = t1 + K * (1 - team1_expected_points)
            New_t2 = t2 + K * (0 - team2_expected_points)
        else:
            New_t1 = t1 + K * (0 - team1_expected_points)
            New_t2 = t2 + K * (1 - team2_expected_points)
        # if team1 has crown
        if team1.crown:
            if a == 1:  # team1 won- gets double point
                pts = New_t1 - t1
                New_t1 += pts
                team1.points = New_t1
                team1.save()
                team2.points = New_t2
                team2.save()
            else:  # team1 lost- team2 gets crown
                team1.crown = False
                team2.crown = True
                team1.points = New_t1
                team2.points = New_t2
                team1.save()
                team2.save()
        # if team2 has crown
        elif team2.crown:

            if a != 1:  # team1 won- gets double point
                pts = New_t2 - t2
                New_t2 += pts
                team2.points = New_t2
                team2.save()
                team1.points = New_t1
                team1.save()
            else:  # team2 lost- team1 gets crown
                team1.crown = True
                team2.crown = False
                team1.points = New_t1
                team2.points = New_t2
                team1.save()
                team2.save()
        else:  # both team without crown
            team1.points = New_t1
            team1.save()
            team2.points = New_t2
            team2.save()


class Contact(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    desc = models.TextField()
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
