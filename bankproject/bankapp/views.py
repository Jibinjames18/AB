from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import District, Branch, Account, Material


def home(request):
    districts = District.objects.all()
    return render(request, 'home.html', {'districts': districts})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('new_page')
        else:
            pass
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('login')
        else:
            pass
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('home')


def new_page(request):
    districts = District.objects.all()
    branches = Branch.objects.all()
    materials = Material.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        mail_id = request.POST.get('mail_id')
        address = request.POST.get('address')
        district_id = request.POST.get('district')
        branch_id = request.POST.get('branch')
        account_type = request.POST.get('account_type')
        materials_provide_selected = request.POST.getlist('materials_provide')
        materials_provide_objects = Material.objects.filter(id__in=materials_provide_selected)

        account = Account.objects.create(name=name, dob=dob, age=age, gender=gender, phone_number=phone_number,
                                         mail_id=mail_id,
                                         address=address, district_id=district_id, branch_id=branch_id,
                                         account_type=account_type)

        account.save()

        account.materials_provide.set(materials_provide_objects)

        return redirect('application_accepted')
    else:
        return render(request, 'new_page.html', {'districts': districts, 'branches': branches,'materials':materials})


def application_accepted(request):
    return render(request, 'application_accepted.html')


def district_wiki(request, district_id):
    try:
        district = District.objects.get(pk=district_id)
        wiki_url = f'https://en.wikipedia.org/wiki/{district.name}'
        return HttpResponseRedirect(wiki_url)
    except District.DoesNotExist:
        return redirect('home')
