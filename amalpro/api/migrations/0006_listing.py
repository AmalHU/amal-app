# Generated by Django 4.0.3 on 2022-04-12 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_serviceproviders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Charges', models.IntegerField()),
                ('serviceType', models.CharField(choices=[('T1', 'Type1'), ('t2', 'Type2')], max_length=2)),
            ],
        ),
    ]