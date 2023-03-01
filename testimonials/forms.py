from django.forms import ModelForm
from .models import Testimonial


class TestimonialAddForm(ModelForm):
    class Meta:
        model = Testimonial
        fields = "__all__"
        
    