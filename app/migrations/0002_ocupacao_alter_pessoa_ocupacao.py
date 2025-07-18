# Generated by Django 5.2.3 on 2025-07-08 12:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ocupacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True, verbose_name='Nome da Ocupação')),
            ],
            options={
                'verbose_name': 'Ocupação',
                'verbose_name_plural': 'Ocupações',
            },
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='ocupacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.ocupacao', verbose_name='Ocupação'),
        ),
    ]
