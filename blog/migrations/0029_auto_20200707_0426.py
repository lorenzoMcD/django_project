# Generated by Django 3.0.5 on 2020-07-07 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_folder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='wordlist',
        ),
        migrations.AddField(
            model_name='wordlist',
            name='folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Folder'),
        ),
    ]
