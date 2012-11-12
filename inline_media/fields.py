#-*- coding: utf-8 -*-

from django.db.models import fields

from inline_media.widgets import TextareaWithInlines


class TextFieldWithInlines(fields.TextField):

    def formfield(self, **kwargs):
        defaults = {"widget": TextareaWithInlines}
        defaults.update(kwargs)
        return super(TextFieldWithInlines, self).formfield(**defaults)

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^inline_media\.fields\.TextFieldWithInlines"])

