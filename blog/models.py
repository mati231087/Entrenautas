from django.db import models
from django.utils import timezone
from usuarios.models import Usuario

class Post(models.Model):
    author = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    likes = models.IntegerField(default=0)
    # otros campos que necesites...

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    # otros campos que necesites...

    def approve(self):
        self.approved_comment = True
        self.save()


# Create your models here.
