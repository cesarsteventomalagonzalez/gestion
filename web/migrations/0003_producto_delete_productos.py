# Generated by Django 5.0.6 on 2024-06-26 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_productos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('cantidad', models.PositiveIntegerField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos/')),
                ('numero_whatsapp', models.CharField(default='+593959682902', max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Productos',
        ),
    ]
