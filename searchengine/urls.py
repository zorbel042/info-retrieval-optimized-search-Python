from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/<str:pk>/', views.search, name='search'),
    path('Jan/aol.html', views.check, name='aol'),
    path('Jan/armed.html', views.check, name='armed'),
    path('Jan/baptist.html', views.check, name='baptist'),
    path('Jan/bill.html', views.check, name='bill'),
    path('Jan/birdnbee.html', views.check, name='birdnbee'),
    path('Jan/bunker.html', views.check, name='bunker'),
    path('Jan/cache.html', views.check, name='cache'),
    path('Jan/child.html', views.check, name='child'),
    path('Jan/creditcard.html', views.check, name='creditcard'),
    path('Jan/debug.html', views.check, name='debug'),
    path('Jan/edwardii.html', views.check, name='edwardii'),
    path('Jan/explain.html', views.check, name='explain'),
    path('Jan/fab.html', views.check, name='fab'),
    path('Jan/galant.html', views.check, name='galant'),
    path('Jan/gravies.html', views.check, name='gravies'),
    path('Jan/harley.html', views.check, name='harley'),
    path('Jan/heartprob.html', views.check, name='heartprob'),
    path('Jan/hippos.html', views.check, name='hippos'),
    path('Jan/jesus.html', views.check, name='jesus'),
    path('Jan/kitty.html', views.check, name='kitty'),
    path('Jan/marriedplay.html', views.check, name='marriedplay'),
    path('Jan/phone.html', views.check, name='phone'),
    path('Jan/problem.html', views.check, name='problem'),
    path('Jan/qc.html', views.check, name='qc'),
    path('Jan/quickies.html', views.check, name='quickies'),
    path('Jan/snow.html', views.check, name='snow'),
    path('Jan/superbowl.html', views.check, name='superbowl'),
    path('Jan/topten.html', views.check, name='topten'),
    path('Jan/y2k.html', views.check, name='y2k'),
    path('Jan/y2kfollow.html', views.check, name='y2kfollow'),
    path('Jan/y2kms.html', views.check, name='y2kms'),
]