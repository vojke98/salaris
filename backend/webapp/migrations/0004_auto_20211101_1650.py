# Generated by Django 3.2.9 on 2021-11-01 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_staff_gender'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Companies',
            new_name='Companie',
        ),
        migrations.RenameModel(
            old_name='Workhours',
            new_name='Workhour',
        ),
    ]
