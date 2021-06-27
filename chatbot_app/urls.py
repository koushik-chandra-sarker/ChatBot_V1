
from django.urls import path
from . import views
urlpatterns = [
    path("", views.Index),
    path("admin/", views.Bot_Admin),
    path("admin/saveCustomBotDataset/", views.saveCustomBotDataset),
    path("corpus/", views.Bot_Corpus),
    path("waysis/", views.Bot_Waysis),
    path("corpus/send-to-botcorpus/", views.sendToBotCorpus),
    path("waysis/send-to-bot-waysis/", views.sendToBotWaysis),

]
