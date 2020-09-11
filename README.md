# django-heroicons

Easily use [Heroicons](https://heroicons.dev/) in your Django templates.

## Installation

1. `pip install django-heroicons`
2. In your `settings.py` file, add `heroicons` to `INSTALLED_APPS`.

## Usage

Inside your template:

```
{% load heroicons %}
{% heroicon 'chevron-right' %}
```

If you want to use the solid icons instead:

```
{% heroicon 'chevron-right' style="solid" %}
```

Thanks to [@steveschoger](https://twitter.com/steveschoger) for the awesome icon set!
