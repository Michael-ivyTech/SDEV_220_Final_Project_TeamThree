from django import template

register = template.Library()

@register.filter
def calc_order_total(order_items):
    total = 0
    for item in order_items:
        total += item.bakedgood.item_cost * item.quantity
    return "%.2f" % total

def sum_total_cost(order_items):
    return sum(item.bakedgood.item_cost * item.quantity for item in order_items)