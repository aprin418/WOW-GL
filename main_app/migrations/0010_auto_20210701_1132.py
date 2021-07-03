# Generated by Django 3.2.4 on 2021-07-01 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20210630_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gear',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='spec',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.RemoveField(
            model_name='spec',
            name='gear',
        ),
        migrations.AddField(
            model_name='spec',
            name='gear',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.gear'),
            preserve_default=False,
        ),
    ]