from django.db import models
from mptt.models import  MPTTModel, TreeForeignKey

# Create your models here.

class MenuItem(MPTTModel):
    name = models.CharField('name',max_length=100)
    url = models.CharField('url',max_length=255)
    position = models.PositiveIntegerField('position',default=1)
    parent = TreeForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='children')
    
    class MPTTMeta:
        order_insertion_by = ['position']
    
    def __str__(self) -> str:
        return str(self.name)
        
    class Meta:
        verbose_name = 'пункт муню'
        verbose_name_plural = 'пункты муню'
        