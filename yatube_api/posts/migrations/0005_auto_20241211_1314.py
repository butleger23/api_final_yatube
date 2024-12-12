# Generated by Django 3.2.16 on 2024-12-11 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20241211_1311'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_user_follower',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='following',
            new_name='following_user',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following_user'), name='unique_user_follower'),
        ),
    ]
