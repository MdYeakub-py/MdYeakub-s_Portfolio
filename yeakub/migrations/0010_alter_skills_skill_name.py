# Generated by Django 4.1.6 on 2023-02-25 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yeakub', '0009_alter_skills_skill_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='skill_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
