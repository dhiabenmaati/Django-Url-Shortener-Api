from django.http import HttpResponseRedirect
from rest_framework.response import Response
from url_shortener_app.models import UrlModel
from url_shortener_app.serializers import UrlSerializer
from rest_framework.decorators import api_view

from django.http import HttpResponse
from django.template import loader

import random
import string


## INDEX
def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


## Get All Links 
@api_view(["GET"])
def urlList(request):
    urls = UrlModel.objects.all()
    serializer = UrlSerializer(urls, many=True)
    return Response(serializer.data)


## Create Link
@api_view(["POST"])
def urlCreate(request):
    if request.method == 'POST':
        data = {}
        data["main_url"] = request.POST['link']

        shortened_url = "".join(random.choices(string.ascii_lowercase, k=9))
        edit_password = random.randint(1000000, 9999999999999999)

        data["shrtened_ur"] = shortened_url
        data["edit_password"] = edit_password
        print(data)
        serializer = UrlSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    return Response("Please check your data")

## Delete Link
@api_view(["DELETE"])
def urlDelete(request, pk):
    url = UrlModel.objects.get(edit_password=pk)
    url.delete()

    return Response("Deleted Record")


## Link Redirection
@api_view(["GET"])
def urlRedirect(request, pk):

    if UrlModel.objects.filter(shrtened_ur=pk).exists():

        url = UrlModel.objects.get(shrtened_ur=pk)
        serializer = UrlSerializer(url, many=False)
        return HttpResponseRedirect(serializer.data["main_url"])

    else:
        return Response("Nothing Found Here")

