# Lesson 1 - Introduction to Django

## Definition
Django is a high-level Python web framework that receives HTTP requests, processes them using Python code, interacts with databases when required, and returns HTTP responses to the client. It follows the MVT (Model-View-Template) architecture.

## Why Django?
- Fast development
- Secure by default
- Scalable
- Built-in ORM
- Authentication system
- Admin Panel
- URL Routing
- Written in Python

## Client vs Server

| Client | Server |
|--------|--------|
| Requests resources | Processes requests |
| Chrome, Firefox, Mobile Apps | Computer hosting the website |
| Sends HTTP Request | Sends HTTP Response |

## HTTP

**HTTP (HyperText Transfer Protocol):** Communication protocol used between the client and the server.

**Request:** Sent by the client asking for a resource.

**Response:** Returned by the server after processing the request.

## Workflow

Client → HTTP Request → Server (Django) → Process Request → HTTP Response → Client

## Django Project vs App

| Project | App |
|---------|-----|
| Complete website | A single module/feature |
| Contains multiple apps | Handles one specific responsibility |

### Example

CRM Project
- Clients App
- Employees App
- Reports App
- Notifications App

## MVT Architecture

| Component | Responsibility |
|-----------|----------------|
| Model | Handles data and database |
| View | Contains business logic |
| Template | Displays data to the user |

## Request Lifecycle

Browser → HTTP Request → Django → URL Dispatcher → View → Model (Optional) → Database (Optional) → Template (Optional) → HTTP Response → Browser

## Important Points

- Django is a backend framework.
- Django is written in Python.
- Every website follows the Request–Response cycle.
- Models and databases are not required for every request.
- Templates are used only when rendering HTML pages.
- Django encourages code organization using Projects and Apps.

## Common Mistakes

❌ Django is a programming language.

✔ Django is a Python web framework.

❌ Every Django project contains only one app.

✔ A project can contain multiple apps.

❌ Every request accesses the database.

✔ Database access depends on the request.

## Interview Questions

1. What is Django?
2. Why is Django called a high-level framework?
3. What is the difference between a Client and a Server?
4. Explain the Request–Response cycle.
5. What is the difference between a Django Project and a Django App?
6. Explain MVT Architecture.
7. Why do companies prefer Django?

## Summary

Django is a Python web framework that simplifies web development by providing built-in tools for URL routing, database interaction, authentication, security, and application structure. Every client request is processed by Django and returned as an HTTP response. Django organizes applications using Projects and Apps while following the MVT architecture.

# Lesson 1.2 - URL Dispatcher

## Definition
The URL Dispatcher is Django's routing system. It matches the requested URL with the routes defined in `urlpatterns` inside `urls.py` and calls the corresponding View function.

## URL Structure

Example:

http://127.0.0.1:8000/blog/

| Part | Meaning |
|------|---------|
| http:// | Protocol used for communication |
| 127.0.0.1 | Loopback IP Address (localhost) |
| 8000 | Port Number |
| /blog/ | URL Path |

## Key Concepts

### URL Dispatcher
- Acts as Django's router.
- Matches the requested URL with `urlpatterns`.
- Calls the appropriate View function.

### urls.py
- Contains all URL routes.
- Acts as the entry point for incoming requests.

### urlpatterns
- A list of URL patterns.
- Maps URL paths to View functions.

Example:

```python
urlpatterns = [
    path("", home),
    path("about/", about),
    path("contact/", contact),
    path("blog/", blog),
]
```

### Loopback Address (127.0.0.1)
- Refers to your own computer.
- Also called **localhost**.
- Used during local development.

### Port Number
- Identifies which application should receive the request.
- Django uses **8000** by default during development.
- Other ports (8001, 8080, 9000, etc.) can also be used.

### URL Path
- Represents the resource requested by the client.
- Examples:
  - `/`
  - `/about/`
  - `/contact/`
  - `/blog/`

## Request Flow

Browser → HTTP Request → Django → URL Dispatcher (`urls.py`) → Match `urlpatterns` → View → Model (Optional) → Database (Optional) → Template (Optional) → HTTP Response → Browser

## Example

User visits:

http://127.0.0.1:8000/about/

Execution Flow:

1. Browser sends an HTTP Request.
2. Django receives the request.
3. `urls.py` checks `urlpatterns`.
4. Django finds the matching path.
5. Django calls `about(request)`.
6. The View processes the request.
7. Django returns an HTTP Response.
8. Browser displays the response.

## Important Points

- Every request first reaches the URL Dispatcher.
- `urls.py` decides which View should execute.
- A URL Path is **not** a View.
- Models, Database, and Templates are optional depending on the request.
- The View always returns an HTTP Response.

## Common Mistakes

❌ `/blog/` is a View.

✔ `/blog/` is a URL Path. The View is the Python function executed after URL matching.

❌ Every request accesses the database.

✔ Database access depends on the View logic.

❌ `urls.py` contains business logic.

✔ Business logic belongs inside Views, not `urls.py`.

## Interview Questions

1. What is the purpose of the URL Dispatcher?
2. What is the role of `urls.py`?
3. What is `urlpatterns`?
4. What is the difference between a URL Path and a View?
5. What is localhost?
6. Why does Django use port 8000?
7. Can a View return a response without accessing the database?

## Summary

The URL Dispatcher is responsible for routing incoming requests. It checks the requested URL against `urlpatterns` inside `urls.py` and executes the matching View. The View processes the request and returns an HTTP Response, with Models, Databases, and Templates being used only when required.

# Lesson 1.3 - Creating Your First Django Project

## Definition
A Django Project is the complete configuration and foundation of a Django application. It contains the settings, URL configuration, and other files required to run the application.

## Project Creation

Command:

```bash
django-admin startproject crm_project
```

### Breakdown

| Command | Purpose |
|----------|---------|
| django-admin | Django's administrative command-line utility |
| startproject | Creates a new Django project |
| crm_project | Name of the project |

## Project Structure

```text
crm_project/
│
├── manage.py
│
└── crm_project/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

## Why Two Folders?

The project contains two folders with the same name because they have different responsibilities.

| Folder | Purpose |
|---------|---------|
| Outer Folder | Project container that stores the entire project. |
| Inner Folder | Python package containing Django's configuration files. |

Example:

```text
crm_project/        ← Project Container
│
└── crm_project/    ← Django Configuration Package
```

## Important Files

### manage.py
- Project-specific command-line utility.
- Used to execute Django commands.

Common Commands:

```bash
python manage.py runserver
python manage.py startapp app_name
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### __init__.py
- Marks the directory as a Python package.
- Rarely modified.

### settings.py
- Configuration file of the project.
- Controls:
  - Installed Apps
  - Database
  - Templates
  - Static Files
  - Time Zone
  - Security Settings
  - Debug Mode

### urls.py
- Handles URL routing.
- Maps URL paths to View functions.

### wsgi.py
- Used for deploying Django applications using WSGI-compatible servers.
- Rarely modified.

### asgi.py
- Used for asynchronous deployments (WebSockets, real-time applications, async support).
- Rarely modified.

## Frequently Edited Files

| File | Frequency |
|------|-----------|
| manage.py | Very Frequently |
| settings.py | Frequently |
| urls.py | Frequently |
| views.py | Frequently |
| models.py | Frequently |
| __init__.py | Rarely |
| wsgi.py | Rarely |
| asgi.py | Rarely |

## Workflow

Create Project → Django Generates Project Structure → Configure `settings.py` → Configure `urls.py` → Create Apps → Build Website

## Important Points

- `django-admin` is used to create Django projects.
- `manage.py` is used after project creation to execute project-specific Django commands.
- The outer folder is the project container.
- The inner folder contains Django configuration files.
- `settings.py` acts as the control panel of the project.
- `urls.py` acts as the routing system of the project.
- `wsgi.py` and `asgi.py` are mainly used during deployment.

## Common Mistakes

❌ Thinking both `crm_project` folders are the same.

✔ The outer folder is the project container, while the inner folder is the Django configuration package.

❌ Using `django-admin` for every command after creating the project.

✔ Use `manage.py` for project-specific commands.

❌ Editing `wsgi.py` or `asgi.py` during development.

✔ Most beginners rarely need to modify these files.

## Interview Questions

1. What is a Django Project?
2. What is the purpose of `django-admin`?
3. What is the difference between `django-admin` and `manage.py`?
4. Why are there two folders with the same project name?
5. What is the purpose of `settings.py`?
6. What is the role of `urls.py`?
7. What is the purpose of `__init__.py`?
8. What is the difference between `wsgi.py` and `asgi.py`?

## Summary

A Django Project provides the foundation required to build a web application. The `django-admin startproject` command generates the project structure, including configuration files such as `settings.py`, `urls.py`, `wsgi.py`, and `asgi.py`. The `manage.py` file is used to execute project-specific Django commands, while the outer folder stores the project and the inner folder acts as the Django configuration package.

# Lesson 1.4 - Virtual Environment & Running the Development Server

## Definition

A Virtual Environment (venv) is an isolated Python environment that contains its own Python interpreter and installed packages, allowing each project to manage its own dependencies independently.

## Why Virtual Environment?

- Prevents dependency conflicts between projects.
- Allows different projects to use different package versions.
- Keeps the global Python installation clean.
- Standard practice in professional development.

## Creating a Virtual Environment

```bash
python -m venv venv
```

### Breakdown

| Command | Purpose |
|----------|---------|
| python | Runs the Python interpreter |
| -m | Executes a Python module |
| venv | Python's built-in virtual environment module |
| venv | Name of the virtual environment folder |

## Activating the Virtual Environment

### Windows (Command Prompt)

```cmd
venv\Scripts\activate
```

### Windows (PowerShell)

```powershell
venv\Scripts\Activate.ps1
```

### macOS/Linux

```bash
source venv/bin/activate
```

## Identifying an Active Virtual Environment

Example:

```text
(venv) C:\Users\Om\django-course>
```

The `(venv)` prefix indicates that the virtual environment is active.

## pip

`pip` is Python's package manager. It installs, upgrades, and removes Python packages from the Python Package Index (PyPI).

## Installing Django

```bash
pip install django
```

Django is installed **inside the active virtual environment**, not globally.

## Checking Django Version

```bash
python -m django --version
```

Displays the installed Django version.

## Creating a Project

```bash
django-admin startproject crm_project
```

Creates a new Django project with the default project structure.

## Running the Development Server

```bash
cd crm_project
python manage.py runserver
```

Starts Django's built-in development server.

Default Address:

```text
http://127.0.0.1:8000/
```

## Internal Workflow

python → manage.py → Load `settings.py` → Initialize Django → Load Installed Apps → Load URL Configuration → Perform System Checks → Start Development Server → Wait for HTTP Requests

## Important Points

- Always activate the virtual environment before working on a project.
- Django packages are installed inside the virtual environment.
- `runserver` starts Django's development server.
- Django automatically reloads when project files are modified.
- Stop the development server using `CTRL + C`.

## Common Mistakes

❌ Installing packages without activating the virtual environment.

✔ Activate the virtual environment first.

❌ Installing Django globally for every project.

✔ Install Django inside the project's virtual environment.

❌ Closing the terminal without deactivating the environment.

✔ Use `deactivate` when you are finished (optional but recommended).

## Interview Questions

1. What is a Virtual Environment?
2. Why should every Django project use a Virtual Environment?
3. What does `python -m` do?
4. What is `pip`?
5. Where are packages installed when using a Virtual Environment?
6. What is the purpose of `runserver`?
7. What is StatReloader?
8. How do you stop Django's development server?

## Summary

A Virtual Environment isolates project dependencies, preventing version conflicts between projects. Django should always be installed inside the active virtual environment. The `runserver` command starts Django's built-in development server, performs system checks, loads the project configuration, and listens for incoming HTTP requests while automatically reloading when project files change.

# Lesson 1.5 - Creating Your First Django App

## Definition

A Django App is a self-contained module responsible for one specific feature of a Django project. A project can contain multiple apps, each handling a different responsibility.

## Why Use Apps?

- Better code organization
- Easier debugging
- Easier teamwork
- Improved maintainability
- Reusable across projects
- Better scalability

## Creating an App

```bash
python manage.py startapp blog
```

### Breakdown

| Command | Purpose |
|----------|---------|
| python | Runs Python |
| manage.py | Executes project-specific Django commands |
| startapp | Creates a new Django app |
| blog | Name of the app |

## App Structure

```text
blog/
│
├── migrations/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

## File Responsibilities

| File | Purpose |
|------|---------|
| views.py | Contains business logic |
| models.py | Defines database models |
| admin.py | Registers models for the Django Admin Panel |
| apps.py | Stores app configuration |
| tests.py | Contains test cases |
| migrations/ | Stores database migration files |
| __init__.py | Marks the directory as a Python package |

## Registering an App

Open `settings.py` and add the app name to `INSTALLED_APPS`.

Example:

```python
INSTALLED_APPS = [
    ...
    "blog",
]
```

Without registration, Django does not load the app.

## Workflow

Create App → Register in `INSTALLED_APPS` → Django Loads App During Startup → Views, Models, Templates and Admin Become Available

## Important Points

- A Django Project can contain multiple apps.
- Each app should have a single responsibility.
- `startproject` creates the project foundation.
- `startapp` creates a feature module.
- Apps must be added to `INSTALLED_APPS`.
- `admin.py` registers models for the admin panel.

## Common Mistakes

❌ Confusing a Project with an App.

✔ A Project contains multiple Apps.

❌ Forgetting to add the app to `INSTALLED_APPS`.

✔ Always register new apps in `settings.py`.

❌ Placing unrelated features inside a single app.

✔ Split features into separate apps based on responsibility.

## Interview Questions

1. What is a Django App?
2. What is the difference between a Project and an App?
3. Why does Django use multiple apps?
4. What is the difference between `startproject` and `startapp`?
5. What is the purpose of `views.py`?
6. What is the purpose of `models.py`?
7. Why must an app be added to `INSTALLED_APPS`?
8. What is the role of `admin.py`?
9. Can a Django project have only one app?
10. Can a Django app be reused in another project?

## Summary

A Django App is a modular component of a Django Project that is responsible for a single feature. Splitting projects into multiple apps improves organization, teamwork, maintainability, and scalability. Every newly created app must be registered in `INSTALLED_APPS` before Django recognizes and loads it.

## Register a Django App

### Location

```text
crm_project/settings.py
```

### Syntax

```python
INSTALLED_APPS = [
    ...
    "blog",
]
```

### Purpose

Registers the app so Django recognizes it and loads it during project startup.

### Why is it Required?

When an app is created using `startapp`, Django does **not** automatically include it in the project. Adding it to `INSTALLED_APPS` tells Django to load its models, admin configuration, templates, static files, and other app components.

### Common Mistakes

❌ Forgetting to register the app.

✔ Always add every new app to `INSTALLED_APPS`.

---

❌ Misspelling the app name.

✔ Ensure the app name matches the folder name exactly.

### Interview Tip

Creating an app and registering an app are two separate steps. An app exists on disk after `startapp`, but Django only loads it after it is added to `INSTALLED_APPS`.
