# Generated by Django 4.1.5 on 2023-01-31 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booktracker', '0006_alter_book_author_alter_bookusers_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Статус книги',
            },
        ),
        migrations.RemoveField(
            model_name='bookusers',
            name='complete',
        ),
        migrations.AddField(
            model_name='bookusers',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='booktracker.bookstatus'),
            preserve_default=False,
        ),
    ]