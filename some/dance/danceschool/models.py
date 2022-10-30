from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser, Group
"""
id
title
content
photo
created_at 
"""


class Profile(models.Model):
    id = models.CharField(max_length=20, help_text="Введите id профиля", primary_key=True, null=False, default=1)
    first_name = models.CharField(max_length=30, help_text="Введите имя пользователя")
    last_name = models.CharField(max_length=30, help_text="Введите фамилию пользователя")
    photo = models.ImageField(upload_to='profiles/%Y/%m/%d/', help_text="Загрузите фотографию пользователя")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    CATEGORIES = (("DD media", "DDM"), ("Mentor", "M"), ("Dancer", "D"), ("Team Leader", "TL"), ("Trainer", "T"),
                  ("Admin", "Adm"))
    RANGS = (("junior", "jun"), ("middle", "mid"), ("senior", "sen"), ("vice president", "VP"))
    balance = models.CharField(max_length=6, help_text="Введите баланс DanceCoin")
    category = models.CharField(max_length=20, choices=CATEGORIES, help_text="Выберете категорию пользователя",
                                null=False, default="Adm")
    rang = models.CharField(max_length=20, choices=RANGS, help_text="Выберете ранг пользователя",
                            null=False, default="sen")

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ["-created_at", "-first_name", "-last_name"]

    def get_absolute_url(self):
        return reverse('', args=[self.id])

    def __str__(self):
        return self.first_name


class Commands(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    members = models.TextField()

    def get_absolute_url(self):
        return "/commands/%i/" % self.id

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=43)
    body = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/post/%i/" % self.id


class Tree(models.Model):
    id = models.AutoField(primary_key=True)
    profile_id = Profile.id
    energy = models.IntegerField(null=True, default=0)
    sun = models.IntegerField(null=True, default=0)
    water = models.IntegerField(null=True, default=0)
    timer = models.TimeField(auto_now=True)


class Achievements(models.Model):
    id = models.AutoField(primary_key=True)
    profile_id = Profile.id
    coin = models.CharField(max_length=100, null=True)
    ICONS = ((coin, "coin"),)
    performed = models.BooleanField()
    icon = models.CharField(max_length=10, choices=ICONS, null=True)
    text = models.CharField(max_length=255)
    value = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.text


class Messenger(models.Model):
    pass
