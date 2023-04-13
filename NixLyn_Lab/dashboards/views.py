from django.shortcuts import render
from django.views.generic import TemplateView
from .models import PostDash
from .forms import PostDash
from django.urls import reverse_lazy

# Create your views here.


class DashBoardsView(TemplateView):
    model           = PostDash
    template_name   = 'dashboards.html'


class RedRoomView(TemplateView):
    model           = PostDash
    template_name   = 'redroom.html'

class BlueRoomView(TemplateView):
    model           = PostDash
    template_name   = 'blueroom.html'

class FranknLabView(TemplateView):
    model           = PostDash
    template_name   = 'frankieslab.html'

class RvsBView(TemplateView):
    model           = PostDash
    template_name   = 'rvsb_events.html'


class RedBenchCMD(TemplateView):
    model           = PostDash
    template_name   = 'redbench_cmd.html'
