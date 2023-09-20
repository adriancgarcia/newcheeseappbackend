# Generated by Django 4.2.5 on 2023-09-20 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheeses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cheese',
            old_name='details',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='cheese',
            old_name='subject',
            new_name='countryoforigin',
        ),
        migrations.AddField(
            model_name='cheese',
            name='typeofcheese',
            field=models.CharField(default='n/a', max_length=200),
            preserve_default=False,
        ),
    ]
