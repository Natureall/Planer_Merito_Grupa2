from django.core.mail import send_mail
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .forms import KontaktForm
from .models import AdminMessage, Notification

User = get_user_model()

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import AdminMessage, Profile
from django.http import JsonResponse
from .models import AdminMessage, Wydarzenie
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date
from .models import AdminMessage, NotatkaKalendarzowa
from django.shortcuts import render
from .models import AdminMessage, Ocena

@login_required
def panel_studenta(request):
    admin_messages = AdminMessage.objects.filter(active=True).order_by('-created_at')
    return render(request, 'panel.html', {
        'admin_messages': admin_messages,
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            from .models import AdminMessage, Profile
            Profile.objects.get_or_create(user=user) 
            login(request, user)
            return redirect('panel_studenta')
        else:
            return render(request, 'login.html', {'error': 'Nieprawidłowy e-mail lub hasło'})
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not email or not password or not confirm_password:
            return render(request, 'register.html', {'error': 'Wszystkie pola są wymagane'})

        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Hasła nie są zgodne'})

        if User.objects.filter(username=email).exists():
            return render(request, 'register.html', {'error': 'Użytkownik z tym adresem e-mail już istnieje'})

        user = User.objects.create_user(username=email, email=email, password=password)
        login(request, user)
        return redirect('panel_studenta')

    return render(request, 'register.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'logout.html')



@login_required

def profil_view(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 or password2:
            if password1 == password2:
                user.set_password(password1)
                message = "Hasło zostało zmienione"
            else:
                error = "Hasła się nie zgadzają"
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']
            profile.save()
        if not error:
            user.save()
            message = "Dane zostały zapisane"
    return render(request, 'profil.html', {'user': user, 'message': message, 'error': error, 'profile': profile})

def logout_confirm_view(request):
    return render(request, 'logout_confirm.html')


def ajax_profil_view(request):
    return render(request, 'profil_content.html')

@login_required
def kalendarz_view(request):
    return render(request, 'kalendarz.html')

@login_required
def ajax_wydarzenia(request):
    events = Wydarzenie.objects.filter(autor=request.user)
    data = [{
        "id": event.id,
        "title": event.tytul,
        "start": event.start.isoformat(),
        "end": event.end.isoformat(),
        "color": event.kolor,
    } for event in events]
    return JsonResponse(data, safe=False)

@login_required
def ajax_dodaj_wydarzenie(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Wydarzenie.objects.create(
            tytul=data['title'],
            start=data['start'],
            end=data['end'],
            kolor=data.get('color', '#3788d8'),
            autor=request.user
        )
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)
 
@login_required
def kalendarz_view(request):
    return render(request, 'kalendarz.html')

@login_required
def ajax_kalendarz(request):
    events = Wydarzenie.objects.all()
    data = [{
        'id': e.id,
        'title': e.tytul,
        'start': e.start.isoformat(),
        'end': e.end.isoformat(),
        'color': e.kolor
    } for e in events]
    return JsonResponse(data, safe=False)




@login_required
def ajax_kalendarz_html(request):
    return render(request, 'ajax_kalendarz.html')





@login_required
def ajax_notatki(request):
    notatki = NotatkaKalendarzowa.objects.filter(user=request.user)
    data = [{
        'id': n.id,
        'title': n.tytul,
        'start': n.data.isoformat(),
        'color': n.kolor,
        'opis': n.opis,
        'tresc_prywatna': n.tresc_prywatna
    } for n in notatki]
    return JsonResponse(data, safe=False)

@csrf_exempt
@login_required
def ajax_dodaj_notatke(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        tytul = body.get('tytul')
        data = parse_date(body.get('data'))
        kolor = body.get('kolor', '#3788d8')
        opis = body.get('opis', '')
        tresc_prywatna = body.get('tresc_prywatna', '')

        notatka = NotatkaKalendarzowa.objects.create(
            tresc_prywatna=tresc_prywatna,
            user=request.user,
            tytul=tytul,
            data=data,
            kolor=kolor,
            opis=opis
        )
        return JsonResponse({'status': 'ok', 'id': notatka.id})
    return JsonResponse({'status': 'error'}, status=400)



@csrf_exempt
@login_required
def ajax_edytuj_notatke(request, notatka_id):
    try:
        notatka = NotatkaKalendarzowa.objects.get(id=notatka_id, user=request.user)
    except NotatkaKalendarzowa.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Notatka nie istnieje'}, status=404)

    if request.method == 'POST':
        body = json.loads(request.body)
        notatka.tytul = body.get('tytul', notatka.tytul)
        notatka.data = parse_date(body.get('data')) or notatka.data
        notatka.opis = body.get('opis', notatka.opis)
        notatka.kolor = body.get('kolor', notatka.kolor)
        notatka.tresc_prywatna = body.get('tresc_prywatna', notatka.tresc_prywatna)
        notatka.save()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)

@csrf_exempt
@login_required
def ajax_usun_notatke(request, notatka_id):
    try:
        notatka = NotatkaKalendarzowa.objects.get(id=notatka_id, user=request.user)
        notatka.delete()
        return JsonResponse({'status': 'ok'})
    except NotatkaKalendarzowa.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Notatka nie istnieje'}, status=404)



@login_required
def ajax_oceny(request):
    oceny = Ocena.objects.filter(user=request.user).order_by('-data')
    return render(request, 'ajax_oceny.html', {'oceny': oceny})



@login_required
def ajax_oceny(request):
    oceny = Ocena.objects.filter(user=request.user).order_by('-data')
    return render(request, 'ajax_oceny.html', {'oceny': oceny})

def ajax_kontakt_view(request):
    if request.method == 'POST':
        form = KontaktForm(request.POST)
        if form.is_valid():
            d = form.cleaned_data
            send_mail(f"Wiadomość: {d['temat']}", d['wiadomosc'], None, [d['email']])
            try:
                wyk = User.objects.get(email=d['email'])
                Notification.objects.create(user=wyk, message=f"Nowa wiadomość od {d['imie']}: {d['temat']}", notif_type='sms')
            except User.DoesNotExist:
                pass
            return JsonResponse({'success': True})
        return JsonResponse({'errors': form.errors}, status=400)
    return render(request, 'ajax_kontakt.html', {'form': KontaktForm()})
@login_required

def ajax_notifications_view(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'main/notifications.html', {'notifications': notifications})
