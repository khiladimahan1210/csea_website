# Generated by Django 2.2 on 2019-10-07 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_event_model_facebook_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_model',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]