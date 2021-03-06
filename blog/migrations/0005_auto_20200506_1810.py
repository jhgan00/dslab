# Generated by Django 3.0.5 on 2020-05-06 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-create_dt']},
        ),
        migrations.AddField(
            model_name='comment',
            name='create_dt',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='CREATE DATE'),
        ),
        migrations.AddField(
            model_name='comment',
            name='modify_dt',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='MODIFY DATE'),
        ),
        migrations.AddField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
