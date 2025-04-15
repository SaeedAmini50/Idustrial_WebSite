from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import TextEntry, Number

# Create your views here.

class PublicTextListView(ListView):
    model = TextEntry
    template_name = 'textInfo/text_list.html'
    context_object_name = 'texts'

    def get_queryset(self):
        return TextEntry.objects.filter(is_visible=True).order_by('unique_id')

@method_decorator(staff_member_required, name='dispatch')
class AdminTextListView(ListView):
    model = TextEntry
    template_name = 'textInfo/admin_text_list.html'
    context_object_name = 'texts'

    def get_queryset(self):
        return TextEntry.objects.all().order_by('unique_id')
    
def single(request):
    texts = TextEntry.objects.filter(is_visible=True).order_by('unique_id') 
    numbers = Number.objects.all()
    return render(request, 'single.html', {'texts': texts, 'numbers': numbers})
