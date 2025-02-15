# Generated by Django 3.2.16 on 2023-01-12 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Point', '0003_category_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='slnum',
            new_name='sl_no',
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='question',
            name='ans',
        ),
        migrations.RemoveField(
            model_name='question',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='question',
            name='op_1',
        ),
        migrations.RemoveField(
            model_name='question',
            name='op_2',
        ),
        migrations.RemoveField(
            model_name='question',
            name='op_3',
        ),
        migrations.RemoveField(
            model_name='question',
            name='op_4',
        ),
        migrations.RemoveField(
            model_name='question',
            name='quest',
        ),
        migrations.RemoveField(
            model_name='question',
            name='sl_no',
        ),
        migrations.RemoveField(
            model_name='question',
            name='timeStamp',
        ),
        migrations.AddField(
            model_name='question',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
