# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import urllib
import urllib2
import json


from django.shortcuts import render, redirect
from .models import Post, profilePic
from .forms import contactForm
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
    form = contactForm()
    pagename = "Above the Noise Communications"
    context = {"pagename": pagename, "form": form}
    template = "home.html"
    return render(request, template, context)

def about(request):
    pic = profilePic.objects.all().first()
    pagename = "About"
    context = {"pagename": pagename,
            "profilePic": pic,
    }
    template = "about.html"
    return render(request, template, context)

def services(request):
    pagename = "Services"
    context = {"pagename": pagename}
    template = "service.html"
    return render(request, template, context)

def contact(request):
    form = contactForm()
    pagename = "Consultations"
    context = {"pagename": pagename, "form":form}
    template = "contact.html"
    return render(request, template, context)


def blog(request):
    the_posts = Post.objects.order_by('-date')
    pagename = "News Feed"
    context = {"pagename": pagename, "the_posts": the_posts}
    template = "blog.html"
    return render(request, template, context)

def process(request):
    title="Contact"
    form = contactForm(request.POST or None)
    confirm_message = None

    if form .is_valid():

    # Beginngin of catcha validation
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        result = json.load(response)

        if result['success']:

        #captcha end


            flash = None
            name=form.cleaned_data['name']
            comment=form.cleaned_data['comment']
            subject='Message from atnpr.com'
            message='%s %s' %(comment, name)
            emailFrom=form.cleaned_data['email']
            emailTo=[settings.EMAIL_HOST_USER]
            send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
            title = "Thanks!"
            confirm_message = "Thanks for the message, we will get right back to you"
            form = None
        else:
            return redirect("/nope")

    context = {'title': title, 'form': form, 'confirm_message': confirm_message, 'flash': flash}
    return redirect("/thanks")


def thanks(request):
    form = contactForm()
    pagename = "Thanks"
    context = {"pagename": pagename}
    template = "thanks.html"
    return render(request, template, context)

def nope(request):
    form = contactForm()
    pagename = "We're Sorry"
    context = {"pagename": pagename}
    template = "nope.html"
    return render(request, template, context)
