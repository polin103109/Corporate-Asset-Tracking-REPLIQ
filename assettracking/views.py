#rom django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from assettracking.models import Company
from assettracking.serializers import CompanySerializer

@csrf_exempt
def company_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        apivar = Company.objects.all()
        serializer = CompanySerializer(apivar, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)