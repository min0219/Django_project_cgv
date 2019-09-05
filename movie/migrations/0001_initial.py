# Generated by Django 2.1.1 on 2018-11-28 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theater_name', models.CharField(max_length=30)),
                ('region_name2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Region')),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('movie_name2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='theater_name2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Theater'),
        ),
    ]