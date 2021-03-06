# Generated by Django 2.0.7 on 2019-04-24 07:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('oneid_meta', '0020_company_dingconfig'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('name_cn', models.CharField(blank=True, default='', max_length=255, verbose_name='中文简称')),
                ('fullname_cn', models.CharField(blank=True, default='', max_length=255, verbose_name='中文全称')),
                ('name_en', models.CharField(blank=True, default='', max_length=255, verbose_name='英文简称')),
                ('fullname_en', models.CharField(blank=True, default='', max_length=255, verbose_name='英文全称')),
                ('icon', models.CharField(blank=True, default='', max_length=1024, verbose_name='图标')),
                ('address', models.CharField(blank=True, default='', max_length=255, verbose_name='办公地址')),
                ('domain', models.CharField(blank=True, default='', max_length=255, verbose_name='公司主页')),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='company_config', to='sites.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='company',
            name='site',
        ),
        migrations.AlterField(
            model_name='dingconfig',
            name='site',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ding_config', to='sites.Site'),
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]
