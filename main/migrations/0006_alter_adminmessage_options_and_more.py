# Generated by Django 5.1.4 on 2025-06-05 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_adminmessage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adminmessage',
            options={'verbose_name': 'Wiadomość administratora', 'verbose_name_plural': 'Wiadomości administratora'},
        ),
        migrations.AlterModelOptions(
            name='notatkakalendarzowa',
            options={'verbose_name': 'Notatka', 'verbose_name_plural': 'Notatki'},
        ),
        migrations.AlterModelOptions(
            name='ocena',
            options={'verbose_name': 'Ocena', 'verbose_name_plural': 'Oceny'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profil', 'verbose_name_plural': 'Profile'},
        ),
        migrations.AlterModelOptions(
            name='wydarzenie',
            options={'verbose_name': 'Wydarzenie', 'verbose_name_plural': 'Wydarzenia'},
        ),
    ]
