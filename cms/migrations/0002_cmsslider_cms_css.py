# Generated by Django 4.1.3 on 2022-12-05 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmsslider',
            name='cms_css',
            field=models.BooleanField(default=False, verbose_name='Main image?'),
        ),
    ]
