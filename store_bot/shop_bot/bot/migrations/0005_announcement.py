# Generated by Django 4.0.2 on 2022-03-21 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_alter_payment_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=2000)),
            ],
            options={
                'verbose_name': ('Announcement',),
                'verbose_name_plural': 'Announcements',
            },
        ),
    ]
