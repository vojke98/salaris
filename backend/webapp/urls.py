from . import views
from django.urls import path



# ovi paths pripadaju URL-u localhost:8000/webapp/

urlpatterns = [
    # ex: /webapp/
    path('', views.foobar, name='foobar'),

    # ex: /webapp/1
    path('<int:id>/', views.getUser, name='getUser')
    


    ##### ovo dole su primjeri iz jednog tutorijala
    
    # ex: /polls/
    #path('', views.index, name='index'),
    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
    # ex: /polls/5/specs
    #path('<int:question_id>/specs/', views.specs, name='specs'),
    # ex: polls/testiranje/10
    #path('testiranje/<str:message>/', views.testiranje, name='testiranje'),
    # ex
    #path('<int:question_id>/vote/', views.vote, name='vote')
    
]
