from content import models

class NotFound:
    """When a 404 error is raised, this will add the not_found_page variable
    to the template (404.html), which contains the 404 SystemPage object.
    The 404 page is never called when settings.DEBUG == True
    The function is made into a class instance, in order that get is only called once"""

    def __call__(self, request):
        """Pass the not found page to the template. It does pass it for every view
        unfortunately as there's no way to determine if the current view is a 404"""

        if not hasattr(self, 'page'):
            self.page = models.SystemPage.objects.get(name='404 Page')

        rendered = self.page.render({'request_path': request.path})
        return {'not_found_page': rendered}

#make object appear as function
not_found = NotFound()