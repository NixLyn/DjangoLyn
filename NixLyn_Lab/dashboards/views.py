from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from .models import PostDash, MyTarget
from .forms import PostDash, EditTarget
from django.urls import reverse_lazy

# Create your views here.


class DashBoardsView(TemplateView):
    model           = MyTarget, PostDash
    template_name   = 'dashboards.html'

class SetTargetView(UpdateView):
    model           = MyTarget, PostDash
    form_class      = EditTarget
    template_name   = 'set_target.html'
    success_url     = reverse_lazy('dashboards')

    def get_object(self):
        return self.request.user

class RedRoomView(TemplateView):
    model           = PostDash, MyTarget
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
    model           = PostDash, PostDash
    template_name   = 'redbench_cmd.html'
