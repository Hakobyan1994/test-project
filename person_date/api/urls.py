from django.urls import path
from .views import PersonDateGetOrPost,PersonDetail

urlpatterns = [
    path('persons/',PersonDateGetOrPost.as_view(),name='persons-list-create'),
    path('person/<int:pk>/',PersonDetail.as_view(),name='person-detail')
]