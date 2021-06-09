# Generated by Django 3.2.3 on 2021-05-25 02:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_ids', models.CharField(max_length=50)),
                ('movie_id', models.IntegerField()),
                ('overview', models.TextField()),
                ('poster_path', models.CharField(max_length=500)),
                ('release_date', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('vote_average', models.FloatField()),
                ('like_users', models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]