# Generated by Django 3.1.6 on 2021-02-04 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=155)),
                ('image', models.FileField(blank=True, upload_to='')),
            ],
        ),
    ]
