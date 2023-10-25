from django.shortcuts import render
from main.models import InformationBox


def index(request):
    information_boxs = InformationBox.get_all_products()
    data = {'InformationBox': information_boxs}
    return render(request, 'main/index.html', data)
