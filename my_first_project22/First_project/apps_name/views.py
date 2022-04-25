from django.shortcuts import render
from django.http import HttpResponse
from apps_name.models import Musician, Album
from apps_name import forms

# Create your views here.

# def homepage(request):
#     return HttpResponse("<h1>This is my first Practices page!!<h1> <a href='/Contract/'>Contract</a> <a href='/About/'>About</a>")
#
# def Contract(request):
#     return HttpResponse("<h3>This is Contract Page!!</h3> <a href='/'>homepage</a> <a href='/About/'>About</a>")
#
# def About(request):
#     return HttpResponse("<h2>About Page From Home Page</h2>")


# def home(request):
#     diction = {
#             'text_1':'I am a text sent form views.py' ,
#             'text_2':'I am Learning django'
#        }
#     return render(request, 'apps_name/index.html', context=diction)

def home(request):
    #select * from Musician oreder_by first_name
    musician_list = Musician.objects.order_by('first_name')
    diction = {'text_1': "This is a list of Musician !", 'musician': musician_list}
    return render(request, 'apps_name/index.html',context=diction)


def About(request):
    return render(request, 'apps_name/About.html')

# def form(request):
#     diction={'heading':"This is  Form Page Create By Html "}
#     return render(request, 'apps_name/forms.html', context=diction)


def form(request):
    Form = forms.user_name()
    diction = {'heading':"This is  Form Page Create By Django Forms ", 'new_form':Form}

    if request.method == 'POST':
        new_form = forms.user_name(request.POST)

        if new_form.is_valid():
            first_name = new_form.cleaned_data['first_name']
            last_name = new_form.cleaned_data['last_name']
            dob       = new_form.cleaned_data['dob']
            Email = new_form.cleaned_data['Email']

            diction.update({'first_name':first_name})
            diction.update({'last_name':last_name})
            diction.update({'dob':dob})
            diction.update({'Email':Email})
            diction.update({'form_submited':"Yes"})

    return render(request, 'apps_name/forms.html', context=diction)
