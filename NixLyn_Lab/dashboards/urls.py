from django.urls import path
from .views import DashBoardsView, RedRoomView, BlueRoomView, FranknLabView, RvsBView, RedBenchCMD


urlpatterns = [
    path('dashboards/',                     DashBoardsView.as_view(),  name='dashboards'),
    path('dashboards/redroom/',             RedRoomView.as_view(),     name='redroom'),
    path('dashboards/redroom/redbench_cmd', RedBenchCMD.as_view(),     name='redbench_cmd'),
    path('dashboards/blueroom/',            BlueRoomView.as_view(),    name='blueroom'),
    path('dashboards/frankieslab/',         FranknLabView.as_view(),   name='frankieslab'),
    path('dashboards/rvsb_events/',         RvsBView.as_view(),        name='rvsb_events'),
]
