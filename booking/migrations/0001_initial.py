# Generated by Django 3.1.1 on 2020-09-27 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('slot_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('slot_title', models.CharField(max_length=40)),
                ('slot_lag', models.FloatField()),
                ('slot_long', models.FloatField()),
                ('slot_charges', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.CharField(max_length=15, null=True, unique=True)),
                ('cost', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('start_timing', models.DateTimeField()),
                ('end_timing', models.DateTimeField(blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('slot_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.slot')),
            ],
        ),
    ]
