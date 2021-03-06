# Generated by Django 4.0.3 on 2022-04-12 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceProviders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullNameSP', models.CharField(max_length=255)),
                ('cnicSP', models.CharField(max_length=13)),
                ('addressSP', models.CharField(max_length=255)),
                ('citySP', models.CharField(max_length=25)),
                ('dobSP', models.DateField()),
                ('languageSP', models.CharField(choices=[('ENG', 'English'), ('UR', 'Urdu')], max_length=3)),
            ],
        ),
    ]
