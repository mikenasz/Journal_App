from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import journal, Mood, Activities


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'role': "radio"
            })
        }


class CreateEntryForm(ModelForm):
    class Meta:
        model = journal
        fields = ('title', 'entry')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Title'})
        self.fields['entry'].widget.attrs.update({'class':'textarea','placeholder':'Enter a journal entry'})


MOOD_CATEGORY = (
    ('Amazing', 'Amazing'),
    ('Meh', 'Meh'),
    ('Terrible', 'Terrible'),

)


class MoodForm(ModelForm):
    mood = forms.ChoiceField(choices=MOOD_CATEGORY, widget=forms.RadioSelect())
    class Meta:
        model = Mood
        fields = ['mood']


Social= (
    ('family', 'family'),
    ('friends', 'friends'),
    ('date', 'date'),
    ('party', 'party'),

)
Hobbies=(
    ('reading','reading'),
    ('gaming', 'gaming'),
    ('sport', 'sport'),
    ('practice', 'practice'),

)
Food=(
('healthy', 'healthy'),
    ('fast food', 'fast food'),
    ('restaurant', 'restaurant'),
    ('sweets', 'sweets'),
)

Health=(
('exercise', 'exercise'),
    ('drink water', 'drink water'),
    ('walk', 'walk'),
    ('yoga', 'yoga'),

)
Chores=(
('shopping', 'shopping'),
    ('cooking', 'cooking'),
    ('cleaning', 'cleaning'),
    ('laundry', 'laundry')
)



class ActivitiesForm(ModelForm):
    social = forms.ChoiceField(choices=Social, widget=forms.RadioSelect())
    hobbies = forms.ChoiceField(choices=Hobbies, widget=forms.RadioSelect())
    food = forms.ChoiceField(choices=Food, widget=forms.RadioSelect())
    health = forms.ChoiceField(choices=Health, widget=forms.RadioSelect())
    chores = forms.ChoiceField(choices=Chores, widget=forms.RadioSelect())

    class Meta:
        model = Activities
        fields = ['social', 'hobbies','food','health','chores']

    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['amazing'].widget.attrs.update({'class': 'form-check-input','type':'radio'})
    #     self.fields['meh'].widget.attrs.update({'class':'form-check-input','type':'radio'})
    #     self.fields['terrible'].widget.attrs.update({'class': 'form-check-input','type':'radio'})
