from django.urls import path

from petstagram.common.views import landing_page

urlpatterns = [
    path("", landing_page),
    # using dynamics path with name="..."
    # path("", landing_page, name="login")
]