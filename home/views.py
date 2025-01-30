from django.shortcuts import render, redirect
import google.generativeai as genai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.conf import settings
from .forms import UserRegistrationForm, LoginForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth import login, logout, authenticate



def chatbot_view(request):
    return render(request, 'index.html')

genai.configure(api_key=settings.GEMINI_API_KEY)
 
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction="precise and concise outputs",
)

@csrf_exempt
@require_POST
def ask_question(request):
    question = request.POST.get("question")
    if not question:
        return JsonResponse({"error": "Question is required"}, status=400)

    chat_session = model.start_chat(history=[{"role": "user", "parts": [question]}])
    response = chat_session.send_message(question)

    return JsonResponse({"answer": response.text})


def signup_view(request):
    # Redirect if user is already authenticated
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('/login/')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    # Redirect if user is already authenticated
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')



@login_required
def profile_update(request):
    try:
        if request.method == 'POST':
            form = UserProfileForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your profile has been updated successfully!')
                return redirect('home:profile_update')  # Add namespace here
        else:
            form = UserProfileForm(instance=request.user)
        
        return render(request, 'home/profile_update.html', {'form': form})
    except Exception as e:
        print(f"Error in profile_update view: {str(e)}")
        messages.error(request, 'An error occurred while updating your profile.')
        return redirect('home:home')  # Add namespace here too