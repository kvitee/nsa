# Generated by Django 4.1 on 2024-11-19 08:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'sliders',
            },
        ),
        migrations.CreateModel(
            name='SliderEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, related_name='entry_image', to=settings.FILER_IMAGE_MODEL)),
                ('slider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slider.slider')),
            ],
            options={
                'db_table': 'slider_entries',
                'ordering': ['number'],
            },
        ),
    ]