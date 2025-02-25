# Generated by Django 3.1.3 on 2022-01-18 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20220118_1309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='course_id',
            new_name='course',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question_id',
        ),
        migrations.AddField(
            model_name='choice',
            name='question_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.question'),
            preserve_default=False,
        ),
    ]
