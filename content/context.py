from content import models

class NotFound:
    """Make the function a class instance, in order that get is only called once"""

    def __call__(self, request):
        """Pass the not found page to the template. It does pass it for every view
        unfortunately as there's no way to determine if the current view is a 404"""
        if not hasattr(self, 'page'):
            self.page = models.SystemPage.objects.get(name='404 Page')

        return {'not_found_page': self.page}

#make object appear as function
not_found = NotFound()