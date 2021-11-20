from django.shortcuts import render
from .models import Video, Dreds_img, Afro_img, Braids_img, Services, AboutMe
from orders.models import Order
from orders.forms import OrderForm
from orders.sendmessage import send_telegram


def webpage(request):
    video = Video.objects.all()
    dreds_img = Dreds_img.objects.all()
    afro_img = Afro_img.objects.all()
    braids_img = Braids_img.objects.all()
    services_dreds = Services.objects.get(pk=1)
    services_afro = Services.objects.get(pk=2)
    services_braids = Services.objects.get(pk=3)
    services_learn = Services.objects.get(pk=4)
    about_me = AboutMe.objects.all()
    form = OrderForm()

    context = {
        'video': video,
        'dreds_img': dreds_img,
        'afro_img': afro_img,
        'braids_img': braids_img,
        'services_dreds': services_dreds,
        'services_afro': services_afro,
        'services_braids': services_braids,
        'services_learn': services_learn,
        'about_me': about_me,
        'form': form
    }

    return render(request, 'index.html', context)


def get_order(request):
    name = request.POST['name']
    phone = request.POST['phone']
    order = Order(name=name, phone=phone)
    order.save()
    send_telegram(tg_name=name, tg_phone=phone)
    return render(request, 'order.html', {'name': name})