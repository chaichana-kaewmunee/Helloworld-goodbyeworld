from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to My Django App</h1>")
# ตัวแปรเก็บสถานะปัจจุบัน
current_state = {"message": "Hello World"}

@api_view(["GET"])
def toggle_message(request):
    if current_state["message"] == "Hello World":
        current_state["message"] = "Goodbye World"
    else:
        current_state["message"] = "Hello World"
    
    return Response({"message": current_state["message"]})
