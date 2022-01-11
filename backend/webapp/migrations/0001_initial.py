# Generated by Django 3.2.9 on 2022-01-11 12:34

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
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('post_no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_key', models.CharField(max_length=30)),
                ('tax_no', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('company_about_info', models.TextField(blank=True)),
                ('address', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='company_address', to='webapp.address')),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
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
                ('tax_no', models.TextField()),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('qualifications', models.TextField(blank=True)),
                ('user_about_info', models.TextField(blank=True)),
                ('password', models.TextField()),
                ('address', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_address', to='webapp.address')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_company', to='webapp.company')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_role', to='webapp.role')),
            ],
        ),
        migrations.CreateModel(
            name='Workhour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateTimeField()),
                ('date_until', models.DateTimeField()),
                ('hourly_rate_at_the_time', models.DecimalField(decimal_places=2, max_digits=10)),
                ('warning', models.BooleanField(default=False)),
                ('company', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='workh_company', to='webapp.company')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='workh_user', to='webapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='JoinRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField()),
                ('response_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(default='PENDING', max_length=8)),
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
