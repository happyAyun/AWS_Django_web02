# Generated by Django 3.2 on 2021-04-20 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(blank=True, default='닉네임을 정해주세요', max_length=200),
        ),
    ]