from django.db import models

class Website(models.Model):
    url = models.URLField(unique=True)

class Directory(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    directory_name = models.CharField(max_length=255)

    def __str__(self):
        return self.directory_name
