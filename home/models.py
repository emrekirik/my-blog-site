from django.db import models
from django.utils import timezone
from django.urls import reverse



class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    cover_image = models.ImageField(
        upload_to='post_image',
    )
    pub_date = models.DateTimeField(blank=True, null=True)
    tag = models.CharField(max_length=200, blank=True, null=True)

   

    def __str__(self):
        return self.title

    def yayinla(self):
        self.pub_date=timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'id' : self.id})


