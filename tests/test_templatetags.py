from django import forms
from django.template import Template, Context
from django.test import TestCase


class MyForm(forms.Form):
    bool_field = forms.BooleanField()
    text_field = forms.CharField()


class TemplateTagsTest(TestCase):
    def setUp(self):
        self.form = MyForm()

    def render(self, template, context={}):
        template = '{% load feedback_tags %}\n' + template
        return Template(template).render(Context(context))

    def test_is_checkbox(self):
        out = self.render('''
            {% for field in form %}
                {% if field|is_checkbox %}{{ field.name }}{% endif %}
            {% endfor %}
        ''', {'form': self.form}).strip()
        self.assertEqual(out, 'bool_field')

    def test_is_not_checkbox(self):
        out = self.render('''
            {% for field in form %}
                {% if not field|is_checkbox %}{{ field.name }}{% endif %}
            {% endfor %}
        ''', {'form': self.form}).strip()
        self.assertEqual(out, 'text_field')
