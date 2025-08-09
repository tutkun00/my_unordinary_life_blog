from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify


class Post(models.Model):

     title = models.CharField(max_length=50)
     thumbnail = models.ImageField(upload_to="thumbnails/")
     content = CKEditor5Field(config_name="default")
     released_at = models.DateTimeField(auto_now_add=True, editable=False)
     is_public = models.BooleanField(default=False)
     slug = models.SlugField(editable=False, unique=True)

     def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


     def __str__(self):
          return self.title