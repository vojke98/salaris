# Generated by Django 3.2.9 on 2021-11-09 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_no', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('post_no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('tax_no', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('address', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='company_address', to='webapp.address')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('min_hourly_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_admin', models.BooleanField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_company', to='webapp.company')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_no', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_address', to='webapp.address')),
                ('company', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_company', to='webapp.company')),
                ('role', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_role', to='webapp.role')),
            ],
        ),
        migrations.CreateModel(
            name='Workhour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateTimeField()),
                ('date_until', models.DateTimeField()),
                ('hourly_rate_at_the_time', models.DecimalField(decimal_places=2, max_digits=10)),
                ('company', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='workh_company', to='webapp.company')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='workh_user', to='webapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leaveReq_company', to='webapp.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leaveReq_user', to='webapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='JoinRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joinReq_company', to='webapp.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joinReq_user', to='webapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address_city', to='webapp.city'),
        ),
    ]
