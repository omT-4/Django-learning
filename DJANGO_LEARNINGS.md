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

# Lesson 1.6 - Understanding Views

## Definition

A View is a Python function (or class) that receives an HTTP request, processes it, and returns an HTTP response.

## Responsibilities of a View

1. Receive the HTTP Request.
2. Process the Request.
3. Return an HTTP Response.

## Basic View

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")
```

## Code Breakdown

### Import

```python
from django.http import HttpResponse
```

Imports Django's `HttpResponse` class.

### View Function

```python
def home(request):
```

Defines a View function.

- `home` → Function name.
- `request` → Automatically created and passed by Django.

### Response

```python
return HttpResponse("Hello, Django!")
```

Creates and returns an HTTP response to the browser.

## Request Object

The `request` object is automatically created by Django and contains information sent by the client.

Examples:

- Requested URL
- HTTP Method (GET, POST)
- Headers
- Cookies
- Session Data
- Logged-in User
- Form Data
- Client IP Address

## HttpResponse

`HttpResponse` creates a valid HTTP response object that Django sends back to the client's browser.

## print() vs HttpResponse()

| print() | HttpResponse() |
|----------|----------------|
| Displays output in the terminal | Sends output to the browser |
| Used for debugging | Used to return HTTP responses |

## Request Flow

Browser → HTTP Request → URL Dispatcher → View → Business Logic → HttpResponse → Browser

## Important Points

- Every View receives a `request` object.
- Every View must return an HTTP response.
- Django automatically passes the `request` object.
- `print()` is not a replacement for `HttpResponse()`.
- Views contain the application's business logic.

## Common Mistakes

❌ Forgetting to return an `HttpResponse`.

✔ Every View must return an HTTP response.

---

❌ Using `print()` to display content in the browser.

✔ Use `HttpResponse()` to send data to the browser.

---

❌ Thinking `request` is created manually.

✔ Django automatically creates and passes the `request` object.

## Interview Questions

1. What is a Django View?
2. What are the responsibilities of a View?
3. What is the purpose of `HttpResponse`?
4. What is the difference between `print()` and `HttpResponse()`?
5. Where does the `request` object come from?
6. What information can the `request` object contain?
7. What happens if a View does not return an `HttpResponse`?

## Summary

A View is the core processing unit of a Django application. It receives an HTTP request, executes the required business logic, and returns an HTTP response. Django automatically provides the `request` object, while `HttpResponse` is used to send data back to the browser.

# Lesson 1.7 - URL Mapping

## Definition

URL Mapping is the process of connecting a requested URL to the appropriate View function. Django performs this mapping using `urlpatterns`.

## Why URL Mapping?

- Connects URLs to Views.
- Organizes application routing.
- Keeps large projects modular and maintainable.
- Allows each app to manage its own URLs.

## Project URLs vs App URLs

| Project `urls.py` | App `urls.py` |
|-------------------|---------------|
| Decides which app should handle the request | Decides which View should handle the request |

## Creating App URLs

Create a new file:

```text
blog/
│
└── urls.py
```

Example:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
]
```

## `path()` Breakdown

```python
path("", views.home, name="home")
```

| Argument | Purpose |
|----------|---------|
| `""` | Matches the remaining URL after the app prefix |
| `views.home` | Calls the `home` View |
| `name="home"` | Assigns a name to the URL for future reference |

## `include()`

Example:

```python
path("blog/", include("blog.urls"))
```

`include()` tells Django to stop routing in the current `urls.py` and continue matching URLs inside `blog/urls.py`.

## `from . import views`

- `.` refers to the current app.
- Imports the `views.py` file from the current directory.

## Request Flow

Browser → HTTP Request → Project `urls.py` → `include()` → App `urls.py` → View → `HttpResponse` → Browser

## Important Points

- Every URL should map to a View.
- Large projects use separate `urls.py` files for each app.
- `include()` delegates URL handling to another app.
- `urlpatterns` stores URL-to-View mappings.

## Common Mistakes

❌ Assuming `path()` directly sends a response.

✔ `path()` only maps URLs to Views.

---

❌ Thinking `""` matches every URL.

✔ It matches the remaining part of the URL after the app prefix.

---

❌ Forgetting to use `include()` for app URLs.

✔ Use `include()` to keep routing modular.

## Interview Questions

1. What is URL Mapping?
2. What is the purpose of `urlpatterns`?
3. What does `path()` do?
4. What is `include()`?
5. Why do Django projects have multiple `urls.py` files?
6. Explain the arguments of `path("", views.home, name="home")`.
7. What does `from . import views` mean?

## Summary

URL Mapping connects incoming URLs to View functions. The project `urls.py` decides which app should handle the request, while each app's `urls.py` decides which View should execute. The `include()` function delegates routing to an app, making Django projects modular and scalable.

# Lesson 1.8 - Mini Project

## Objective

Build a simple multi-page Django application by connecting URLs to Views and returning different HTTP responses.

## Multiple Views

Example:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Home")

def about(request):
    return HttpResponse("About Page")

def contact(request):
    return HttpResponse("Contact Page")
```

Each View is responsible for handling one page.

## URL Mapping

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
```

Each URL maps to a specific View.

## Complete Request Flow

Browser → HTTP Request → Project `urls.py` → `include()` → App `urls.py` → Matching `path()` → View → `HttpResponse` → Browser

## Responsibilities

| Component | Responsibility |
|-----------|----------------|
| Browser | Sends HTTP Request |
| Project `urls.py` | Routes request to the correct app |
| `include()` | Delegates routing to the app |
| App `urls.py` | Maps URL to a View |
| View | Processes the request |
| `HttpResponse` | Returns data to the browser |

## Important Points

- One View should handle one responsibility.
- Every URL must map to a View.
- Every View must return an `HttpResponse`.
- `include()` keeps routing modular.
- Django follows the URL mappings exactly as defined.

## Common Mistakes

❌ Mapping a URL to the wrong View.

✔ Always verify URL-to-View mappings.

---

❌ Forgetting to define a URL pattern.

✔ Every accessible page needs a corresponding `path()` entry.

---

❌ Assuming Django guesses the correct View.

✔ Django only executes the View explicitly mapped in `urlpatterns`.

## Interview Questions

1. Explain the complete Django request lifecycle.
2. Why do we use multiple Views?
3. What is the purpose of `include()`?
4. What happens if a URL pattern is missing?
5. What happens if a URL is mapped to the wrong View?

## Summary

A Django application works by routing incoming requests from the browser through the project's `urls.py`, then the app's `urls.py`, which maps the request to a specific View. The View processes the request and returns an `HttpResponse`, which Django sends back to the browser.

# Lesson 2.1 - Templates & render()

## Definition

A Django Template is an HTML file that defines how a webpage should look. Templates separate the presentation (HTML) from the application's business logic (Python).

## Why Templates?

- Keep HTML separate from Python code.
- Improve readability and maintainability.
- Make collaboration between frontend and backend developers easier.
- Avoid writing HTML inside `HttpResponse()`.

## `render()`

`render()` is a helper function provided by Django that loads an HTML template, converts it into an `HttpResponse`, and returns it to the browser.

## Import

```python
from django.shortcuts import render
```

## Basic Syntax

```python
return render(request, "home.html")
```

## Argument Breakdown

| Argument | Purpose |
|----------|---------|
| `request` | The `HttpRequest` object automatically passed by Django |
| `"home.html"` | The template file to render |

## Internal Workflow

View → `render()` → Locate Template → Read HTML → Create `HttpResponse` → Browser

## `HttpResponse()` vs `render()`

| `HttpResponse()` | `render()` |
|------------------|------------|
| Returns plain text or raw HTML | Returns a rendered HTML template |
| HTML is written inside Python | HTML is stored in a separate file |
| Suitable for simple responses | Suitable for complete web pages |

## Important Points

- Templates are HTML files.
- `render()` loads templates and returns an `HttpResponse`.
- `render()` does not replace `HttpResponse`; it uses it internally.
- Separating logic from presentation keeps projects clean and maintainable.

## Common Mistakes

❌ Writing large HTML blocks inside `HttpResponse()`.

✔ Store HTML inside template files and use `render()`.

---

❌ Thinking `render()` directly sends HTML.

✔ `render()` first creates an `HttpResponse`, then Django sends it to the browser.

## Interview Questions

1. What is a Django Template?
2. What is the purpose of `render()`?
3. What is the difference between `HttpResponse()` and `render()`?
4. Why does Django encourage separating HTML from Python?
5. What happens if the template file is missing?

## Summary

Templates allow Django applications to separate presentation from business logic. The `render()` function reads an HTML template, creates an `HttpResponse`, and sends the rendered page to the browser, making it the preferred way to build real-world web applications.

# Lesson 2.2 - Templates Folder & Template Rendering

## Definition

Django Templates are stored inside a `templates` directory so that Django can locate and render HTML files efficiently.

## Recommended Folder Structure

```text
blog/
│
├── templates/
│   └── blog/
│       └── home.html
```

Each app maintains its own template directory to avoid filename conflicts.

## Why `templates/blog/`?

Large projects often contain multiple apps.

Example:

```text
blog/home.html
shop/home.html
```

By storing templates inside app-specific folders, Django can uniquely identify each template.

## Rendering a Template

```python
from django.shortcuts import render

def home(request):
    return render(request, "blog/home.html")
```

## Internal Workflow

View → `render()` → Locate `templates/blog/home.html` → Read HTML → Create `HttpResponse` → Browser

## Why Not Store HTML Anywhere?

Django follows a convention:

- Search only in template directories.
- Avoid searching the entire project.
- Improve performance and maintainability.

## Important Points

- Store templates inside the `templates` folder.
- Use an app-specific folder inside `templates`.
- Pass the relative path (`blog/home.html`) to `render()`.
- Missing templates raise a `TemplateDoesNotExist` exception.

## Common Mistakes

❌ Placing HTML files outside the `templates` directory.

✔ Always store templates inside `templates/app_name/`.

---

❌ Using only `home.html` when multiple apps contain templates with the same name.

✔ Use `app_name/home.html`.

## Interview Questions

1. Why do we create a `templates` folder?
2. Why is there an app folder inside `templates`?
3. How does Django locate templates?
4. What happens if a template file is missing?
5. Why does Django follow a standard template directory structure?

## Summary

Django locates templates by searching designated `templates` directories. Organizing templates inside `templates/app_name/` avoids conflicts, improves maintainability, and allows Django to render the correct HTML page efficiently.

# Lesson 2.3 - Passing Data to Templates (Context)

## Definition

Context is a Python dictionary used to send data from a View to a Django Template.

## Why Context?

- HTML cannot execute Python code.
- Makes web pages dynamic.
- Allows different users to see different data.
- Separates business logic from presentation.

## Creating Context

```python
context = {
    "name": "Om",
    "city": "Mumbai"
}
```

## Passing Context

```python
return render(request, "blog/home.html", context)
```

## Accessing Context in HTML

```html
<h1>Welcome {{ name }}</h1>
<p>City: {{ city }}</p>
```

## `render()` Arguments

```python
render(request, template_name, context)
```

| Argument | Purpose |
|----------|---------|
| `request` | HttpRequest object provided by Django |
| `template_name` | HTML template to render |
| `context` | Dictionary containing data for the template |

## Internal Workflow

Browser → HTTP Request → Project `urls.py` → App `urls.py` → View → Context Dictionary → `render()` → Template → Replace Variables → Create `HttpResponse` → Browser

## Important Points

- Context is always a dictionary.
- Keys in the dictionary become template variables.
- Template variable names must match dictionary keys.
- Context makes templates dynamic.

## Common Mistakes

❌ Forgetting to pass the context dictionary.

✔ Pass the dictionary as the third argument to `render()`.

---

❌ Using different names in the template and context.

✔ Ensure dictionary keys match template variable names.

---

❌ Expecting HTML to execute Python.

✔ HTML only displays the data Django passes through Context.

## Interview Questions

1. What is Context?
2. Why does Django use Context?
3. Why is Context a dictionary?
4. How do templates access Context values?
5. What happens if a template variable does not exist?

## Summary

Context is the bridge between Python and HTML. A View prepares data in a dictionary, `render()` passes it to the template, and Django replaces template variables with their corresponding values before sending the final HTML page to the browser.

# Lesson 2.4 - Django Template Language (DTL)

## Definition

Django Template Language (DTL) is a special syntax used inside HTML templates to display dynamic data and perform simple presentation logic.

## Why DTL?

- HTML cannot display Python variables by itself.
- Makes templates dynamic.
- Keeps business logic separate from presentation.
- Provides safe and simple template features.

## DTL Components

### Variables

```html
{{ name }}
```

Displays data from the Context dictionary.

### Tags

```html
{% tag %}
```

Used for template logic such as loops and conditions.

### Filters

```html
{{ name|upper }}
```

Modify how data is displayed without changing the original value.

### Django Comments

```html
{# This is a comment #}
```

Removed before the response reaches the browser.

## Common Filters

| Filter | Purpose |
|---------|---------|
| `upper` | Convert text to uppercase |
| `lower` | Convert text to lowercase |
| `title` | Capitalize each word |

## Internal Workflow

View → Context → `render()` → Template → DTL Processes Variables/Tags/Filters → `HttpResponse` → Browser

## Important Points

- `{{ }}` displays variables.
- `{% %}` performs template logic.
- `{# #}` creates Django-only comments.
- Filters modify display, not the original data.

## Common Mistakes

❌ Writing Python code directly inside templates.

✔ Use DTL instead.

---

❌ Thinking filters modify the original Context.

✔ Filters only affect how data is displayed.

---

❌ Using HTML comments for sensitive notes.

✔ Use Django comments for server-side comments.

## Interview Questions

1. What is Django Template Language?
2. Why does Django use DTL?
3. What is the difference between Variables, Tags, and Filters?
4. What is the purpose of Filters?
5. What is the difference between HTML comments and Django comments?

## Summary

DTL extends HTML by allowing templates to display dynamic data and perform simple presentation logic. It provides Variables, Tags, Filters, and Django Comments while maintaining a clear separation between business logic and presentation.

# Lesson 2.5 - Template Tags (`if`, `for`, `empty`)

## Definition

Template Tags add simple presentation logic to Django Templates. They allow templates to make decisions, repeat content, and control what is displayed.

## Why Template Tags?

- Display content conditionally.
- Repeat HTML without duplication.
- Keep templates dynamic while leaving business logic in Views.

## `if` Tag

```html
{% if is_logged_in %}
    <p>Welcome!</p>
{% else %}
    <p>Please Login.</p>
{% endif %}
```

Used for conditional rendering.

## `for` Tag

```html
{% for fruit in fruits %}
    <li>{{ fruit }}</li>
{% endfor %}
```

Repeats HTML for every item in a collection.

## `empty` Tag

```html
{% for fruit in fruits %}
    <li>{{ fruit }}</li>
{% empty %}
    <li>No Fruits Available</li>
{% endfor %}
```

Displays fallback content when the collection is empty.

## Internal Workflow

Browser → HTTP Request → Project `urls.py` → App `urls.py` → View → Create Context → `render()` → Template → Execute Tags → Create `HttpResponse` → Browser

## Important Points

- `{% if %}` controls conditional display.
- `{% for %}` repeats content.
- `{% empty %}` handles empty collections.
- Template Tags should contain only presentation logic.

## Common Mistakes

❌ Writing business logic inside templates.

✔ Keep calculations, database queries, and processing inside Views.

---

❌ Writing repetitive HTML manually.

✔ Use `{% for %}` loops.

## Interview Questions

1. What are Template Tags?
2. Why does Django provide `{% if %}` and `{% for %}`?
3. What is the purpose of `{% empty %}`?
4. What is the difference between presentation logic and business logic?
5. Why should complex logic remain inside Views?

## Summary

Template Tags allow Django Templates to perform simple presentation logic such as conditions and loops. They make templates dynamic while maintaining a clear separation between presentation and business logic.

# Lesson 2.6 - Template Inheritance

## Definition

Template Inheritance allows multiple templates to share a common layout while defining their own unique content.

## Why Template Inheritance?

- Eliminates duplicate HTML.
- Improves maintainability.
- Keeps layouts consistent.
- Makes updates faster.

## `base.html`

`base.html` stores the reusable layout shared by multiple pages.

Typical content includes:

- `<html>`
- `<head>`
- Navigation Bar
- Footer
- CSS Links
- JavaScript Links

## Template Block

```html
{% block content %}

{% endblock %}
```

A block is a placeholder that child templates replace with their own content.

## Extending a Template

```html
{% extends "blog/base.html" %}
```

This tells Django to use `base.html` as the parent layout.

## Child Template

```html
{% extends "blog/base.html" %}

{% block content %}

<h1>Home Page</h1>

{% endblock %}
```

Only the page-specific content is written.

## Internal Workflow

Browser → HTTP Request → Project `urls.py` → App `urls.py` → View → Context → `render("blog/home.html")` → Open Child Template → Load `base.html` → Replace Blocks → Generate Final HTML → Create `HttpResponse` → Browser

## Important Points

- `base.html` contains reusable layout.
- Child templates contain only unique content.
- `{% extends %}` creates the parent-child relationship.
- `{% block %}` defines replaceable sections.

## Common Mistakes

❌ Rewriting `<html>`, `<head>`, and `<body>` in child templates.

✔ Keep them only in `base.html`.

---

❌ Forgetting `{% extends %}`.

✔ Every child template should extend the appropriate parent template.

## Interview Questions

1. What is Template Inheritance?
2. Why do we use `base.html`?
3. What is the purpose of `{% extends %}`?
4. What is the purpose of `{% block %}`?
5. How does Template Inheritance improve maintainability?

## Summary

Template Inheritance allows Django templates to reuse a common layout through `base.html`. Child templates extend the parent template and replace predefined blocks with page-specific content, reducing duplication and improving maintainability.

# Lesson 2.7 - Mini Project

## Objective

Build a professional multi-page Django website by combining:

- Templates
- render()
- Context
- Django Template Language (DTL)
- Template Tags
- Template Inheritance

## Project Structure

blog/
├── templates/
│   └── blog/
│       ├── base.html
│       ├── home.html
│       ├── about.html
│       └── contact.html

## Workflow

Browser
→ HTTP Request
→ Project urls.py
→ include()
→ App urls.py
→ View
→ Context Dictionary
→ render()
→ Child Template
→ extends
→ Base Template
→ Replace Blocks
→ Process DTL
→ Generate Final HTML
→ Create HttpResponse
→ Browser

## Concepts Used

- render()
- Context
- Variables
- Filters
- if
- for
- empty
- Template Inheritance

## Important Points

- base.html contains reusable layout.
- Child templates contain page-specific content.
- Context provides dynamic data.
- DTL displays and formats data.
- Template Tags add presentation logic.

## Summary

Day 2 combined Django's template system into a complete workflow. A request is routed to a View, which prepares Context data, renders a child template, inherits the layout from base.html, processes DTL, generates the final HTML, and returns an HttpResponse to the browser.    