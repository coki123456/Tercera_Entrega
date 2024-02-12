# Generated by Django 5.0.2 on 2024-02-12 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='posteos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('titulo', models.CharField(max_length=200)),
                ('texto', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
