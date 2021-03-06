# Generated by Django 2.2.8 on 2021-03-15 08:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riskdetails',
            name='risk_active_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='riskdetails',
            name='risk_amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='riskdetails',
            name='risk_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='insurance.RiskName', to_field='name'),
        ),
        migrations.AlterField(
            model_name='riskname',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
