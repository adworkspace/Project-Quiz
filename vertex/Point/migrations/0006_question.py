# Generated by Django 3.2.16 on 2023-01-12 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Point', '0005_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('q_no', models.AutoField(primary_key=True, serialize=False)),
                ('quest', models.TextField(max_length=500)),
                ('op_1', models.CharField(max_length=50)),
                ('op_2', models.CharField(max_length=50)),
                ('op_3', models.CharField(max_length=50)),
                ('op_4', models.CharField(max_length=50)),
                ('ans', models.CharField(max_length=50)),
                ('desc', models.TextField(max_length=500)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
