from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name = 'Note',
            fields = [
                ('uuid', models.UUIDField(name='UUID', auto_created=True, primary_key=True, serialize=False, )),
                ('header', models.TextField('Header', blank=True, max_length=128)),
                ('body', models.TextField('Body', blank=True)),
                ('image', models.ImageField('Image', blank=True)),
                ('created_date', models.DateTimeField('Created Date', auto_now_add=True)),
                ('last_modified', models.DateTimeField('Last Modified', auto_now=True))
            ]
        )
    ]
