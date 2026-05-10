import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_postgalleryimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postgalleryimage',
            name='image',
            field=models.ImageField(blank=True, upload_to='posts/gallery/'),
        ),
        migrations.AddField(
            model_name='postgalleryimage',
            name='video',
            field=models.FileField(
                blank=True,
                upload_to='posts/gallery/videos/',
                validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'webm', 'mov'])],
            ),
        ),
    ]
