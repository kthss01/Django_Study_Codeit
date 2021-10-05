from django.db.models import fields
from django.forms import ModelForm, widgets, RadioSelect

from podomarket.models import Post
from .models import User


# class SignupForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ["nickname", "kakao_id", "address"]
        
#     def signup(self, request, user):
#         user.nickname = self.cleaned_data["nickname"]
#         user.kakao_id = self.cleaned_data["kakao_id"]
#         user.address = self.cleaned_data["address"]
#         user.save()
        
class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "item_price",
            "item_condition",
            "item_details",
            "image1",
            "image2",
            "image3",
        ]
        widgets = {
            "item_condition": RadioSelect,
        }
        
class PostUpdateForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "item_price",
            "item_condition",
            "item_details",
            "image1",
            "image2",
            "image3",
            "is_sold"
        ]
        widgets = {
            "item_condition": RadioSelect,
        }
        
class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "nickname",
            "kakao_id",
            "address",
            "profile_pic",
        ]