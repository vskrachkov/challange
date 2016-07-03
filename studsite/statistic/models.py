import json
import ast

from django.db import models
from django.core.exceptions import ValidationError
from django.apps import apps


def trigger_validation(value):
    """Raises ValidationError if value not in TRIGGERS."""
    TRIGGERS = ('create', 0), ('update', 1), ('delete', 2)
    if value not in (v[0] for v in TRIGGERS):
        raise ValidationError('Incorrect value. Please choose one of \
            the next value: {vals}'.format(vals=[v[0] for v in TRIGGERS]))


class ModelInstancesChange(models.Model):

    class Meta:
        verbose_name = 'ModelInstancesChange'
        verbose_name_plural = 'ModelInstancesChanges'

    app_label = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    change_time = models.DateTimeField(editable=False)
    change_type = models.CharField(
        validators=[trigger_validation], max_length=50)
    pre_saved_data = models.CharField(max_length=50)

    def __str__(self):
        return '{0}.{1}, {2}, {3}'.format(self.app_label,
                                          self.model_name,
                                          self.change_type,
                                          self.change_time)

    def _get_model(self):
        """Returns model ..."""
        return apps.get_model(self.app_label, model_name=self.model_name)

    def _get_pre_saved_data(self):
        """
        Returns model instance data that be before dataes have been changed or
        created. Method returns dictionary or string if string not been
        converted to dictionary. That's why control this moment.

        """
        try:
            data = ast.literal_eval(self.pre_saved_data)
        except SyntaxError:
            return self.pre_saved_data
        return data

    @property
    def model(self):
        return self._get_model()

    @property
    def data(self):
        return self._get_pre_saved_data()
