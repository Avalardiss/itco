# Generated by Django 3.1.6 on 2021-08-31 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffing', '0016_auto_20210831_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldier',
            name='all_nal',
            field=models.CharField(blank=True, default=0, max_length=100, verbose_name='Всего в наличии'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='soldier',
            name='all_nekomplekt',
            field=models.CharField(blank=True, default=0, max_length=100, verbose_name='Всего некомплект'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='soldier',
            name='all_percent',
            field=models.CharField(blank=True, default=0, max_length=100, verbose_name='Всего % укомплектованности'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='soldier',
            name='all_state',
            field=models.CharField(blank=True, default=0, max_length=100, verbose_name='Всего по штату'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='soldier',
            name='kontrakt_nal',
            field=models.CharField(blank=True, default=0, max_length=200, verbose_name='Военнослужащие по контракту на должностях солдат и сержантов в наличии'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='soldier',
            name='kontrakt_nekomplekt',
            field=models.CharField(blank=True, default=0, max_length=200, verbose_name='Военнослужащие по контракту на должностях солдат и сержантов некомплект'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='soldier',
            name='kontrakt_percent',
            field=models.CharField(blank=True, default=0, max_length=200, verbose_name='Военнослужащие по контракту на должностях солдат и сержантов % укомплектованности'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='soldier',
            name='kontrakt_state',
            field=models.CharField(blank=True, default=0, max_length=200, verbose_name='Военнослужащие по контракту на должностях солдат и сержантов по штату'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='soldier',
            name='name',
            field=models.CharField(blank=True, default=0, max_length=100, verbose_name='Орган управления'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='soldier',
            name='off_nal',
            field=models.CharField(blank=True, default=0, max_length=100, verbose_name='Офицеры в наличии'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='soldier',
            name='off_nekomplekt',
            field=models.CharField(blank=True, default=0, max_length=100, verbose_name='Офицеры некомплект'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='soldier',
            name='off_percent',
            field=models.CharField(blank=True, default=0, max_length=100, verbose_name='Офицеры % укомплектованности'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='soldier',
            name='off_state',
            field=models.CharField(blank=True, default=0, max_length=100, verbose_name='Офицеры по штату'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='soldier',
            name='prap_nal',
            field=models.CharField(blank=True, default=0, max_length=100, verbose_name='Прапорщики в наличии'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='soldier',
            name='prap_nekomplekt',
            field=models.CharField(blank=True, default=0, max_length=100, verbose_name='Прапорщики некомплект'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='soldier',
            name='prap_percent',
            field=models.CharField(blank=True, default=0, max_length=100, verbose_name='Прапорщики % укомплектованности'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='soldier',
            name='prap_state',
            field=models.CharField(blank=True, default=0, max_length=100, verbose_name='Прапорщики по штату'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='soldier',
            name='srok_nal',
            field=models.CharField(blank=True, default=0, max_length=100, verbose_name='Военнослужащие срочной службы в наличии'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='soldier',
            name='srok_nekomplekt',
            field=models.CharField(blank=True, default=0, max_length=100, verbose_name='Военнослужащие срочной службы некомплект'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='soldier',
            name='srok_percent',
            field=models.CharField(blank=True, default=0, max_length=100, verbose_name='Военнослужащие срочной службы % укомплектованности'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='soldier',
            name='srok_state',
            field=models.CharField(blank=True, default=0, max_length=100, verbose_name='Военнослужащие срочной службы по штату'),
            preserve_default=False,
        ),
    ]