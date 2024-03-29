# Generated by Django 2.2.3 on 2019-11-20 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20191120_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='reviews',
            field=models.ManyToManyField(to='main_app.Review'),
        ),
    ]
