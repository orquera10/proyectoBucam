from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_image_add_body_and_banner_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostGalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='posts/gallery/')),
                ('alt_text', models.CharField(blank=True, max_length=180)),
                ('order', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='core.post')),
            ],
            options={
                'verbose_name': 'imagen de galeria',
                'verbose_name_plural': 'imagenes de galeria',
                'ordering': ['order', 'created_at'],
            },
        ),
    ]
