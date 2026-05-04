"""from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello")"""

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import test_task
from django.http import JsonResponse
from .tasks import add


@api_view(["GET"])
def trigger_task(request):
    test_task.delay()  # Sends task to queue, Returns immediately, Worker runs it later
    return Response({"message": "Task triggered"})


@csrf_exempt
def trigger_task_1(request):
    if request.method == "POST":
        x = int(request.POST.get("x", 0))
        y = int(request.POST.get("y", 0))
        result = add.delay(x, y)
        return JsonResponse({"status": "Task triggered", "task_id": result.id})
    return JsonResponse({"error": "Invalid request"}, status=400)
