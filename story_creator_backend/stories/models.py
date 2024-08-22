# stories/models.py
from django.db import models
from django.contrib.auth.models import User


class Story(models.Model):
    title = models.CharField(max_length=200)
    first_sentence = models.TextField(default='No sentence provided')
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='story_images/', null=True, blank=True)

    def __str__(self):
        return self.title

class Contribution(models.Model):
    story = models.ForeignKey(Story, related_name='contributions', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contribution to {self.story.title} by {self.user.username}"
