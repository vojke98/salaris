from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING

model = models.Model

# Create your models here.
class City(model):
    post_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}, {}".format(self.post_no, self.name)

    class Meta:
        verbose_name_plural = 'Cities'


class Address(model):
    house_no = models.CharField(max_length=10)
    street = models.CharField(max_length=200)
    city = models.ForeignKey(City, related_name="address_city", on_delete=CASCADE)

    def __str__(self):
        return "{} {}, {}".format(self.street, self.house_no, self.city)

    class Meta:
        verbose_name_plural = 'Addresses'


class Company(model):
    reference_key = models.CharField(max_length=30, unique=True)
    tax_no = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, related_name="company_address", on_delete=DO_NOTHING, blank=True)
    company_about_info = models.TextField(blank=True)

    def __str__(self):
        return "{}, {}".format(self.name, self.address,  self.tax_no)

    class Meta:
        verbose_name_plural = 'Companies'


class Role(model):
    company = models.ForeignKey(Company, related_name="role_company", on_delete=CASCADE)
    name = models.CharField(max_length=20)
    min_hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    is_admin = models.BooleanField()

    def __str__(self):
        return "{} at {} has minimal hourly rate of {}€.".format(self.name, self.company, self.min_hourly_rate)


class User(model):
    tax_no = models.TextField(blank=False, unique=True)
    first_name = models.TextField(blank=False)
    last_name = models.TextField(blank=False)
    address = models.ForeignKey(Address, related_name="user_address", on_delete=DO_NOTHING, blank=True)
    email = models.EmailField(blank=False, unique=True)
    company = models.ForeignKey(Company, related_name='user_company', on_delete=DO_NOTHING, blank=True, null=True)
    role = models.ForeignKey(Role, related_name='user_role', on_delete=DO_NOTHING, blank=True, null=True)
    qualifications = models.TextField(blank=True)
    user_about_info = models.TextField(blank=True)
    password = models.TextField(blank=False)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)


class Workhour(model):
    user = models.ForeignKey(User, related_name="workh_user", on_delete=DO_NOTHING, blank=True)
    company = models.ForeignKey(Company, related_name="workh_company", on_delete=DO_NOTHING, blank=True)
    date_from = models.DateTimeField()
    date_until = models.DateTimeField()
    hourly_rate_at_the_time = models.DecimalField(max_digits=10, decimal_places=2)
    warning = models.BooleanField(default=False)

    def __str__(self):
        return "{} worked in {}, in period from {} - {}".format(self.user, self.company,self.date_from, self.date_until)


class JoinRequest(model):
    user = models.ForeignKey(User, related_name="joinReq_user", on_delete=CASCADE)
    company = models.ForeignKey(Company, related_name="joinReq_company", on_delete=CASCADE)
    request_date = models.DateTimeField()
    response_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=8, default="PENDING") #APPROVED, PENDING, REJECTED

    def __str__(self):
        return "{} requested to join {} on '{}'".format(self.user, self.company, self.request_date)