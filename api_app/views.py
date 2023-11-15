from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(csrf_exempt, name = 'dispatch')
class StudentAPI(View):
    def get(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is  not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type = 'application/json')
        stu =Student.objects.all()
        serializer = StudentSerializer(stu, many =True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type = 'application/json')
    
    def post(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            response_data = {'msg':'Data Created/Inserted'}
            json_data = JSONRenderer().render(response_data)
            return HttpResponse(json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')
    
    def put(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id = id)
        # complete update -required all data from front end/client
        # serializer = StudentSerializer(stu,data = pythondata)
        # Partial Update - all data not required
        serializer = StudentSerializer(stu, data =pythondata,partial = True)
        if serializer.is_valid():
            serializer.save()
            response_data = {'msg': 'Data Updated!'}
            json_data= JSONRenderer().render(response_data)
            return HttpResponse(json_data, content_type = 'application/json')
        json_data= JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')
    
    def delete(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        response_data = {'msg' :'Data Deleted!'}
        # json_data = JSONRenderer().render(response_data)
        # return HttpResponse(json_data, content_type = 'application/json')
        # instead of using above two line we can also use the jsonresponse function method 
        return JsonResponse(response_data, safe = False)
    
