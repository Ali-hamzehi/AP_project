# Generated by Django 4.1.4 on 2023-07-09 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ulp', models.JSONField(blank=True, null=True)),
                ('attr', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
