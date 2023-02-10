from django.db import models


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    subtitle = models.CharField(max_length=150, blank=True, null=True)
    body = models.TextField(max_length=15000)
    photo = models.ImageField(null=True, blank=True, upload_to='posts/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/news/post/%i" % self.id
