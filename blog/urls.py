from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('tableau/', views.TableauListView, name='tableau'),
    path('peintre/',views.PeintreListView.as_view(), name="peintre"),
    path('tableau/<int:pk>', views.TableauDetailView, name='tableau-detail'),
    path('addcomments/<int:pk>', views.addComments, name='add-comments'),
    path('mon-compte/', views.MonCompte, name='compte'),
    path('connexion/', views.Connexion, name='connexion'),
    path('administration/', views.AdministrationSite, name='administration'),
    path('modifier-tableau/<int:pk>', views.UpdateTableau, name='modifier-tableau'),
    path('ajouter-tableau/', views.CreateTableau, name='ajouter-tableau'),
    path('search-tableau/', views.SearchTableau, name='search'),
    path('addtype/',views.AddType,name='addtype'),
    path('filtre/',views.FiltreTableau, name='filtre'),
    path('contact/', views.Contact, name='contact'),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
