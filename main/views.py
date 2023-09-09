from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'my_name': 'Cheeryl Aisyah Retnowibowo',
        'my_npm' : '2206813706',
        'my_class': 'PBP C',
    }

    return render(request, "main.html", context)