from django.db import models

# Create your models here.
class Article(models.Model):
    title   = models.CharField(max_length=100)
    slug    = models.SlugField()
    body    = models.TextField()
    img     = models.ImageField()
    date    = models.DateTimeField(auto_now_add=True, blank=True)
    article_auther  = models.CharField(max_length=100)

    def __str__(self):
        return self.title


    def snippet(self):
        return self.body[:100] + "..."
