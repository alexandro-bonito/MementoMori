# Generated by Django 4.2.13 on 2024-10-01 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Memento', '0003_registrationcounter_visitorcounter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=74)),
            ],
        ),
        migrations.DeleteModel(
            name='RegistrationCounter',
        ),
        migrations.DeleteModel(
            name='VisitorCounter',
        ),
    ]
