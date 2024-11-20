# Generated by Django 4.2 on 2024-11-20 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name': 'слайдер', 'verbose_name_plural': 'слайдеры'},
        ),
        migrations.AlterModelOptions(
            name='sliderentry',
            options={'ordering': ['number'], 'verbose_name': 'элемент слайдера', 'verbose_name_plural': 'элементы слайдеров'},
        ),
        migrations.AddField(
            model_name='slider',
            name='slug',
            field=models.SlugField(default='start_page_slider', max_length=255, unique=True, verbose_name='короткое уникальное название (slug)'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='name',
            field=models.CharField(max_length=255, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='sliderentry',
            name='image',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, related_name='entry_image', to=settings.FILER_IMAGE_MODEL, verbose_name='картинка'),
        ),
        migrations.AlterField(
            model_name='sliderentry',
            name='number',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='порядок'),
        ),
        migrations.AlterField(
            model_name='sliderentry',
            name='slider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entry_slider', to='slider.slider', verbose_name='слайдер'),
        ),
    ]
