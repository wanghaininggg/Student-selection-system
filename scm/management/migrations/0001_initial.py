# Generated by Django 2.0.2 on 2018-03-03 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('classID', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='班级编号')),
                ('className', models.CharField(max_length=30, verbose_name='班级名称')),
                ('classGrade', models.CharField(default='2017', max_length=4, verbose_name='班级年级')),
            ],
            options={
                'verbose_name': '班级',
                'verbose_name_plural': '班级',
            },
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroomName', models.CharField(max_length=30, verbose_name='教室名称')),
            ],
            options={
                'verbose_name': '教室',
                'verbose_name_plural': '教室',
            },
        ),
        migrations.CreateModel(
            name='ClassTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classTime', models.CharField(max_length=30, verbose_name='上课时间')),
            ],
            options={
                'verbose_name': '上课时间',
                'verbose_name_plural': '上课时间',
            },
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('instituteID', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='学院编号')),
                ('instituteName', models.CharField(max_length=30, verbose_name='学院名称')),
                ('institutePhohe', models.CharField(blank=True, max_length=20, null=True, verbose_name='学院电话')),
                ('instituteMailbox', models.EmailField(blank=True, max_length=254, null=True, verbose_name='学院邮箱')),
                ('instituteInformation', models.CharField(blank=True, max_length=1000, null=True, verbose_name='学院信息')),
            ],
            options={
                'verbose_name': '学院',
                'verbose_name_plural': '学院',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('majorID', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='专业编号')),
                ('majorName', models.CharField(max_length=30, verbose_name='专业名称')),
                ('majorInformation', models.CharField(blank=True, max_length=1000, null=True, verbose_name='学院信息')),
                ('majorInstitute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Institute', verbose_name='所在学院')),
            ],
            options={
                'verbose_name': '专业',
                'verbose_name_plural': '专业',
            },
        ),
        migrations.AddField(
            model_name='class',
            name='classInstitute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Institute', verbose_name='所在学院'),
        ),
        migrations.AddField(
            model_name='class',
            name='classMajor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Major', verbose_name='所在专业'),
        ),
    ]
