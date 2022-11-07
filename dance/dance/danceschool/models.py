from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _
from accounts.models import User
"""
id
title
content
photo
created_at 
"""


class Profile(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, help_text="Введите имя пользователя")
    last_name = models.CharField(max_length=30, help_text="Введите фамилию пользователя")
    photo = models.ImageField(upload_to='profiles/%Y/%m/%d/', help_text="Загрузите фотографию пользователя", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    CATEGORIES = (("DD media", "DDM"), ("Mentor", "M"), ("Dancer", "D"), ("Team Leader", "TL"), ("Trainer", "T"),
                  ("Admin", "Adm"))
    RANGS = (("junior", "jun"), ("middle", "mid"), ("senior", "sen"), ("vice president", "VP"))
    balance = models.IntegerField(help_text="Введите баланс DanceCoin", default=0)
    energy = models.IntegerField(help_text="Введите баланс энергии", default=0)
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
        return self.first_name and self.last_name


class Commands(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(Profile, related_name="user_teams")
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    created_by = models.ForeignKey(
        Profile,
        related_name="teams_created",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    def get_absolute_url(self):
        return "/commands/%i/" % self.id

    def __str__(self):
        return self.name

    def get_users(self):
        return self.members.all()

# reverse 'danceschool:staff_profile(?P<id>[0-9]+)'


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=43)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/post/%i/" % self.id


class Tree(models.Model):
    id = models.AutoField(primary_key=True)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    energy = models.IntegerField(null=True, default=0)
    sun = models.IntegerField(null=True, default=0)
    water = models.IntegerField(null=True, default=0)
    timer = models.TimeField(auto_now=True)


class Achievements(models.Model):
    id = models.AutoField(primary_key=True)
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
