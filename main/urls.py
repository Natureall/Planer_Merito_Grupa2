from .views import ajax_kontakt_view, ajax_notifications_view
from django.urls import path
from .views import ajax_oceny, ajax_profil_view, logout_confirm_view, profil_view, panel_studenta, login_view, register_view, logout_view
from . import views
from .views import ajax_oceny, ajax_notatki, ajax_dodaj_notatke, ajax_edytuj_notatke, ajax_usun_notatke
from .views import ajax_oceny, ajax_kalendarz_html


urlpatterns = [
    path('ajax/notatki/', ajax_notatki, name='ajax_notatki'),
    path('ajax/notatka/dodaj/', ajax_dodaj_notatke, name='ajax_dodaj_notatke'),
    path('ajax/kontakt/', ajax_kontakt_view, name='ajax_kontakt'),
    path('ajax/notifications/', ajax_notifications_view, name='ajax_notifications'),
    path('ajax/oceny/', ajax_oceny, name='ajax_oceny'),
    path('ajax/edytuj_notatke/<int:notatka_id>/', ajax_edytuj_notatke, name='ajax_edytuj_notatke'),
    path('ajax/usun_notatke/<int:notatka_id>/', ajax_usun_notatke, name='ajax_usun_notatke'),
    path('ajax/notatki/', ajax_notatki, name='ajax_notatki'),
    path('ajax/notatka/dodaj/', ajax_dodaj_notatke, name='ajax_dodaj_notatke'),
    path('ajax/kalendarz/html/', ajax_kalendarz_html, name='ajax_kalendarz_html'),
    path('ajax/profil/', ajax_profil_view, name='ajax_profil'),
    path('logout/confirm/', logout_confirm_view, name='logout_confirm'),
    path('profil/', profil_view, name='profil'),
    path('', panel_studenta, name='panel_studenta'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('kalendarz/', views.kalendarz_view, name='kalendarz'),
    path('ajax/wydarzenia/', views.ajax_wydarzenia, name='ajax_wydarzenia'),
    path('ajax/dodaj/', views.ajax_dodaj_wydarzenie, name='ajax_dodaj_wydarzenie'),
    path('ajax/kalendarz/', views.ajax_kalendarz, name='ajax_kalendarz'),

    

]