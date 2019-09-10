# Generated by Django 2.2.1 on 2019-09-10 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('short_id', models.SlugField(max_length=6, primary_key=True, serialize=False)),
                ('http_url', models.URLField()),
                ('publish_date', models.DateTimeField(auto_now=True)),
                ('count', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Urls',
            },
        ),
    ]
