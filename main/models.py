from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
class Profile(models.Model):
    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profile"
    STATUS_CHOICES = [
        ('student', 'Student'),
        ('absolwent', 'Absolwent'),
        ('prowadzacy', 'Prowadzący'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    index_number = models.CharField(max_length=20, blank=True, null=True)
    field_of_study = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='student')
    is_public = models.BooleanField(default=True)
    document = models.FileField(upload_to='documents/', null=True, blank=True)
    last_login_display = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username



class Wydarzenie(models.Model):
    class Meta:
        verbose_name = "Wydarzenie"
        verbose_name_plural = "Wydarzenia"
    tytul = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField()
    kolor = models.CharField(max_length=7, default='#3788d8')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)





class NotatkaKalendarzowa(models.Model):
    class Meta:
        verbose_name = "Notatka"
        verbose_name_plural = "Notatki"

    tresc_prywatna = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tytul = models.CharField(max_length=200)
    data = models.DateField()
    opis = models.TextField(blank=True, null=True)
    kolor = models.CharField(max_length=20, default='#3788d8')

    def __str__(self):
        return f"{self.tytul} - {self.user.username}"

class Ocena(models.Model):
    class Meta:
        verbose_name = "Ocena"
        verbose_name_plural = "Oceny"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    przedmiot = models.CharField(max_length=100)
    wartosc = models.DecimalField(max_digits=3, decimal_places=1)
    komentarz = models.TextField(blank=True, null=True)
    data = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.przedmiot}: {self.wartosc}"


class Ocena(models.Model):
    class Meta:
        verbose_name = "Ocena"
        verbose_name_plural = "Oceny"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    przedmiot = models.CharField(max_length=100)
    wartosc = models.DecimalField(max_digits=3, decimal_places=1)
    komentarz = models.TextField(blank=True, null=True)
    data = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.przedmiot}: {self.wartosc}"


class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    notif_type = models.CharField(max_length=10, default='sms')

    def __str__(self):
        return f"{self.user.email} – [{self.notif_type}] {self.message[:20]}"


class AdminMessage(models.Model):
    class Meta:
        verbose_name = "Wiadomość administratora"
        verbose_name_plural = "Wiadomości administratora"
    title = models.CharField(max_length=200)
    content = models.TextField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
