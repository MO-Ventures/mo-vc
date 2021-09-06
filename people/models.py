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

class Employee(SortableMixin):
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    name = models.CharField(max_length=20)
    sector = models.CharField(max_length=20, choices=Sector.choices, default=Sector.VC)
    sector2 = models.CharField(max_length=20, choices=Sector.choices, blank=True)
    position = models.CharField(max_length=60)
    photo = models.ImageField(upload_to='people/profile_pics')
    description = HTMLField('description')

    class Meta:
        ordering = ["the_order"]

    def __str__(self):
        return self.name
