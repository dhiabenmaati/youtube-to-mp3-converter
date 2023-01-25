import random
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.template import loader

from django.templatetags.static import static
import youtube_dl

# Create your views here.

## Get All Links 
@api_view(["GET"])
def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


## Get Link Api
@api_view(["POST"])
def getLink(request):

    if request.method == 'POST':

        video_url = request.POST['link']
        video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
        
        storage_name = random.randint(1000000, 999999999999999)
        storage_name = str(storage_name)
        filename = f"youtube_mp3_app/static/"+storage_name+".mp3"
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':filename,
        }
        
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
        print("Download complete... {}".format(filename))

        download_url = "http://127.0.0.1:8000/static/"+storage_name+".mp3"
        return HttpResponse(download_url)
