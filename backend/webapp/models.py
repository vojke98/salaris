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


class Staff(model):
    tax_no = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.ForeignKey(Role, related_name="staff_role", on_delete=DO_NOTHING)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.ForeignKey(Address, related_name="staff_adr", on_delete=models.DO_NOTHING)
    email = models.EmailField()
    gender = models.CharField(max_length=1) #M/F
    phone_no = models.CharField(max_length=20)

    def __str__(self):
        return "{}, {}\n{} {}$\n{} {}".format(self.last_name, self.first_name, self.role, self.hourly_rate, self.email, self.phone_no)


class Company(model):
    tax_no = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, related_name="comp_adr", on_delete=models.DO_NOTHING)
    ceo = models.ForeignKey(Staff, related_name="comp_ceo", on_delete=models.DO_NOTHING)

    def __str__(self):
        return "Name: {},\nAddress: {},\nCEO: {}\nTax number: {}".format(self.name, self.address, self.ceo, self.tax_no)


class Workhour(model):
    staff_id = models.ForeignKey(Staff, related_name="work_staff", on_delete=models.DO_NOTHING)
    comp_id = models.ForeignKey(Company, related_name="work_comp", on_delete=models.DO_NOTHING)
    date_from = models.DateTimeField()
    date_until = models.DateTimeField()

    def __str__(self):
        return "Company: {}, Worker: {}, From: {}, Until: {}".format(self.comp_id, self.staff_id, self.date_from, self.date_until)
