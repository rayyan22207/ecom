# 🛒 E‑Commerce API Backend (Built on SaaS Foundations)

This is a full-stack, **API-first e-commerce backend** built using Django, Django REST Framework, Tailwind CSS, and more.

> ⚠️ **Note:** This project is under active development. The goal is to build a clean, scalable API-powered e-commerce backend from scratch, inspired by the [SaaS Foundations](https://github.com/codingforentrepreneurs/SaaS-Foundations) structure.

---

## 🧱 Based On

This project is based on the open-source **[SaaS Foundations](https://github.com/codingforentrepreneurs/SaaS-Foundations)** repo by Coding for Entrepreneurs. Their architecture served as the starting point.  
Big thanks to their work! This project extends that foundation into a full **multi-domain e-commerce system** with:

- Clean modular app structure (`accounts`, `catalog`, `cart`, `orders`, `payments`, etc.)
- REST API using Django REST Framework
- JWT-based authentication
- Paddle integration (planned)
- Analytics, comments, activity tracking
- Tailwind-based frontend (portfolio UI)

---

## ⚙️ Getting Started

### 1. Clone & Setup Environment

```bash
git clone https://github.com/yourusername/ecom-api-backend.git
cd ecom-api-backend
```
### Create Virtual Environment

*macOS/Linux*
```bash
python3 -m venv venv
source venv/bin/activate
```

*Windows*
```bash
python -m virtualenv venv # if it doesn't work then pip install virtualenv
.\venv\Scripts\activate
```
### 3. Install Requirements
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
### 🔐 Setup Environment Variables
## Create a .env file at the project root:
```ini
DJANGO_SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:pass@localhost:5432/ecom_db

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your@email.com
EMAIL_HOST_PASSWORD=your-email-password

STRIPE_SECRET_KEY=optional
PADDLE_VENDOR_ID=optional
PADDLE_API_KEY=optional
```
## Generate a Django secret key:
``` bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
### 🚀 First Run
```bash
# Activate virtual env if not already
source venv/bin/activate     # or .\venv\Scripts\activate (Windows)

cd src/

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Pull Tailwind vendor files
python manage.py vendor_pull

# Start dev server
python manage.py runserver
```
## 📦 Project Modules

- `accounts/` – Custom user model, profile, address book  
- `catalog/` – Products, categories, media, inventory  
- `cart/` – User cart, cart items (anonymous and logged-in)  
- `orders/` – Checkout flow, order status tracking  
- `payments/` – Paddle integration (coming soon)  
- `comments/` – Product reviews and moderation  
- `analytics/` – Stats, tracking, user activity  
- `frontend/` – Minimal portfolio-styled Tailwind frontend  
- `docs/` – API schema (OpenAPI), usage examples (planned)  

---

## 📡 API Endpoints (v1)

> All routes are versioned and mounted under `/api/v1/`

- `POST   /auth/register` – Register a new user  
- `POST   /auth/login` – Obtain JWT token  
- `GET    /catalog/products/` – List products  
- `GET    /catalog/categories/` – List categories  
- `GET    /cart/` – View current cart  
- `POST   /cart/items/` – Add item to cart  
- `GET    /orders/` – View user orders  
- `GET    /users/me/` – User profile  
- `GET    /users/me/stats/` – Analytics stats  
- `POST   /reviews/` – Submit a product review  
- `POST   /checkout/` – Start checkout (Paddle - coming soon)  

---

## 📜 License & Attribution

This project is built on top of the amazing work by **[SaaS Foundations](https://github.com/codingforentrepreneurs/SaaS-Foundations)**.  
Their project is licensed under the [MIT License](https://github.com/codingforentrepreneurs/SaaS-Foundations/blob/main/LICENSE), and this project continues to respect and extend that license.

> MIT License applies unless otherwise specified.

---

## 🛠️ Roadmap

- [x] Custom user model + auth  
- [x] Catalog system  
- [x] Cart & Orders  
- [ ] Paddle checkout integration  
- [ ] Reviews system  
- [ ] Basic analytics  
- [ ] GraphQL support  
- [ ] Multi-tenant SaaS mode  

---

## 📬 Contact

Made with ❤️ by **Rayyan Aqil**  
_Portfolio coming soon..._
