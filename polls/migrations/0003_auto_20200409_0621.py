# Generated by Django 3.0.5 on 2020-04-09 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]