# Generated by Django 4.2.2 on 2023-07-14 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0011_person_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='img1',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
