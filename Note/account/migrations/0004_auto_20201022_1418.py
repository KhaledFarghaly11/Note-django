# Generated by Django 3.0.3 on 2020-10-22 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20201021_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debit', models.IntegerField()),
                ('amount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.AmountUser')),
            ],
        ),
        migrations.CreateModel(
            name='Debose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debose', models.IntegerField()),
                ('amount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.AmountUser')),
            ],
        ),
        migrations.DeleteModel(
            name='Debose_and_debit',
        ),
    ]
