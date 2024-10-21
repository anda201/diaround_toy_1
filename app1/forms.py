from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            # TextInput 한 줄짜리 텍스트를 입력받는 용도
            'title' : forms.TextInput(
                attrs= {
                    'class': 'title-input',
                    'placeholder': 'title',
                }
            ),
            # Textarea 여러 줄의 텍스트를 입력받을 수 있는 위젯
            'content' : forms.Textarea(
                attrs= {
                    'class': 'content-input',
                    'placeholder': 'Enter the contents.',
                }
            ),
        }