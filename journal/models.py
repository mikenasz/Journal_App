from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class journal(models.Model):
    title = models.CharField(max_length=200)
    entry = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

MOOD_CATEGORY = (
    ('Amazing', 'Amazing'),
    ('Meh', 'Meh'),
    ('Terrible', 'Terrible'),

)

class Mood(models.Model):
    mood = models.CharField(max_length=20, blank=True, choices=MOOD_CATEGORY)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    #amazing = models.BooleanField(default=False)
    #meh = models.BooleanField(default=False)
    #terrible = models.BooleanField(default=False)

    #def __str__(self):
       # return 'Mood'.format(self.id)


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


class Activities(models.Model):
    social = models.CharField(max_length=20, blank=True, choices=Social)
    hobbies = models.CharField(max_length=20, blank=True, choices=Hobbies)
    food = models.CharField(max_length=20, blank=True, choices=Food)
    health = models.CharField(max_length=20, blank=True, choices=Health)
    chores = models.CharField(max_length=20, blank=True, choices=Chores)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
