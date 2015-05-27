from urllib.parse import urlparse

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.template import Context


def send_email_template(template, context, to, email_from=None, html=None, attachments=[]):
    """
    Renders an email template with this format:
        {% if subject %}Subject{% endif %}
        {% if message %}Email body{% endif %}
    
    context can be a dictionary or a template.Context instance
    """
    
    if isinstance(context, dict):
        context = Context(context)
    if isinstance(to, str):
        to = [to]
    
    if not 'site' in context:
        from orchestra import settings
        url = urlparse(settings.ORCHESTRA_SITE_URL)
        context['site'] = {
            'name': settings.ORCHESTRA_SITE_NAME,
            'scheme': url.scheme,
            'domain': url.netloc,
        }
    
    #subject cannot have new lines
    subject = render_to_string(template, {'subject': True}, context).strip()
    message = render_to_string(template, {'message': True}, context).strip()
    msg = EmailMultiAlternatives(subject, message, email_from, to, attachments=attachments)
    if html:
        html_message = render_to_string(html, {'message': True}, context)
        msg.attach_alternative(html_message, "text/html")
    msg.send()

