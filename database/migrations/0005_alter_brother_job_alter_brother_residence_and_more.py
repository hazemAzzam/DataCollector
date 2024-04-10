# Generated by Django 5.0.3 on 2024-04-09 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_remove_relative_date_of_birth_relative_qualification_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brother',
            name='job',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Job'),
        ),
        migrations.AlterField(
            model_name='brother',
            name='residence',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Residence'),
        ),
        migrations.AlterField(
            model_name='current_wife_data',
            name='job',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Job'),
        ),
        migrations.AlterField(
            model_name='current_wife_data',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='current_wife_data',
            name='qualification',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Qualification'),
        ),
        migrations.AlterField(
            model_name='current_wife_data',
            name='residence',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Residence'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='job',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Job'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='residence',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Residence'),
        ),
        migrations.AlterField(
            model_name='relative',
            name='job',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Job'),
        ),
        migrations.AlterField(
            model_name='relative',
            name='residence',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Residence'),
        ),
        migrations.AlterField(
            model_name='supports',
            name='date_of_birth',
            field=models.DateField(blank=True, verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='supports',
            name='national_number',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='National Number'),
        ),
        migrations.AlterField(
            model_name='supports',
            name='notes',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='wife_borther',
            name='job',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Job'),
        ),
        migrations.AlterField(
            model_name='wife_borther',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='wife_borther',
            name='qualification',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Qualification'),
        ),
        migrations.AlterField(
            model_name='wife_borther',
            name='residence',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Residence'),
        ),
    ]
