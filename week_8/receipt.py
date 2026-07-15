def print_receipt(name, food, quantity, price, delivery_charge):

    subtotal = quantity * price

    service_charge = subtotal * 0.05

    grand_total = subtotal + service_charge + delivery_charge

    print("\n========== RECEIPT ==========")

    print(f"Customer : {name}")
    print(f"Food     : {food}")
    print(f"Quantity : {quantity}")
    print(f"Price    : RM {price:.2f}")

    print("------------------------------")

    print(f"Subtotal        : RM {subtotal:.2f}")
    print(f"Service Charge  : RM {service_charge:.2f}")
    print(f"Delivery Charge : RM {delivery_charge:.2f}")

    print("------------------------------")

    print(f"TOTAL : RM {grand_total:.2f}")

    print("==============================")