# Generated by Django 4.1 on 2022-08-24 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artwork',
            options={'ordering': ['-data_end_look']},
        ),
        migrations.AddField(
            model_name='artwork',
            name='english_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Англиское название'),
        ),
        migrations.AddField(
            model_name='artwork',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='artwork',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер тома или сезона'),
        ),
        migrations.CreateModel(
            name='Image_Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images_artwork/', verbose_name='Снимоок')),
                ('artwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.artwork')),
            ],
        ),
    ]
