from django.db import models
from django.db.models.deletion import DO_NOTHING

model = models.Model

# Create your models here.
class City(model):
    post_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}, {}".format(self.post_no, self.name)


class Address(model):
    house_no = models.CharField(max_length=10)
    street = models.CharField(max_length=200)
    city = models.ForeignKey(City, related_name="adr_city", on_delete=DO_NOTHING)

    def __str__(self):
        return "{} {}, {}".format(self.street, self.house_no, self.city)


class Role(model):
    name = models.CharField(max_length=20)
    min_hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "{} - {}".format(self.name, self.min_hourly_rate)


class User(model):
    tax_no = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.ForeignKey(Address, related_name="staff_adr", on_delete=models.DO_NOTHING)
    email = models.EmailField()

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)


class Company(model):
    tax_no = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, related_name="comp_adr", on_delete=models.DO_NOTHING)
    ceo = models.ForeignKey(User, related_name="comp_ceo", on_delete=models.DO_NOTHING)

    def __str__(self):
        return "Name: {},\nAddress: {},\nCEO: {}\nTax number: {}".format(self.name, self.address, self.ceo, self.tax_no)


class User_Company(model):
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.ForeignKey(User, related_name="usr_comp_usrid", on_delete=models.DO_NOTHING)
    company_id = models.ForeignKey(Company, related_name="company_id", on_delete=models.DO_NOTHING)
    role_id =models.ForeignKey(Role, related_name="role_id", on_delete=models.DO_NOTHING)



class Workhour(model):
    user_company_id = models.ForeignKey(User_Company, related_name="user_comp_id", on_delete=models.DO_NOTHING, blank =True)
    date_from = models.DateTimeField()
    date_until = models.DateTimeField()

    def __str__(self):
        return "User company id: {}, From: {}, Until: {}".format(self.user_company_id, self.date_from, self.date_until)
