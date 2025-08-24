from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class EventBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=100)
    date = blocks.DateBlock()
    time = blocks.TimeBlock(required=False)
    description = blocks.TextBlock()

    class Meta:
        template = 'home/blocks/event_block.html'
        icon = 'date'


class GalleryBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.CharBlock(max_length=200, required=False)

    class Meta:
        template = 'home/blocks/gallery_block.html'
        icon = 'image'


class HomePage(Page):
    template = 'home/home_page.html'
    max_count = 1

    # Hero section
    hero_title = models.CharField(
        max_length=200,
        default="Our Lady of Fatima Church",
        help_text="Main title for the hero section"
    )
    hero_subtitle = models.CharField(
        max_length=200,
        default="A Community of Faith and Love",
        help_text="Subtitle for the hero section"
    )
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Background image for hero section"
    )

    # Welcome section
    welcome_content = RichTextField(
        blank=True,
        help_text="Welcome message content"
    )

    # Events and Gallery
    events = StreamField([
        ('event', EventBlock()),
    ], blank=True, help_text="Upcoming events")

    gallery_images = StreamField([
        ('gallery_item', GalleryBlock()),
    ], blank=True, help_text="Parish gallery images")

    # Contact information
    contact_address = RichTextField(blank=True)
    contact_phone = models.CharField(max_length=50, blank=True)
    contact_email = models.EmailField(blank=True)
    contact_email_secondary = models.EmailField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_title'),
            FieldPanel('hero_subtitle'),
            FieldPanel('hero_image'),
        ], heading="Hero Section"),

        FieldPanel('welcome_content'),

        MultiFieldPanel([
            FieldPanel('events'),
            FieldPanel('gallery_images'),
        ], heading="Events & Gallery"),

        MultiFieldPanel([
            FieldPanel('contact_address'),
            FieldPanel('contact_phone'),
            FieldPanel('contact_email'),
            FieldPanel('contact_email_secondary'),
        ], heading="Contact Information"),
    ]