from django.urls import path, include
from . import views
from .views import SignUpView

app_name = 'polls'
urlpatterns = [
	path('', views.index, name='index'),
	path('logout/', views.logout_view, name='logout'),
	path('signup/', SignUpView.as_view(), name='signup'),
	path('<int:question_id>/', views.detail, name='detail'),
	path('<int:question_id>/results/', views.results, name='results'),
	path('<int:question_id>/vote/', views.vote, name='vote'),
]