# Generated by Django 2.1.5 on 2019-04-13 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0014_auto_20190413_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='figure',
            field=models.FileField(upload_to=''),
        ),
    ]
