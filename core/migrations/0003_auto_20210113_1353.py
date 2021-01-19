# Generated by Django 3.1.3 on 2021-01-13 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_noticia_autorais_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticia',
            old_name='reportagem',
            new_name='reportagem_pt1',
        ),
        migrations.AddField(
            model_name='noticia',
            name='reportagem_pt2',
            field=models.TextField(blank=True, max_length=800),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='autor',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]