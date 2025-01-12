from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserCreateSerializer
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserRegistrationForm
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# List all users (Admin Access) or retrieve details
class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser] 
    
class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

# Register a new user
class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserCreateSerializer
    permission_classes = [AllowAny]

    # save the user
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generate token
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        
        # Return the tokens in the response
        return Response({
            'user': CustomUserCreateSerializer(user).data,
            'access_token': access_token,
            'refresh_token': refresh_token,
        }, status=status.HTTP_201_CREATED) 
        
# Create view for form handling
def register_user(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()       # create the user
            messages.success(request, 'Registration successful')
            # redirect to login page after successfully registered
            return redirect('login')
        else:
            print(form.errors)  # Debugging output for failed form validation
            messages.error(request, 'There was an error with your registration.')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})
   
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate the user using the form data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Generate JWT token on successful authentication
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                refresh_token = str(refresh)

                # Check if the request expects a JSON response
                if request.content_type == 'application/json' or 'application/json' in request.META.get('HTTP_ACCEPT', ''):
                    return Response({
                        'access_token': access_token,
                        'refresh_token': refresh_token,
                    }, status=status.HTTP_200_OK)
                else:
                    # Handle the non-API (form-based) response, e.g., redirect to homepage
                    login(request, user)
                    return redirect('users:home')
            else:
                messages.error(request, 'Invalid credentials. Please try again.')
        else:
            messages.error(request, 'Invalid form submission. Please try again.')

    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})


# view for homepage
@login_required
def home(request):
    return render(request, 'users/home.html')

# View for Introduction (Learn More)

def learn_more(request):
    return render(request, 'users/learn_more.html')


# Add Authentication
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'This is a protected endpoint' })
