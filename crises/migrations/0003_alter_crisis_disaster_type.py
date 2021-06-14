# Generated by Django 3.2.4 on 2021-06-14 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crises', '0002_alter_crisis_disaster_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crisis',
            name='disaster_type',
            field=models.CharField(choices=[('Tsunami', 'Tsunami'), ('Hurricane', 'Hurricaine'), ('Flood', 'Flood'), ('Earthquake', 'Earthquake'), ('War', 'War'), ('Pandemic', 'Pandemic'), ('Wildfire', 'Wildfire')], max_length=20),
        ),
    ]
