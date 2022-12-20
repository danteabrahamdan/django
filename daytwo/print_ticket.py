from week2.wsgi import *
from django.template.loader import get_template
from weasyprint import HTML


def print_ticket():
    template = get_template('ticket.html')
    context = { "name": "Hello world" }
    html_template = template.render(context)
    HTML(string=html_template).write_pdf(target='ticket.pdf')

print_ticket()