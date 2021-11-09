from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING

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
    city = models.ForeignKey(City, related_name="address_city", on_delete=CASCADE)

    def __str__(self):
        return "{} {}, {}".format(self.street, self.house_no, self.city)


class Company(model):
    id = models.CharField(max_length=30, primary_key=True)
    tax_no = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, related_name="company_address", on_delete=DO_NOTHING, blank=True)

    def __str__(self):
        return "Name: {},\nAddress: {}\nTax number: {}".format(self.name, self.address,  self.tax_no)


class Role(model):
    company = models.ForeignKey(Company, related_name="role_company", on_delete=CASCADE)
    name = models.CharField(max_length=20)
    min_hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    is_admin = models.BooleanField()

    def __str__(self):
        return "{} in {} has minimal hourly rate {}{}.".format(self.name, self.company, self.min_hourly_rate, " and manages company" if self.is_admin else '')


class User(model):
    tax_no = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.ForeignKey(Address, related_name="user_address", on_delete=DO_NOTHING, blank=True)
    email = models.EmailField()
    company = models.ForeignKey(Company, related_name='user_company', on_delete=DO_NOTHING, blank=True)
    role = models.ForeignKey(Role, related_name='user_role', on_delete=DO_NOTHING, blank=True)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)


class Workhour(model):
    user = models.ForeignKey(User, related_name="workh_user", on_delete=DO_NOTHING, blank=True)
    company = models.ForeignKey(Company, related_name="workh_company", on_delete=DO_NOTHING, blank=True)
    date_from = models.DateTimeField()
    date_until = models.DateTimeField()
    hourly_rate_at_the_time = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "User: {}, Company: {}, From: {}, Until: {}".format(self.user, self.company,self.date_from, self.date_until)

class JoinRequest(model):
    user = models.ForeignKey(User, related_name="joinReq_user", on_delete=CASCADE)
    company = models.ForeignKey(Company, related_name="joinReq_company", on_delete=CASCADE)
    request_date = models.DateTimeField()

    def __str__(self):
        return "User '{}' requested to join '{}' on '{}'".format(self.user, self.company, self.request_date)

class LeaveRequest(model):
    user = models.ForeignKey(User, related_name="leaveReq_user", on_delete=CASCADE)
    company = models.ForeignKey(Company, related_name="leaveReq_company", on_delete=CASCADE)
    request_date = models.DateTimeField()

    def __str__(self):
        return "User '{}' requested to leave '{}' on '{}'".format(self.user, self.company, self.request_date)