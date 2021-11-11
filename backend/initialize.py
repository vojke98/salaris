import os
import shutil
import socket
import subprocess

def create_super_user():
    filename = "./create_super_user.sh"
    if not os.path.exists(filename):
        bash = "#!/bin/bash\necho \"from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@salaris.com', '#tpo2021')\" | python manage.py shell"
        with open(filename, "w") as f:
            f.write(bash)

    cmd = 'create_super_user.sh' if os.name == 'nt' else './create_super_user.sh'
    os.system(cmd)


def clear_migrations():
    try:
        shutil.rmtree("./webapp/migrations")
    except OSError as e:
        pass #print("Error: %s - %s." % (e.filename, e.strerror))

    if os.path.exists("./db.sqlite3"):
        os.remove("./db.sqlite3")

    filename = "./webapp/migrations/__init__.py"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write("")


def initialize():
    os.system('python manage.py makemigrations')
    os.system('python manage.py migrate')


def load_dummy_data():
    filename = "./dummy_data.json"
    if not os.path.exists(filename):
        data = '[{"model":"webapp.city","pk":1,"fields":{"post_no":1000,"name":"Ljubljana"}},{"model":"webapp.city","pk":2,"fields":{"post_no":2000,"name":"Maribor"}},{"model":"webapp.city","pk":3,"fields":{"post_no":4000,"name":"Kranj"}},{"model":"webapp.address","pk":1,"fields":{"house_no":"51a","street":"Gerbi\u010deva ulica 51a","city":1000}},{"model":"webapp.address","pk":2,"fields":{"house_no":"2","street":"Ro\u017ena dolina cesta V","city":1000}},{"model":"webapp.address","pk":3,"fields":{"house_no":"50","street":"Ne znam za Dinu","city":1000}},{"model":"webapp.address","pk":4,"fields":{"house_no":"1","street":"Tr\u017ea\u0161ka cesta","city":1000}},{"model":"webapp.address","pk":5,"fields":{"house_no":"69","street":"Neka cesta","city":4000}},{"model":"webapp.company","fields":{"id":"sal0123456","tax_no":"SI01234567","name":"Salaris","address":4}},{"model":"webapp.company","fields":{"id":"sra0123456","tax_no":"SI12345678","name":"Njesra v2","address":5}},{"model":"webapp.role","pk":1,"fields":{"company":"sal0123456","name":"CEO","min_hourly_rate":50,"is_admin":true}},{"model":"webapp.role","pk":2,"fields":{"company":"sal0123456","name":"MANAGER","min_hourly_rate":20,"is_admin":true}},{"model":"webapp.role","pk":3,"fields":{"company":"sal0123456","name":"WORKER","min_hourly_rate":10,"is_admin":false}},{"model":"webapp.role","pk":4,"fields":{"company":"sra0123456","name":"CEO","min_hourly_rate":4.99,"is_admin":true}},{"model":"webapp.user","pk":1,"fields":{"tax_no":"01234567","first_name":"Dejan","last_name":"Vojinovi\u0107","email":"dv@gmail.com","address":1,"company":"sal0123456","role":3}},{"model":"webapp.user","pk":2,"fields":{"tax_no":"12345678","first_name":"Ademir","last_name":"Jusi\u0107","email":"aj@gmail.com","address":2,"company":"sal0123456","role":1}},{"model":"webapp.user","pk":3,"fields":{"tax_no":"23456789","first_name":"Dino","last_name":"\u010celikovi\u0107","email":"dc@gmail.com","address":3,"company":"sal0123456","role":2}},{"model":"webapp.user","pk":4,"fields":{"tax_no":"34567890","first_name":"Janez","last_name":"Novak","email":"jn@gmail.com","address":3,"company":"sra0123456","role":2}},{"model":"webapp.workhour","pk":1,"fields":{"date_from":"2021-11-7 08:00:00.000000-08:00","date_until":"2021-11-7 16:00:00.000000-08:00","company":"sal0123456","user":1,"hourly_rate_at_the_time":50}},{"model":"webapp.workhour","pk":2,"fields":{"date_from":"2021-11-8 08:00:00.000000-08:00","date_until":"2021-11-8 16:00:00.000000-08:00","company":"sal0123456","user":1,"hourly_rate_at_the_time":50}},{"model":"webapp.workhour","pk":3,"fields":{"date_from":"2021-11-7 8:00:00.000000-08:00","date_until":"2021-11-7 16:00:00.000000-08:00","company":"sal0123456","user":2,"hourly_rate_at_the_time":50}},{"model":"webapp.workhour","pk":4,"fields":{"date_from":"2021-11-9 08:00:00.000000-08:00","date_until":"2021-11-9 16:00:00.000000-08:00","company":"sal0123456","user":2,"hourly_rate_at_the_time":50}},{"model":"webapp.workhour","pk":5,"fields":{"date_from":"2021-11-8 08:00:00.000000-08:00","date_until":"2021-11-8 16:00:00.000000-08:00","company":"sal0123456","user":3,"hourly_rate_at_the_time":50}},{"model":"webapp.workhour","pk":6,"fields":{"date_from":"2021-11-9 08:00:00.000000-08:00","date_until":"2021-11-9 16:00:00.000000-08:00","company":"sal0123456","user":3,"hourly_rate_at_the_time":50}},{"model":"webapp.joinRequest","pk":1,"fields":{"user":4,"company":"sra0123456","request_date":"2021-11-9 16:00:00.000000-08:00"}},{"model":"webapp.leaveRequest","pk":1,"fields":{"user":1,"company":"sal0123456","request_date":"2021-11-9 16:00:00.000000-08:00"}}]'
        with open(filename, "w", encoding='utf-8') as f:
            f.write(data)

    os.system('python manage.py loaddata dummy_data.json')

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

clear_migrations()
initialize()
create_super_user()
load_dummy_data()
cmd = 'python manage.py runserver ' + get_ip() + ':8000'
os.system(cmd)