# Generated by Django 3.2.6 on 2022-05-25 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isay', '0005_alter_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='services',
            field=models.CharField(choices=[('C', 'Counseling'), ('T', 'Psychological Testing'), ('F', 'Career Guidance, Graduate Placement and Follow-up'), ('H', 'Human Development Services'), ('P', 'Peer Facilitating Program')], default='C', max_length=100),
        ),
    ]