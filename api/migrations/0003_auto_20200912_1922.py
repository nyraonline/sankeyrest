# Generated by Django 3.0.5 on 2020-09-12 13:52

from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200912_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='_id',
            field=djongo.models.fields.ObjectIdField(auto_created=True, default='emp2020-09-12 13:52:19.747311+00:00', primary_key=True, serialize=False),
        ),
    ]
