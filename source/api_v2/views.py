import json
from django.views.decorators.csrf import ensure_csrf_cookie

from django.http import JsonResponse, Http404
from django.views.generic.base import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api_v2.serializers import ArticleSerializer, DetailSerializer, UpdateSerializer
from webapp.models import Article


class ArticleListView(View):
    def get(self, request, *args, **kwargs):
        objects = Article.objects.all()
        serializer = ArticleSerializer(objects, many=True)
        return JsonResponse(serializer.data, safe=False)



class ArticleDetailView(APIView):
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        objects = self.get_object(pk)
        serializer = DetailSerializer(objects)
        return JsonResponse(serializer.data)

    def put(self, request, pk, format=None):
        objects = self.get_object(pk)
        serializer = DetailSerializer(objects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        objects = Article.objects.get(id=pk)
        objects.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







class ArticleCreateView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            article = serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            response = JsonResponse({'errors': serializer.errors})
            response.status_code = 400
            return response