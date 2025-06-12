# Inventory Management System

A simple Django-based **inventory management system** following the **MVT (Model–View–Template)** pattern.  
Built with:

- 🔐 Django's built-in authentication (login, logout, register)
- 🗃️ Default SQLite database
- 🧱 Clean MVT folder structure
- CRUD operations for warehouses, items, transactions
- 📊 Reports like fast/slow-moving items, FSN & ABC analysis

---

## 📁 Project Structure

inventory_mgmt/
├── inventory_mgmt/              # Django app
│   ├── models.py       # Model (data layer)
│   ├── views.py        # View (logic & control)
│   ├── urls.py         # Route definitions
│   ├── templates/      # Template (HTML rendering)
│   └── forms.py        # (Optional) Django forms
├── db.sqlite3          # Default SQLite database
├── manage.py
├── requirements.txt
└── project/       # Django project config
    ├── settings.py
    ├── urls.py
    └── wsgi.py


## 🚀 Setup & Run Locally

1. **Clone the repo**  
   ```bash
   git clone https://github.com/nadhiffarizi/inventory-mgmt.git
   cd inventory-mgmt
2. Create and activate a virtual environment
   python -m venv venv
   source venv/bin/activate    # Windows: venv\Scripts\activate
3. Install dependencies
   pip install -r requirements.txt
4. Run migrations
   python manage.py migrate
5. Create a superuser
   python manage.py createsuperuser
6. Start the development server
   python manage.py runserver

visit localhost:8000

