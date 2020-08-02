from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse

class Content(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,
                            related_name='contents_created',
                            on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,
                            blank=True)
    created=models.DateField(auto_now_add=True,
                            db_index=True)
    # choice && graph
    users_like=models.ManyToManyField(settings.AUTH_USER_MODEL,
                            related_name='contents_liked',
                            blank=True)
    # votes
    # views
    # shares
    # comments

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('contents:detail', args=[self.id, self.slug])
