from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('parkings', '0029_parking_domain'),
    ]

    operations = [
        migrations.AddField(
            model_name='permitarea',
            name='domain',
            field=models.ForeignKey(
                to='parkings.EnforcementDomain',
                default=1,
                on_delete=models.PROTECT,
                related_name='permit_areas'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='permitseries',
            name='owner',
            field=models.ForeignKey(
                to='parkings.Operator',
                blank=True,
                null=True,
                on_delete=models.PROTECT,
                related_name='permit_series_set'),
        ),
        migrations.AlterField(
            model_name='permitarea',
            name='identifier',
            field=models.CharField(max_length=10, verbose_name='identifier'),
        ),
        migrations.AlterUniqueTogether(
            name='permitarea',
            unique_together={('domain', 'identifier')},
        ),
    ]
