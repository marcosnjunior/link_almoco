# Generated by Django 5.0 on 2024-10-18 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('aberto', models.BooleanField(default=True)),
            ],
        ),
    ]
