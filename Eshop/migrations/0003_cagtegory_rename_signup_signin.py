# Generated by Django 4.1 on 2022-09-13 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0002_remove_signup_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='cagtegory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='signup',
            new_name='signin',
        ),
    ]
