from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from phonenumber_field.modelfields import PhoneNumberField
from .models import User

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(), message="User with that email already exists")]
    )
    nin = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(), message="User with that National ID number already exists")]
    )
    phone_number = PhoneNumberField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    # password = serializers.
    class Meta:
        model = User
        fields = ('nin', 'password', 'phone_number', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'phone_number': {'required': True}
        }
