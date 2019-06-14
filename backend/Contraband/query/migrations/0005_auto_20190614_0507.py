# Generated by Django 2.2.2 on 2019-06-14 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0004_auto_20190613_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='hash_code',
            field=models.CharField(default='WXqg5PFyxQk75WMlmhPhfOrIcU4AuYxR2KXlnLrnk8pwmkCRdFnHgYCIPMlVvL03', max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='queryfilter',
            name='query',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Query', unique=True),
        ),
    ]
