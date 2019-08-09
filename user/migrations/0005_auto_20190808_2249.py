# Generated by Django 2.2.4 on 2019-08-08 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190808_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.AddField(
            model_name='profile',
            name='height',
            field=models.CharField(blank=True, max_length=10, verbose_name='키'),
        ),
        migrations.AddField(
            model_name='profile',
            name='nickname',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='weight',
            field=models.CharField(blank=True, max_length=10, verbose_name='몸무게'),
        ),
        migrations.AlterModelTable(
            name='user',
            table='auth_user',
        ),
    ]