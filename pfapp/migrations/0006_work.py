# Generated by Django 4.2.2 on 2023-07-09 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0005_rename_user_projects_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('desc', models.TextField(blank=True)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pfapp.person')),
            ],
        ),
    ]
