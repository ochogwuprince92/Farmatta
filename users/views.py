from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserCreateSerializer
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserRegistrationForm

# List all users (Admin Access) or retrieve details
class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

# Register a new user
class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserCreateSerializer
    permission_classes = [AllowAny]

# Create view for form handling
def register_user(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()                 # create the user
            messages.success(request, 'Registration successful')
            # redirect to login page after successfully registered
            return redirect('login')
        else:
            messages.error(request, 'There was an error with your registration.')
    else:
        form = CustomUserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})