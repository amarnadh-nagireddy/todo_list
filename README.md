
# **Django To-Do App**  

## **Overview**  
This is a simple **To-Do web application** built using **Django** that allows users to **manage tasks efficiently**. Users can **create, update, delete, and mark tasks as completed** while keeping track of their progress. The app also includes **user authentication** with login and registration functionality.  

## **Features**  
✅ **User Authentication** (Register, Login, Logout)  
✅ **Create, Read, Update, and Delete (CRUD) tasks**  
✅ **Mark tasks as completed**  
✅ **Filter completed and pending tasks**  
✅ **Secure database storage using PostgreSQL**  

## **Tech Stack**  
- **Backend:** Django (Python)  
- **Database:** PostgreSQL  
- **Frontend:** HTML, CSS, Bootstrap  
- **Authentication:** Django built-in authentication  

## **Installation & Setup**  
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/amarnadhNagireddy/todo_list.git
   cd todo_list
   ```

2. **Create & Activate Virtual Environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Mac/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure PostgreSQL Database**  
   Update your `settings.py` with your PostgreSQL credentials:  
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }

5. **Run Migrations**  
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser** (Optional)  
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the Server**  
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**  
   Open your browser and go to:  
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


## **License**  
This project is **open-source** and free to use.  
