# Generated by Django 4.1.2 on 2022-10-30 14:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendmail',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('ec091880-cc20-4ccc-989f-aa6f7ab35a22'), editable=False),
        ),
    ]
