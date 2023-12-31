import datetime
import json
from main.forms import ItemForm
from .models import Item
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.core import serializers
# Tugas 4
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Tugas 6
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)

    context = {
        'my_name': request.user.username,
        'my_class': 'PBP C',
        'items' : items,
        'total_items' : items.count(),
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

@csrf_exempt
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        # Tugas 4
        item = form.save(commit=False)
        item.user = request.user
        item.save()    
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}

    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Tugas 4
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    
    context = {'form':form}

    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, "Sorry, incorrect username or password.\nPlease try again.")
    context = {}

    return render(request, 'login.html', context)

@csrf_exempt
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')

    return response

# Menambahkan satu item
def decrement_item(request, id):
    item = Item.objects.get(id=id)

    if (item.amount > 0):
        item.amount -= 1
        item.save()
        if item.amount <= 0:
           Item.objects.filter(pk=id).delete()

    return HttpResponseRedirect(reverse("main:show_main"))

# Mengurangi satu item
def increment_item(request, id):
    item = Item.objects.get(id=id)

    item.amount += 1
    item.save()
    
    return HttpResponseRedirect(reverse("main:show_main"))

# Menghapus item
def remove_item(request, id):
    Item.objects.filter(pk=id).delete()

    return HttpResponseRedirect(reverse("main:show_main"))

# Edit item
def edit_item(request, id):
    # Get product berdasarkan ID
    item = Item.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)

# Mengembalikan data JSON
def get_item_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        size = request.POST.get("size")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_item = Item(name=name, price=price, size=size, amount=amount, description=description, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def remove_item_ajax(request, id):
    item = Item.objects.get(pk=id)
    item.delete()
    response = HttpResponseRedirect(reverse("main:show_main"))
    return response

def get_total_products(request):
    total_items = Item.objects.filter(user=request.user).count()
    return JsonResponse({'total_items': total_items})

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            price = int(data["price"]),
            size = int(data["size"]),
            amount = int(data["amount"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)