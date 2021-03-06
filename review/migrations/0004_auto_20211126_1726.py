# Generated by Django 3.2.9 on 2021-11-26 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_auto_20211126_1724'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'Review', 'verbose_name_plural': 'Reviews'},
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='user',
        ),
        migrations.AddField(
            model_name='reviews',
            name='name',
            field=models.CharField(default=1, max_length=20, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reviews',
            name='text',
            field=models.TextField(verbose_name='Text'),
        ),
    ]
