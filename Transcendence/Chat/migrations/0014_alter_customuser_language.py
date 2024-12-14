# Generated by Django 4.2.9 on 2024-03-20 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0013_alter_customuser_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='language',
            field=models.CharField(choices=[('TR', 'Turkish'), ('FR', 'French'), ('EN', 'English')], default='EN', max_length=2),
        ),
    ]
