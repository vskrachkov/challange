from django import template
from django.core.urlresolvers import reverse
from django.apps import apps


register = template.Library()


@register.filter
def admin_url(val):
    return reverse(
        'admin:{0}_{1}_change'.format(
            val._meta.app_label,
            val._meta.model_name
        ),
        args=(val.id,)
    )


# class GetAdminURLNode(template.Node):

#     def __init__(self, obj):
#         self.obj = obj

#     def render(self, context):
#         return reverse(
#             'admin:{0}_{1}_change'.format(
#                 self.obj._meta.app_label,
#                 self.obj._meta.model_name
#             ),
#             args=(self.obj.id,)
#         )


# @register.tag(name='edit')
# def do_get_admin_url(parser, token):
#     try:
#         tag_name, obj_name = token.split_contents()
#     except ValueError:
#         raise template.TemplateSyntaxError(
#             '{0} tag required a single argument'.format(tag_name))
#     obj = template.Variable(obj_name)
#     obj = apps.get_model(obj, model_name=obj)
#     if not ((getattr(getattr(obj, '_meta')), 'app_label', None) and
#             getattr(getattr(obj, '_meta')), 'model_name', None):

#         raise template.TemplateSyntaxError(
#             "tag's argument must be a model object")

#     return GetAdminURLNode(obj)
