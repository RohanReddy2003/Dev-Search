# Generated by Django 4.2.4 on 2023-08-15 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', max_length=2000, null=True, upload_to=''),
        ),
    ]
