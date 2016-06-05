from django import template
from django.core.urlresolvers import reverse
from django.apps import apps


register = template.Library()


@register.filter
def admin_url(val):
    """Returns url for object's admin page."""
    return reverse(
        'admin:{0}_{1}_change'.format(
            val._meta.app_label,
            val._meta.model_name
        ),
        args=(val.id,)
    )


class AdminURLNode(template.Node):
    """Returns url for object's admin page."""
    def __init__(self, obj):
        self.obj = obj

    def render(self, context):
            return reverse(
                'admin:{0}_{1}_change'.format(
                    context[self.obj]._meta.app_label,
                    context[self.obj]._meta.model_name
                ),
                args=(context[self.obj].id,)
            )


@register.tag(name='edit')
def do_get_admin_url(parser, token):
    try:
        tag_name, obj = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "tag required a single argument")
    return AdminURLNode(obj)
