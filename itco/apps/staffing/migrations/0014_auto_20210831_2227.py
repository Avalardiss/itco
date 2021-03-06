# Generated by Django 3.1.6 on 2021-08-31 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffing', '0013_auto_20210831_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldier',
            name='all_nal',
            field=models.CharField(blank=True, max_length=100, verbose_name='Всего в наличии'),
        ),
        migrations.AlterField(
            model_name='soldier',
            name='all_nekomplekt',
            field=models.CharField(blank=True, max_length=100, verbose_name='Всего некомплект'),
        ),
        migrations.AlterField(
            model_name='soldier',
            name='all_percent',
            field=models.CharField(blank=True, max_length=100, verbose_name='Всего % укомплектованности'),
        ),
        migrations.AlterField(
            model_name='soldier',
            name='all_state',
            field=models.CharField(blank=True, max_length=100, verbose_name='Всего по штату'),
        ),
        migrations.AlterField(
            model_name='soldier',
            name='kontrakt_nal',
            field=models.CharField(blank=True, max_length=200, verbose_name='Военнослужащие по контракту на должностях солдат и сержантов в наличии'),
        ),
        migrations.AlterField(
            model_name='soldier',
            name='kontrakt_nekomplekt',
            field=models.CharField(blank=True, max_length=200, verbose_name='Военнослужащие по контракту на должностях солдат и сержантов некомплект'),
        ),
        migrations.AlterField(
            model_name='soldier',
            name='kontrakt_percent',
            field=models.CharField(blank=True, max_length=200, verbose_name='Военнослужащие по контракту на должностях солдат и сержантов % укомплектованности'),
        ),
        migrations.AlterField(
            model_name='soldier',
            name='kontrakt_state',
            field=models.CharField(blank=True, max_length=200, verbose_name='Военнослужащие по контракту на должностях солдат и сержантов по штату'),
        ),
        migrations.AlterField(
            model_name='soldier',
            name='off_nal',
            field=models.CharField(blank=True, max_length=100, verbose_name='Офицеры в наличии'),
        ),
        migrations.AlterField(
            model_name='soldier',
            name='off_nekomplekt',
            field=models.CharField(blank=True, max_length=100, verbose_name='Офицеры некомплект'),
        ),
        migrations.AlterField(
            model_name='soldier',
            name='off_percent',
            field=models.CharField(blank=True, max_length=100, verbose_name='Офицеры % укомплектованности'),
        ),
        migrations.AlterField(
            model_name='soldier',
            name='off_state',
            field=models.CharField(blank=True, max_length=100, verbose_name='Офицеры по штату'),
        ),
        migrations.AlterField(
            model_name='soldier',
            name='prap_nal',
            field=models.CharField(blank=True, max_length=100, verbose_name='Прапорщики в наличии'),
        ),
        migrations.AlterField(
            model_name='soldier',
            name='prap_nekomplekt',
            field=models.CharField(blank=True, max_length=100, verbose_name='Прапорщики некомплект'),
        ),
        migrations.AlterField(
            model_name='soldier',
            name='prap_percent',
            field=models.CharField(blank=True, max_length=100, verbose_name='Прапорщики % укомплектованности'),
        ),
        migrations.AlterField(
            model_name='soldier',
            name='prap_state',
            field=models.CharField(blank=True, max_length=100, verbose_name='Прапорщики по штату'),
        ),
        migrations.AlterField(
            model_name='soldier',
            name='srok_nal',
            field=models.CharField(blank=True, max_length=100, verbose_name='Военнослужащие срочной службы в наличии'),
        ),
        migrations.AlterField(
            model_name='soldier',
            name='srok_nekomplekt',
            field=models.CharField(blank=True, max_length=100, verbose_name='Военнослужащие срочной службы некомплект'),
        ),
        migrations.AlterField(
            model_name='soldier',
            name='srok_percent',
            field=models.CharField(blank=True, max_length=100, verbose_name='Военнослужащие срочной службы % укомплектованности'),
        ),
        migrations.AlterField(
            model_name='soldier',
            name='srok_state',
            field=models.CharField(blank=True, max_length=100, verbose_name='Военнослужащие срочной службы по штату'),
        ),
    ]
