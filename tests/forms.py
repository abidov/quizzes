from .models import Test, Question, Answer, TestResult
from django import forms


class TestCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': 'form-control mr-sm-2'})
        self.fields['title'].widget.attrs.update({'class': 'form-control mr-sm-2',
                                                  'type': 'text',
                                                  'placeholder': 'Title',
                                                  'aria-label': 'Title',
                                                  })
        self.fields['description'].widget.attrs.update({'class': 'form-control mr-sm-2',
                                                        'placeholder': 'Description',
                                                        'aria-label': 'Description',
                                                        })
        self.fields['image'].widget.attrs.update({'class': 'form-control-file'})

    class Meta:
        model = Test
        exclude = ['user', 'is_active']


class TestUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': 'form-control mr-sm-2'})
        self.fields['title'].widget.attrs.update({'class': 'form-control mr-sm-2',
                                                  'placeholder': 'Title',
                                                  'aria-label': 'Title',
                                                  })
        self.fields['description'].widget.attrs.update({'class': 'form-control mr-sm-2',
                                                        'placeholder': 'Description',
                                                        'aria-label': 'Description',
                                                        })

        self.fields['is_active'].widget.attrs.update({'class': 'form-control mr-sm-2',
                                                      'placeholder': 'Is Active',
                                                      'aria-label': 'Is Active',
                                                      })
        self.fields['image'].widget.attrs.update({'class': 'form-control-file'})

    class Meta:
        model = Test
        exclude = ['user', 'questions_id']


class QuestionCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['problem'].widget.attrs.update({'class': 'form-control mr-sm-2',
                                                    'placeholder': 'Problem',
                                                    'aria-label': 'Problem',
                                                    })

    class Meta:
        model = Question
        exclude = ['test']


class AnswerCreateForm(forms.ModelForm):

    class Meta:
        model = Answer
        exclude = ['question', ]
