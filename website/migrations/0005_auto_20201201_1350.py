# Generated by Django 3.1.3 on 2020-12-01 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20201128_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='class_room',
            name='room_icon',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='exam',
            name='day',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='website.day'),
        ),
        migrations.AddField(
            model_name='exam',
            name='subject',
            field=models.CharField(choices=[('Englisch', 'Englisch'), ('Deutsch', 'Deutsch'), ('Mathe', 'Mathe'), ('Französisch', 'Französisch'), ('Latein', 'Latein'), ('Spanisch', 'Spanisch'), ('Physik', 'Physik'), ('Chemie', 'Chemie'), ('Biologie', 'Biologie'), ('Erdkunde', 'Erdkunde'), ('Kunst', 'Kunst'), ('Musik', 'Musik'), ('Powi', 'Powi'), ('Geschichte', 'Geschichte'), ('Sport', 'Sport'), ('Evangelisch', 'Evangelisch'), ('Katholisch', 'Katholisch'), ('Ethik', 'Ethik'), ('LSD', 'LSD'), ('Informatik', 'Informatik'), ('Cambridge', 'Cambridge'), ('NaWi', 'NaWi')], default='Englisch', max_length=100),
        ),
        migrations.AddField(
            model_name='homework',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='class_room',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date of creation'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='description',
            field=models.TextField(max_length=5000, verbose_name='Exam topics'),
        ),
        migrations.AlterField(
            model_name='hw_subject',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('is_admin', 'User is Admin or not'), ('edit_content', 'User may edit content'), ('delete_content', 'User may delete content'), ('add_content', 'User may add content'), ('upload_image', 'User may upload images'), ('edit_room', 'User may change room settings')),
            },
        ),
        migrations.CreateModel(
            name='Exam_File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_file', models.FileField(upload_to='website/media')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.exam')),
            ],
        ),
        migrations.AddField(
            model_name='class_room',
            name='members',
            field=models.ManyToManyField(to='website.GroupMember'),
        ),
    ]
