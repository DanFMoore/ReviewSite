from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from content.models import SystemPage

class ContentConfig(AppConfig):
    """This is a ridiculously complicated way to just register signal receivers"""
    name = 'content'

    def ready(self):
        """Register receiver to create initial system pages, on site install"""

        @receiver(post_migrate, weak=False, sender=self)
        def install_initial_records(sender, **kwargs):
            """Automatically create initial system pages"""

            SystemPage.objects.get_or_create(name='Home Page', defaults={
                'title': 'Home Page',
                'content': 'Add your home page content here'
            })

            SystemPage.objects.get_or_create(name='404 Page', defaults={
                'title': "Page not found",
                'content': "Page not found"
            })
