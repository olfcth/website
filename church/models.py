from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet


@register_snippet
class NewsItem(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    content = RichTextField()
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']
        verbose_name = "News Item"
        verbose_name_plural = "News Items"

    def __str__(self):
        return self.title


class AboutPage(Page):
    template = 'church/about_page.html'

    introduction = RichTextField(blank=True)
    history_content = RichTextField(blank=True)
    mission_statement = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduction'),
        FieldPanel('history_content'),
        FieldPanel('mission_statement'),
    ]


class NewsPage(Page):
    template = 'church/news_page.html'

    introduction = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduction'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['news_items'] = NewsItem.objects.all()[:10]
        return context


class MassSchedulePage(Page):
    template = 'church/mass_schedule_page.html'

    introduction = RichTextField(blank=True)
    weekday_masses = RichTextField(blank=True)
    weekend_masses = RichTextField(blank=True)
    special_masses = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduction'),
        MultiFieldPanel([
            FieldPanel('weekday_masses'),
            FieldPanel('weekend_masses'),
            FieldPanel('special_masses'),
        ], heading="Mass Schedule"),
    ]


class ContactPage(Page):
    template = 'church/contact_page.html'

    introduction = RichTextField(blank=True)
    address = RichTextField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    office_hours = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduction'),
        MultiFieldPanel([
            FieldPanel('address'),
            FieldPanel('phone'),
            FieldPanel('email'),
            FieldPanel('office_hours'),
        ], heading="Contact Information"),
    ]


class ParishCouncilPage(Page):
    template = 'church/parish_council_page.html'

    introduction = RichTextField(blank=True)
    council_members = StreamField([
        ('member', blocks.StructBlock([
            ('name', blocks.CharBlock(max_length=100)),
            ('position', blocks.CharBlock(max_length=100)),
            ('description', blocks.TextBlock(required=False)),
            ('photo', ImageChooserBlock(required=False)),
        ])),
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduction'),
        FieldPanel('council_members'),
    ]