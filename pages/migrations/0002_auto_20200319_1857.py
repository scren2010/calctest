# Generated by Django 3.0.4 on 2020-03-19 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TimeField()),
                ('cover', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterModelOptions(
            name='calchscode',
            options={'ordering': ('id',)},
        ),
        migrations.AlterField(
            model_name='calchscode',
            name='rate',
            field=models.CharField(max_length=255, verbose_name='Ставка ввозной таможенной пошлины'),
        ),
    ]
