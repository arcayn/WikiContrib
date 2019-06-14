# Generated by Django 2.2.2 on 2019-06-14 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0005_auto_20190614_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='hash_code',
            field=models.CharField(default='mDOvrtJLymJcEYfSKj7Kys3UKQfio0QSpLyObpxFHxj1yTLmgkzyEN0N2FuYiZUL', max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='queryfilter',
            name='query',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='query.Query'),
        ),
    ]
