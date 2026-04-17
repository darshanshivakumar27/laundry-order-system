from fastapi import FastAPI

app = FastAPI()

# In-memory storage
orders = []
order_id_counter = 1


@app.get("/")
def home():
    return {"message": "Laundry Management System Running"}


# CREATE ORDER
@app.post("/create-order")
def create_order(name: str, phone: str, item: str, quantity: int, price: float):
    global order_id_counter

    total = quantity * price

    order = {
        "id": order_id_counter,
        "name": name,
        "phone": phone,
        "item": item,
        "quantity": quantity,
        "price": price,
        "total": total,
        "status": "RECEIVED"
    }

    orders.append(order)
    order_id_counter += 1

    return {"message": "Order created", "order": order}


# VIEW ORDERS
@app.get("/orders")
def get_orders():
    return {"orders": orders}


# UPDATE STATUS
@app.put("/update-status/{order_id}")
def update_status(order_id: int, status: str):
    for order in orders:
        if order["id"] == order_id:
            order["status"] = status
            return {"message": "Updated", "order": order}

    return {"error": "Order not found"}


# FILTER ORDERS
@app.get("/orders/filter")
def filter_orders(status: str = None, phone: str = None):
    filtered = orders

    if status:
        filtered = [o for o in filtered if o["status"] == status]

    if phone:
        filtered = [o for o in filtered if o["phone"] == phone]

    return {"filtered_orders": filtered}


# DASHBOARD
@app.get("/dashboard")
def dashboard():
    total_orders = len(orders)
    total_revenue = sum(o["total"] for o in orders)

    status_count = {}
    for o in orders:
        status = o["status"]
        status_count[status] = status_count.get(status, 0) + 1

    return {
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "orders_by_status": status_count
    }