from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import ScannedQR, Event
import json
from django.http import JsonResponse
from django.db import IntegrityError



# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')


def logout_view(request):
    if request.method == 'GET':
        auth_logout(request)
        return render(request, 'login.html', {'success': 'Logout successful'})
    else:
        return render(request, 'login.html', {'error': 'Invalid request method'})

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return render(request, 'login.html', {'success': 'Login successful'})
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html', {'error': 'Invalid request method'})

@login_required
def register_qr(request):
    if request.method == 'GET':
        events = Event.objects.all()
        return render(request, 'register_qr.html', {'events': events})
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            unique_id = data.get('unique_id')
            event_id = data.get('event_id')
            
            if not all([unique_id, event_id]):
                return JsonResponse({'error': 'Missing required fields'}, status=400)
            
            try:
                # Get the event or return 404
                try:
                    event = Event.objects.get(id=event_id)
                except Event.DoesNotExist:
                    return JsonResponse({'error': 'Event not found'}, status=404)
                
                # Create the record with event relationship
                ScannedQR.objects.create(
                    unique_id=unique_id,
                    event=event,
                    is_scanned=True
                )
                return JsonResponse({'success': 'QR code registered successfully'})
            except IntegrityError:
                return JsonResponse({'error': 'QR code already registered for this event'}, status=400)
                
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)