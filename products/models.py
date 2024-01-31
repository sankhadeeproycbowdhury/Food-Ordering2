from django.db import models
import uuid

# Create your models here.


class BaseModel(models.Model):
     uid = models.UUIDField(default = uuid.uuid4 , editable = False , Primary_key = True)
     created_at = models.DateTimeField(auto_created = True)
     update_at = models.DateTimeField(auto_created = True)
     
     class Meta:
         abstract = True
     


class Product(BaseModel):
   
   product_name = models.CharField(max_length = 100)
   product_slug = models.SlugField(unique = True)
   product_description = models.TextField()
   product_price = models.IntegerField(default = 0)
   product_demo_price = models.IntegerField(default = 0)
   quantity = models.CharField(null = True , blank = True)
   

class ProductMetaInformation(BaseModel):
    product = models.OneToOneField(Product , on_delete = models.CASCADE , related_name = "meta_info")
    product_quantity = models.CharField(null = True , blank = True)
    product_measuring = models.CharField(max_length = 100 , null = True , blank = True , choices = (('KG','KG') , ('L','L') , ('ML' , 'ML'),(None,None)))
    is_restrict = models.BooleanField(default = False)
    restrict_quantity = models.IntegerField()
    

class ProductImages(BaseModel):
    product = models.ForeignKey(Product , on_delete = models.CASCADE , related_name = "images")
    product_images = models.ImageField(upload_to="products")

   
   
   