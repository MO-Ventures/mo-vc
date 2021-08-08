from adminsortable.models import SortableMixin
from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Sector(models.TextChoices):
    Leadership = 'Leadership', 'Leadership'
    VC = 'VC', 'VC'
    PE = 'PE', 'PE'
    Management = 'Management', 'Management'
    Advisory_board = 'Advisory Board', 'Advisory_Board'

class Introduction(models.Model):
    heading = models.CharField(max_length=30)
    subheading = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Introduction"
    
    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return "Introduction"

class People(SortableMixin):
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    name = models.CharField(max_length=20)
    sector = models.CharField(max_length=20, choices=Sector.choices, default=Sector.VC)
    sector2 = models.CharField(max_length=20, choices=Sector.choices, blank=True)
    position = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='people/profile_pics')
    description = HTMLField('description')

    class Meta:
        ordering = ["the_order"]

    def __str__(self):
        return self.name
