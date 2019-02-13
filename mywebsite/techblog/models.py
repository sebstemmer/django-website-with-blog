from django import forms
from django.db import models

# start wagtail includes
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtail.core.fields import StreamField
from wagtail.core import blocks
# end wagtail includes


class TechblogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'TechblogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class TechblogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=500)
    body = StreamField([
        ('bodyBlock', blocks.RawHTMLBlock())
    ])
    tags = ClusterTaggableManager(through=TechblogPageTag, blank=True)
    categories = ParentalManyToManyField('techblog.TechblogCategory', blank=True)

    template = 'techblog/page.html'

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Blog information"),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]


class TechblogPageGalleryImage(Orderable):
    page = ParentalKey(TechblogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


@register_snippet
class TechblogCategory(models.Model):
    name = models.CharField(max_length=255)

    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'blog categories'
