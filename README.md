# 🧺 Mini Laundry Order Management System (AI-First)

## 📌 Project Overview

This project is a simple backend system for managing laundry/dry-cleaning orders. It allows users to create orders, track their status, and view business insights like total revenue and order distribution.

The system is built using **FastAPI** and follows a clean and minimal API-based design.

---

## 🎯 Objectives

- Create and manage laundry orders
- Track order status
- Calculate billing
- Provide dashboard insights

---

## 🚀 Features Implemented

### ✅ 1. Create Order

- Add customer details (name, phone)
- Add garment details (item, quantity, price)
- Automatically calculates total bill
- Assigns unique order ID

---

### ✅ 2. Order Status Management

Each order has a status:

- RECEIVED
- PROCESSING
- READY
- DELIVERED

You can update order status anytime.

---

### ✅ 3. View Orders

- View all orders
- Displays complete order details

---

### ✅ 4. Filter Orders

- Filter by status
- Filter by phone number

---

### ✅ 5. Dashboard (Analytics)

- Total number of orders
- Total revenue
- Orders grouped by status

---

## 🛠️ Tech Stack

- **Python 3**
- **FastAPI**
- **Uvicorn**

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/laundry-order-system.git
cd laundry-order-system
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Server

```bash
python -m uvicorn app:app --reload
```

### 5. Open API Docs

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

| Method | Endpoint                  | Description         |
| ------ | ------------------------- | ------------------- |
| POST   | /create-order             | Create a new order  |
| GET    | /orders                   | Get all orders      |
| PUT    | /update-status/{order_id} | Update order status |
| GET    | /orders/filter            | Filter orders       |
| GET    | /dashboard                | View analytics      |

---

## 📊 Sample API Output

### Create Order Response:

```json
{
  "message": "Order created",
  "order": {
    "id": 1,
    "name": "Darshan",
    "phone": "9876543210",
    "item": "Shirt",
    "quantity": 2,
    "price": 50,
    "total": 100,
    "status": "RECEIVED"
  }
}
```

---

### Dashboard Response:

```json
{
  "total_orders": 2,
  "total_revenue": 200,
  "orders_by_status": {
    "RECEIVED": 1,
    "PROCESSING": 1
  }
}
```

---

## 🤖 AI Usage Report (Critical Requirement)

### Tools Used:

- ChatGPT

### How AI Helped:

- Generated initial FastAPI structure
- Assisted in debugging errors
- Helped design API endpoints
- Improved code readability and structure

### Issues Faced:

- Virtual environment not detected correctly
- FastAPI module not found error
- Missing variables in dashboard logic

### Fixes / Improvements:

- Used `python -m uvicorn` to fix environment issues
- Corrected logic bugs in dashboard and filtering
- Cleaned and structured the code

---

## ⚖️ Trade-offs

- Used in-memory storage instead of database (faster to implement, but not scalable)
- No authentication implemented (kept simple as per assignment scope)

---

## 📸 Screenshots

Screenshots are available in the `/screenshots` folder:

- create_order.png
- view_orders.png
- update_status.png
- filter_orders.png
- dashboard.png

---

## 📁 Project Structure

```
laundry-order-system/
│
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
    ├── create_order.png
    ├── view_orders.png
    ├── update_status.png
    ├── filter_orders.png
    └── dashboard.png
```

---

## 📌 Conclusion

This project demonstrates a simple and effective backend system for managing laundry operations. It focuses on clean API design, quick development, and effective use of AI tools.

---

## 🙌 Author

Darshan S
