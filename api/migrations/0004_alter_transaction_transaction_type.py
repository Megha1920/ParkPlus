# Generated by Django 5.0 on 2023-12-26 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_schedule_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('debit', 'Debit'), ('credit', 'Credit')], max_length=10),
        ),
    ]
