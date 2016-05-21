from django.db import models


class Group(models.Model):
    name = models.CharField(verbose_name=u'Код группы', max_length=50)

    class Meta:
        verbose_name = u'Группа'
        verbose_name_plural = u'Группы'

    def __str__(self):
        return u'Группа <{0}>'.format(self.name)


class Student(models.Model):
    first_name = models.CharField(verbose_name=u'Имя', max_length=50)
    second_name = models.CharField(verbose_name=u'Отчество', max_length=50)
    last_name = models.CharField(verbose_name=u'Фамилия', max_length=50)
    student_ID = models.IntegerField(verbose_name=u'Номер студенческого')
    group = models.ForeignKey('Group', on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'Студент'
        verbose_name_plural = u'Студенты'

    @property
    def full_name(self):
        return '{0} {1} {2}'.format(self.first_name,
                                    self.second_name,
                                    self.last_name)

    def __str__(self):
        return u'Студент <{0}>'.format(self.full_name)


class Starosta(models.Model):
    group = models.OneToOneField('Group', on_delete=models.CASCADE)
    student = models.OneToOneField('Student', on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'Староста'
        verbose_name_plural = u'Старосты'

    @property
    def name(self):
        return self.student.full_name

    @property
    def group_name(self):
        return self.group.name

    def __str__(self):
        return u'Староста группы {0}, {1}'.format(self.name, self.group_name)
