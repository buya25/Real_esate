from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CommentForm(forms.Form):
    user_name = forms.CharField(max_length=200, label='Your Name')
    comment_text = forms.CharField(widget=forms.Textarea, label='Comment')

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-primary'))
