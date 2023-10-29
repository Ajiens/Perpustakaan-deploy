from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    title = models.TextField(null=True, blank=True)
    cover_link = models.TextField(null=True, blank=True)
    author = models.TextField(null=True, blank=True)
    rating_count = models.IntegerField(null=True, blank=True)
    review_count = models.IntegerField(null=True, blank=True)
    average_rating =  models.FloatField(null=True, blank=True)
    five_star_ratings =  models.IntegerField(null=True, blank=True)
    four_star_ratings =  models.IntegerField(null=True, blank=True)
    three_star_ratings =  models.IntegerField(null=True, blank=True)
    two_star_ratings =  models.IntegerField(null=True, blank=True)
    one_star_ratings =  models.IntegerField(null=True, blank=True)
    number_of_pages =  models.IntegerField(null=True, blank=True)
    date_published =  models.TextField(null=True, blank=True)
    publisher =  models.TextField(null=True, blank=True)
    isbn =  models.IntegerField(null=True, blank=True)
    description =  models.TextField(null=True, blank=True)
    harga =  models.IntegerField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    