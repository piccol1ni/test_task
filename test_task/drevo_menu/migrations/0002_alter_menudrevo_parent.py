# Generated by Django 4.2.7 on 2023-11-14 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drevo_menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menudrevo',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drevo_menu.menudrevo'),
        ),
    ]
