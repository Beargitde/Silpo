from django.shortcuts import render
from django.views.generic.edit import FormView
from .form import Feedbackform
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import QRcode

class QRListView(ListView):
    model = QRcode

class FeedBackview(FormView):
    form_class = Feedbackform
    template_name = 'qrservice/qr.html'
    success_url = reverse_lazy('qrservice:ok')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# Create your views here.
