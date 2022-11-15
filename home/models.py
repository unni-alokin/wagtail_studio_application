from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel


# Work listing Page
class HomePage(Page):
    
    template = "home/home_page.html"
    intro = RichTextField(blank = True)

    # to order work to order as latest work first
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        workpages = self.get_children().live().order_by('-first_published_at')
        context['workpages'] = workpages
        return context


# Work Details Page
class WorkDetailsPage(Page):

    template = "home/work_details_page.html"
    
    work_title = models.CharField(max_length = 250, null = True)
    work_subtitle = models.CharField(max_length = 250, null = True)
    work_description = RichTextField(
        features=['h2', 'h3', 'bold', 'italic', 'link'],
        max_length = 5000, 
        null = True)

    content_panels = Page.content_panels + [

        MultiFieldPanel([
                FieldPanel('work_title'),
                FieldPanel('work_subtitle'),
            ], heading = "Work title & Subtitle" ),

        FieldPanel('work_description'),
        
        MultiFieldPanel([
                InlinePanel('thumbnail', label = "Thumbnail images"),
                InlinePanel('gallery_images', label = "Gallery images"),
            ], heading = "Images")]

    subpage_types = []

    def thumbnail_image(self):
        gallery_item = self.thumbnail.first()
        if gallery_item:
            return gallery_item.thumbnail
        else:
            return None



# Orderables for Thumbnail images and Gallery Images 
class WorkDetailsPagethumbnailImage(Orderable):

    page = ParentalKey(WorkDetailsPage, on_delete = models.CASCADE, related_name = 'thumbnail')
    thumbnail = models.ForeignKey(
        'wagtailimages.Image', on_delete = models.CASCADE, related_name = 'thumbnail', blank = True
    )

    panels = [
        FieldPanel('thumbnail'),
    ]

class WorkDetailsPageGalleryImage(Orderable):
 
    page = ParentalKey(WorkDetailsPage, on_delete = models.CASCADE, related_name = 'gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete = models.CASCADE,
    )
    panels = [
        FieldPanel('image'),
    ]

    