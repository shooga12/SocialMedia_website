# Generated by Django 4.2.3 on 2023-07-20 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_moviedata_typ'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='typ',
            field=models.CharField(default='action', max_length=200),
        ),
    ]
