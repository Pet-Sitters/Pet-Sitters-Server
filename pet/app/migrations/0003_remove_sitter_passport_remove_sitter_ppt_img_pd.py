# Generated by Django 5.0.6 on 2024-05-31 14:34

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_admin_employee_id_admin_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitter',
            name='passport',
        ),
        migrations.RemoveField(
            model_name='sitter',
            name='ppt_img',
        ),
        migrations.CreateModel(
            name='PD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_num', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('given_dt', models.DateField(null=True)),
                ('birth_dt', models.DateField(null=True)),
                ('given_code', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(999999)])),
                ('given_nm', models.CharField(max_length=255, null=True)),
                ('first_nm', models.CharField(max_length=255, null=True)),
                ('second_name', models.CharField(max_length=255, null=True)),
                ('sur_name', models.CharField(blank=True, max_length=255, null=True)),
                ('addr_nm', models.TextField(max_length=500, null=True)),
                ('pic_img', models.ImageField(null=True, upload_to='passports/')),
                ('sitter', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.sitter')),
            ],
        ),
    ]
