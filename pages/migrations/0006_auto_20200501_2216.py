# Generated by Django 3.0.4 on 2020-05-01 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20200320_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagesite',
            name='cover',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='imagesite',
            name='title',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
