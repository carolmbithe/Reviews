from .models import Project
#......
class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['profile']
        
