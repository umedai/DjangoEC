# Generated by Django 3.1.4 on 2022-06-19 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='department',
        ),
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, max_length=30, verbose_name='住所'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='tel',
            field=models.CharField(blank=True, max_length=30, verbose_name='電話番号'),
        ),
    ]
