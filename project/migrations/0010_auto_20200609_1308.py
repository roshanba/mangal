# Generated by Django 3.2.dev20200604053612 on 2020-06-09 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_auto_20200609_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='location',
            field=models.CharField(choices=[('Koulukatu', 'Koulukatu'), ('Ideapark', 'Ideapark')], default='Koulukatu', max_length=30),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='people',
            field=models.TextField(),
        ),
    ]
