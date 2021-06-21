# Generated by Django 3.2.4 on 2021-06-21 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crises', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ngoresource',
            name='ngo_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ngo_resources', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ngoresource',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ngo_resources', to='crises.resource'),
        ),
        migrations.AddField(
            model_name='crisis',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crises', to=settings.AUTH_USER_MODEL),
        ),
    ]
