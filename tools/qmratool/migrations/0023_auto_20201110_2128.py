# Generated by Django 3.1.1 on 2020-11-10 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qmratool', '0022_auto_20201110_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riskassessment',
            name='exposure',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='qmratool.exposure'),
        ),
    ]
