# Generated by Django 4.1.6 on 2023-02-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yeakub', '0010_alter_skills_skill_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
