# Generated by Django 4.2.2 on 2023-06-28 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_rename_student_student_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_info',
            name='image',
            field=models.ImageField(default='image', upload_to='images'),
            preserve_default=False,
        ),
    ]
