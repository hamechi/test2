# Generated by Django 4.0.3 on 2022-03-21 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_most_post_image_post_is_deleted'),
        ('pay', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=30)),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='post/%d/')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('ma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='helloo', to='post.post')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('ti', models.CharField(max_length=30)),
                ('bo', models.TextField()),
                ('ma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hello', to='post.post')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Most',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]