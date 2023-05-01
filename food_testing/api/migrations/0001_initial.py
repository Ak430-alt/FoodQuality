# Generated by Django 3.2.8 on 2022-11-02 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                #('name', models.CharField(max_length = 256 , null= True)),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('methane', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
            ],
        ),
    ]
