from django.db import models
from course.models import *
from django.conf import settings
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils import timezone


# ----------------------------------------------------------------------------------------------------------------------------
class Coupon(models.Model):
    code = models.CharField(max_length=30,unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.code

# ----------------------------------------------------------------------------------------------------------------------------
class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='cart')
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(default=datetime.now)
    total_peyment = models.IntegerField(default=0,blank=True, null=True)
    paid = models.BooleanField(default=False)
    coupon = models.OneToOneField(Coupon,on_delete=models.CASCADE,blank=True, null=True)

    class Meta:
        ordering = ('-created',)


    def get_count_stuff(self):
        return self.stuff.all().count()

    def __str__(self):
        return f'{self.user} - {self.updated}'

    def get_total_price(self):
        total = sum(item.price for item in self.stuff.all())
        if self.coupon:
            discount_price = (self.coupon.discount/100)* total
            self.total_peyment = total - discount_price
            self.save()
            return total - discount_price
        self.total_peyment = total
        self.save()
        return total
# ----------------------------------------------------------------------------------------------------------------------------
class Stuff(models.Model):
     title = models.TextField()
     price = models.IntegerField(blank=True, null=True)
     code = models.IntegerField(blank=True, null=True)
     picture = models.ImageField()
     teacher = models.TextField()
     course = models.ForeignKey(Course,blank=True, null=True, on_delete=models.CASCADE)
     cart = models.ForeignKey(Cart,blank=True, null=True, on_delete=models.CASCADE,related_name='stuff')

     def __str__(self):
         return str(self.title)
# ----------------------------------------------------------------------------------------------------------------------------
class Department(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='department')
    def __str__(self):
        return f'{self.user}'

# ----------------------------------------------------------------------------------------------------------------------------
from jalali_date import datetime2jalali, date2jalali


class Receipt(models.Model):
    department = models.ForeignKey(Department,blank=True, null=True, on_delete=models.CASCADE,related_name='receipt')
    text = models.TextField()
    code = models.DecimalField(max_digits=5, decimal_places=0,unique=True)
    courses = models.ManyToManyField(Course ,blank=True,related_name="receipt")
    created = models.DateTimeField(default=datetime.now)
    Hash_code = models.CharField(max_length=500)
    pay = models.IntegerField(default=0,blank=True, null=True)


    def __str__(self):
        return f"{self.user}-{self.code}"

    def hash_code_simple(self):
        return self.Hash_code[0:10]

    def date(self):
        return str(14)+datetime2jalali(self.created).strftime('%y/%m/%d')

    def Course_Detail(self):
        return self.course.title_persion
# ----------------------------------------------------------------------------------------------------------------------------
