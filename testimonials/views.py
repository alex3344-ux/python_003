from django.shortcuts import render
from testimonials.models import Testimonial



from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .forms import TestimonialAddForm
# Create your views here.

class TestimonialListView(ListView):
    model = Testimonial
    template_name = 'testimonials_list.html'
    context_object_name = 'testimonials'


class TestimonialAddView(CreateView):
    model = Testimonial
    template_name = "testimonials_add.html"
    success_url = "/testimonials/"
    form_class = TestimonialAddForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save(commit=True)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class TestimonialUpdateViev(UpdateView):
    model = Testimonial
    template_name = "testimonials_add.html"
    form_class = TestimonialAddForm
    success_url = "/testimonials/"

class TestimonialDeleteView(DeleteView):
    model = Testimonial
    template_name = "testimonials_delete.html"
    success_url = "/testimonials/"
