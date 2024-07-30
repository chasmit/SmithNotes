from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name = 'Note',
            fields = [
                ('id', models.BigAutoField(name='id', auto_created=True, primary_key=True, serialize=False)),
                ('header', models.TextField('header', blank=True, max_length=128)),
                ('body', models.TextField('body', blank=True)),
                ('image', models.ImageField('image', blank=True)),
                ('created_date', models.DateTimeField('created date', auto_now_add=True)),
                ('last_modified', models.DateTimeField('last modified', auto_now=True))
            ]
        )
    ]
