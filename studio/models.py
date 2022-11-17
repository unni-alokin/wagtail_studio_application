from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from ckeditor.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from django import forms       
from wagtail.admin import widgets
from wagtail.snippets.models import register_snippet

# Create your models here.



# Work Listing Page
class WorkIndexPage(Page):

    template = "work/work_index_page.html"
    intro = RichTextField(blank = True)
    max_count = 1
    # to order work to order as latest work first
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        workpages = self.get_children().live().order_by('-first_published_at')
        context['workpages'] = workpages
        return context
    
    subpage_types = ['WorkDetailsPage']





# Work Details Page
class WorkDetailsPage(Page):

    template = "work/work_details_page.html"
    subpage_types = []
    parent_page_type = ['WorkIndexPage']

    work_title = models.CharField(max_length = 250, null = True)
    work_subtitle = models.CharField(max_length = 250, null = True)
    work_description = RichTextField(
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


    def thumbnail_image(self):
        gallery_item = self.thumbnail.first()
        if gallery_item:
            return gallery_item.thumbnail
        else:
            return None
    # to get the previous sibling
    def prev_portrait(self):
     if self.get_prev_sibling():
        return self.get_prev_sibling().url
     else:
        return self.get_siblings().last().url

    # to get the next sibling
    def next_portrait(self):
     if self.get_next_sibling():
        return self.get_next_sibling().url
     else:
        return self.get_siblings().first().url




# Orderables for Thumbnail images
class WorkDetailsPagethumbnailImage(Orderable):

    page = ParentalKey(WorkDetailsPage, on_delete = models.CASCADE, related_name = 'thumbnail')
    thumbnail = models.ForeignKey(
        'wagtailimages.Image', on_delete = models.CASCADE, related_name = 'thumbnail', blank = True
    )

    panels = [
        FieldPanel('thumbnail'),
    ]

# Orderables for Gallery images
class WorkDetailsPageGalleryImage(Orderable):
 
    page = ParentalKey(WorkDetailsPage, on_delete = models.CASCADE, related_name = 'gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete = models.CASCADE,
    )
    panels = [
        FieldPanel('image'),
    ]



# About Page
class AboutPage(Page):

    template = "about/about_page.html"

    max_count = 1

    subpage_types = [ ]
    
    creator_name = models.CharField(blank = True, max_length = 100)
    creator_profession = models.CharField(blank = True, max_length = 200)
    creator_description = RichTextField(blank = True, max_length = 5000)

    content_panels = Page.content_panels + [

        MultiFieldPanel(
            [
                FieldPanel('creator_name'),
                FieldPanel('creator_profession'),
                FieldPanel('creator_description'),
            ],heading = "Creator Description"
        ),

        InlinePanel('gallery_images', label="Gallery images"),
    ]

# About Page Orderables
class AboutPageImage(Orderable):
    
    max_count = 1
    page = ParentalKey(AboutPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE,
    )
    panels = [
        FieldPanel('image'),
    ]





# Blog Page

# Blog listing page models
class BlogIndexPage(Page):

    template = "blog/blog_index_page.html"

    subpage_types = ['BlogPage']
    
    
    intro = RichTextField(blank=True,  max_length = 100)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('first_published_at')
        context['blogpages'] = blogpages
        return context




# Blog Page Models
class BlogPage(Page):

    template = "blog/blog_page.html"
    

    blog_title = models.CharField(blank=True,  max_length = 100)
    blog_date = models.DateField("Post date")
    blog_abstract = RichTextField(blank = True, max_length = 500)
    blog_description = RichTextField(blank=True, max_length = 5000)


    content_panels = Page.content_panels + [

        MultiFieldPanel(
            [
                FieldPanel('blog_title'),
                FieldPanel('blog_date'),
            ], heading = "Blog title and date"),

        MultiFieldPanel(
            [
                FieldPanel('blog_abstract'),
                FieldPanel('blog_description'),
            ], heading = "Blog abstract and description"),

        MultiFieldPanel(
            [
                InlinePanel('gallery_images', label="Gallery images"),
            ], heading = "Blog Images")
    ]

    subpage_types = []
    parent_page_type = ['BlogIndexPage']


    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    def prev_portrait(self):
     if self.get_prev_sibling():
        return self.get_prev_sibling().url
     else:
        return self.get_siblings().last().url

    def next_portrait(self):
     if self.get_next_sibling():
        return self.get_next_sibling().url
     else:
        return self.get_siblings().first().url




# Blog Page Images Orderables
class BlogPageImage(Orderable):
    max_count = 1
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE,
    )

    panels = [
        FieldPanel('image'),
    ]





# Model Forms
class Contact(models.Model):
    Name = models.CharField(max_length = 100)
    Email = models.EmailField()
    Subject = models.CharField(max_length = 100)
    Message = models.CharField(max_length = 350) 
    


# Snippets

@register_snippet
class EmailSnippet(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100, null = True)
    IsActive=models.BooleanField(null=True)
    panels = [ 
        FieldPanel("name"),
        FieldPanel("email"),
        FieldPanel("IsActive"),
    ]
    def str(self):
        return self.name


