# Generated by Django 3.0.5 on 2020-07-27 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bodydetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=40)),
                ('weight', models.CharField(default='', max_length=50)),
                ('blood', models.CharField(default='', max_length=40)),
                ('evidence', models.CharField(default='', max_length=40)),
                ('body', models.FileField(upload_to='files/pdfs/')),
            ],
            options={
                'db_table': 'bodydetails',
            },
        ),
    ]