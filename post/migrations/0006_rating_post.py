# Generated by Django 3.1.4 on 2020-12-24 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='post.post'),
        ),
    ]
