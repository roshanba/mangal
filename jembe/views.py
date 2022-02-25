from datetime import datetime
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.utils.translation import gettext as _
from django.utils import translation
from django.contrib import messages
from project.models import Menu
from jembe.models import Language
from jembe.forms import ReservationForm, ContactForm
from django.views import View



def home(request):
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]
    menusa = Menu.objects.all()
    day=datetime.now()
    day=day.strftime("%A")
    return render(request,
                  "index.html",
                  {'menusa': menusa,
                  'day':day})
   


class NewReservation(CreateView):

    template_name = "reservation.html"
    form_class = ReservationForm

    def form_valid(self, form):
        new = form.save(commit=False)
        new.save()
        # sends a flash message to the user
        messages.success(
            self.request,
            "Thank you for successfully booking a new reservation \n" +
            "You will receive an email shortly about the status of your booking.")
        # redirect the user back to his/her dashboard
        return redirect("/payments")


class Contact(CreateView):

    template_name = "contact.html"
    form_class = ContactForm

    def form_valid(self, form):
        new = form.save(commit=False)
        new.save()
        # send a flash message to the user
        messages.success(
            self.request,
            "Your message was sent successfully")
        # redirect the user back to contact page
        return redirect("/contact")


def payment(request):
    return render(request, "payment.html")

def changeLanguage(request, lang_code):

    language_pref = lang_code
    translation.activate(lang_code)
    request.session[translation.LANGUAGE_SESSION_KEY] = language_pref


    language_preference = Language.objects.all()
    if len(language_preference) > 0:
        language_preference = language_preference[0]
        language_preference.language_pref = lang_code
    else:
        language_preference = Language.objects.create(language_pref=lang_code)
    language_preference.save()

    menusa = Menu.objects.all()
    day=datetime.now()
    day=day.strftime("%A")
    return render(request, "index.html", {'menusa': menusa,
                  'day':day})
