# Generated by Django 2.2.4 on 2019-10-25 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='it',
            name='ip_MRN',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='it',
            name='ip_cg',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='it',
            name='ip_first',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='it',
            name='ip_last',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='it',
            name='ip_tg',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='nit',
            name='p_MRN',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='nit',
            name='p_cg',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='nit',
            name='p_first',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='nit',
            name='p_last',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='nit',
            name='p_tg',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='nurses',
            name='n_UNIT',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='nurses',
            name='n_first',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='nurses',
            name='n_last',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]