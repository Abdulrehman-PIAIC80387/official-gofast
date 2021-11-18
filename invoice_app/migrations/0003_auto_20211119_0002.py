# Generated by Django 3.2.3 on 2021-11-18 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0002_auto_20211116_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='services',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='Customer Name')),
            ],
        ),
        migrations.AlterField(
            model_name='invoice',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
