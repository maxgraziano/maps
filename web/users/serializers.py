from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
import uuid

User = get_user_model()

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD

    def validate(self, attrs):
        credentials = {
            'email': attrs.get('email'),
            'password': attrs.get('password')
        }

        user = authenticate(**credentials)

        if user is None or not user.is_active or not user.is_verified:
            raise AuthenticationFailed('No active account found with the given credentials.', 'no_active_account')
        
        data = super().validate(attrs)
        data.update({
            'user': {
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'profile_photo': f"{settings.BACKEND_ROOT_URL}{user.profile_photo.url}" if user.profile_photo else None
            }
        })
        return data

class UserSerializer(serializers.ModelSerializer):
    # first_name
    #  - Trimmed Length = 0 ("This field may not be blank.")
    first_name = serializers.CharField(
        required=True,
        validators=[
            RegexValidator(regex="^[a-zA-Z- ]*$", inverse_match=False, message="Only letters, spaces, and hyphens allowed."),
            MinLengthValidator(2, message="Must be at least 2 characters."),
            MaxLengthValidator(150, message="Must be no more than 150 characters.")
        ]
    )
    # last_name
    #  - Trimmed Length = 0 ("This field may not be blank.")
    last_name = serializers.CharField(
        required=True,
        validators=[
            RegexValidator(regex="^[a-zA-Z- ]*$", inverse_match=False, message="Only letters, spaces, and hyphens allowed."),
            MinLengthValidator(2, message="Must be at least 2 characters."),
            MaxLengthValidator(150, message="Must be no more than 150 characters.")
        ]        
    )
    # email: validator managed by serializers.EmailField
    #  - Validate email format. ("Enter a valid email address.")
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with this email address already exists."
            )
        ]
    )
    # password: validators managed by settings.AUTH_PASSWORD_VALIDATORS
    #  - Length >= 8 [MinimumLengthValidator] ("This password is too short. It must contain at least 8 characters.")
    #  - Password can't be entirely numeric [NumericPasswordValidator] ("This password is entirely numeric.")
    #  - Password is different from email, username, first_name, last_name [UserAttributeSimilarityValidator] (Backend only)
    #  - Password is not common [CommonPasswordValidator] (Backend only)
    password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[
            MaxLengthValidator(128, message="This password is too long. It must contain at most 128 characters.")
        ]        
    )

    # profile_photo
    # - "The file must be less than 5 MB." (Frontend)
    # - "The file must be a jpeg, png, or gif." (Frontend)
    # - "The submitted data was not a file. Check the encoding type on the form." (Backend)
    profile_photo = serializers.ImageField(
        required=False
    )

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'profile_photo')

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        # email is required for creating a user
        if 'email' not in validated_data:
            raise serializers.ValidationError({"email": "This field is required."})
        
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            profile_photo=validated_data.get('profile_photo', None),

            is_verified=False,
            activation_token=uuid.uuid4(),
            activation_token_expires=timezone.now() + timedelta(days=1)
        )
        return user
    
    def update(self, instance, validated_data):
        # remove email from validated_data, it should not be updated
        validated_data.pop('email', None)

        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)

        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
    
    def save(self, **kwargs):
        instance = super().save(**kwargs)
        instance.profile_photo=self.validated_data.get('profile_photo', instance.profile_photo)
        instance.save()
        return instance