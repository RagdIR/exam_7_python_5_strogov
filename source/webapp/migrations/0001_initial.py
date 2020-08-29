# Generated by Django 2.2 on 2020-08-29 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300, verbose_name='Вопрос')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создания опроса')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant', models.CharField(max_length=300, verbose_name='Текст варианта')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='poll', to='webapp.Poll', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Текст варианта',
                'verbose_name_plural': 'Тексты вариантов',
            },
        ),
    ]