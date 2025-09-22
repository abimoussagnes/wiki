from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.get_content, name="content"),
    path("search/", views.search, name="search"),
    path("new/", views.new , name="new"),
    path("result/", views.create_entry, name="create_entry"),
    path("random/", views.random_page, name="random"),
    path("wiki/<str:name>/edit/", views.edit_page, name="edit"),
    path("wiki/<str:name>/new/", views.edited_page, name="edited_page")
]
