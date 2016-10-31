from __future__ import absolute_import

from celery import task

@task(name="app.tasks.print_text")
def print_text():
	return "Hola soy una celery task"