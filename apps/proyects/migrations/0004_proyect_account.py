# Generated by Django 4.2.1 on 2023-05-30 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('proyects', '0003_alter_proyect_options_alter_task_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyect',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.account'),
        ),
    ]
