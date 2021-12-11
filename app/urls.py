from django.urls import path, include
from app.views import CommentView, hello
from rest_framework.urlpatterns import format_suffix_patterns


comment_list = CommentView.as_view({
    'post': 'create',
    'get': 'list'
})

comment_detail = CommentView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('comments/', comment_list, name='comment_list'),
    path('comments/<int:pk>', comment_detail, name='comment_detail')
])