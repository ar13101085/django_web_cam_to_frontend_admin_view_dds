import os
import random
import cv2

from django.http import JsonResponse
from django.shortcuts import render
from PIL import Image

class Staticdata:
    cam1=0;
    cam2=0;
    cam3=0;
# Create your views here.
def myapp(request):
    return render(request,'index.html');
def runopencv(request):
     #return render(request,"opencv.html")
     #return HttpResponse("Hello",content_type="application/json");
     man={'man':12,'name':'Arif'};
     man['isLove']=True
     return JsonResponse(man)
def getphotoinfo(request):
    if Staticdata.cam1>158:
        Staticdata.cam1=0;
    elif Staticdata.cam2>156:
        Staticdata.cam2=0;
    elif Staticdata.cam3>129:
        Staticdata.cam3=0;
    photo={};
    photo['cam_name']=request.GET['name'];
    #idx=random.randint(0,2);
    #photo['cam_name']=listCam[idx];



    listPerson=['p1','p2','p3','p4','p5'];
    listStatus=["standing","sitting"];

    person={};


    if photo['cam_name']=='cam1':

        photo['path'] = '/img/cam1/' + str(Staticdata.cam1) + '.jpg';

        img = Image.open(os.getcwd() + '/static/img/cam1/' + str(Staticdata.cam1) + '.jpg')
        img2 = img.crop((random.randint(0, 50), random.randint(0, 50), random.randint(40, 300), random.randint(30, 300)))
        temp_path = os.getcwd() + '/static/img/temp/cam1_' + str(Staticdata.cam1) + '.jpg';
        img2.save(temp_path)
        #photo['person_photo']='/img/temp/cam1_' + str(Staticdata.cam1) + '.jpg';

        person['camname']="camera 1";
        person['id']=listPerson[random.randint(0,4)];
        person['status']=listStatus[random.randint(0,1)];
        person['photopath']='/img/temp/cam1_' + str(Staticdata.cam1) + '.jpg';

        Staticdata.cam1 += 1;
    elif photo['cam_name']=='cam2':
        photo['path'] = '/img/cam2/' + str(Staticdata.cam2) + '.jpg';
        img = Image.open(os.getcwd() + '/static/img/cam2/' + str(Staticdata.cam2) + '.jpg')
        img2 = img.crop((random.randint(0, 50), random.randint(0, 50), random.randint(40, 300), random.randint(30, 300)))
        temp_path = os.getcwd() + '/static/img/temp/cam2_' + str(Staticdata.cam2) + '.jpg';
        img2.save(temp_path)
        #photo['person_photo'] = '/img/temp/cam2_' + str(Staticdata.cam2) + '.jpg';

        person['camname'] = "camera 2";
        person['id'] = listPerson[random.randint(0, 4)];
        person['status'] = listStatus[random.randint(0, 1)];
        person['photopath'] = '/img/temp/cam2_' + str(Staticdata.cam2) + '.jpg';

        Staticdata.cam2 += 1;
    else:
        photo['path'] = '/img/cam3/' + str(Staticdata.cam3) + '.jpg';
        img = Image.open(os.getcwd() + '/static/img/cam3/' + str(Staticdata.cam3) + '.jpg')
        img2 = img.crop((random.randint(0, 50), random.randint(0, 50), random.randint(40, 300), random.randint(30, 300)))
        temp_path = os.getcwd() + '/static/img/temp/cam3_' + str(Staticdata.cam3) + '.jpg';
        img2.save(temp_path)
        #photo['person_photo'] = '/img/temp/cam3_' + str(Staticdata.cam3) + '.jpg';

        person['camname'] = "camera 3";
        person['id'] = listPerson[random.randint(0, 4)];
        person['status'] = listStatus[random.randint(0, 1)];
        person['photopath'] = '/img/temp/cam3_' + str(Staticdata.cam3) + '.jpg';

        Staticdata.cam3 += 1;

    photo['person']=person;
    #Staticdata.indexvalue += 1;

    return JsonResponse(photo);