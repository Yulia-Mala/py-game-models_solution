from django.db import models


class Race(models.Model):
    RACES_TO_CHOICE = [
        ("elf", "Elf"),
        ("dwarf", "Dwarf"),
        ("human", "Human"),
        ("ork", "Ork")
    ]
    name = models.CharField(max_length=255,
                            unique=True,
                            choices=RACES_TO_CHOICE)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.TextField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
