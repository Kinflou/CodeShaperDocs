## System Imports
import warnings
import time


## Application Imports


## Library Imports


WORDS_PER_MINUTE = 200


def html_page_context(app, pagename, templatename, context, doctree):
	if templatename != 'page.html':
		return
	
	if not app.config.page_read_time:
		warnings.warn("edit_on_github_project not specified")
		return
	
	page = None
	
	if len(context['rellinks']) > 2:
		page = context['rellinks'][2][1]
	
	minutes = None
	words = 0
	
	if 'meta' in context:
		if context['meta']:
			words = context['meta']['wordcount']['words']
			minutes = context['meta']['wordcount']['minutes']
	
	estimated_time = None
	
	if words > 0:
		estimated_time = ''
		estimated_seconds = float.__round__(words / (WORDS_PER_MINUTE / 60), 1)
		estimated_time_minutes = int(time.strftime(" %M", time.gmtime(estimated_seconds)).replace(' 0', ''))
		estimated_time_seconds = int(time.strftime(" %S", time.gmtime(estimated_seconds)).replace(' 0', ''))
		
		if estimated_time_minutes > 0:
			estimated_time += f'{estimated_time_minutes} minutes and '
		
		if estimated_time_seconds > 0:
			estimated_time += f'{estimated_time_seconds} seconds'
	
	if page:
		print(f"{page}: {words} - {minutes} - {estimated_time}")
	
	if not estimated_time:
		return
	
	context['page_read_time'] = f'📚 Estimated reading time: {estimated_time}'


def setup(app):
	app.add_config_value('page_read_time', True, False)
	app.connect('html-page-context', html_page_context)
