# Generated by Django 2.2 on 2019-10-07 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_event_model_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_model',
            name='facebook_url',
            field=models.URLField(default='https://www.facebook.com/iitgcsea/'),
        ),
    ]
