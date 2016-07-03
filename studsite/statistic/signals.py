from datetime import datetime

from django.db.models.signals import post_delete, post_save, pre_save

from students.models import Student, Group
from .models import ModelInstancesChange


class StudentAppModelsSignals:
    """Recives signals from student app models."""

    @staticmethod
    def change(val):
        if val:
            return 'create'
        else:
            return 'update'

    def without_underline_befor_keys(instance):
        dic = {}
        for k, v in instance.__dict__.items():
            if k.startswith('_'):
                pass
            else:
                dic[k] = v
        return dic

    @classmethod
    def pre_save_callback(cls, sender, instance, **kwargs):
        """Saves pre instance data into database before it be changed."""
        cls.pre_saved_data = cls.without_underline_befor_keys(instance)

    @classmethod
    def post_save_callback(cls, sender, instance, created, **kwargs):
        app_label = instance._meta.app_label
        model_name = instance._meta.model.__name__
        change_type = cls.change(created)
        change_time = datetime.now()
        ModelInstancesChange(app_label=app_label,
                             model_name=model_name,
                             change_type=change_type,
                             change_time=change_time,
                             pre_saved_data=cls.pre_saved_data).save()

    @classmethod
    def post_delete_callback(cls, sender, instance, **kwargs):
        pre_saved_data = cls.without_underline_befor_keys(instance)
        app_label = instance._meta.app_label
        model_name = instance._meta.model.__name__
        change_type = 'delete'
        change_time = datetime.now()
        ModelInstancesChange(app_label=app_label,
                             model_name=model_name,
                             change_type=change_type,
                             change_time=change_time,
                             pre_saved_data=pre_saved_data).save()

pre_save.connect(
    StudentAppModelsSignals.pre_save_callback, sender=Student)
post_save.connect(
    StudentAppModelsSignals.post_save_callback, sender=Student)
post_delete.connect(
    StudentAppModelsSignals.post_delete_callback, sender=Student)
