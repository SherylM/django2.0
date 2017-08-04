from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import Textbook
from .models import Prepbook

#Generic views
class TextbookIndexView(generic.ListView):
    template_name = 'buytextbooks/textbooks.html'

    def get_queryset(self):
        return Textbook.objects.all()
            #retuns object_list
class PrepbookIndexView(generic.ListView):
    template_name = 'buytextbooks/prepbooks.html'

    def get_queryset(self):
        return Prepbook.objects.all()

class TextbookDetailView(generic.DetailView):
    model = Textbook
    template_name = 'buytextbooks/detailtextbook.html'

class PrepbookDetailView(generic.DetailView):
    model = Prepbook
    template_name = 'buytextbooks/detailprepbook.html'

        # Create your views here.

def blog(request):
    return render(request, 'buytextbooks/blog.html')

def home(request):
    return render(request, 'buytextbooks/home.html')
