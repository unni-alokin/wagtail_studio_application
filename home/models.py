from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from studio import models

class HomePage(Page):
    
    max_count = 1

    subpage_types = ['studio.WorkIndexPage', 'studio.BlogIndexPage', 'studio.AboutPage']


    