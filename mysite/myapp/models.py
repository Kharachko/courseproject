from django.db import models

class Manga(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, default="Unknown Author")
    description = models.TextField(default="No description available")

    def __str__(self):
        return self.title

class Chapter(models.Model):
    manga = models.ForeignKey(Manga, related_name='chapters', on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    title = models.CharField(max_length=200, default="Chapter Title")
    pdf_file = models.FileField(upload_to='chapters/', default=None)

    def __str__(self):
        return f"Chapter {self.number}: {self.title}"
