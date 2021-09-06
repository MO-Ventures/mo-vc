from django.db import models

class Region(models.TextChoices):
    America = 'America', 'America'
    Asia = 'Asia', 'Asia'
    Europe = 'Europe', 'Europe'

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=60)
    region = models.CharField(max_length=30, choices=Region.choices, default=Region.Asia)
    url = models.URLField(max_length=60)
    image = models.ImageField(upload_to="company")

    class Meta:
        ordering = ["-name"]
    
    def __str__(self):
        return self.name

class Statistics(models.Model):
    show_people = models.BooleanField(default=True)
    people = models.PositiveIntegerField("Number of employees")
    show_raised = models.BooleanField(default=True)
    raised = models.PositiveIntegerField("Raised (in billion won)")
    show_funds = models.BooleanField(default=True)
    funds = models.PositiveIntegerField("Number of active funds")

    class Meta:
        verbose_name_plural = "Statistics"
    
    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return "Statistics"