# Generated by Django 3.1.7 on 2021-05-08 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List_vacant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='Наименование оперативно-территориального объединения, соединения, территориального органа, воинской части, подразделения, организации')),
                ('name_group', models.CharField(blank=True, max_length=200, verbose_name='Наименование должностных групп')),
                ('classifier', models.CharField(blank=True, max_length=200, verbose_name='Классификатор должностных групп')),
                ('military_position_state', models.CharField(blank=True, max_length=200, verbose_name='Воинская (специальная) должность по штату')),
                ('date_vacant', models.CharField(blank=True, max_length=200, verbose_name='Дата образования ваканта')),
                ('rank_state', models.CharField(blank=True, max_length=200, verbose_name='Воинское (специальное) звание по штату')),
                ('tariff', models.CharField(blank=True, max_length=200, verbose_name='Тарифный разряд')),
                ('vus', models.CharField(blank=True, max_length=200, verbose_name='ВУС')),
                ('name_candidate', models.CharField(blank=True, max_length=200, verbose_name='Ф.И.О.')),
                ('rank', models.CharField(blank=True, max_length=200, verbose_name='Воинское (специальное) звание')),
            ],
            options={
                'verbose_name': 'Список вакантов',
                'verbose_name_plural': 'Список вакантов',
            },
        ),
        migrations.CreateModel(
            name='Soldier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Орган управления')),
                ('all_state', models.CharField(blank=True, max_length=100, verbose_name='Всего по штату')),
                ('all_nal', models.CharField(blank=True, max_length=100, verbose_name='Всего в наличии')),
                ('all_nekomplekt', models.CharField(blank=True, max_length=100, verbose_name='Всего некомплект')),
                ('all_percent', models.CharField(blank=True, max_length=100, verbose_name='Всего % укомплектованности')),
                ('off_state', models.CharField(blank=True, max_length=100, verbose_name='Офицеры по штату')),
                ('off_nal', models.CharField(blank=True, max_length=100, verbose_name='Офицеры в наличии')),
                ('off_nekomplekt', models.CharField(blank=True, max_length=100, verbose_name='Офицеры некомплект')),
                ('off_percent', models.CharField(blank=True, max_length=100, verbose_name='Офицеры % укомплектованности')),
                ('prap_state', models.CharField(blank=True, max_length=100, verbose_name='Прапорщики по штату')),
                ('prap_nal', models.CharField(blank=True, max_length=100, verbose_name='Прапорщики в наличии')),
                ('prap_nekomplekt', models.CharField(blank=True, max_length=100, verbose_name='Прапорщики некомплект')),
                ('prap_percent', models.CharField(blank=True, max_length=100, verbose_name='Прапорщики % укомплектованности')),
                ('kontrakt_state', models.CharField(blank=True, max_length=200, verbose_name='Военнослужащие по контракту на должностях солдат и сержантов по штату')),
                ('kontrakt_nal', models.CharField(blank=True, max_length=200, verbose_name='Военнослужащие по контракту на должностях солдат и сержантов в наличии')),
                ('kontrakt_nekomplekt', models.CharField(blank=True, max_length=200, verbose_name='Военнослужащие по контракту на должностях солдат и сержантов некомплект')),
                ('kontrakt_percent', models.CharField(blank=True, max_length=200, verbose_name='Военнослужащие по контракту на должностях солдат и сержантов % укомплектованности')),
                ('srok_state', models.CharField(blank=True, max_length=100, verbose_name='Военнослужащие срочной службы по штату')),
                ('srok_nal', models.CharField(blank=True, max_length=100, verbose_name='Военнослужащие срочной службы в наличии')),
                ('srok_nekomplekt', models.CharField(blank=True, max_length=100, verbose_name='Военнослужащие срочной службы некомплект')),
                ('srok_percent', models.CharField(blank=True, max_length=100, verbose_name='Военнослужащие срочной службы % укомплектованности')),
            ],
            options={
                'verbose_name': 'Таблица за войска',
                'verbose_name_plural': 'Таблица за войска',
            },
        ),
        migrations.CreateModel(
            name='Vacant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomer', models.CharField(blank=True, max_length=100, verbose_name='№ п/п')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Орган управления (№ в/ч)')),
                ('location', models.CharField(blank=True, max_length=100, verbose_name='Место дислокации')),
                ('vacant_position', models.CharField(blank=True, max_length=100, verbose_name='Вакантная должность (наименование)')),
                ('rank_state', models.CharField(blank=True, max_length=100, verbose_name='В/зв (специальное) по штату')),
                ('tariff', models.CharField(blank=True, max_length=100, verbose_name='Тарифный разряд')),
                ('vus', models.CharField(blank=True, max_length=100, verbose_name='ВУС')),
                ('date_vacant', models.CharField(blank=True, max_length=100, verbose_name='С какой даты должность вакантна')),
                ('candidate', models.CharField(blank=True, max_length=50, verbose_name='Кто подобран (в/зв, спец., призывается), Ф.И.О.)')),
            ],
            options={
                'verbose_name': 'Перечень вакантных должностей',
                'verbose_name_plural': 'Перечень вакантных должностей',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Орган управления')),
                ('all_state', models.CharField(blank=True, max_length=100, verbose_name='Всего по штату')),
                ('all_nal', models.CharField(blank=True, max_length=100, verbose_name='Всего в наличии')),
                ('all_nekomplekt', models.CharField(blank=True, max_length=100, verbose_name='Всего некомплект')),
                ('all_percent', models.CharField(blank=True, max_length=100, verbose_name='Всего % укомплектованности')),
                ('off_state', models.CharField(blank=True, max_length=100, verbose_name='Офицеры (в/сл) по штату')),
                ('off_nal', models.CharField(blank=True, max_length=100, verbose_name='Офицеры (в/сл) в наличии')),
                ('off_nekomplekt', models.CharField(blank=True, max_length=100, verbose_name='Офицеры (в/сл) некомплект')),
                ('off_percent', models.CharField(blank=True, max_length=100, verbose_name='Офицеры % укомплектованности')),
                ('prap_state', models.CharField(blank=True, max_length=100, verbose_name='Прапорщики по штату')),
                ('prap_nal', models.CharField(blank=True, max_length=100, verbose_name='Прапорщики в наличии')),
                ('prap_nekomplekt', models.CharField(blank=True, max_length=100, verbose_name='Прапорщики некомплект')),
                ('prap_percent', models.CharField(blank=True, max_length=100, verbose_name='Прапорщики % укомплектованности')),
                ('sotr_state', models.CharField(blank=True, max_length=100, verbose_name='Сотрудники по штату')),
                ('sotr_nal', models.CharField(blank=True, max_length=100, verbose_name='Сотрудники в наличии')),
                ('sotr_nekomplekt', models.CharField(blank=True, max_length=100, verbose_name='Сотрудники некомплект')),
                ('sotr_percent', models.CharField(blank=True, max_length=100, verbose_name='Сотрудники % укомплектованности')),
            ],
            options={
                'verbose_name': 'Таблица за территориальные органы',
                'verbose_name_plural': 'Таблица за территориальные органы',
            },
        ),
    ]
