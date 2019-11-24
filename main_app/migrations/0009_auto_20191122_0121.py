# Generated by Django 2.2.3 on 2019-11-22 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20191120_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Movie')),
            ],
        ),
    ]
