# Generated by Django 3.2.7 on 2021-09-30 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('viajes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_destino', models.CharField(max_length=100)),
                ('viaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viajes.viaje')),
            ],
        ),
    ]
