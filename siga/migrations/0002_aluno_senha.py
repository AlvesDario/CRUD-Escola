# Generated by Django 2.2 on 2019-05-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siga', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='senha',
            field=models.CharField(default='123456', max_length=6),
        ),
    ]
