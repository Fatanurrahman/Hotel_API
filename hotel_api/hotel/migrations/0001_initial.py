# Generated by Django 2.0.3 on 2018-12-20 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=250)),
                ('harga', models.IntegerField()),
                ('jumlah_review', models.IntegerField()),
                ('lokasi', models.CharField(max_length=50)),
            ],
        ),
    ]