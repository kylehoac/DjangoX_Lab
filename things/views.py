from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Thing
from django.urls import reverse_lazy

class ThingListView(ListView):
    template_name = "things/thing_list.html"
    model = Thing


class ThingDetailView(DetailView):
    template_name = "things/thing_detail.html"
    model = Thing


class ThingCreateView(CreateView):
    template_name = "things/thing_create.html"
    model = Thing

    fields = ["name","reviewer","rating"]

class ThingUpdateView(UpdateView):
    template_name = "things/thing_update.html"
    model = Thing

    fields = ["name","reviewer","rating"]
    
class ThingDeleteView(DeleteView):
    template_name = "things/thing_delete.html"
    model = Thing

    success_url = reverse_lazy("thing_list")