from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Soldier(models.Model):
    id = models.AutoField('ID', auto_created=True, primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_soldier")
    name = models.CharField('Орган управления', max_length = 100, blank=True)

    all_state = models.CharField('Всего по штату', max_length = 100, blank=True)
    all_nal = models.CharField('Всего в наличии', max_length = 100, blank=True)
    all_nekomplekt = models.CharField('Всего некомплект', max_length = 100, blank=True)
    all_percent = models.CharField('Всего % укомплектованности', max_length = 100, blank=True)

    off_state = models.CharField('Офицеры по штату', max_length = 100, blank=True)
    off_nal = models.CharField('Офицеры в наличии', max_length = 100, blank=True)
    off_nekomplekt = models.CharField('Офицеры некомплект', max_length = 100, blank=True)
    off_percent = models.CharField('Офицеры % укомплектованности', max_length = 100, blank=True)

    prap_state = models.CharField('Прапорщики по штату', max_length = 100, blank=True)
    prap_nal = models.CharField('Прапорщики в наличии', max_length = 100, blank=True)
    prap_nekomplekt = models.CharField('Прапорщики некомплект', max_length = 100, blank=True)
    prap_percent = models.CharField('Прапорщики % укомплектованности', max_length = 100, blank=True)

    kontrakt_state = models.CharField('Военнослужащие по контракту на должностях солдат и сержантов по штату', max_length = 200, blank=True)
    kontrakt_nal = models.CharField('Военнослужащие по контракту на должностях солдат и сержантов в наличии', max_length = 200, blank=True)
    kontrakt_nekomplekt = models.CharField('Военнослужащие по контракту на должностях солдат и сержантов некомплект', max_length = 200, blank=True)
    kontrakt_percent = models.CharField('Военнослужащие по контракту на должностях солдат и сержантов % укомплектованности', max_length = 200, blank=True)

    srok_state = models.CharField('Военнослужащие срочной службы по штату', max_length = 100, blank=True)
    srok_nal = models.CharField('Военнослужащие срочной службы в наличии', max_length = 100, blank=True)
    srok_nekomplekt = models.CharField('Военнослужащие срочной службы некомплект', max_length = 100, blank=True)
    srok_percent = models.CharField('Военнослужащие срочной службы % укомплектованности', max_length = 100, blank=True)   
    members = models.ManyToManyField(User, related_name="members_soldier", blank=True)

    pub_date = models.DateTimeField('date_published', auto_now=True)


    class Meta:
        verbose_name = 'Таблица за войска'
        verbose_name_plural = 'Таблица за войска'

    def __str__(self):
        return self.id
    def __str__(self):
        return self.name
    def __str__(self):
        return self.all_state
    def __str__(self):
        return self.all_nal
    def __str__(self):
        return self.all_nekomplekt
    def __str__(self):
        return self.all_percent
    def __str__(self):
        return self.off_state
    def __str__(self):
        return self.off_nal
    def __str__(self):
        return self.off_nekomplekt
    def __str__(self):
        return self.off_percent
    def __str__(self):
        return self.prap_state
    def __str__(self):
        return self.prap_nal
    def __str__(self):
        return self.prap_nekomplekt
    def __str__(self):
        return self.prap_percent
    def __str__(self):
        return self.kontrakt_state
    def __str__(self):
        return self.kontrakt_nal
    def __str__(self):
        return self.kontrakt_nekomplekt
    def __str__(self):
        return self.kontrakt_percent
    def __str__(self):
        return self.srok_state
    def __str__(self):
        return self.srok_nal
    def __str__(self):
        return self.srok_nekomplekt
    def __str__(self):
        return self.srok_percent
    
    def get_absolute_url(self):
        return reverse('staffing:soldier-detail', args=[str(self.id)])


class Worker(models.Model):
    id = models.AutoField('ID', auto_created=True, primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_worker")
    name = models.CharField('Орган управления', max_length = 100, blank=True)

    all_state = models.CharField('Всего по штату', max_length = 100, blank=True)
    all_nal = models.CharField('Всего в наличии', max_length = 100, blank=True)
    all_nekomplekt = models.CharField('Всего некомплект', max_length = 100, blank=True)
    all_percent = models.CharField('Всего % укомплектованности', max_length = 100, blank=True)

    off_state = models.CharField('Офицеры (в/сл) по штату', max_length = 100, blank=True)
    off_nal = models.CharField('Офицеры (в/сл) в наличии', max_length = 100, blank=True)
    off_nekomplekt = models.CharField('Офицеры (в/сл) некомплект', max_length = 100, blank=True)
    off_percent = models.CharField('Офицеры % укомплектованности', max_length = 100, blank=True)

    prap_state = models.CharField('Прапорщики по штату', max_length = 100, blank=True)
    prap_nal = models.CharField('Прапорщики в наличии', max_length = 100, blank=True)
    prap_nekomplekt = models.CharField('Прапорщики некомплект', max_length = 100, blank=True)
    prap_percent = models.CharField('Прапорщики % укомплектованности', max_length = 100, blank=True)

    sotr_state = models.CharField('Сотрудники по штату', max_length = 100, blank=True)
    sotr_nal = models.CharField('Сотрудники в наличии', max_length = 100, blank=True)
    sotr_nekomplekt = models.CharField('Сотрудники некомплект', max_length = 100, blank=True)
    sotr_percent = models.CharField('Сотрудники % укомплектованности', max_length = 100, blank=True)   
    members = models.ManyToManyField(User, related_name="members_worker", blank=True)

    pub_date = models.DateTimeField('date_published', auto_now=True)

    class Meta:
        verbose_name = 'Таблица за территориальные органы'
        verbose_name_plural = 'Таблица за территориальные органы'


    def __str__(self):
        return self.id
    def __str__(self):
        return self.name
    def __str__(self):
        return self.all_state
    def __str__(self):
        return self.all_nal
    def __str__(self):
        return self.all_nekomplekt
    def __str__(self):
        return self.all_percent
    def __str__(self):
        return self.off_state
    def __str__(self):
        return self.off_nal
    def __str__(self):
        return self.off_nekomplekt
    def __str__(self):
        return self.off_percent
    def __str__(self):
        return self.prap_state
    def __str__(self):
        return self.prap_nal
    def __str__(self):
        return self.prap_nekomplekt
    def __str__(self):
        return self.prap_percent
    def __str__(self):
        return self.sotr_state
    def __str__(self):
        return self.sotr_nal
    def __str__(self):
        return self.sotr_nekomplekt
    def __str__(self):
        return self.sotr_percent
    
    def get_absolute_url(self):
        return reverse('staffing:worker-detail', args=[str(self.id)])


class Vacant(models.Model):
    id = models.AutoField('ID', auto_created=True, primary_key=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="author_vacant")
    nomer = models.CharField('№ п/п', max_length = 100, null=False, blank=True)       
    name = models.CharField('Орган управления (№ в/ч)', max_length = 100, blank=True)
    location = models.CharField('Место дислокации', max_length = 100, blank=True)
    vacant_position = models.CharField('Вакантная должность (наименование)', max_length = 100, blank=True)
    rank_state = models.CharField('В/зв (специальное) по штату', max_length = 100, blank=True)
    tariff = models.CharField('Тарифный разряд', max_length = 100, blank=True)
    vus = models.CharField('ВУС', max_length = 100, blank=True)
    date_vacant = models.CharField('С какой даты должность вакантна', max_length = 100, blank=True)
    candidate = models.CharField('Кто подобран (в/зв, спец., призывается), Ф.И.О.)', max_length = 50, blank=True)
    members = models.ManyToManyField(User, related_name="members_vacant", blank=True)
    
    class Meta:
        verbose_name = 'Перечень вакантных должностей'
        verbose_name_plural = 'Перечень вакантных должностей'
    
    def __str__(self):
        return self.id
    def __str__(self):
        return self.nomer
    def __str__(self):
        return self.name
    def __str__(self):
        return self.location
    def __str__(self):
        return self.vacant_position
    def __str__(self):
        return self.rank_state
    def __str__(self):
        return self.tariff
    def __str__(self):
        return self.vus
    def __str__(self):
        return self.date_vacant
    def __str__(self):
        return self.candidate

    def get_absolute_url(self):
        return reverse('staffing:vacant-detail', args=[str(self.id)])
        


class List_vacant(models.Model):
    id = models.AutoField('ID', auto_created=True, primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_list_vacant")
    name = models.CharField('Наименование оперативно-территориального объединения, соединения, территориального органа, воинской части, подразделения, организации', max_length = 200, blank=True)  
    name_group = models.CharField('Наименование должностных групп', max_length = 200, blank=True)
    classifier = models.CharField('Классификатор должностных групп', max_length = 200, blank=True)
    military_position_state = models.CharField('Воинская (специальная) должность по штату', max_length = 200, blank=True)
    date_vacant = models.CharField('Дата образования ваканта', max_length = 200, blank=True)
    rank_state = models.CharField('Воинское (специальное) звание по штату', max_length = 200, blank=True)
    tariff = models.CharField('Тарифный разряд', max_length = 200, blank=True)
    vus = models.CharField('ВУС', max_length = 200, blank=True)
    name_candidate = models.CharField('Ф.И.О.', max_length = 200, blank=True)
    rank = models.CharField('Воинское (специальное) звание', max_length = 200, blank=True)
    members = models.ManyToManyField(User, related_name="members_list_vavcant", blank=True)

    class Meta:
        verbose_name = 'Список вакантов'
        verbose_name_plural = 'Список вакантов'

    def __str__(self):
        return self.id
    def __str__(self):
        return self.name
    def __str__(self):
        return self.name_group
    def __str__(self):
        return self.classifier
    def __str__(self):
        return self.military_position_state
    def __str__(self):
        return self.date_vacant
    def __str__(self):
        return self.rank_state
    def __str__(self):
        return self.tariff
    def __str__(self):
        return self.vus
    def __str__(self):
        return self.name_candidate
    def __str__(self):
        return self.rank

    def get_absolute_url(self):
        return reverse('staffing:list_vacant-detail', args=[str(self.id)])


class All_staff(models.Model):
    id = models.AutoField('ID', auto_created=True, primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_all_staff")
    name = models.CharField('Орган управления', max_length = 100, blank=True)

    all_state = models.CharField('Всего по штату', max_length = 100, blank=True)
    all_nal = models.CharField('Всего в наличии', max_length = 100, blank=True)
    all_nekomplekt = models.CharField('Всего некомплект', max_length = 100, blank=True)
    all_percent = models.CharField('Всего % укомплектованности', max_length = 100, blank=True)

    off_state = models.CharField('Офицеры по штату', max_length = 100, blank=True)
    off_nal = models.CharField('Офицеры в наличии', max_length = 100, blank=True)
    off_nekomplekt = models.CharField('Офицеры некомплект', max_length = 100, blank=True)
    off_percent = models.CharField('Офицеры % укомплектованности', max_length = 100, blank=True)

    prap_state = models.CharField('Прапорщики по штату', max_length = 100, blank=True)
    prap_nal = models.CharField('Прапорщики в наличии', max_length = 100, blank=True)
    prap_nekomplekt = models.CharField('Прапорщики некомплект', max_length = 100, blank=True)
    prap_percent = models.CharField('Прапорщики % укомплектованности', max_length = 100, blank=True)

    kontrakt_state = models.CharField('Военнослужащие по контракту на должностях солдат и сержантов по штату', max_length = 200, blank=True)
    kontrakt_nal = models.CharField('Военнослужащие по контракту на должностях солдат и сержантов в наличии', max_length = 200, blank=True)
    kontrakt_nekomplekt = models.CharField('Военнослужащие по контракту на должностях солдат и сержантов некомплект', max_length = 200, blank=True)
    kontrakt_percent = models.CharField('Военнослужащие по контракту на должностях солдат и сержантов % укомплектованности', max_length = 200, blank=True)

    srok_state = models.CharField('Военнослужащие срочной службы по штату', max_length = 100, blank=True)
    srok_nal = models.CharField('Военнослужащие срочной службы в наличии', max_length = 100, blank=True)
    srok_nekomplekt = models.CharField('Военнослужащие срочной службы некомплект', max_length = 100, blank=True)
    srok_percent = models.CharField('Военнослужащие срочной службы % укомплектованности', max_length = 100, blank=True)   
    members = models.ManyToManyField(User, related_name="members_all_staff", blank=True)

    pub_date = models.DateTimeField('date_published', auto_now=True)


    class Meta:
        verbose_name = 'ИТОГО за ЦО'
        verbose_name_plural = 'ИТОГО за ЦО'

    def __str__(self):
        return self.id
    def __str__(self):
        return self.name
    def __str__(self):
        return self.all_state
    def __str__(self):
        return self.all_nal
    def __str__(self):
        return self.all_nekomplekt
    def __str__(self):
        return self.all_percent
    def __str__(self):
        return self.off_state
    def __str__(self):
        return self.off_nal
    def __str__(self):
        return self.off_nekomplekt
    def __str__(self):
        return self.off_percent
    def __str__(self):
        return self.prap_state
    def __str__(self):
        return self.prap_nal
    def __str__(self):
        return self.prap_nekomplekt
    def __str__(self):
        return self.prap_percent
    def __str__(self):
        return self.kontrakt_state
    def __str__(self):
        return self.kontrakt_nal
    def __str__(self):
        return self.kontrakt_nekomplekt
    def __str__(self):
        return self.kontrakt_percent
    def __str__(self):
        return self.srok_state
    def __str__(self):
        return self.srok_nal
    def __str__(self):
        return self.srok_nekomplekt
    def __str__(self):
        return self.srok_percent
    
    def get_absolute_url(self):
        return reverse('staffing:all_staff-detail', args=[str(self.id)])

