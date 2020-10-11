# Generated by Django 3.0.3 on 2020-10-06 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('choice_1', models.CharField(max_length=30)),
                ('choice_2', models.CharField(max_length=30)),
                ('choice_3', models.CharField(max_length=30)),
                ('choice_4', models.CharField(max_length=30)),
                ('correct_ans', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]