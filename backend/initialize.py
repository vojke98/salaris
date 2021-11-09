import os
import shutil

def create_super_user():

    if os.path.exists('create_super_user.sh'):
        cmd = 'create_super_user.sh'
        os.system(cmd)
    else:
        print('create_super_user.sh doesnt exist\n')


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


def load_initial_data():
    os.system('python manage.py loaddata initial_data.json')

clear_migrations()
initialize()
create_super_user()
load_initial_data()
os.system('python manage.py runserver')