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