# Generated by Django 2.0.6 on 2021-04-13 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('orders', models.IntegerField(default=1, verbose_name='排序')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='上次修改时间')),
                ('title', models.CharField(max_length=40, verbose_name='广告标题')),
                ('link', models.CharField(max_length=200, verbose_name='广告连接')),
                ('image_url', models.ImageField(blank=True, max_length=255, null=True, upload_to='banner')),
                ('re_mark', models.TextField(verbose_name='备注信息')),
            ],
            options={
                'verbose_name': '轮播广告',
                'verbose_name_plural': '轮播广告',
                'db_table': 'bz_banner',
            },
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('orders', models.IntegerField(default=1, verbose_name='排序')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='上次修改时间')),
                ('title', models.CharField(max_length=40, verbose_name='导航标题')),
                ('link', models.CharField(max_length=200, verbose_name='导航连接')),
                ('position', models.IntegerField(choices=[(1, '顶部导航'), (2, '尾部导航')], default=1, verbose_name='导航栏位置')),
                ('is_site', models.BooleanField(default=False, verbose_name='是否是站外地址')),
            ],
            options={
                'verbose_name': '导航菜单',
                'verbose_name_plural': '导航菜单',
                'db_table': 'bz_nav',
            },
        ),
    ]
