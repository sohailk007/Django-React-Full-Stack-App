# 🎉 Referral Banking System (Django + React)

This project implements a simple **account referral system** with **introducer → beneficiary logic**.  
Built using **Django REST Framework** for the backend and **React** for the frontend.

---

## 🚀 Features
- Users can register/login (JWT authentication).
- Create accounts with optional **introducer**.
- Beneficiary is automatically calculated:
  - If introducer has introduced an **odd number of people** → beneficiary = introducer.
  - If introducer has introduced an **even number of people** → beneficiary = introducer’s introducer’s beneficiary (fallback to introducer).
- View all accounts in a table (account ID, introducer, beneficiary).
- Protected routes (only logged-in users can access account pages).

---

## 🛠️ Tech Stack
- **Backend**: Django, Django REST Framework, JWT Auth
- **Frontend**: React, Axios, React Router
- **Database**: SQLite (default, can switch to PostgreSQL/MySQL)

---

## 📂 Project Structure

### Backend (`backend/`)

backend/
│── accounts/
│ │── models.py # Account model with introducer/beneficiary logic
│ │── serializers.py # DRF serializers
│ │── views.py # API endpoints
│ │── urls.py # Account-related routes
│── users/ # Authentication (JWT login/register)
│── backend/ # Django project settings


### Frontend (`frontend/`)
frontend/
│── src/
│ │── api.js # Axios instance (with JWT token support)
│ │── App.js # Main router
│ │── components/
│ │ │── AccountForm.js
│ │ │── ProtectedRoute.js
│ │── pages/
│ │── AccountPage.js
│ │── Login.js
│ │── Register.js
│ │── Home.js
│ │── NotFound.js


---

## ⚙️ Installation

### 1. Backend Setup (Django + DRF)
```bash
# Clone the repo
git clone https://github.com/your-username/referral-banking.git
cd referral-banking/backend

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start backend
python manage.py runserver
Backend will be running at 👉 http://127.0.0.1:8000/

2. Frontend Setup (React)
cd ../frontend

# Install dependencies
npm install

# Start frontend
npm start
Frontend will be running at 👉 http://localhost:3000/

🔑 API Endpoints
Accounts
GET /api/accounts/ → List all accounts

POST /api/accounts/create/ → Create new account
Payload:

{
  "introducer": 1   // optional
}
Example Response:

{
  "account_id": 2,
  "introducer": 1,
  "beneficiary": 1
}
Auth
POST /api/users/register/ → Register

POST /api/users/login/ → Login (returns JWT token)

🖼️ Frontend Screens
Login/Register: JWT auth

Create Account: Enter optional introducer ID

Accounts List: Displays table of all accounts (ID, introducer, beneficiary)

✅ Workflow
Create the first account (no introducer).

Create another account with introducer=1 → beneficiary = 1.

Create more accounts with same introducer → alternating beneficiary logic applies.

📌 Notes
If you try to create an account with a non-existing introducer ID → API returns 400 error.

Only authenticated users can create/view accounts (via ProtectedRoute).

