from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class DataMixin():
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(DataMixin, models.Model):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class Post(DataMixin, models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='posts/')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.id} --> {self.title}"

class Rating(models.Model):
    rating = models.FloatField()
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(
        Post, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.rating} --> {self.author}"
