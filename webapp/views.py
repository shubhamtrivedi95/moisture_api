from django.http import HttpResponse
from django.forms import ModelForm
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from . serializers import sensorsSerializer
from . models import Machines
from django.shortcuts import get_object_or_404,render
from django.views.generic.detail import DetailView

from . forms import GetData


def post_create(request):
    form = GetData(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        Machines.objects.filter(TokenNo=request.POST.get("TokenNo")).update(Enable=1)
    context={
        "form":form ,
    }
    return render(request,'page.html',context)

class StackView(DetailView):

    model = Machines
    queryset = Machines.objects.all()
    template_name = "receive.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class StackList(generics.ListCreateAPIView):

    queryset = Machines.objects.all()
    serializer_class = sensorsSerializer


class uniqueStackList(generics.ListCreateAPIView):


    queryset = Machines.objects.filter(Enable=1)
    serializer_class = sensorsSerializer
    lookup_url_kwarg = "MC_No"

    def get_queryset(self):
        return self.queryset.filter(StackNo=self.kwargs.get(self.lookup_url_kwarg))

class uniqueStackViewList(generics.ListCreateAPIView):



    queryset = Machines.objects.all()
    serializer_class = sensorsSerializer
    lookup_url_kwarg = "MC_No"

    def get_queryset(self):
        return self.queryset.filter(StackNo=self.kwargs.get(self.lookup_url_kwarg))




class MultiOperation(generics.UpdateAPIView):

    queryset = Machines.objects.all()
    serializer_class = sensorsSerializer
    lookup_url_kwarg = "MC_No"
    def get_queryset(self):
        rm_No = self.kwargs.get(self.lookup_url_kwarg)
        return self.queryset.filter(StackNo=rm_No)

    def perform_update(self, serializer):
        sensor=get_object_or_404(
            Machines,
            StackNo=self.kwargs.get(self.lookup_url_kwarg),
            TokenNo=self.request.data["TokenNo"],
        )
        serializer.save(sensor=sensor)

    def get_object(self):
        # print(self.request.data['TokenNo'])
        # print(type(self.request.data))
        return get_object_or_404(
            self.get_queryset(),
            StackNo=self.kwargs.get(self.lookup_url_kwarg),
            TokenNo=self.request.data["TokenNo"],
        )




def welcome(request):
    return HttpResponse("<h2> Moisture Meter API.<h2>")