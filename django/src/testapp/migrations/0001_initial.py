# Generated by Django 2.1.5 on 2021-06-25 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='testapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('otherstuff', models.DecimalField(decimal_places=2, max_digits=7)),
                ('desc2', models.TextField(default='richard likes lolis')),
            ],
        ),
    ]
