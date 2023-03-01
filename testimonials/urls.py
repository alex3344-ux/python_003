from django.urls import path
from .views import TestimonialListView

app_name = "testimonials"

urlpatterns = [
    path('', TestimonialListView.as_view(), name="testimonial_list"),

    path('add', TestimonialListView.as_view(), name='testimonials_add'),
    path('<int:pk>/update', TestimonialListView.as_view(), name="testimonials_update"),
    path('<int:pk>/delete', TestimonialListView.as_view(), name='testimonials_delete'),
]