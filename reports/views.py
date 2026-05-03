"""from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello")"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import test_task


@api_view(["GET"])
def trigger_task(request):
    test_task.delay()  # Sends task to queue, Returns immediately, Worker runs it later
    return Response({"message": "Task triggered"})
