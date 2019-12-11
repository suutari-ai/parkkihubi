from django.contrib.gis.db.models.fields import MultiPolygonField
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkings', '0027_parkingcheck_performer'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnforcementDomain',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('created_at', models.DateTimeField(
                    auto_now_add=True,
                    verbose_name='time created')),
                ('modified_at', models.DateTimeField(
                    auto_now=True,
                    verbose_name='time modified')),
                ('code', models.CharField(
                    max_length=10,
                    unique=True,
                    verbose_name='code')),
                ('name', models.CharField(max_length=40, verbose_name='name')),
                ('geom', MultiPolygonField(
                    srid=3879, verbose_name='geometry')),
            ],
            options={
                'ordering': ('code', ),
            },
        ),
    ]
