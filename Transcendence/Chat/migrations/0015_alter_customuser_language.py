# Generated by Django 4.2.9 on 2024-03-20 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0014_alter_customuser_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='language',
            field=models.CharField(choices=[('FR', 'French'), ('EN', 'English'), ('TR', 'Turkish')], default='EN', max_length=2),
        ),
    ]
