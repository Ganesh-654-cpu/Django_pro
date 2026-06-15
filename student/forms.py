# from django.forms import ModelForm
# from .models import reg Person

# class personform(ModelForm):
#     class Meta:
#         model=person
#         fields='__all__'

from django.forms import ModelForm
from .models import person

class PersonForm(ModelForm):
    class Meta:
        model = person
        fields = '__all__'