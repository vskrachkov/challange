from django.core.signals import request_started
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver


@receiver(request_started)
def my_callback(sender, **kwargs):
    print("Request started!")


@receiver(pre_save)
def save_callback(sender, **kwargs):
    obj = kwargs.get('instance', None)
    print(obj._meta.app_label, obj._meta.model_name)
    print(obj.__dict__)


@receiver(pre_delete)
def delete_callback(sender, **kwargs):
    obj = kwargs.get('instance', None)
    print(obj._meta.app_label, obj._meta.model_name)
    print(obj.__dict__)
