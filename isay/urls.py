from django.urls import path, include
from .views import HomeTemplateView, Home2TemplateView, TeamTemplateView, ServicesTemplateView, NewsTemplateView, AppointmentTemplateView, ManageAppointmentTemplateView, LoginTemplateView, SignupTemplateView, profile, ModifyProfileTemplateView

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("index/", Home2TemplateView.as_view(), name = "home2"),
    path("team/", TeamTemplateView.as_view(), name = "team"),
    path("services/", ServicesTemplateView.as_view(), name = "services"),
    path("news/", NewsTemplateView.as_view(), name = "news"),
    path("make-an-appointment/", AppointmentTemplateView.as_view(), name="appointment"),
    path("manage-appointments/", ManageAppointmentTemplateView.as_view(), name="manage"),
    path('signup/', SignupTemplateView.as_view(), name='signup'),
    path('profile/',profile, name ="profile"),
    path('modify_profile/',ModifyProfileTemplateView.as_view(), name ="modify_profile"),
]
