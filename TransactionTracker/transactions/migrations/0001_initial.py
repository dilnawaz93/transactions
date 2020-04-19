# Generated by Django 3.0.5 on 2020-04-14 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'transaction_type',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.BigIntegerField(unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('parent_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='transactions.Transaction')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.TransactionType')),
            ],
            options={
                'db_table': 'transaction',
            },
        ),
    ]
