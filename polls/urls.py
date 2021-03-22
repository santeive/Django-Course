from django.urls import path
from . import views

# Agregamos app_name para diferenciar las vistas entre apps, 
# es decir si hay una vista con el mismo nombre en diferentes apps
app_name = 'polls'

urlpatterns = [
     # ex: /polls/
    path('', views.index, name="index"),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]