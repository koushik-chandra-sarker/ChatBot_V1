from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

from .Bot_Corpus import Bot as BotCorpus
from .Bot_Waysis import Bot as BotWaysis
from .models import CustomBotDataset


def Index(request):
    return render(request, template_name='index.html')


def Bot_Corpus(request):
    return render(request, template_name='chatwithcorpus.html')


def Bot_Waysis(request):
    return render(request, template_name='chatwithwaysis.html')


def Bot_Admin(request):
    ReviewInstances = CustomBotDataset.objects.filter(Q(active=False))
    Instances = CustomBotDataset.objects.all()
    return render(request, template_name='admin.html',
                  context={"ReviewInstances": ReviewInstances, "Instances": Instances})


def sendToBotCorpus(request):
    sender_message = request.POST.get('message')

    response = BotCorpus.getResponse(sender_message)

    return JsonResponse({"reply": str(response)})


dataset = CustomBotDataset.objects.filter(Q(active=True) & Q(answer__isnull=False) & Q(question__isnull=False))
BotWaysis.trainModel(dataset)


def sendToBotWaysis(request):
    sender_message = request.POST.get('message')

    response = BotWaysis.getResponse(sender_message)
    if str(response) == '%Bot_Waysis_False%':
        CustomBotDataset.objects.create(question=sender_message, active=False)
        response = "I am sorry, For this query you can contact my admin.Email: koushiksk.ks@gmail.com, " \
                   "Call: 01622774190 "

    return JsonResponse({"reply": str(response)})


def saveCustomBotDataset(request):
    if request.method == "POST":
        id = request.POST.get("id")
        question = request.POST.get("question")
        answer = request.POST.get("answer")
        active = request.POST.get("active")
        print(id, " : ", question, ": ", answer, ": ", active)
        if id == "":
            customBotDataset = CustomBotDataset(question=question, answer=answer, active=active)
        else:
            customBotDataset = CustomBotDataset(id=id, question=question, answer=answer, active=active)
        customBotDataset.save()
        return JsonResponse({"status": "true"})

    return JsonResponse({"status": "false"})


def tain_waysis_bot(request):
    dataset = CustomBotDataset.objects.filter(Q(active=True) & Q(answer__isnull=False) & Q(question__isnull=False))
    BotWaysis.trainModel(dataset)
    return JsonResponse({"status": "true"})