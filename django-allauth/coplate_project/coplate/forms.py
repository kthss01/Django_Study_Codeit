from django.db.models import fields
from django.forms import ModelForm, widgets, RadioSelect, Textarea
from .models import User, Review


# class SignupForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ["nickname"]

#     def signup(self, request, user):
#         user.nickname = self.cleaned_data["nickname"]
#         user.save()
        
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "restaurant_name",
            "restaurant_link",
            "rating",
            "image1",
            "image2",
            "image3",
            "content",
        ]
        widgets = {
            "rating": RadioSelect,
        }
          
class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "nickname",
            "profile_pic",
            "intro",
        ]
        widgets = {
            "intro": Textarea,
        }