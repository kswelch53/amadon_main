from django.shortcuts import render, HttpResponse, redirect
from decimal import Decimal
from apps.app_one.models import Product

secret_key = "checkitout"

# def index(request):
    # print("This is index in views.py")
    # if 'chargeamount' not in request.session:
        # request.session['chargeamount'] = 0
        # request.session['counter'] = 0
        # print("Chargeamount is", request.session['chargeamount'])
    # return render(request, 'app_one/index.html')

def index3(request):
    print("This is index3 in views.py")
    counter = 0
    if 'chargeamount' not in request.session:
        request.session['chargeamount'] = 0
        request.session['counter'] = 0
        print("Chargeamount is", request.session['chargeamount'])
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'app_one/index3.html', context)


def clear(request):
    print("This is clear function in views.py");
    request.session['chargeamount'] = 0
    request.session['counter'] = 0
    return redirect('/')


def process_order(request):
    print("This is process_order in views.py")
    print("Option is:", request.POST['quantity'])

    # request.session['tshirtprice'] = 19.99
    # request.session['sweaterprice'] = 29.99
    # request.session['cupprice'] = 4.99
    # request.session['bookprice'] = 49.99

    if request.method == "POST":
        print("Item is:", request.POST['item'])

    # item is the id number of the Product object
    # there are 4 products: tshirt, sweater, cup and book
    if request.POST["item"] == "1":
        quantity = int(request.POST['quantity'])
        price = 19.99 * quantity
        price = round(price, 2)
        # price = Decimal(price)
        request.session['counter'] = request.session['counter'] + quantity
        counter = request.session['counter']
        print("T-shirt price is: $", price, "Counter is:", counter)

        request.session['price'] = price

        request.session['chargeamount'] = round(request.session['chargeamount'] + price, 2)
        print("Your charge is: $", request.session['chargeamount'])
        return redirect('app1:checkout')

    if request.POST["item"] == "2":
        quantity = int(request.POST['quantity'])
        price = 29.99 * quantity
        price = round(price, 2)
        request.session['counter'] = request.session['counter'] + quantity
        counter = request.session['counter']
        print("Sweater price is: $", price, "Counter is:", counter)
        request.session['price'] = price
        request.session['chargeamount'] = round(request.session['chargeamount'] + price, 2)
        print("Your charge is: $", request.session['chargeamount'])
        return redirect('app1:checkout')

    if request.POST["item"] == "3":
        quantity = int(request.POST['quantity'])
        price = 4.99 * quantity
        price = round(price, 2)
        request.session['counter'] = request.session['counter'] + quantity
        counter = request.session['counter']
        print("Cup price is: $", price, "Counter is:", counter)
        request.session['price'] = price
        request.session['chargeamount'] = round(request.session['chargeamount'] + price, 2)
        print("Your charge is: $", request.session['chargeamount'])
        return redirect('app1:checkout')

    if request.POST["item"] == "4":
        quantity = int(request.POST['quantity'])
        price = 49.99 * quantity
        price = round(price, 2)
        request.session['counter'] = request.session['counter'] + quantity
        counter = request.session['counter']
        print("Book price is: $", price, "Counter is:", counter)
        request.session['price'] = price
        request.session['chargeamount'] = round(request.session['chargeamount'] + price, 2)
        print("Your charge is: $", request.session['chargeamount'])
        return redirect('app1:checkout')

    return redirect('/')


def checkout(request):
    print("This is checkout function in views.py")

    # context = {

    # }

    return render(request, 'app_one/checkout.html')
