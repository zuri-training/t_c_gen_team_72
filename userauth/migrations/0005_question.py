# Generated by Django 4.0.6 on 2022-08-06 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0004_privacypolicyquestions_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]