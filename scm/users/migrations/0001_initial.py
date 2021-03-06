# Generated by Django 2.0.2 on 2018-03-03 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='用户编号')),
                ('userName', models.CharField(max_length=20, verbose_name='用户姓名')),
                ('userPassword', models.CharField(max_length=20, verbose_name='用户密码')),
                ('userIdentity', models.CharField(choices=[('教师', '教师'), ('学生', '学生')], default='学生', max_length=2, verbose_name='用户身份')),
                ('userAddTime', models.DateField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['-userAddTime'],
            },
        ),
    ]
