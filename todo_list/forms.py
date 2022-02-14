from django.forms import ModelForm, TextInput
from todo_list.models import *

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'