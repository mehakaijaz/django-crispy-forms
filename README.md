# Django Crispy Forms

Django Crispy Forms is a Django application that helps you control the rendering behaviour of your Django forms in a very elegant and DRY way. By using it, you can style Django forms quickly and easily, by using the built-in methods and templates provided by the package.
The best way to have Django DRY forms. Build programmatic reusable layouts out of components, having full control of the rendered HTML without writing HTML in templates. All this without breaking the standard way of doing things in Django, so it plays nice with any other form application.


## Installation

You can install Django Crispy Forms via pip:

```bash
pip install django-crispy-forms
```

## Usage

```python
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class MyForm(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')

    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

```
```html
<form method="post">
    {% csrf_token %}
    {{ form.name.label_tag }}
    {{ form.name }}
    {{ form.email.label_tag }}
    {{ form.email }}
    <button type="submit">Submit</button>
</form>

```

## Enhancing Form Presentation with Django-Crispy-Forms:
django-crispy-forms supports Django 4.2+ with Python 3.8+.

The application mainly provides:

* A filter named ``|crispy``that will render elegant div based forms. Think of it as the built-in methods: ``as_table``, ``as_ul`` and ``as_p``. You cannot tune up the output, but it is easy to start using it.
A tag named ``{% crispy %}`` that will render a form based on your configuration and specific layout setup. This gives you amazing power without much hassle, helping you save tons of time.
Django-crispy-forms supports several frontend frameworks, such as Twitter `Bootstrap` (versions 2, 3, and 4),` tailwind`, `Bulma` and `Foundation`. You can also easily adapt your custom company's one, creating your own, see the docs for more information. You can easily switch among them using ``CRISPY_TEMPLATE_PACK`` setting variable.
