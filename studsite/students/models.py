from django.db import models
from django.core.exceptions import ValidationError


class Group(models.Model):
    name = models.CharField(verbose_name=u'Код группы', max_length=50)

    class Meta:
        verbose_name = u'Группа'
        verbose_name_plural = u'Группы'

    def __str__(self):
        return u'Группа <{0}>'.format(self.name)

    @property
    def starosta_list(self):
        return [
            st for st in self.student_set.all() if st.starosta
        ]

    def get_starosta(self):
        if self.starosta_list:
            return self.starosta_list[0]

    def save(self):
        if self.student_set and self.starosta_list:
            self.starosta = self.get_starosta()
        super().save()


class Student(models.Model):
    first_name = models.CharField(verbose_name=u'Имя', max_length=50)
    second_name = models.CharField(verbose_name=u'Отчество', max_length=50)
    last_name = models.CharField(verbose_name=u'Фамилия', max_length=50)
    student_ID = models.IntegerField(verbose_name=u'Номер студенческого')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    starosta = models.BooleanField(
        verbose_name=u'Назначить старостой', blank=True, default=False)

    @property
    def starosta_list(self):
        return [
            st for st in self.group.student_set.all() if st.starosta
        ]

    class Meta:
        verbose_name = u'Студент'
        verbose_name_plural = u'Студенты'

    @property
    def full_name(self):
        return '{0} {1} {2}'.format(
            self.first_name, self.second_name, self.last_name)

    def __str__(self):
        if not self.starosta:
            return u'Студент <{0}, {1}>'.format(
                self.full_name, self.group.name)
        else:
            return u'Студент <{0}, {1}, Староста группы>'.format(
                self.full_name, self.group.name)

    def clean(self):
        if self.starosta and self.starosta_list:
            raise ValidationError(
                {'starosta': (u'У этой группы уже есть староста.')})
