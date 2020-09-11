from django import template
from django.utils.html import mark_safe
from django.contrib.staticfiles import finders

register = template.Library()

@register.simple_tag
def heroicon(icon_name, **kwargs):
	if 'style' in kwargs:
		style = kwargs['style']
	else:
		style = 'outline'
	
	if style not in ['solid', 'outline']:
		raise Exception('{} is not a valid style. Must be "solid" or "outline".'.format(style))
	
	result = finders.find('heroicons/{}/{}.svg'.format(style, icon_name))
	if not result:
		raise Exception('{} is not a valid icon!'.format(icon_name))
	
	with open(result) as f: icon = f.read()
	return mark_safe(icon)
