# Generated by Django 3.2.16 on 2022-12-09 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='years_of_experience',
            field=models.CharField(choices=[('LESS THAN 1 YEAR', 'Less than 1 year'), ('1 YEAR', '1 Year'), ('2 YEAR', '2 Year'), ('3 YEAR', '3 Year'), ('4 YEAR', '4 Year'), ('5 OR MORE YEAR', '5 or More year')], default='Less than 1 year', max_length=50),
        ),
    ]
