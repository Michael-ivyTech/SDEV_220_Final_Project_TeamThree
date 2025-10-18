from django.shortcuts import render, redirect, get_object_or_404
from database.models import BakedGood, Customer, OrderInfo, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def home(request):
    employ = check_email(request.user)
    context = {"name": request.user, "employed": employ} 
    return render(request, 'home.html', context)

def menu(request):
    items = BakedGood.objects.all()
    return render(request, 'menu.html', {'items': items})

def order(request):
    """Display order form."""
    items = BakedGood.objects.all()
    return render(request, 'order.html', {'items': items})

def order_submit(request):
    if request.method == "POST":
        customer_name = request.user.username
        customer_email = request.user.email
        # Create customer
        customer = Customer.objects.create(
            user=customer_name,
            email=customer_email
        )

        # Create order record
        order_info = OrderInfo.objects.create(customer=customer)

        # Loop through all baked goods
        for item in BakedGood.objects.all():
            qty_str = request.POST.get(f"quantity_{item.id}")
            if qty_str and int(qty_str) > 0:
                quantity = int(qty_str)
                # Create OrderItem instead of adding BakedGood directly
                OrderItem.objects.create(
                    orderinfo=order_info,
                    bakedgood=item,
                    quantity=quantity
                )

        return redirect('confirmation', order_id=order_info.id)

    return redirect('orders')


def confirmation(request, order_id):
    order = OrderInfo.objects.get(id=order_id)
    order_items = order.orderitem_set.all()

    # Calculate total cost
    total_cost = sum(item.bakedgood.item_cost * item.quantity for item in order_items)

    return render(request, 'confirmation.html', {
        'order': order,
        'total_cost': total_cost
    })


def employee(request):
    # Get all orders, most recent first
    orders = OrderInfo.objects.all().order_by('-created_at')
    
    return render(request, 'employee.html', {
        'orders': orders
    })

def complete_order(request, order_id):
    order = get_object_or_404(OrderInfo, id=order_id)
    order.completed = True  # remove the order
    return redirect('employee')  # redirect back to the employee panel

def check_email(usery):
    user = User.objects.get(id=usery.id)
    heyer_domain = "heyerlysbake.com"

    if user.email.endswith(heyer_domain):
        employeey = True
    else:
        employeey = False

    return employeey
