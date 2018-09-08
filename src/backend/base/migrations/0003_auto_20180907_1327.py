# Generated by Django 2.0.5 on 2018-09-07 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20180707_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
                ('born', models.DateTimeField()),
                ('age', models.IntegerField()),
                ('prize', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='solution',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='task',
        ),
        migrations.RemoveField(
            model_name='task',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Solution',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
