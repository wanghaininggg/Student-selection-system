# Generated by Django 2.0.2 on 2018-03-04 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20180304_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='selectcourse',
            name='selectCourseStatus',
            field=models.CharField(choices=[('0', '开课'), ('1', '未开课')], default='0', max_length=3, verbose_name='课程状态'),
        ),
    ]
