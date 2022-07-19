from django.urls import path
from . import views 
from .views import ActiveLinkView, RecentLinkView
app_name="link"

urlpatterns = [
    path("create/", views.PostCreateApi.as_view(), name="api_create"),
    path("update/<int:pk>", views.PostUpdateApi.as_view(), name="api_update"),
    path("delete/<int:pk>", views.PostDeleteApi.as_view(), name="api_delete"),
    path("active/", ActiveLinkView.as_view(), name="active_link"),
    path("recent/", RecentLinkView.as_view(), name="recent_link"),
    path("", views.PostListApi.as_view(), name="api_list"),
]