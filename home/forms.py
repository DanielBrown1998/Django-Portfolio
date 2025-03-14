from django.forms import ModelForm
from home.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        field = [
            "name",
            "description",
            "link_github",
            "tecnology"
        ]
