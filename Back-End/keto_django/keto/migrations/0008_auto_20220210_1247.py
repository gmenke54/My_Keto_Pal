# Generated by Django 3.2 on 2022-02-10 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keto', '0007_auto_20220210_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]