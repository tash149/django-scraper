from django.db import models


# Create your models here.

class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{]'.format(self.search)         # when we don't write this admin site would have searches with search objects, writing this would allow the actual search topic on the list


    class Meta:
        verbose_name_plural = 'Searches'  # when we have registered our models in the admin.py we would need to change the interface from Searchs to Searches

