from django.urls import path
from .views import DashBoardsView, RedRoomView, BlueRoomView, FranknLabView, RvsBView, RedBenchCMD, SetTargetView


urlpatterns = [
    path('',                     DashBoardsView.as_view(),   name='dashboards'),
    path('set_target/',          SetTargetView.as_view(),    name='set_target'),
    path('redroom/',             RedRoomView.as_view(),      name='redroom'),
    path('redroom/redbench_cmd', RedBenchCMD.as_view(),      name='redbench_cmd'),
    path('blueroom/',            BlueRoomView.as_view(),     name='blueroom'),
    path('frankieslab/',         FranknLabView.as_view(),    name='frankieslab'),
    path('rvsb_events/',         RvsBView.as_view(),         name='rvsb_events'),
]
