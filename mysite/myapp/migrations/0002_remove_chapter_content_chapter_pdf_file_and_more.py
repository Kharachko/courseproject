# Generated by Django 5.0.6 on 2024-05-18 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='content',
        ),
        migrations.AddField(
            model_name='chapter',
            name='pdf_file',
            field=models.FileField(default=None, upload_to='chapters/'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='number',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='title',
            field=models.CharField(default='Chapter Title', max_length=200),
        ),
        migrations.AlterField(
            model_name='manga',
            name='author',
            field=models.CharField(default='Unknown Author', max_length=200),
        ),
        migrations.AlterField(
            model_name='manga',
            name='description',
            field=models.TextField(default='No description available'),
        ),
    ]
