# Generated by Django 3.2 on 2021-04-13 06:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0002_auto_20210413_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='QnA',
            fields=[
                ('qna_id', models.AutoField(primary_key=True, serialize=False)),
                ('qna_title', models.CharField(max_length=250)),
                ('qna_content', models.TextField()),
                ('qna_img', models.CharField(max_length=250)),
                ('book_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book')),
            ],
        ),
        migrations.CreateModel(
            name='QnA_Reply',
            fields=[
                ('reply_id', models.AutoField(primary_key=True, serialize=False)),
                ('reply_content', models.TextField()),
                ('qna_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menubar.qna')),
            ],
        ),
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('memo_id', models.AutoField(primary_key=True, serialize=False)),
                ('memo_title', models.CharField(max_length=250)),
                ('memo_content', models.TextField()),
                ('memo_date', models.DateTimeField(auto_now=True)),
                ('memo_img', models.CharField(max_length=250)),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book_article')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
