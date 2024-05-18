from django.db import models

class Manga(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Chapter(models.Model):
    manga = models.ForeignKey(Manga, related_name='chapters', on_delete=models.CASCADE)
    number = models.IntegerField()
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return f"Chapter {self.number}: {self.title}"
