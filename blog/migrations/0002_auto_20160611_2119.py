# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-11 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=100, verbose_name='Sender name')),
                ('sender_age', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Sender age')),
                ('partner_name', models.CharField(max_length=100, verbose_name='Partner name')),
                ('partner_age', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Partner age')),
                ('story', models.TextField(blank=True, verbose_name='Story')),
                ('relationship_time_number', models.DecimalField(blank=True, decimal_places=0, max_digits=2, verbose_name='Relationship time number')),
                ('relationship_time', models.CharField(choices=[('Days', 'Days'), ('Weeks', 'Weeks'), ('Months', 'Months'), ('Years', 'Years')], default='Days', max_length=100, verbose_name='Date Period')),
                ('lifestyle', models.CharField(blank=True, choices=[('Sporting', 'Sporting'), ('Adventurous', 'Adventurous'), ('Homelike', 'Homelike'), ('Partier', 'Partier'), ('Fitness', 'Fitness')], max_length=100, verbose_name='Lifestyle')),
                ('personality', models.CharField(max_length=100, verbose_name='Personality')),
                ('cost_pretension', models.DecimalField(blank=True, decimal_places=2, max_digits=3, verbose_name='Cost pretension')),
                ('ideal_place', models.CharField(max_length=100, verbose_name='Ideal place')),
                ('sender_email', models.EmailField(max_length=12, verbose_name='Sender email')),
                ('sender_phone', models.CharField(blank=True, max_length=12, verbose_name='Sender phone')),
                ('additional_info', models.TextField(blank=True, verbose_name='Additionl info')),
            ],
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='message',
            name='customer_email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Customer email'),
        ),
        migrations.AlterField(
            model_name='message',
            name='phone_email',
            field=models.CharField(blank=True, max_length=12, verbose_name='Phone email'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender_name',
            field=models.CharField(max_length=100, verbose_name='Sender name'),
        ),
    ]