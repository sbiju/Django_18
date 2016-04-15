from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from .models import SignUp, Post
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import SignUpForm, ContactForm, PostForm
from django.contrib import messages


def home(request):
    title = "Sign Up Now"
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        "template_title": title,
        "form": form,
    }
    if request.user.is_authenticated() and request.user.is_staff:
        queryset = SignUp.objects.all().order_by('-timestamp')
        context = {
            "queryset": queryset,
        }
    return render(request, "home.html", context)


def contact(request):
    title = 'Contact Us'
    form = ContactForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        full_name = form.cleaned_data.get('full_name')
        subject = 'Site Contact Form'
        from_email = settings.EMAIL_HOST_USER
        to_email = from_email
        contact_message = "%s:%s via %s" %(full_name, message, email)
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False)

    context = {
        "form": form,
        "title": title
    }
    return render(request, "contact.html", context)


def post_list(request):
    queryset_list = Post.objects.all()
    context = {
        "object_list": queryset_list,
    }
    return render(request, "post_list.html", context)


def post_detail(request, id):
    instance = get_object_or_404(Post, id=id)

    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post_detail.html", context)


def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid:
        instance = form.save(commit=False)
        instance.save()

    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)


def post_update(request, id):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None,request.FILES or None, instance=instance)
    if form.is_valid:
        instance = form.save(commit=False)
        instance.save()
        return redirect("post_list")
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "post_update.html", context)


def about(request):
    return render(request, "about.html", {})


def pappaya(request):
    return render(request, "pappaya.html", {})


def sugarcane(request):
    return render(request, "sugarcane.html", {})


def lakshmi(request):
    return render(request, "lakshmi.html", {})
