from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'New Balance 550 Beige',
        'size': '38',
        'price': 'Rp3.000.000',
        'qty': '3'
    }

    return render(request, "main.html", context)