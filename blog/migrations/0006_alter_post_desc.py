# Generated by Django 5.1.1 on 2024-10-10 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='desc',
            field=models.TextField(),
        ),
    ]