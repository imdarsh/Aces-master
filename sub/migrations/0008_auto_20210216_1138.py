# Generated by Django 3.1.6 on 2021-02-16 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub', '0007_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='option1',
        ),
        migrations.RemoveField(
            model_name='question',
            name='option2',
        ),
        migrations.RemoveField(
            model_name='question',
            name='option3',
        ),
        migrations.RemoveField(
            model_name='question',
            name='option4',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question',
        ),
    ]
