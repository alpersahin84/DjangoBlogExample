# Generated by Django 4.1.5 on 2023-02-11 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_rename_aricle_comment_article'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
    ]
