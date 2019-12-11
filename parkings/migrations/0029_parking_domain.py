from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkings', '0028_enforcementdomain'),
    ]

    operations = [
        migrations.AddField(
            model_name='parking',
            name='domain',
            field=models.ForeignKey(
                to='parkings.EnforcementDomain',
                default=1,
                on_delete=models.PROTECT,
                related_name='parkings'),
            preserve_default=False,
        ),
    ]
