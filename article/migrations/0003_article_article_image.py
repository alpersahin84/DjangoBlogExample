# Generated by Django 4.1.5 on 2023-02-01 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_article_author_alter_article_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Makaleye Fotoğraf Ekleyin'),
        ),
    ]
