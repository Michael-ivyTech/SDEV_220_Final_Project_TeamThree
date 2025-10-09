from django.shortcuts import render, redirect, get_object_or_404
from database.models import BakedGood, Customer, OrderInfo, OrderItem

def home(request):
    return render(request, 'home.html')

def menu(request):
    items = BakedGood.objects.all()
    return render(request, 'menu.html', {'items': items})

def order(request):
    """Display order form."""
    items = BakedGood.objects.all()
    return render(request, 'order.html', {'items': items})

def order_submit(request):
    if request.method == "POST":
        customer_name = request.POST.get("customer_name")
        customer_email = request.POST.get("customer_email")

        # Split name safely
        name_parts = customer_name.strip().split()
        first_name = name_parts[0]
        last_name = name_parts[-1] if len(name_parts) > 1 else ""

        # Create customer
        customer = Customer.objects.create(
            first_name=first_name,
            last_name=last_name,
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
    order.delete()  # remove the order
    return redirect('employee')  # redirect back to the employee panel