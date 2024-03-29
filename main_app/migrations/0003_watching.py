# Generated by Django 2.2.3 on 2019-11-19 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_movie_actors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='watch date')),
                ('time', models.CharField(choices=[('M', 'Morning'), ('A', 'Afternoon'), ('E', 'Evening')], default='M', max_length=1)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Movie')),
            ],
        ),
    ]
