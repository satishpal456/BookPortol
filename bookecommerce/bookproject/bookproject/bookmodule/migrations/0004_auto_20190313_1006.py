# Generated by Django 2.1 on 2019-03-13 10:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookmodule', '0003_sellerprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOfUser', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('userAddress', models.CharField(max_length=30, null=True, verbose_name='Address')),
                ('usermobile', models.CharField(max_length=30, null=True, verbose_name='Mobile No')),
                ('email', models.EmailField(max_length=70, null=True, unique=True, verbose_name='E-mail')),
                ('userProfile1', models.FileField(blank=True, null=True, upload_to='userProfile/')),
                ('user', models.OneToOneField(on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='sellerprofile',
            name='selleremail',
        ),
    ]
