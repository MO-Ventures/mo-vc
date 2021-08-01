from adminsortable.models import SortableMixin
from django.db import models

# Create your models here.
class Sector(models.TextChoices):
    VC = 'VC', 'VC'
    PE = 'PE', 'PE'
    Management = 'Management', 'Management'

class People(SortableMixin):
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    name = models.CharField(max_length=20)
    sector = models.CharField(max_length=20, choices=Sector.choices, default=Sector.VC)
    position = models.CharField(max_length=20)
    email = models.EmailField()
    photo = models.ImageField(upload_to='people/profile_pics')
    description = models.TextField()

    class Meta:
        ordering = ["the_order"]

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.title