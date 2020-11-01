from django.shortcuts import render

# Vistas.
def home(request):
    context = {
        'title':'Óptica Marfull'
    }
    return render(request, 'cuenta\home.html', context)
