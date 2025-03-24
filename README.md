# Django E-Commerce Platform

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.0-brightgreen)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

A full-featured e-commerce platform built with Django, featuring product management, cart functionality, user authentication, and search capabilities.


## ✨ Key Features

- **Product Catalog**
  - Category-based product organization
  - Price filtering and sorting
  - Product search with auto-suggestions
- **Shopping Cart**
  - Session-based cart system
  - Discount code integration
  - Checkout process
- **User System**
  - Authentication (Register/Login/Password Reset)
  - Order history tracking
  - Profile management
- **Admin Dashboard**
  - Product/Inventory management
  - Order processing
  - Sales analytics

## 🛠️ Technical Highlights

- **Backend**
  - Django ORM for database operations
  - Class-Based Views (CBVs) for core functionality
  - Custom middleware for cart processing
  - PostgreSQL database (production-ready)
  
- **Frontend**
  - Bootstrap 5 responsive design
  - AJAX for cart updates
  - Template inheritance system
  
- **Performance**
  - Caching with Redis
  - Optimized database queries
  - Pagination for product listings

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-ecommerce.git
   cd django-ecommerce
   ```
2. Set up virtual environment:
3. Install dependencies:
4. Configure environment variables:
5. Run migrations:
6. Create superuser:
7. Run development server:


## 📂 Project Structure
```bash
django-ecommerce/
├── ecommerce/               # Main project settings
├── product/           # Product models/views
├── cart/               # Shopping cart logic
├── account/              # Authentication system
├── templates/          # HTML templates
├── static/             # CSS/JS/Images
└── manage.py           # Django CLI
```
