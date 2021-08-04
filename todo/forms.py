from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Task

# create form for adding editing tasks
class TaskForm(forms.ModelForm):
    Title = forms.CharField(
        label="Task Title",
        widget=forms.Textarea
    )
    Description = forms.CharField(
        label="Extra Information",
        widget=forms.Textarea
    )
    Completed = forms.BooleanField(
        label="Completed",
        required=False
    )

    class Meta:
        model = Task
        fields = ['Title', 'Description', 'Completed']
    
    # integrating django_crispy_forms
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'taskform'        # form id in the DOM
        self.helper.form_class = 'taskform'     # form class in the DOM
        self.helper.form_method = 'post'        # form method to be used in sending
        self.helper.form_action = ''            # url to send POST data  changed later hence is empty for now

        self.helper.add_input(Submit('submit', 'Submit'))       #submit button
    
    
