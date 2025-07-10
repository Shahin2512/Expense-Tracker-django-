A simple Django web application to manage personal expenses. Users can:
- Add income and expense entries
- View total expenses
- Filter expenses by category or date
- Visualize data using pie and line charts with Chart.js

## ⚙️ Setup Instructions
```bash
# 1. Clone the repository
https://github.com/your-username/expense-tracker.git
cd expense-tracker

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install django

# 4. Apply migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create superuser (for admin login)
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver

## 🌐 Features
- Add and list all expenses
- Total spent overview
- Delete expenses
- Visual charts:
  - 📊 Pie Chart: Category-wise spending
  - 📈 Line Chart: Daily expense trend

## 🧪 Tech Stack
- Backend: Django
- Frontend: HTML, Bootstrap
- Charts: Chart.js
- Database: SQLite (default) 

<img width="1917" height="949" alt="Screenshot 2025-07-11 011336" src="https://github.com/user-attachments/assets/1eb02f5c-763e-4730-b7c3-a2f91aaaaebd" />
