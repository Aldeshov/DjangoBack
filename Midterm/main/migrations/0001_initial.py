# Generated by Django 3.1.7 on 2021-03-20 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookjournalbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.bookjournalbase')),
                ('num_pages', models.IntegerField()),
                ('genre', models.CharField(max_length=255)),
            ],
            bases=('base.bookjournalbase',),
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('bookjournalbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.bookjournalbase')),
                ('type', models.SmallIntegerField(choices=[(0, 'Bullet'), (1, 'Food'), (2, 'Travel'), (3, 'Sport')], default=0)),
                ('publisher', models.IntegerField()),
            ],
            bases=('base.bookjournalbase',),
        ),
    ]
