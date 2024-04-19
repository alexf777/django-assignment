from django.views import View
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.shortcuts import render
from .models import Page

class PageView(View):
    def get(self, request, page_id):
        try:
            page = Page.objects.get(pk=page_id)
            user_status = 'Logged in' if request.user.is_authenticated else 'Not logged in'
            user_ip = request.META.get('REMOTE_ADDR', '')
            context = {
                'page': page,
                'user_status': user_status,
                'user_ip': user_ip
            }
            template = get_template('page.html')
            return HttpResponse(template.render(context, request))
        except Page.DoesNotExist:
            raise Http404("Page not found")
        
def custom_404(request, exception):
    context = {'message': 'Page not found'}
    return render(request, '404.html', context, status=404)