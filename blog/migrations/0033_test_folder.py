# Generated by Django 3.0.5 on 2020-07-07 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20200707_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Folder'),
        ),
    ]
