# Generated by Django 2.2 on 2019-09-05 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=25500)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]