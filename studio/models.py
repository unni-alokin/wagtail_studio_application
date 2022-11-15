from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from django import forms       
from wagtail.admin import widgets


# Create your models here.


# tixxwujvrtuepktz


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

    intro = RichTextField(blank=True,  max_length = 100)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('first_published_at')
        context['blogpages'] = blogpages
        return context

    subpage_types = [
        'studio.BlogPage',
    ]



# Blog Page Models
class BlogPage(Page):

    template = "blog/blog_page.html"
    

    blog_title = models.CharField(blank=True,  max_length = 100)
    blog_date = models.DateField("Post date")
    blog_description = RichTextField(blank=True, max_length = 5000)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    content_panels = Page.content_panels + [
        FieldPanel('blog_title'),
        FieldPanel('blog_date'),
        FieldPanel('blog_description'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

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
    



