from django.http import JsonResponse
from django.shortcuts import render
import speech_recognition as sr

def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def start_detection(request):
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Please speak now...")
            audio_data = recognizer.listen(source)
            print("Processing...")
            text = recognizer.recognize_google(audio_data)
            return JsonResponse({"message": text})
    except sr.UnknownValueError:
        return JsonResponse({"error": "Could not understand the audio."})
    except sr.RequestError:
        return JsonResponse({"error": "Error with the speech recognition service."})
