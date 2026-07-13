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

# Module 3.1 - Introduction to Databases, Models & ORM

## Definition

A Database is an organized collection of data that stores information permanently.

A Model is a Python class that defines the structure of a database table.

ORM (Object Relational Mapper) translates Python code into SQL and converts database results back into Python objects.

## Why Databases?

- Variables are temporary.
- Data disappears when the program ends.
- Databases store information permanently.

## Database Terminology

| Term | Meaning |
|------|---------|
| Database | Collection of organized data |
| Table | Stores similar records |
| Row (Record) | One complete entry |
| Column (Field) | One attribute of a record |

## Model

```python
class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
```

A Model defines the blueprint of a database table.

## ORM

```python
Pet.objects.all()
```

Django ORM converts this Python code into SQL automatically.

## Internal Execution

View → Model → ORM → SQL → Database → SQL Result → ORM → Python Objects → View → Context → render() → Template → Browser

## CRUD Operations

- Create → Add data
- Read → Retrieve data
- Update → Modify data
- Delete → Remove data

## Important Points

- Models define structure.
- Databases store data.
- ORM connects Python and SQL.
- Variables are temporary; databases are permanent.

## Common Mistakes

❌ Thinking Models store data.

✔ Models only define the table structure.

---

❌ Thinking ORM stores data.

✔ ORM translates between Python and SQL.

## Interview Questions

1. What is a Database?
2. What is a Model?
3. What is ORM?
4. Why does Django use Models?
5. Why is ORM useful?
6. Explain the relationship between Models, ORM, and the Database.

## Summary

Models define the database structure, ORM translates Python operations into SQL, and the database stores information permanently. Together they allow Django developers to work with databases using Python instead of writing raw SQL.

# Module 3.2 - Creating Your First Model

## Definition

A Django Model is a Python class that defines the structure of a database table.

## Model Location

Every Django app contains a `models.py` file where Models are created.

## Basic Model

```python
from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
```

## Components

| Component | Purpose |
|----------|---------|
| `class Pet` | Defines the Model |
| `models.Model` | Gives the class Django Model capabilities |
| `CharField` | Stores short text |
| `IntegerField` | Stores whole numbers |

## Why Inherit from `models.Model`?

Inheritance gives the class:

- ORM integration
- Database support
- Query methods
- Automatic ID field
- Migration support
- Save/Delete functionality

## Internal Workflow

Developer → Model Class → Django Reads Fields → Creates Model Metadata → Waits for Migration

## Important Points

- Models define structure, not data.
- Every field becomes a database column.
- Django automatically creates an `id` field.
- Choose field types carefully to match the data.

## Common Mistakes

❌ Thinking a Model immediately creates a table.

✔ A Model only defines the blueprint. Migrations create the table.

---

❌ Using `CharField` for numeric values.

✔ Use `IntegerField` or another numeric field when appropriate.

## Interview Questions

1. What is a Django Model?
2. Why do Models inherit from `models.Model`?
3. What is a Field?
4. Why do we use `CharField(max_length=...)`?
5. Why is choosing the correct field type important?

## Summary

A Model is a Python blueprint that describes the structure of a database table. Fields define columns, inheritance gives Django-specific database functionality, and the Model is later converted into a real table through migrations.

# Module 3.3 - Migrations

## Definition

A Migration is a set of instructions that tells Django how to create or modify database tables based on changes made to Models.

## Why Migrations?

- Safely update database structure.
- Prevent accidental data loss.
- Keep database schema versioned.
- Allow teams to share database changes.

## `makemigrations`

```bash
python manage.py makemigrations
```

Creates migration files by comparing the current Models with the previous state.

**Does not modify the database.**

## `migrate`

```bash
python manage.py migrate
```

Executes pending migration files and updates the database schema.

## Migration Folder

Example:

```text
migrations/
│
├── __init__.py
├── 0001_initial.py
├── 0002_add_phone.py
```

Each file records one database change.

## Internal Workflow

Developer → Edit Model → Save → `makemigrations` → Migration File → `migrate` → Database Updated

## Important Points

- Models define structure.
- Migration files record changes.
- `migrate` applies those changes.
- Database updates only after `migrate`.

## Common Mistakes

❌ Editing Models without creating migrations.

✔ Run `makemigrations`.

---

❌ Creating migrations but forgetting `migrate`.

✔ Apply pending migrations.

---

❌ Deleting migration files manually.

✔ Only do so if you fully understand the migration history.

## Interview Questions

1. What is a Migration?
2. Why are `makemigrations` and `migrate` separate commands?
3. What is stored in the `migrations` folder?
4. Why doesn't Django update the database automatically?
5. What happens if you forget to run `migrate`?

## Summary

Migrations safely translate Model changes into database schema changes. `makemigrations` creates migration instructions, while `migrate` executes them to update the database.

# Module 3.4 - Django Admin & Superuser

## Definition

Django Admin is Django's built-in web interface that allows authorized administrators to manage database records.

A Superuser is an administrator with full permissions.

## Create a Superuser

```bash
python manage.py createsuperuser
```

After entering a username, email, and password, Django creates an administrator account.

## Registering a Model

```python
from django.contrib import admin
from .models import Pet

admin.site.register(Pet)
```

Only registered Models appear in the Admin Panel.

## Internal Workflow

Developer → Model → Migration → Database → Register Model → Admin Panel → ORM → Database

## Why Register Models?

- Prevent accidental exposure of sensitive data.
- Give developers control over what appears in the Admin Panel.

## Important Points

- Django Admin is built into every Django project.
- A Superuser has complete administrative privileges.
- Models must be registered before they appear in the Admin Panel.
- The Admin Panel communicates with the database through Django's ORM.

## Common Mistakes

❌ Creating a Superuser before running migrations.

✔ Run migrations first.

---

❌ Forgetting to register a Model.

✔ Use `admin.site.register(ModelName)`.

---

❌ Giving unnecessary Superuser access.

✔ Follow the Principle of Least Privilege (users should have only the permissions they need).

## Interview Questions

1. What is Django Admin?
2. What is a Superuser?
3. Why must Models be registered?
4. How does Django Admin communicate with the database?
5. Why shouldn't every employee be a Superuser?

## Summary

Django Admin provides a ready-made administration interface for managing database records. Superusers can access the Admin Panel, and registered Models become available for CRUD operations without requiring custom HTML pages.

# Module 3.5 - Adding Data Through Django Admin

## Definition

A Record (Row) is one complete entry inside a database table.

Django Admin allows administrators to perform CRUD operations on database records through a web interface.

## Example

Pet Table

| ID | Name | Species | Age |
|----|------|----------|-----|
| 1 | Bruno | Dog | 3 |
| 2 | Luna | Cat | 2 |

Each row is one Record.

## Save Workflow

Browser
→ Admin Form
→ Validate Input
→ Create Model Object
→ ORM
→ Generate SQL
→ Database
→ Save Record
→ Success Response
→ Browser

## CRUD Operations

- Create → Add a new record.
- Read → View existing records.
- Update → Modify an existing record.
- Delete → Remove a record.

## Important Points

- Models define the table.
- Records store actual data.
- Django Admin uses the ORM internally.
- IDs are generated automatically and uniquely.

## Common Mistakes

❌ Assuming Admin directly writes SQL.

✔ Admin uses the ORM to generate SQL.

---

❌ Thinking visitors use Django Admin.

✔ Django Admin is for authorized administrators only.

## Interview Questions

1. What is a Record?
2. Difference between a Model and a Record?
3. What happens when Save is clicked?
4. Why are IDs automatically generated?
5. Why is Django Admin useful during development?

## Summary

Django Admin allows administrators to create, read, update, and delete database records without writing SQL. The ORM translates Model operations into SQL, while the database stores the actual records.

# Module 3.6 - Django ORM: Retrieving Data

## Definition

A Query is a request for data.

A QuerySet is a collection of Model objects returned by the Django ORM.

## Retrieve All Records

```python
from .models import Pet

pets = Pet.objects.all()
```

## Components

| Component | Purpose |
|----------|---------|
| `Pet` | Django Model representing the database table |
| `objects` | Default manager used to interact with Model records |
| `.all()` | Retrieves every record from the table |

## Internal Workflow

Browser
→ Request
→ View
→ `Pet.objects.all()`
→ ORM
→ SQL Query
→ Database
→ QuerySet
→ Context
→ render()
→ Template
→ Browser

## SQL Equivalent

```sql
SELECT * FROM Pet;
```

The ORM generates this SQL automatically.

## Important Points

- `.all()` returns a QuerySet, not a single object.
- A QuerySet contains Model objects.
- The ORM converts database rows into Python objects.
- Use the ORM instead of writing raw SQL for most applications.

## Common Mistakes

❌ Assuming `.all()` returns one record.

✔ It returns a QuerySet containing all matching records.

---

❌ Confusing the Model with the database table.

✔ The Model represents the table; the ORM works through the Model.

## Interview Questions

1. What is a Query?
2. What is a QuerySet?
3. What is the purpose of `objects`?
4. What does `.all()` return?
5. Why is the ORM preferred over raw SQL?

## Summary

The Django ORM retrieves database records as Python objects. `Pet.objects.all()` returns a QuerySet containing every record in the `Pet` table, allowing Views to pass dynamic data to Templates without writing SQL.

# Module 3.7 - Displaying Database Data

## Definition

A QuerySet retrieved by the ORM is passed through Context to a Template, where Django Template Language (DTL) displays the data as HTML.

## View Example

```python
from django.shortcuts import render
from .models import Pet

def home(request):
    pets = Pet.objects.all()

    return render(
        request,
        "blog/home.html",
        {
            "pets": pets
        }
    )
```

## Template Example

```html
<h1>Pet List</h1>

{% if pets %}

    {% for pet in pets %}

        <h3>{{ pet.name }}</h3>
        <p>Species: {{ pet.species }}</p>
        <p>Age: {{ pet.age }}</p>

    {% endfor %}

{% else %}

    <h3>No pets available.</h3>

{% endif %}
```

## Internal Workflow

Browser
→ Request
→ View
→ ORM
→ SQL
→ Database
→ QuerySet
→ Context
→ render()
→ Template
→ Generated HTML
→ Browser

## Important Points

- `.all()` returns a QuerySet.
- QuerySets contain Model objects.
- Context carries the QuerySet to the Template.
- `{% for %}` loops over QuerySets.
- `{{ }}` displays object fields.

## Common Mistakes

❌ Using `{{ pets.name }}`.

✔ Use `{{ pet.name }}` inside the loop.

---

❌ Forgetting `{% endfor %}`.

✔ Every loop must be closed.

---

❌ Writing Python syntax inside DTL.

✔ DTL has its own syntax.

## Interview Questions

1. What is a QuerySet?
2. How does a View send data to a Template?
3. Why do we use `{% for %}`?
4. Why can't we access `pets.name`?
5. Explain the complete request lifecycle from database to browser.

## Summary

The View retrieves records using the ORM, stores them in Context, and passes them to the Template. Django Template Language loops through the QuerySet and generates dynamic HTML that is sent back to the Browser. 

# Module 3.8 - Mini Project: Pet Directory

## Project Goal

Build a complete Django application that retrieves Pet records from the database and displays them dynamically in a web page.

## Complete Django Pipeline

Browser
→ Request
→ Project URLs
→ App URLs
→ View
→ ORM
→ Database
→ QuerySet
→ Context
→ render()
→ Template
→ Generated HTML
→ Browser

## Components Used

- Model (`Pet`)
- Migrations
- Django Admin
- ORM (`Pet.objects.all()`)
- Context
- Template (`{% for %}`)
- DTL (`{{ }}`)

## Design Principles

- Single Responsibility Principle (SRP)
- Separation of Concerns
- MVT Architecture

## Summary

This project combines every concept learned in Days 1–3 into one complete request lifecycle, demonstrating how Django routes a request, retrieves data from the database, and generates dynamic HTML for the browser.

# Module 4.1 - Filtering Data using filter()

---

# Learning Objectives

After completing this module you should be able to:

- Understand why filter() exists.
- Differentiate between all() and filter().
- Retrieve only matching records.
- Understand how ORM generates SQL.
- Explain why filtering should happen inside the database.
- Explain the performance benefits of filtering.

---

# Core Concepts

## What is filter()?

filter() is an ORM method used to retrieve only those records that satisfy one or more conditions.

Unlike all(), it does not retrieve unnecessary records.

It always returns a QuerySet.

---

# Why was filter() introduced?

Imagine a database containing 20 lakh client records.

A manager asks:

"Show me only pending cases."

Using

Client.objects.all()

would retrieve every client before filtering.

This wastes:

- CPU
- RAM
- Network bandwidth
- Time

Instead,

Client.objects.filter(status="Pending")

asks the database to perform the filtering.

---

# Syntax

## Retrieve Dogs

```python
Pet.objects.filter(species="Dog")
```

---

## Multiple Conditions

```python
Pet.objects.filter(
    species="Dog",
    age=2
)
```

Meaning

Species = Dog

AND

Age = 2

---

# Internal Workflow

Browser
↓
Request
↓
View
↓
Pet.objects.filter()
↓
ORM
↓
Generate SQL
↓
Database
↓
Filtered Records
↓
ORM
↓
Filtered QuerySet
↓
Context
↓
render()
↓
Template
↓
Browser

---

# SQL Equivalent

Python

```python
Pet.objects.filter(species="Dog")
```

Equivalent SQL

```sql
SELECT *
FROM Pet
WHERE species='Dog';
```

The developer never writes SQL manually.

The ORM generates it automatically.

---

# all() vs filter()

| all() | filter() |
|-------|----------|
| Retrieves every record | Retrieves matching records only |
| Returns QuerySet | Returns QuerySet |
| Can waste resources | More efficient |
| Used when every record is needed | Used when only specific records are needed |

---

# Real-world Example

Client Record Management System

Database

Rahul - Pending

Priya - Completed

Amit - Pending

Neha - Completed

Requirement

Show only pending clients.

Correct Query

```python
Client.objects.filter(status="Pending")
```

Returned QuerySet

Rahul

Amit

---

# Why Database Filtering is Better

Instead of

Database
↓
All Records
↓
Python
↓
Filtering

Use

Database
↓
Filtering
↓
Required Records
↓
Python

This reduces:

- CPU usage
- Memory usage
- Processing time
- Browser loading time
- Network bandwidth

---

# Common Mistakes

❌ Using all() then filtering in Python.

```python
pets = Pet.objects.all()

for pet in pets:
    if pet.species == "Dog":
        ...
```

✔ Correct

```python
Pet.objects.filter(species="Dog")
```

---

❌ Assuming filter() returns one object.

✔ It always returns a QuerySet.

---

❌ Assuming filter() changes the database.

✔ filter() only retrieves data.

---

# Summary

filter() retrieves only the records that satisfy one or more conditions.

It returns a QuerySet.

The ORM converts filter() into an SQL WHERE clause.

Filtering inside the database is faster, scalable and memory efficient than retrieving every record and filtering in Python.

---

# Interview Questions

1. What is filter()?
2. Why is filter() preferred over all()?
3. What does filter() return?
4. Does filter() modify the database?
5. Explain the SQL generated by filter().
6. Explain the complete execution of filter().
7. Why should filtering happen in the database instead of Python?

---

# Key Takeaways

✓ filter() always returns a QuerySet.

✓ QuerySet contains only matching Model objects.

✓ The ORM converts filter() into SQL.

✓ Let the database perform filtering.

✓ Avoid retrieving unnecessary records.

✓ Database filtering improves scalability and performance.

# Module 4.2 - Retrieving a Single Record using get()

---

# Learning Objectives

After completing this module you should be able to:

- Understand the purpose of get().
- Differentiate between get() and filter().
- Know when get() should be used.
- Understand the exceptions raised by get().
- Retrieve a single Model object for detail pages.

---

# Core Concepts

## What is get()?

get() is an ORM method used to retrieve exactly one record from the database.

Unlike filter(), it returns a single Model object instead of a QuerySet.

---

# Why was get() introduced?

Many applications need exactly one object.

Examples:

- Client Details
- Employee Profile
- Product Page
- Blog Post
- User Profile

Using get() clearly expresses the intent that only one record is expected.

---

# Syntax

## Retrieve by ID

```python
Pet.objects.get(id=1)
```

## Retrieve by Name

```python
Pet.objects.get(name="Bruno")
```

(Only use this if the field is guaranteed to be unique.)

---

# Internal Workflow

Browser
→ Request
→ View
→ Pet.objects.get(id=1)
→ ORM
→ Generate SQL
→ Database
→ Single Row
→ ORM
→ Model Object
→ Context
→ render()
→ Template
→ Browser

---

# SQL Equivalent

Python

```python
Pet.objects.get(id=1)
```

Equivalent SQL

```sql
SELECT *
FROM Pet
WHERE id=1;
```

---

# get() vs filter()

| get() | filter() |
|--------|-----------|
| Returns one Model object | Returns a QuerySet |
| Expects exactly one record | Can return zero, one or many |
| Raises exceptions if expectations are not met | Returns an empty QuerySet if nothing matches |
| Best for detail pages | Best for lists and searches |

---

# Exceptions

## DoesNotExist

Raised when no matching record exists.

Example:

```python
Pet.objects.get(id=100)
```

if ID 100 doesn't exist.

---

## MultipleObjectsReturned

Raised when more than one record matches.

Example:

```python
Pet.objects.get(species="Dog")
```

if multiple Dogs exist.

---

# Real-world Example

CRM System

Manager opens:

/clients/25/

Use:

```python
Client.objects.get(id=25)
```

This retrieves one Client object for the detail page.

---

# Common Mistakes

❌ Using get() for non-unique fields.

❌ Assuming get() returns a QuerySet.

❌ Using a for loop after get().

❌ Forgetting that get() raises exceptions.

---

# Summary

get() retrieves exactly one Model object. It is ideal for detail pages and unique lookups. Unlike filter(), it raises exceptions when no record or multiple records are found.

---

# Interview Questions

1. What is get()?
2. What does get() return?
3. Difference between get() and filter()?
4. What is DoesNotExist?
5. What is MultipleObjectsReturned?
6. When should get() be used?

---

# Key Takeaways

✓ get() returns one Model object.

✓ filter() returns a QuerySet.

✓ Use get() when exactly one record is expected.

✓ get() may raise DoesNotExist or MultipleObjectsReturned.

✓ Choosing get() improves readability and clearly expresses intent.

# ==========================================================
# Module 4.3 - Ordering Data using order_by()
# ==========================================================

# Learning Objectives

After completing this module you should be able to:

• Understand the purpose of order_by().
• Sort records in ascending and descending order.
• Sort records using multiple fields.
• Combine filter() and order_by().
• Understand how ORM generates SQL ORDER BY queries.
• Explain why sorting should happen inside the database.
• Understand performance benefits of database sorting.

==========================================================

# The Four Fundamental Questions

## What is order_by()?

order_by() is an ORM method used to sort the retrieved records based on one or more fields.

It never modifies the database.

It only changes the order in which records are returned.

It returns an Ordered QuerySet.

----------------------------------------------------------

## Why was order_by() introduced?

Databases do not always return records in the order users expect.

Users usually want data sorted such as:

• Alphabetically
• Latest First
• Oldest First
• Highest Marks
• Lowest Price
• Nearest Deadline

Instead of manually sorting records in Python, Django allows the database to perform sorting efficiently.

----------------------------------------------------------

## What problem does order_by() solve?

Without order_by():

Database
↓

Returns records

↓

Python manually sorts them

↓

More CPU usage
More Memory usage
More Development Time

With order_by():

Database
↓

Sorts records

↓

Returns ordered records

↓

Python simply displays them

This approach is:

✓ Faster
✓ Cleaner
✓ Scalable
✓ Memory Efficient

----------------------------------------------------------

## Where does it fit?

Browser
↓

Request

↓

View

↓

order_by()

↓

ORM

↓

Database

↓

Ordered QuerySet

↓

Context

↓

render()

↓

Template

↓

Browser

==========================================================

# Mental Model

Imagine a school teacher checking exam papers.

The principal says,

"Arrange students according to marks."

Would the teacher randomly distribute answer sheets?

No.

The teacher arranges them first.

95

↓

90

↓

88

↓

75

↓

60

Similarly,

order_by() arranges database records before sending them to Django.

==========================================================

# Core Concepts

order_by() performs sorting.

Sorting can be:

Ascending

or

Descending.

The database performs the sorting.

The ORM simply generates the SQL.

The returned data remains a QuerySet.

==========================================================

# Syntax

## Ascending Order

```python
Pet.objects.order_by("name")
```

Meaning:

Retrieve Pet records sorted alphabetically by name.

----------------------------------------------------------

## Descending Order

```python
Pet.objects.order_by("-age")
```

Meaning:

Retrieve Pet records sorted from highest age to lowest age.

----------------------------------------------------------

## Multiple Fields

```python
Pet.objects.order_by(
    "species",
    "name"
)
```

Meaning:

First sort by Species.

If Species is identical,

sort by Name.

----------------------------------------------------------

## Combining filter() and order_by()

```python
Pet.objects.filter(
    species="Dog"
).order_by("age")
```

Meaning:

Retrieve Dogs

↓

Sort them according to Age.

==========================================================

# Syntax Breakdown

Example

```python
Pet.objects.filter(
    species="Dog"
).order_by("age")
```

Breakdown

Pet
↓

Model

objects
↓

Default ORM Manager

filter()
↓

Retrieve matching records

species
↓

Field Name

"Dog"
↓

Condition Value

order_by()
↓

Sorting Method

"age"
↓

Sort according to Age

==========================================================

# Return Type

order_by() returns:

Ordered QuerySet

NOT

List

NOT

Tuple

NOT

Dictionary

==========================================================

# Internal Workflow

Browser

↓

Request

↓

View

↓

order_by()

↓

ORM

↓

Generate SQL

↓

Database

↓

Sort Records

↓

Return Ordered Rows

↓

ORM

↓

Ordered QuerySet

↓

Context

↓

render()

↓

Template

↓

Generated HTML

↓

Browser

==========================================================

# SQL Equivalent

Python

```python
Pet.objects.order_by("name")
```

SQL

```sql
SELECT *
FROM Pet
ORDER BY name ASC;
```

----------------------------------------------------------

Descending

Python

```python
Pet.objects.order_by("-age")
```

SQL

```sql
SELECT *
FROM Pet
ORDER BY age DESC;
```

==========================================================

# Examples

Example 1

```python
Pet.objects.order_by("name")
```

Alphabetical order.

----------------------------------------------------------

Example 2

```python
Pet.objects.order_by("-age")
```

Highest age first.

----------------------------------------------------------

Example 3

```python
Pet.objects.order_by(
    "species",
    "name"
)
```

Sort by Species.

Then Name.

----------------------------------------------------------

Example 4

```python
Pet.objects.filter(
    species="Dog"
).order_by("age")
```

Retrieve Dogs.

Sort according to Age.

==========================================================

# Real-world Business Example

Client Record Management System

Manager asks:

"Show Pending Clients sorted according to Deadline."

Correct ORM Query

```python
Client.objects.filter(
    status="Pending"
).order_by("deadline")
```

Benefits

✓ Important work appears first.

✓ Employees know which task has priority.

✓ Better productivity.

==========================================================

# Comparison Table

| all() | filter() | get() | order_by() |
|--------|----------|--------|------------|
| Retrieves all records | Retrieves matching records | Retrieves one record | Sorts retrieved records |
| Returns QuerySet | Returns QuerySet | Returns Model Object | Returns Ordered QuerySet |

==========================================================

# Common Mistakes

❌ Sorting manually in Python.

Instead,

✔ Use order_by().

----------------------------------------------------------

❌ Thinking order_by() changes the database.

It only changes retrieval order.

----------------------------------------------------------

❌ Forgetting '-' for descending order.

Ascending

```python
Pet.objects.order_by("age")
```

Descending

```python
Pet.objects.order_by("-age")
```

==========================================================

# Best Practices

✓ Let the database perform sorting.

✓ Combine filter() before order_by() whenever required.

✓ Use meaningful fields for sorting.

✓ Never manually sort database records in Python unless absolutely necessary.

==========================================================

# Performance Notes

Database sorting is:

• Faster

• Memory Efficient

• CPU Efficient

• Scalable

Python sorting:

• More Memory

• More CPU

• More Time

==========================================================

# Software Engineering Perspective

order_by() follows the principle:

Move work closer to the data.

Instead of:

Database

↓

Python Sorting

↓

Browser

Use:

Database Sorting

↓

Browser

This reduces workload on the application server.

==========================================================

# Summary

order_by() sorts retrieved records without modifying the database.

Ascending order is default.

Use "-" for descending order.

Multiple fields can be used.

Sorting should always be delegated to the database whenever possible.

==========================================================

# Interview Questions

1. What is order_by()?

2. What does it return?

3. Difference between ascending and descending?

4. Why should sorting happen in the database?

5. Explain SQL generated by order_by().

6. Can filter() and order_by() be combined?

7. Does order_by() modify the database?

==========================================================

# Key Takeaways

✓ order_by() sorts records.

✓ Default sorting is ascending.

✓ Prefix "-" for descending.

✓ Returns Ordered QuerySet.

✓ Database sorting is faster than Python sorting.

✓ Combine filter() and order_by() for efficient retrieval.

✓ order_by() never modifies the database.

# ==========================================================
# Module 4.4 - Excluding Records using exclude()
# ==========================================================

# Learning Objectives

After completing this module you should be able to:

• Understand the purpose of exclude().
• Understand why exclude() was introduced.
• Differentiate between filter() and exclude().
• Combine exclude() with filter() and order_by().
• Understand the SQL generated by exclude().
• Explain why exclusion should happen inside the database.
• Understand the performance benefits of database-side exclusion.

==========================================================

# The Four Fundamental Questions

## What is exclude()?

exclude() is an ORM method used to retrieve every record except those matching one or more specified conditions.

It returns a QuerySet.

It never modifies the database.

----------------------------------------------------------

## Why was exclude() introduced?

Sometimes it is easier to describe what data should NOT be retrieved.

Instead of writing complicated logic in Python after retrieving every record,

exclude() lets the database remove unwanted records before they reach the application.

----------------------------------------------------------

## What problem does exclude() solve?

Without exclude()

Database

↓

Returns every record

↓

Python removes unwanted records

↓

More CPU Usage

More Memory Usage

More Processing Time

With exclude()

Database

↓

Removes unwanted records

↓

Returns only required records

↓

Python simply displays them

Benefits

✓ Faster

✓ Cleaner

✓ Scalable

✓ Memory Efficient

----------------------------------------------------------

## Where does it fit?

Browser

↓

Request

↓

View

↓

exclude()

↓

ORM

↓

Generate SQL

↓

Database

↓

Remaining Rows

↓

ORM

↓

QuerySet (Model Objects)

↓

Context

↓

render()

↓

Template

↓

Browser

==========================================================

# Mental Model

Imagine a teacher preparing a class photograph.

The principal says,

"Everyone except Class 10 students should come."

The teacher simply does not call Class 10 students.

They are excluded before the photograph is taken.

Similarly,

exclude() removes unwanted records before they reach Django.

==========================================================

# Core Concepts

exclude() retrieves records that DO NOT satisfy the given condition.

It performs filtering inside the database.

The returned object is always a QuerySet.

The original database records remain unchanged.

==========================================================

# Syntax

## Exclude One Condition

```python
Pet.objects.exclude(species="Dog")
```

Meaning

Retrieve every Pet except Dogs.

----------------------------------------------------------

## Exclude Multiple Conditions

```python
Pet.objects.exclude(
    species="Dog",
    age=2
)
```

Meaning

Exclude records where both conditions match.

----------------------------------------------------------

## Combine filter() and exclude()

```python
Pet.objects.filter(
    species="Dog"
).exclude(age=1)
```

Meaning

Retrieve Dogs

↓

Exclude Dogs aged 1

↓

Return remaining Dogs.

----------------------------------------------------------

## Combine exclude() and order_by()

```python
Client.objects.exclude(
    status="Completed"
).order_by("deadline")
```

Meaning

Exclude completed clients

↓

Sort remaining clients by deadline.

==========================================================

# Syntax Breakdown

Example

```python
Pet.objects.exclude(species="Dog")
```

Breakdown

Pet

↓

Model

objects

↓

Default ORM Manager

exclude()

↓

Exclude matching records

species

↓

Field Name

"Dog"

↓

Condition Value

==========================================================

# Return Type

exclude() returns

QuerySet

NOT

Model Object

NOT

List

NOT

Dictionary

==========================================================

# Internal Workflow

Browser

↓

Request

↓

View

↓

exclude()

↓

ORM

↓

Generate SQL

↓

Database

↓

Remaining Rows

↓

ORM

↓

QuerySet (Model Objects)

↓

Context

↓

render()

↓

Template

↓

Generated HTML

↓

Browser

==========================================================

# SQL Equivalent

Python

```python
Pet.objects.exclude(species="Dog")
```

SQL

```sql
SELECT *
FROM Pet
WHERE NOT species='Dog';
```

----------------------------------------------------------

Python

```python
Client.objects.exclude(status="Completed")
```

SQL

```sql
SELECT *
FROM Client
WHERE NOT status='Completed';
```

==========================================================

# Examples

Example 1

```python
Pet.objects.exclude(species="Dog")
```

Returns

Cats

Rabbits

Birds

----------------------------------------------------------

Example 2

```python
Pet.objects.filter(
    species="Dog"
).exclude(age=1)
```

Returns

Dogs except one-year-old Dogs.

----------------------------------------------------------

Example 3

```python
Client.objects.exclude(
    status="Completed"
).order_by("deadline")
```

Returns

All active clients ordered by deadline.

==========================================================

# Real-world Business Example

Client Record Management System

Manager asks

"Show every client except completed cases."

Correct ORM Query

```python
Client.objects.exclude(
    status="Completed"
)
```

Benefits

✓ Cleaner dashboard

✓ Employees focus only on active work

✓ Better productivity

✓ Faster page loading

==========================================================

# Comparison Table

| filter() | exclude() |
|-----------|-----------|
| Includes matching records | Excludes matching records |
| Returns QuerySet | Returns QuerySet |
| SQL uses WHERE | SQL uses WHERE NOT |

==========================================================

# Common Mistakes

❌ Retrieving every record then removing unwanted records using Python.

✔ Use exclude().

----------------------------------------------------------

❌ Thinking exclude() deletes records.

✔ It only excludes them from the retrieved QuerySet.

----------------------------------------------------------

❌ Confusing filter() with exclude().

filter()

Returns matching records.

exclude()

Returns everything except matching records.

==========================================================

# Best Practices

✓ Let the database perform exclusion.

✓ Combine filter(), exclude() and order_by() when required.

✓ Avoid writing manual exclusion logic in Python.

✓ Keep ORM queries expressive and readable.

==========================================================

# Performance Notes

Database-side exclusion

✓ Lower CPU Usage

✓ Lower Memory Usage

✓ Better Scalability

✓ Better Performance

✓ Faster Response Time

Python-side exclusion

✗ Higher CPU Usage

✗ Higher Memory Usage

✗ More Processing

==========================================================

# Software Engineering Perspective

exclude() follows the principle:

Move work closer to the data.

Instead of retrieving unnecessary records and removing them in Python,

let the database exclude them before returning results.

==========================================================

# Summary

exclude() retrieves every record except those matching the specified condition.

It returns a QuerySet.

It generates SQL using WHERE NOT.

Database-side exclusion improves performance, scalability and maintainability.

==========================================================

# Interview Questions

1. What is exclude()?

2. What does exclude() return?

3. Difference between filter() and exclude()?

4. Does exclude() modify the database?

5. Explain the SQL generated by exclude().

6. Why should exclusion happen in the database?

7. Can exclude() be combined with filter() and order_by()?

==========================================================

# Key Takeaways

✓ exclude() returns a QuerySet.

✓ It retrieves records that DO NOT match the condition.

✓ SQL equivalent uses WHERE NOT.

✓ exclude() never modifies the database.

✓ Database-side exclusion is faster than Python-side exclusion.

✓ Combine filter(), exclude() and order_by() for powerful ORM queries.

# ==========================================================
# Module 4.6 - OneToOneField & ManyToManyField
# ==========================================================

## Learning Objectives

- Understand One-to-One relationships.
- Understand Many-to-Many relationships.
- Differentiate between OneToOneField, ForeignKey and ManyToManyField.
- Understand how Django stores Many-to-Many relationships.
- Choose the correct relationship for real-world applications.

---

## The Four Fundamental Questions

### What are OneToOneField and ManyToManyField?

They are Django model fields used to represent One-to-One and Many-to-Many relationships between models.

### Why were they introduced?

Not every relationship is One-to-Many. Different real-world situations require different relationship types.

### What problem do they solve?

They prevent data duplication and accurately model relationships between database tables.

### Where do they fit?

Browser → Request → View → Model Relationship → ORM → Database → ORM → Model Objects → Context → render() → Template → Browser

---

## Relationship Types

### One-to-One (1:1)

One record is connected to exactly one record.

Examples:
- User ↔ Profile
- Person ↔ Passport
- Employee ↔ ID Card

Django Field:

```python
models.OneToOneField()
```

---

### One-to-Many (1:M)

One record is connected to many records.

Examples:
- Lawyer → Clients
- Teacher → Students
- Author → Books

Django Field:

```python
models.ForeignKey()
```

---

### Many-to-Many (M:M)

Many records connect to many records.

Examples:
- Student ↔ Courses
- Doctor ↔ Hospitals
- Actor ↔ Movies

Django Field:

```python
models.ManyToManyField()
```

---

## Syntax

### OneToOneField

```python
user = models.OneToOneField(
    User,
    on_delete=models.CASCADE
)
```

Meaning:
Each Profile belongs to one User.

---

### ManyToManyField

```python
courses = models.ManyToManyField(Course)
```

Meaning:
A Student can join many Courses.
A Course can have many Students.

---

## Syntax Breakdown

### OneToOneField

- user → Field name
- OneToOneField → One-to-One relationship
- User → Related model
- on_delete → Action when related record is deleted
- CASCADE → Delete related record

### ManyToManyField

- courses → Field name
- ManyToManyField → Many-to-Many relationship
- Course → Related model

---

## Internal Workflow

Browser → Request → View → ORM → Database → Related Tables → ORM → Model Objects → Context → render() → Template → Browser

---

## How ManyToMany Works

Django automatically creates a hidden junction table.

Example:

Student Table

| ID | Name |
|----|------|
|1|Om|
|2|Rahul|

Course Table

| ID | Name |
|----|------|
|1|Python|
|2|Django|

Hidden Junction Table

| Student_ID | Course_ID |
|------------|-----------|
|1|1|
|1|2|
|2|2|

This table stores relationships between both models.

---

## Comparison

| Relationship | Django Field | Example |
|--------------|--------------|---------|
| One-to-One | OneToOneField | User ↔ Profile |
| One-to-Many | ForeignKey | Lawyer → Clients |
| Many-to-Many | ManyToManyField | Student ↔ Courses |

---

## Real-world CRM Example

Employee ↔ ID Card → OneToOneField

Lawyer → Clients → ForeignKey

Lawyer ↔ Specializations → ManyToManyField

---

## Common Mistakes

❌ Using ForeignKey for User ↔ Profile.

✔ Use OneToOneField.

---

❌ Using ForeignKey for Student ↔ Courses.

✔ Use ManyToManyField.

---

❌ Creating the junction table manually.

✔ Django creates it automatically.

---

## Best Practices

- Choose relationships based on business requirements.
- Avoid duplicate data.
- Let Django manage junction tables.
- Think about relationship cardinality before designing models.

---

## Software Engineering Perspective

Proper relationship design improves:

- Data Consistency
- Storage Efficiency
- Maintainability
- Scalability
- Database Normalization

---

## Summary

Django provides three relationship fields:

- OneToOneField → One-to-One
- ForeignKey → One-to-Many
- ManyToManyField → Many-to-Many

Choosing the correct relationship results in a cleaner, scalable and maintainable database design.

---

## Interview Questions

1. Difference between OneToOneField, ForeignKey and ManyToManyField.
2. Why does Django create a junction table?
3. Explain One-to-One with an example.
4. Explain Many-to-Many with an example.
5. When would you use ManyToManyField instead of ForeignKey?

---

## Key Takeaways

✓ OneToOneField represents One-to-One.

✓ ForeignKey represents One-to-Many.

✓ ManyToManyField represents Many-to-Many.

✓ Django automatically creates a junction table.

✓ Choose relationships according to business requirements.

# ==========================================================
# Module 4.7 - Database Design (CRMS Mini Project)
# ==========================================================

## Learning Objectives

- Understand database design.
- Identify entities and relationships.
- Design normalized databases.
- Apply ForeignKey, OneToOneField and ManyToManyField.
- Think before coding.

---

## The Four Fundamental Questions

### What is Database Design?

Planning what tables to create, what data each table stores, and how tables relate to each other.

### Why?

To reduce redundancy, improve consistency, scalability and maintainability.

### What problem does it solve?

Poor database design causes duplicated data, difficult updates and poor scalability.

### Workflow

Requirements → Identify Entities → Identify Relationships → Database Design → Models → ORM → Database

---

## Entity Identification

Real-world nouns usually become models.

Example:

- Lawyer
- Client
- Employee
- Document
- Specialization
- EmployeeIDCard

---

## Relationship Selection

| Models | Relationship | Django Field |
|---------|--------------|--------------|
| Lawyer → Client | One-to-Many | ForeignKey |
| Employee → Client | One-to-Many | ForeignKey |
| Client → Document | One-to-Many | ForeignKey |
| Employee ↔ ID Card | One-to-One | OneToOneField |
| Lawyer ↔ Specialization | Many-to-Many | ManyToManyField |

---

## CRM Database Structure

Lawyer
- Name
- Phone
- Email
- Specializations

Client
- Name
- Contact
- Lawyer
- Employee

Employee
- Name
- Phone
- ID Card

Document
- Title
- Client

EmployeeIDCard
- Card Number

Specialization
- Name

---

## Why This Design?

✓ No duplicate data

✓ Easy updates

✓ Better scalability

✓ Better consistency

✓ Lower storage usage

---

## Software Engineering Perspective

A good database design stores information once and connects tables using relationships instead of duplication.

---

## Summary

Database design starts before coding. Identify entities, define relationships, normalize data, then create Django models.

---

## Key Takeaways

✓ Requirements come before models.

✓ Nouns usually become models.

✓ Relationships connect models.

✓ Good design improves scalability and maintainability.

# ==========================================================
# Module 4.8 - Day 4 Grand Challenge & Revision
# ==========================================================

## Learning Objectives

- Revise ORM retrieval methods.
- Compare relationship types.
- Explain the complete request-to-response workflow.
- Apply database design principles.
- Think like a backend developer.

---

## ORM Retrieval Methods

| Method | Returns | Purpose |
|---------|----------|---------|
| all() | QuerySet | Retrieve all records |
| filter() | QuerySet | Retrieve matching records |
| get() | Model Object | Retrieve one record |
| exclude() | QuerySet | Exclude matching records |
| order_by() | Ordered QuerySet | Sort records |

---

## Relationship Types

| Django Field | Relationship | Example |
|--------------|--------------|---------|
| OneToOneField | One-to-One | Employee ↔ ID Card |
| ForeignKey | One-to-Many | Lawyer → Clients |
| ManyToManyField | Many-to-Many | Student ↔ Courses |

---

## Complete Workflow

Browser → Request → project/urls.py → include() → app/urls.py → View → ORM Query → ORM → SQL → Database → Database Rows → ORM → Model Object/QuerySet → Context → render() → Template → HttpResponse → Browser

---

## Database Design Process

Requirements → Identify Entities → Identify Relationships → Database Design → Models → ORM → Database

---

## Software Engineering Principles

✓ Normalize data.

✓ Avoid redundancy.

✓ Store relationships instead of duplicate information.

✓ Let the database handle filtering and sorting.

✓ Choose relationship types based on business rules.

---

## Summary

Day 4 focused on efficient data retrieval, relationship design, normalization, and scalable backend architecture.

---

## Key Takeaways

✓ ORM translates Python operations into SQL.

✓ QuerySet contains Model Objects.

✓ Use the correct relationship field for each business scenario.

✓ Good database design improves maintainability and scalability.

# ==========================================================
# Module 5.1 - Introduction to CRUD
# ==========================================================

## Learning Objectives

- Understand CRUD.
- Explain Create, Read, Update and Delete.
- Identify CRUD operations in real applications.
- Understand where CRUD fits in Django.

---

## CRUD

CRUD represents the four basic database operations.

| Letter | Meaning |
|---------|---------|
| C | Create |
| R | Read |
| U | Update |
| D | Delete |

Almost every database application performs these operations.

---

## The Four Fundamental Questions

### What is CRUD?

CRUD is the complete lifecycle of managing database records.

### Why?

Applications need to create, retrieve, modify and remove data.

### What problem does it solve?

CRUD makes applications interactive instead of read-only.

### Workflow

Browser → HTTP Request → URL → View → ORM → Database → ORM → Context → render() → Template → Browser

---

## CRUD Operations

### Create

Adds a new record.

Examples:

- Register User
- Add Client
- Create Product

---

### Read

Retrieves data.

Methods:

- all()
- filter()
- get()
- exclude()
- order_by()

---

### Update

Modifies existing records.

Example:

Change employee salary.

---

### Delete

Permanently removes records.

Example:

Delete duplicate client.

---

## CRUD in CRMS

| Operation | Example |
|-----------|---------|
| Create | Register Client |
| Read | View Client Details |
| Update | Correct Client Information |
| Delete | Remove Duplicate Client |

---

## Software Engineering Perspective

CRUD distributes responsibilities:

- Browser → User interaction
- View → Business logic
- ORM → Database communication
- Database → Persistent storage

---

## Summary

CRUD forms the foundation of every database-driven application.

---

## Key Takeaways

✓ CRUD = Create, Read, Update, Delete.

✓ Read operations were covered in Days 3–4.

✓ CRUD makes applications interactive.

✓ ORM performs CRUD operations on the database.

# ==========================================================
# Module 5.2 - Creating Records (create() & save())
# ==========================================================

## Learning Objectives

- Create database records using Django ORM.
- Understand create() and save().
- Differentiate between both methods.
- Understand record creation workflow.

---

## The Four Fundamental Questions

### What are create() and save()?

Both are ORM techniques used to insert records into the database.

### Why?

Different applications require different levels of flexibility.

### What problem do they solve?

They eliminate the need to write raw SQL INSERT statements.

### Workflow

Browser → HTTP Request → URL → View → create()/save() → ORM → SQL INSERT → Database → ORM → Model Object → Context → render() → Template → Browser

---

## create()

Creates a model object and immediately saves it.

Syntax:

```python
Model.objects.create(field=value)
```

Example:

```python
Client.objects.create(
    name="Rahul",
    phone="9876543210"
)
```

Use when all required data is already available.

---

## save()

Creates a model object first.

Nothing is stored until save() is called.

Syntax:

```python
client = Client(
    name="Rahul",
    phone="9876543210"
)

client.save()
```

Use when data needs validation or modification before saving.

---

## Comparison

| create() | save() |
|-----------|---------|
| One-step operation | Two-step operation |
| Saves immediately | Saves only after save() |
| Less flexible | More flexible |
| Best for simple inserts | Best for multi-step workflows |

---

## SQL Equivalent

```sql
INSERT INTO Client(...)
VALUES(...);
```

The ORM generates this automatically.

---

## Common Mistakes

❌ Assuming `Client(...)` inserts into the database.

✔ Only `save()` writes to the database.

---

## Software Engineering Perspective

Use create() for simple workflows.

Use save() when review, validation or editing is required before insertion.

---

## Key Takeaways

✓ create() inserts immediately.

✓ save() provides flexibility.

✓ Creating an object is not the same as saving it.

✓ ORM converts Python into SQL INSERT statements.

# ==========================================================
# Module 5.3 - Updating Records (save())
# ==========================================================

## Learning Objectives

- Update existing database records.
- Retrieve records using get().
- Modify fields.
- Save updated records.
- Understand INSERT vs UPDATE behavior.

---

## The Four Fundamental Questions

### What is Updating?

Updating modifies an existing database record without creating a new one.

### Why?

To keep data accurate while avoiding duplicate records.

### What problem does it solve?

Maintains data consistency, relationships and database integrity.

### Workflow

Browser → HTTP Request → URL → View → get() → ORM → SQL SELECT → Database → Model Object → Modify Field → save() → ORM → SQL UPDATE → Database → Context → render() → Template → Browser

---

## Updating Records

Step 1

Retrieve object.

```python
client = Client.objects.get(id=1)
```

---

Step 2

Modify field.

```python
client.phone = "9999999999"
```

---

Step 3

Save.

```python
client.save()
```

---

## SQL Equivalent

```sql
UPDATE Client
SET phone='9999999999'
WHERE id=1;
```

---

## Create vs Update

| Create | Update |
|---------|---------|
| INSERT | UPDATE |
| New record | Existing record |
| create() / save() | get() + save() |

---

## Common Mistakes

❌ Creating duplicate records instead of updating.

❌ Forgetting save().

❌ Updating the wrong object.

---

## Software Engineering Perspective

Updating preserves:

- Data consistency
- Relationships
- Scalability
- Maintainability

---

## Key Takeaways

✓ Retrieve first.

✓ Modify fields.

✓ save() writes changes.

✓ save() performs UPDATE for existing objects.

# ==========================================================
# Module 5.4 - Deleting Records with delete()
# ==========================================================

## Learning Objectives
- Delete existing database records.
- Understand delete().
- Understand SQL DELETE.
- Understand CASCADE deletion.
- Differentiate hard deletion from soft deletion.

---

## The Four Fundamental Questions

### What is delete()?
A Django ORM method used to permanently remove database records.

### Why?
To remove duplicate, incorrect, test or unnecessary records.

### What problem does it solve?
It prevents unwanted records from remaining permanently in the database.

### Workflow
Browser → HTTP Request → URL → View → get() → ORM → SQL SELECT → Database → Model Object → delete() → ORM → SQL DELETE → Database → Response → Browser

---

## Deleting One Record

```python
client = Client.objects.get(id=5)
client.delete()
```

Step 1: Retrieve the model object.
Step 2: Permanently delete it.

---

## SQL Equivalent

```sql
DELETE FROM Client
WHERE id=5;
```

---

## Update vs Delete

| Update | Delete |
|---|---|
| Modifies existing record | Removes existing record |
| get() + modify + save() | get() + delete() |
| SQL UPDATE | SQL DELETE |
| Record remains | Record is removed |

---

## CASCADE

```python
lawyer = models.ForeignKey(
    Lawyer,
    on_delete=models.CASCADE
)
```

If the parent Lawyer is deleted, related Client records are also deleted.

---

## Hard Delete vs Soft Delete

### Hard Delete
Record is permanently removed.

### Soft Delete
Record remains but is marked inactive.

Example:

```python
is_active = models.BooleanField(default=True)
```

Soft deletion is useful when historical data, auditing or restoration is important.

---

## Important Correction

get() is not mandatory for every deletion.

Single object:

```python
client = Client.objects.get(id=5)
client.delete()
```

Multiple matching objects:

```python
Client.objects.filter(status="Inactive").delete()
```

Django deletes only the explicitly targeted object or QuerySet.

---

## Software Engineering Perspective

Before deleting data, consider:

- Data integrity
- Maintainability
- Reliability
- Auditability
- Business requirements
- Reversibility
- Related records

---

## Key Takeaways

✓ delete() permanently removes records.

✓ SQL DELETE is generated internally.

✓ CASCADE may delete related child records.

✓ Use Update for corrections.

✓ Consider soft deletion when historical data must be preserved.

# ==========================================================
# Module 5.5 - Introduction to Django Forms & ModelForm
# ==========================================================

## Purpose of Forms
Forms provide users with an interface to enter and submit data without accessing Python code.

## Core Workflow
User → Form → HTTP Request → View → Validation → Model Instance → ORM → Database

## Django Form Types

| Type | Purpose |
|---|---|
| forms.Form | General-purpose form with manually defined fields |
| forms.ModelForm | Form connected to a model |

## ModelForm
A ModelForm can:
- Generate form fields from model fields.
- Receive submitted data.
- Validate data.
- Display errors.
- Create or update model instances.

## forms.py
Usually created manually inside the Django app:

app/
├── forms.py
├── models.py
├── views.py
└── urls.py

## GET Request
Used to request a resource/page.

Form example:
GET → View → Empty Form → Template → Browser

## POST Request
Used to submit data to the server.

Form example:
POST → View → Bound ModelForm → Validation

If valid:
Valid Form → save() → ORM → SQL INSERT/UPDATE → Database

If invalid:
Invalid Form → Errors → Template → Browser

## Component Responsibilities
Model → Defines database structure.
ModelForm → Handles user input and validation for model data.
View → Controls application workflow.
Template → Presents the interface.
ORM → Translates Python/model operations into database queries.
Database → Stores data persistently.

## Form vs ModelForm

| Form | ModelForm |
|---|---|
| General-purpose | Connected to model |
| Fields usually defined manually | Can derive fields from model |
| Supports validation | Supports validation |
| Not automatically tied to model saving | Can create/update model instances |

## Key Takeaways
✓ Forms allow users to submit data.
✓ ModelForm connects form logic to a model.
✓ GET usually retrieves the form.
✓ POST submits form data.
✓ Validation happens before invalid data is saved.
✓ The view controls the workflow.

# ==========================================================
# Module 5.6 - Building and Processing a ModelForm
# ==========================================================

## Learning Objectives
- Create a ModelForm.
- Understand forms.py.
- Understand ModelForm inheritance.
- Understand class Meta, model and fields.
- Handle GET and POST requests.
- Understand request.POST.
- Understand bound and unbound forms.
- Validate submitted data with is_valid().
- Save valid data with form.save().
- Display forms in templates.
- Understand CSRF protection.
- Understand POST-Redirect-GET.

## Complete Architecture

models.py → forms.py → views.py → urls.py → template → user

Form submission:

User → POST Request → View → ModelForm → Validation → Model Instance → ORM → Database

## Model

```python
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
```

Model = Blueprint of database table.
Model Object = One database record/row.

## Why ModelForm?

Without a form, the developer manually creates records:

```python
Client.objects.create(
    name="Rahul",
    email="rahul@example.com",
    phone="9876543210"
)
```

Real users need an interface to submit their own data.

## forms.py

Usually created manually inside the Django app:

```text
blog/
├── admin.py
├── apps.py
├── forms.py
├── models.py
├── urls.py
└── views.py
```

Purpose:
Define form classes and their validation/configuration.

The template displays the form.
The view controls the workflow.
The ModelForm handles model-based input and validation.

## Complete ModelForm

```python
from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["name", "email", "phone"]
```

## from django import forms

```python
from django import forms
```

Imports Django's forms system.

Examples of available capabilities:

```text
forms.Form
forms.ModelForm
forms.CharField
forms.EmailField
```

## from .models import Client

```python
from .models import Client
```

The `.` means the current Django app.

```text
. → Current App → models.py → Client
```

Client is imported because ClientForm needs to know which model it is connected to.

## ModelForm Inheritance

```python
class ClientForm(forms.ModelForm):
```

ClientForm inherits ModelForm capabilities.

These include:
- Generating fields from a model.
- Receiving submitted data.
- Validation.
- Storing validation errors.
- Creating model instances.
- Updating model instances.

Mental model:

```text
ClientForm → inherits from → forms.ModelForm → receives ModelForm capabilities
```

Similar to:

```python
class Pet(models.Model):
```

Pet inherits model capabilities.

## class Meta

```python
class Meta:
```

Meta is the ModelForm's configuration or instruction sheet.

It answers:

```text
Which model should this form use?
Which model fields should this form expose?
```

Mental model:

```text
ModelForm = Worker
Meta = Instructions for worker
```

## model = Client

```python
model = Client
```

Connects ClientForm to the Client model.

Django can inspect the model fields and generate corresponding form fields.

```text
models.CharField → Text Input
models.EmailField → Email Input
models.BooleanField → Checkbox
```

## fields

```python
fields = ["name", "email", "phone"]
```

Controls which model fields are exposed through the form.

Example model:

```text
name
email
phone
salary
internal_notes
```

Form:

```python
fields = ["name", "email", "phone"]
```

User sees only:
- name
- email
- phone

Explicit field selection improves clarity and helps prevent unnecessary exposure of internal fields.

## fields = "__all__"

```python
fields = "__all__"
```

Includes all editable model fields.

Use carefully because internal or sensitive fields could become exposed.

Explicit field lists are usually safer:

```python
fields = ["name", "email", "phone"]
```

Important:
Hiding a field from a form alone is not complete security. Backend permissions and business rules must also be enforced.

## Complete View

```python
from django.shortcuts import render, redirect
from .forms import ClientForm

def add_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("add_client")
    else:
        form = ClientForm()

    return render(
        request,
        "blog/add_client.html",
        {"form": form}
    )
```

## def add_client(request)

```python
def add_client(request):
```

Creates a view named add_client.

Django automatically passes the HTTP request object to the view.

## request.method

```python
if request.method == "POST":
```

Checks the HTTP method used by the request.

```text
GET → Request/retrieve the page or empty form.
POST → Submit data to the server.
```

## GET Request

When the user first visits the page:

```python
else:
    form = ClientForm()
```

`ClientForm()` contains no submitted data.

Therefore, it is an unbound form.

```text
ClientForm() → Empty Unbound Form
```

## POST Request

When the user submits the form:

```python
form = ClientForm(request.POST)
```

The submitted data is passed to ClientForm.

The form is now bound.

```text
ClientForm(request.POST) → Bound Form
```

## request.POST

Contains submitted POST form data.

Conceptually:

```python
{
    "name": "Rahul",
    "email": "rahul@example.com",
    "phone": "9876543210"
}
```

Technically, Django stores POST form data in a dictionary-like object called QueryDict.

## Bound vs Unbound Form

```text
ClientForm()
→ Unbound form without submitted data.

ClientForm(request.POST)
→ Bound form containing submitted data.
```

## is_valid()

```python
if form.is_valid():
```

Runs validation and returns:

```text
True → Data is valid.
False → Data is invalid and errors are stored in the form.
```

`is_valid()` does not save data.

Example:

```text
rahul@example.com → Valid EmailField value.
banana → Invalid EmailField value.
```

Invalid workflow:

```text
Submitted Data → is_valid() → False → Errors stored in form → View → Template → Browser
```

## form.save()

```python
form.save()
```

Creates or updates and saves a model instance using valid form data.

For a new Client:

```text
Valid ModelForm → form.save() → Client Model Object → ORM → SQL INSERT → Database → New Row
```

`form.save()` does not perform the validation check itself.

Important distinction:

```text
is_valid() → Validates data.
save() → Saves model instance.
```

## Why is_valid() Must Come Before save()

Correct:

```python
form = ClientForm(request.POST)

if form.is_valid():
    form.save()
```

Workflow:

```text
User Data → Validation → Save
```

Validation prevents invalid data from reaching the database.

## Sending Form to Template

```python
return render(
    request,
    "blog/add_client.html",
    {"form": form}
)
```

Context:

```python
{"form": form}
```

Key:
`"form"`

Value:
`ClientForm` object.

Template accesses it using:

```django
{{ form }}
```

## Template

```html
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Add Client</button>
</form>
```

## method="POST"

```html
<form method="POST">
```

Tells the browser to submit form data using an HTTP POST request.

Without specifying POST, HTML forms use GET by default.

## csrf_token

```django
{% csrf_token %}
```

CSRF stands for Cross-Site Request Forgery.

Django uses the CSRF token to protect POST forms from forged requests.

Without the required CSRF token, Django normally rejects the POST request with:

```text
403 Forbidden
```

## form.as_p

```django
{{ form.as_p }}
```

Displays form fields and wraps each field in a paragraph element.

Conceptually generated HTML:

```html
<p>
    <label for="id_name">Name:</label>
    <input type="text" name="name">
</p>
```

The ModelForm generates the fields, so the developer doesn't need to manually create every HTML input.

## URL Connection

Inside app/urls.py:

```python
from django.urls import path
from .views import add_client

urlpatterns = [
    path("add-client/", add_client, name="add_client"),
]
```

Visiting:

```text
/blog/add-client/
```

executes the `add_client` view.

## Complete GET Workflow

```text
Browser
→ HTTP GET Request
→ project/urls.py
→ include()
→ app/urls.py
→ add_client View
→ request.method is not POST
→ ClientForm()
→ Empty Unbound Form
→ Context Dictionary
→ render()
→ add_client.html
→ {{ form.as_p }}
→ HTTP Response
→ Browser Displays Form
```

## Complete POST Workflow - Valid Data

```text
Browser
→ HTTP POST Request
→ project/urls.py
→ include()
→ app/urls.py
→ add_client View
→ request.method == "POST"
→ ClientForm(request.POST)
→ Bound Form
→ form.is_valid()
→ True
→ form.save()
→ Client Model Instance
→ ORM
→ SQL INSERT
→ Database
→ New Row Created
→ redirect("add_client")
→ Browser Sends New GET Request
→ Empty Form Created
→ Template
→ HTTP Response
→ Browser
```

## Complete POST Workflow - Invalid Data

```text
Browser
→ HTTP POST Request
→ URL Routing
→ View
→ ClientForm(request.POST)
→ Bound Form
→ form.is_valid()
→ False
→ Errors Stored in Form
→ No save()
→ Same Bound Form Passed Through Context
→ render()
→ Template
→ Browser Displays Errors
```

## POST-Redirect-GET

Recommended pattern after successful submission:

```text
POST → Save → Redirect → GET
```

Example:

```python
if form.is_valid():
    form.save()
    return redirect("add_client")
```

Purpose:
Helps prevent accidental duplicate form submissions when the user refreshes the page.

## Common Mistakes

### No POST Check

Wrong:

```python
form = ClientForm(request.POST)
```

without checking the request method.

### No Validation

Wrong:

```python
form.save()
```

without:

```python
form.is_valid()
```

### Form Not Sent to Template

Wrong:

```python
return render(request, "blog/add_client.html")
```

when the template requires the form.

Correct:

```python
return render(
    request,
    "blog/add_client.html",
    {"form": form}
)
```

### No Redirect After Successful POST

May lead to accidental form resubmission on refresh.

## Security and Least Privilege

Suppose Client contains:

```text
name
phone
email
document_type
deadline
status
assigned_employee
internal_notes
```

Receptionist should only enter:

```text
name
phone
email
document_type
deadline
```

Use:

```python
fields = [
    "name",
    "phone",
    "email",
    "document_type",
    "deadline",
]
```

Do not unnecessarily expose:
- status
- assigned_employee
- internal_notes

Possible problems:
- Unauthorized status changes.
- Incorrect employee assignments.
- Exposure of confidential internal notes.
- Business workflow manipulation.

Security principle:

```text
Least Privilege → Give users only the access necessary for their job.
```

Hiding fields alone is not complete security. Backend permission checks and business rules must also be enforced.

## Component Responsibilities

```text
Model → Defines database structure.
ModelForm → Handles model-based input and validation.
View → Controls GET/POST workflow.
Template → Displays form and errors.
ORM → Translates model operations into database queries.
Database → Stores records permanently.
```

## Important Corrections

```text
forms.py does not display the form.
→ Template displays it.

forms.py does not control the complete workflow.
→ View controls it.

is_valid() does not save data.
→ It validates and returns True/False.

save() does not confirm validity.
→ It saves the model instance.

ORM is not limited to views.
→ It translates Python/model operations into database queries.

get() is not required for ModelForm creation.
→ form.save() can create a new model instance from valid submitted data.
```

## Key Takeaways

✓ forms.py defines forms.
✓ ModelForm inherits powerful form capabilities.
✓ Meta configures the ModelForm.
✓ model selects the connected model.
✓ fields controls exposed fields.
✓ ClientForm() creates an unbound form.
✓ ClientForm(request.POST) creates a bound form.
✓ request.POST is a QueryDict containing submitted POST data.
✓ is_valid() validates and returns True/False.
✓ Invalid form errors are stored in the form.
✓ save() creates or updates and saves a model instance.
✓ GET usually displays the empty form.
✓ POST submits form data.
✓ csrf_token protects POST forms.
✓ form.as_p renders fields as paragraphs.
✓ POST-Redirect-GET helps prevent duplicate resubmission.
✓ Explicit fields and backend permissions improve security.

# ==========================================================
# Module 5.7 - Validation and Cleaning Data
# ==========================================================

## Learning Objectives
- Understand validation and why it is necessary.
- Understand built-in validation.
- Understand is_valid().
- Understand raw data vs cleaned_data.
- Access cleaned data.
- Create custom field validation.
- Understand ValidationError.
- Understand field-level and form-level validation.
- Understand where deeper business logic belongs.

## What is Validation?
Validation checks whether submitted data follows application rules.

```text
Submitted Data → Validation → Valid? → Save / Show Errors
```

Validation protects data integrity, reliability, reporting and business workflows.

## Built-in Validation
Model and form fields provide validation rules.

```python
email = models.EmailField()
name = models.CharField(max_length=100)
```

Examples:
- Email format.
- Required fields.
- Maximum length.
- Data type conversion.

```text
Model Field Rules → ModelForm → Form Validation
```

## is_valid()

```python
form.is_valid()
```

Triggers validation and returns:

```text
True → Form is valid.
False → Form is invalid and errors are stored.
```

It does not save data.

## Raw Data vs Cleaned Data

```text
request.POST → Raw submitted data.
cleaned_data → Successfully validated and converted data.
```

Example:

```text
Raw "21" → Python integer 21
Raw date text → Python date object
```

## cleaned_data

```python
form.cleaned_data
```

Contains successfully cleaned field values after validation.

Example:

```python
{
    "name": "Rahul Sharma",
    "email": "rahul@example.com",
    "phone": "9876543210"
}
```

Access:

```python
name = form.cleaned_data["name"]
```

or:

```python
name = form.cleaned_data.get("name")
```

Normally access cleaned_data after validation has run.

## Custom Field Validation

Naming pattern:

```text
clean_<fieldname>()
```

Examples:

```text
phone → clean_phone()
email → clean_email()
deadline → clean_deadline()
```

Django automatically runs these methods during validation.

## clean_phone()

```python
def clean_phone(self):
    phone = self.cleaned_data["phone"]

    if not phone.isdigit():
        raise forms.ValidationError(
            "Phone number must contain only digits."
        )

    if len(phone) != 10:
        raise forms.ValidationError(
            "Phone number must contain exactly 10 digits."
        )

    return phone
```

Workflow:

```text
Basic Field Validation
→ Retrieve cleaned phone
→ Apply custom rules
→ Invalid? Raise ValidationError
→ Valid? Return phone
```

## Understanding self

```python
def clean_phone(self):
```

`self` refers to the current form instance.

Therefore:

```python
self.cleaned_data
```

means the cleaned data belonging to the current form.

## Why Return the Cleaned Value?

```python
return phone
```

A `clean_<fieldname>()` method should return the approved cleaned value.

Pattern:

```text
Get Value → Check Rules → Raise Error if Invalid → Return Value if Valid
```

Returning the value does not immediately save it to the database. The complete form must first pass validation, and then `form.save()` must execute.

## ValidationError

```python
raise forms.ValidationError("Invalid phone number.")
```

Signals that validation has failed.

Workflow:

```text
Invalid Value
→ ValidationError
→ Error attached to form
→ is_valid() returns False
→ View renders same bound form
→ Template displays error
```

ValidationError itself does not directly display anything in the browser.

## Better Phone Validation

Length alone is insufficient:

```text
abcdefghij
```

has 10 characters.

Use:

```python
if not phone.isdigit():
```

and:

```python
if len(phone) != 10:
```

## Deadline Validation

```python
from django.utils import timezone

def clean_deadline(self):
    deadline = self.cleaned_data["deadline"]

    if deadline < timezone.localdate():
        raise forms.ValidationError(
            "Deadline cannot be in the past."
        )

    return deadline
```

This is a custom business rule because Django cannot automatically know the application's deadline policy.

## Field-Level Validation

Used when validating one specific field.

```python
def clean_phone(self):
```

Even if one field has many rules, field-level validation remains appropriate.

Example:

```text
Phone must:
- Contain digits.
- Be exactly 10 digits.
- Start with an allowed digit.

Still → clean_phone()
```

## Form-Level Validation

Used when multiple fields must be compared together.

```python
def clean(self):
    cleaned_data = super().clean()

    start_date = cleaned_data.get("start_date")
    end_date = cleaned_data.get("end_date")

    if start_date and end_date and start_date > end_date:
        raise forms.ValidationError(
            "Start date cannot be after end date."
        )

    return cleaned_data
```

Example:

```text
start_date + end_date → clean()
```

## Important Distinction

```text
One field with many rules
→ clean_<fieldname>()

Multiple fields compared together
→ clean()

Broader workflow, permissions or database state
→ Deeper backend business logic
```

## PAN Example

Rules such as:

```text
PAN must have required length.
Certain characters must be letters.
Certain characters must be digits.
```

all apply to one field.

Therefore:

```python
def clean_pan_number(self):
```

not necessarily `clean()`.

## cleaned_data["field"] vs cleaned_data.get("field")

```python
self.cleaned_data["phone"]
```

Expects the key to exist. Can raise `KeyError` if missing.

```python
self.cleaned_data.get("phone")
```

Returns `None` if the key doesn't exist.

`.get()` can be safer when another validation stage may already have removed or rejected a field.

## Invalid Form Workflow

```text
Browser
→ HTTP POST
→ URL Routing
→ View
→ ClientForm(request.POST)
→ Bound Form
→ form.is_valid()
→ Built-in Validation
→ Custom clean_<fieldname>()
→ ValidationError
→ Error Attached to Form
→ is_valid() returns False
→ save() Does Not Execute
→ Same Bound Form + Errors
→ Context
→ render()
→ Template
→ Browser Displays Errors
```

## Valid Form Workflow

```text
Browser
→ POST
→ View
→ Bound ModelForm
→ is_valid()
→ Built-in Validation
→ Custom Field Validation
→ Form-Level Validation
→ Valid
→ True
→ form.save()
→ Model Instance
→ ORM
→ SQL INSERT/UPDATE
→ Database
```

## Displaying Errors

Display form:

```django
{{ form.as_p }}
```

Display all errors:

```django
{{ form.errors }}
```

Display phone errors:

```django
{{ form.phone.errors }}
```

The bound form retains submitted values when validation fails.

## Built-in vs Custom Validation

| Built-in | Custom |
|---|---|
| Email format | Exact phone rules |
| Required fields | Deadline cannot be past |
| Maximum length | Organization rules |
| Data conversion | Cross-field rules |

## Deeper Business Logic

Some rules depend on more than simple form input.

Example:

```text
Client cannot become Completed
unless:
- Required documents exist.
- Mandatory tasks are complete.
- Required approvals are complete.
```

Such rules may require:
- Form-level validation.
- Model validation.
- Permission checks.
- Service/business-logic layer.

## CRMS Validation Examples

```text
Client Name → Cannot be empty.
Phone → Valid required format.
Email → Valid email format.
Deadline → Cannot be in past.
Document Type → Must be supported.
Assigned Employee → Must be authorized.
Status → Cannot violate workflow rules.
```

## Common Mistakes

### Thinking is_valid() Saves Data
Wrong:

```text
is_valid() → Saves data
```

Correct:

```text
is_valid() → Validates.
save() → Saves.
```

### Accessing cleaned_data Too Early
Prefer:

```python
if form.is_valid():
    email = form.cleaned_data["email"]
```

### Forgetting return

```python
def clean_phone(self):
    phone = self.cleaned_data["phone"]
    # validation
    return phone
```

### Checking Only Length
Ten letters can also have length 10. Validate format too.

### Confusing Many Rules with Many Fields

```text
One field + many rules → clean_<fieldname>()
Multiple fields together → clean()
```

## Software Engineering Perspective

Validation improves:
- Data integrity.
- Productivity.
- Scalability.
- Reporting accuracy.
- Reliability.
- User experience.
- Business operations.
- Cost efficiency.

Bad data can cause:

```text
Invalid Data
→ Incorrect Records
→ Incorrect Reports
→ Incorrect Decisions
→ Financial/Operational Consequences
```

## Key Takeaways

✓ Validation checks application rules.
✓ is_valid() triggers validation.
✓ is_valid() returns True or False.
✓ is_valid() does not save data.
✓ request.POST contains raw submitted data.
✓ cleaned_data contains validated and converted values.
✓ clean_<fieldname>() validates one field.
✓ clean() validates relationships between multiple fields.
✓ ValidationError signals validation failure.
✓ Custom cleaning methods must return valid cleaned values.
✓ Returning a value does not immediately save it.
✓ `.get()` can safely return None for missing keys.
✓ Invalid forms retain submitted values and errors.
✓ Broader workflow and authorization rules may require deeper backend logic.

# ==========================================================
# Day 6 - Module 6.1 - Introduction to Authentication
# ==========================================================

## Learning Objectives
- Authentication
- Authorization
- User
- Session
- Password Hashing
- Login
- Logout
- Django Authentication Framework
- Authentication Workflow

# Authentication

Authentication verifies the identity of a user.

Question answered:

"Who are you?"

Examples:
- Gmail Login
- Instagram Login
- ATM Card + PIN
- Fingerprint Unlock

Workflow:

User
→ Username & Password
→ Authentication
→ Identity Verified

# Authorization

Authorization determines what an authenticated user is allowed to do.

Question answered:

"What are you allowed to do?"

Examples:
- Employee can view clients.
- Receptionist cannot view salaries.
- Owner can create admins.
- Lawyer can edit assigned clients.

Workflow:

Authentication
→ User Identified
→ Authorization
→ Permissions Checked
→ Access Granted / Denied

# Authentication vs Authorization

Authentication:
- Verifies identity.
- Happens before authorization.

Authorization:
- Checks permissions.
- Happens after authentication.

Rule:

Authentication
→ WHO are you?

Authorization
→ WHAT can you do?

# Django User

A User is an object representing someone who can log into the application.

Common fields:

- id
- username
- email
- password (hashed)
- first_name
- last_name
- is_active
- is_staff
- is_superuser

# Password Hashing

Passwords are never stored as plain text.

Instead Django stores:

pbkdf2_sha256$...

Hashing is one-way.

Workflow:

User Password
→ Hash
→ Store Hash

Login:

Entered Password
→ Hash Again
→ Compare Hashes
→ Match?
→ Login Success

Advantages:
- Protects user privacy.
- Database leak doesn't expose passwords.
- Company cannot recover original passwords.

# Session

A Session is a temporary identity maintained after successful login.

Purpose:
- Avoid entering password on every page.
- Remember logged-in user.

Workflow:

Login
→ Session Created
→ Session ID
→ Browser Cookie
→ Future Requests
→ Session Verified
→ request.user available

Session ends when:
- User logs out.
- Session expires.
- Server invalidates session.

# Login

Successful login:

Valid Credentials
→ authenticate()
→ Password Hash Verification
→ login()
→ Session Created
→ Browser Stores Session Cookie
→ User Authenticated

# Logout

Workflow:

User
→ logout()
→ Session Destroyed
→ Session Cookie Removed
→ Anonymous User

# Anonymous User

User who is not logged in.

Occurs when:
- Never logged in.
- Logged out.
- Session expired.

# Authenticated User

User whose identity has been successfully verified.

Can perform actions according to permissions.

# Superuser

Highest privileged Django user.

Capabilities:
- Django Admin Access
- Manage Users
- Manage Groups
- CRUD Operations
- Assign Permissions

# Complete Authentication Workflow

User
→ Username + Password
→ Browser
→ HTTP POST
→ View
→ authenticate()
→ Django Authentication System
→ User Table
→ Password Hash Verification
→ Valid?
    ├── Yes
    │     → login()
    │     → Session Created
    │     → Session Cookie
    │     → Future Requests
    │     → request.user
    └── No
          → Invalid Credentials
          → Login Page Again

Logout:

User
→ logout()
→ Session Destroyed
→ Browser Removes Cookie
→ Anonymous User

# Authentication in CRMS

Authentication:
- Login
- Logout
- Identity Verification

Authorization:
- Employee cannot delete records.
- Receptionist cannot view salaries.
- Lawyer edits assigned clients.
- Owner manages admins.

# Key Takeaways

✓ Authentication verifies identity.
✓ Authorization controls permissions.
✓ Authentication always happens before authorization.
✓ Django stores hashed passwords.
✓ Hashing is one-way.
✓ Sessions remember logged-in users.
✓ Browser stores Session ID in cookies.
✓ logout() destroys session.
✓ Anonymous users are not logged in.
✓ Superuser has highest permissions.

# ==========================================================
# Day 6 - Module 6.2 - Django Built-in User Model
# ==========================================================

## Learning Objectives
- Built-in User model
- User fields
- create_user()
- create()
- Password hashing
- is_active
- is_staff
- is_superuser

## Built-in User Model

Import:

from django.contrib.auth.models import User

Purpose:
- Pre-built database model
- Authentication system
- Password hashing
- Admin integration
- Sessions
- Permissions

## Common Fields

id
username
password
email
first_name
last_name
is_active
is_staff
is_superuser
date_joined
last_login

## username

Unique username used for login by default.

## password

Stored as a hash.

Never plain text.

## email

Used for:
- Notifications
- Password reset
- Verification

## first_name

Stores user's first name.

## last_name

Stores user's last name.

## is_active

True
→ Login allowed

False
→ Login denied

Useful instead of deleting users.

## is_staff

True
→ Django Admin access

False
→ No Admin access

Does not mean Superuser.

## is_superuser

Highest privilege.

Can:
- Manage users
- Manage permissions
- Manage groups
- Access all admin features

## create_user()

Creates user.

Automatically hashes password.

Workflow:

Python
→ create_user()
→ Password Hash
→ User Model
→ ORM
→ SQL INSERT
→ Database

## create()

Creates database row only.

Does NOT hash password.

Never use for creating users with passwords.

## Password Hashing

Password
→ Hash
→ Database

Login:

Entered Password
→ Hash
→ Compare Stored Hash
→ Login Success

## Why User Model?

Without it developers would need to build:
- Login
- Logout
- Sessions
- Hashing
- Admin integration
- Permissions
- User database

Django already provides everything.

## Staff vs Superuser

Staff:
Admin access.

Superuser:
Full administrative privileges.

## Complete Registration Workflow

Registration Form
→ View
→ create_user()
→ Password Hash
→ User Model
→ ORM
→ SQL INSERT
→ Database

## Login Workflow

Username + Password
→ authenticate()
→ Hash
→ Compare Hash
→ login()
→ Session
→ Browser Cookie
→ Authenticated User

## Key Takeaways

✓ User is Django's built-in authentication model.
✓ Passwords are hashed automatically using create_user().
✓ Never use create() for passwords.
✓ is_active controls login.
✓ is_staff controls admin access.
✓ is_superuser gives highest privileges.
✓ Django's User model improves productivity and security.

# ==========================================================
# Day 6 - Module 6.3 - Login, Logout & Sessions
# ==========================================================

## Learning Objectives
- authenticate()
- login()
- logout()
- request.user
- Sessions
- Session Cookies
- Login & Logout Workflow

## authenticate()

Purpose:
Verify user credentials.

Returns:
- User object (valid credentials)
- None (invalid credentials)

Workflow:
Username + Password
→ authenticate()
→ Authentication System
→ User Table
→ Hash Password
→ Compare Hashes
→ User Object / None

## login()

Purpose:
Log in an authenticated user.

Creates:
- Session
- Session ID
- Browser Cookie

Workflow:
User Object
→ login()
→ Session Created
→ Session ID
→ Cookie Stored
→ Future Requests

## logout()

Purpose:
End the current session.

Workflow:
logout()
→ Session Destroyed
→ Cookie Removed
→ AnonymousUser

## request.user

Represents the current user making the request.

Before login:
AnonymousUser

After login:
Authenticated User object

After logout:
AnonymousUser

Useful attributes:
- request.user.username
- request.user.email
- request.user.is_staff
- request.user.is_superuser
- request.user.is_authenticated

## Login Workflow

Browser
→ Login Form
→ POST Request
→ View
→ authenticate()
→ User Table
→ Hash Password
→ Compare Hashes
→ Valid?
    ├── No → Invalid Login
    └── Yes
          → User Object
          → login()
          → Session Created
          → Session Cookie
          → request.user
          → Dashboard

## Logout Workflow

Authenticated User
→ logout()
→ Session Destroyed
→ Cookie Removed
→ AnonymousUser
→ Redirect

## authenticate() vs login() vs logout()

authenticate()
- Verifies credentials
- Returns User/None
- Does not create a session

login()
- Creates a session
- Stores session cookie
- User becomes authenticated

logout()
- Removes session
- Deletes session cookie
- User becomes anonymous

## Key Takeaways

✓ authenticate() verifies identity.
✓ login() creates a session.
✓ logout() destroys the session.
✓ request.user contains the current User object.
✓ Sessions allow future requests without re-entering the password.
✓ Cookies store the Session ID in the browser.

# ==========================================================
# Day 6 - Module 6.4 - User Registration (UserCreationForm)
# ==========================================================

## Learning Objectives
- UserCreationForm
- Registration
- Password Confirmation
- Validation
- Password Hashing
- Registration Workflow

## UserCreationForm

Import:

from django.contrib.auth.forms import UserCreationForm

Purpose:
- Built-in registration form
- Specifically designed for Django User model

Provides:
- Username
- Password1
- Password2
- Validation
- Password hashing

## Default Fields

- username
- password1
- password2

## Why Two Password Fields?

Password1
→ Original password

Password2
→ Confirmation password

Purpose:
- Prevent typing mistakes
- Ensure intended password is stored

## GET Request

UserCreationForm()

Creates an empty (unbound) registration form.

## POST Request

UserCreationForm(request.POST)

Creates a bound form containing submitted user data.

## Built-in Validation

Checks:
- Username uniqueness
- Password confirmation
- Password length
- Password similarity
- Numeric-only password

If validation fails:
- Error messages displayed
- User remains on registration page

## form.save()

Workflow:

form.save()
→ create_user()
→ Password Hashing
→ User Model
→ ORM
→ SQL INSERT
→ Database
→ User Account Created

## Registration Workflow

Browser
→ GET
→ UserCreationForm()
→ Empty Form
→ User Enters Data
→ POST
→ UserCreationForm(request.POST)
→ Validation
→ Username Unique?
→ Passwords Match?
→ Strong Password?
→ Valid?
    ├── No → Display Errors
    └── Yes
          → form.save()
          → create_user()
          → Password Hashing
          → ORM
          → SQL INSERT
          → Database
          → Redirect

## ModelForm vs UserCreationForm

ModelForm
- Used for custom models
- General CRUD
- No password confirmation by default

UserCreationForm
- Used for Django User model
- Registration only
- Built-in validation
- Password confirmation
- Automatic password hashing

## Key Takeaways

✓ UserCreationForm is built specifically for user registration.
✓ Automatically validates username and passwords.
✓ Passwords are hashed before storage.
✓ Password confirmation prevents typing mistakes.
✓ form.save() creates a secure user account.

# ==========================================================
# Day 6 - Module 6.5 - Protecting Pages with login_required
# ==========================================================

## Learning Objectives
- Protected Views
- @login_required
- request.user.is_authenticated
- LOGIN_URL
- LOGIN_REDIRECT_URL
- Authentication vs Authorization

## Protected View

A protected view allows access only to authenticated users.

Example:

@login_required
def dashboard(request):
    ...

## login_required

Purpose:
Protect a view by checking if the user is authenticated.

Workflow:

Browser
→ GET
→ @login_required
→ request.user.is_authenticated
→ True?
    ├── No
    │     → Redirect
    │     → LOGIN_URL
    └── Yes
          → View
          → Template
          → Browser

## request.user.is_authenticated

Returns:
- True (authenticated user)
- False (anonymous user)

## Anonymous User

Not logged in.

request.user
→ AnonymousUser

request.user.is_authenticated
→ False

## Authenticated User

Logged in with a valid session.

request.user
→ User Object

request.user.is_authenticated
→ True

## LOGIN_URL

Location where unauthenticated users are redirected.

Example:

LOGIN_URL = "/login/"

## LOGIN_REDIRECT_URL

Location where users are redirected after successful login.

Example:

LOGIN_REDIRECT_URL = "/dashboard/"

## Why login_required?

Benefits:
- Cleaner code
- Less repetition
- Easier maintenance
- Consistent authentication checks

## Authentication vs Authorization

Authentication:
Checks if the user is logged in.

Authorization:
Checks what the logged-in user is allowed to do.

login_required only performs authentication.

## Complete Workflow

Browser
→ GET Protected Page
→ @login_required
→ request.user.is_authenticated
→ True?
    ├── No
    │     → LOGIN_URL
    └── Yes
          → Protected View
          → Business Logic
          → Template
          → Browser

## Key Takeaways

✓ @login_required protects specific views.
✓ Anonymous users are redirected to LOGIN_URL.
✓ Authenticated users can access protected views.
✓ LOGIN_REDIRECT_URL controls where users go after login.
✓ login_required checks authentication, not authorization.

# ==========================================================
# Day 6 - Module 6.6 - Authorization, Permissions & Groups
# ==========================================================

## Learning Objectives
- Authorization
- Permissions
- Groups
- has_perm()
- is_staff
- is_superuser

## Authorization

Determines what an authenticated user is allowed to do.

Question:
"What are you allowed to do?"

## Authentication vs Authorization

Authentication
- Verifies identity
- Uses authenticate() and login()

Authorization
- Checks permissions
- Uses request.user.has_perm()

## Django Permissions

Every model automatically gets permissions:

- Add
- Change
- Delete
- View

Example:

Client Model

→ Add Client
→ Change Client
→ Delete Client
→ View Client

## request.user.has_perm()

Purpose:
Checks whether the current user has a specific permission.

Returns:
- True
- False

Example:

request.user.has_perm("crm.delete_client")

## Groups

Purpose:
Assign permissions to many users at once.

Benefits:
- Less repetitive work
- Easier maintenance
- Better scalability

Examples:
- Manager
- Receptionist
- Lawyer
- HR

## is_staff

Allows access to Django Admin.

Does not grant every permission.

## is_superuser

Has all permissions automatically.

Permission checks always succeed.

## Authorization Workflow

Browser
→ Protected View
→ @login_required
→ Authenticated?
→ request.user.has_perm()
→ Allowed?
    ├── No → Permission Denied
    └── Yes → Execute View

## Least Privilege Principle

Give users only the permissions required for their job.

## Key Takeaways

✓ Authentication verifies identity.
✓ Authorization verifies permissions.
✓ Permissions belong to users or groups.
✓ Groups simplify permission management.
✓ has_perm() checks authorization.
✓ Superusers bypass permission checks.

# ==========================================================
# Day 6 - Module 6.7 - Working with request.user
# ==========================================================

## Learning Objectives
- request.user
- AnonymousUser
- User Object
- Personalization
- User-specific Queries
- Ownership of Data

## request.user

Represents the current user associated with the request.

Before Login:
→ AnonymousUser

After Login:
→ Current authenticated User object

## Common Attributes

request.user.username
request.user.email
request.user.first_name
request.user.last_name
request.user.is_staff
request.user.is_superuser
request.user.is_authenticated

## request.user.is_authenticated

Returns:
- True
- False

## Why request.user Exists

After login():
- Session created
- Session cookie stored
- Django identifies the current user
- Automatically attaches the User object to every request

## User-Specific Queries

Instead of:

Client.objects.all()

Use:

Client.objects.filter(
    assigned_to=request.user
)

Benefits:
- Better security
- Better performance
- Data privacy
- Ownership of records

## request.user in Templates

Examples:

{{ request.user.username }}

{{ request.user.first_name }}

{% if request.user.is_authenticated %}

## Personalized Workflow

Browser
→ Login
→ authenticate()
→ login()
→ Session
→ request.user
→ View
→ ORM Filter
→ Database
→ Template
→ Browser

## Ownership

Each user sees only their own records.

Example:

Client.objects.filter(
    assigned_to=request.user
)

## Key Takeaways

✓ request.user represents the current logged-in user.
✓ Anonymous users receive AnonymousUser.
✓ request.user enables personalization.
✓ Use request.user in ORM queries to return only relevant data.
✓ Filtering by request.user improves both security and performance.

# ==========================================================
# Day 6 - Module 6.8 - Authentication & Authorization Revision
# ==========================================================

## Topics Covered

- UserCreationForm
- create_user()
- authenticate()
- login()
- logout()
- Sessions
- request.user
- login_required
- Permissions
- Groups
- has_perm()
- User-specific ORM Queries

## Registration Workflow

Browser
→ GET
→ UserCreationForm()
→ Empty Form
→ POST
→ UserCreationForm(request.POST)
→ Validation
→ form.save()
→ create_user()
→ Password Hash
→ ORM
→ SQL INSERT
→ Database
→ User Created

## Login Workflow

Username + Password
→ authenticate()
→ Credentials Verified
→ login()
→ Session Created
→ Browser Cookie
→ request.user

## Page Protection

@login_required
→ Checks if user is authenticated.
→ Redirects to LOGIN_URL if not.

## Authorization

request.user.has_perm("app.permission")
→ Checks specific permissions.

## Groups

Assign one set of permissions to multiple users.

Benefits:
- Easier maintenance
- Less repetitive work
- Better scalability

## User-Specific Queries

Bad:

Client.objects.all()

Good:

Client.objects.filter(
    assigned_to=request.user
)

Benefits:
- Security
- Privacy
- Performance
- Data ownership

## Logout

logout()
→ Session Destroyed
→ Cookie Removed
→ request.user becomes AnonymousUser

## Authentication vs Authorization

Authentication:
Who are you?

Authorization:
What are you allowed to do?

## Complete Authentication Pipeline

Registration
→ Validation
→ Password Hash
→ Database
→ Login
→ authenticate()
→ login()
→ Session
→ request.user
→ @login_required
→ has_perm()
→ ORM
→ Database
→ Template
→ Browser
→ logout()

## Key Takeaways

✓ authenticate() verifies credentials.
✓ login() creates an authenticated session.
✓ request.user represents the current user.
✓ login_required protects views.
✓ has_perm() checks authorization.
✓ Groups simplify permission management.
✓ Filter data using request.user for security.

# ==========================================================
# Day 7 - Module 7.1 - Django Project Architecture
# ==========================================================

## Learning Objectives
- Software Architecture
- MTV Responsibilities
- SRP
- Request Lifecycle
- Multi-App Architecture

## Software Architecture

Blueprint of a Django application.

Defines:
- Project structure
- Responsibilities
- Communication between components

## Responsibilities

### Model

- Database structure
- Relationships
- Data rules

### View

- Business logic
- Handles requests
- Calls ORM
- Returns responses

### Template

- Presentation
- UI
- Display data

### URLs

- Route browser requests
- Connect URLs to views

## Single Responsibility Principle (SRP)

Each component should have one responsibility.

Benefits:
- Easier maintenance
- Easier debugging
- Better scalability
- Cleaner code

## Multi-App Architecture

Example:

accounts/
clients/
employees/
dashboard/
reports/

Benefits:
- Separation of concerns
- Reusability
- Team collaboration
- Better organization

## Complete Request Lifecycle

Browser
→ URL Dispatcher
→ View
→ @login_required
→ request.user.has_perm()
→ ORM
→ SQL Query
→ Database
→ Model Objects
→ Context Dictionary
→ render()
→ Template
→ Browser

## Common Mistakes

✗ One giant app
✗ Business logic inside templates
✗ HTML inside models
✗ Direct SQL instead of ORM (when ORM is sufficient)
✗ Client.objects.all() for user-specific data

## Key Takeaways

✓ Models manage data.
✓ Views manage business logic.
✓ Templates manage presentation.
✓ URLs manage routing.
✓ Apps should be modular.
✓ Follow SRP for maintainable software.

# ==========================================================
# Day 7 - Module 7.2 - CRMS System Design
# ==========================================================

## Learning Objectives
- Requirement Analysis
- Entity Identification
- Relationship Design
- App Planning
- Database Planning
- Workflow Design

## Development Process

Requirements
→ Analysis
→ Entities
→ Relationships
→ Apps
→ Database
→ Authentication
→ CRUD
→ Dashboard
→ Reports
→ Deployment

## Main Entities

- Client
- Employee
- Lawyer
- Task
- Document
- Report

## Relationships

Lawyer
→ One-to-Many
→ Client

Client
→ One-to-Many
→ Document

Employee
→ One-to-Many
→ Task

Employee
→ One-to-Many
→ Report

## Recommended Apps

accounts/
clients/
employees/
tasks/
documents/
reports/
dashboard/

## Recommended Employee Design

Employee

Fields:
- user
- role
- department
- joining_date

Role Examples:
- Owner
- Manager
- Lawyer
- Receptionist
- Employee

## Add Client Workflow

Login
→ Dashboard
→ Add Client Form
→ Validation
→ form.save()
→ ORM
→ SQL INSERT
→ Database
→ Browser

## Complete System Workflow

Employee
→ Login
→ authenticate()
→ login()
→ Session
→ Dashboard
→ Protected View
→ Permission Check
→ ORM
→ Database
→ Context
→ Template
→ Browser
→ Logout

## Key Takeaways

✓ Plan before coding.
✓ Entities become models.
✓ Relationships define the database.
✓ Separate features into apps.
✓ Authentication should exist before CRUD.
✓ Proper planning reduces future redesign.

# ==========================================================
# Day 7 - Module 7.3 - Dashboard & Role-Based Navigation
# ==========================================================

## Learning Objectives
- Dashboard Design
- Role-Based Navigation
- Sidebar Design
- Quick Actions
- Dashboard Security
- Dashboard Workflow

## Dashboard

The homepage users see after logging in.

Purpose:
- Central control
- Navigation
- Notifications
- Quick actions

## Role-Based Dashboards

Owner
- Employees
- Reports
- Settings
- Clients

Manager
- Team Progress
- Reports
- Tasks

Lawyer
- Assigned Clients
- Cases
- Hearings
- Documents

Receptionist
- Add Client
- Upload Documents
- Appointments

Employee
- Assigned Tasks
- Pending Tasks
- Tomorrow's Tasks
- Notifications

## Sidebar

Provides quick navigation throughout the application.

Benefits:
- Easy navigation
- Faster workflow
- Consistent layout

## Quick Actions

Examples:
- Add Client
- Upload Document
- Search Client
- Generate Report

Benefits:
- Faster work
- Higher productivity

## Dashboard Security

Hide menus based on role.

Still protect every view using:

@login_required

request.user.has_perm()

Never rely only on hidden buttons.

## Dashboard Workflow

Login
→ authenticate()
→ login()
→ Session
→ request.user
→ Role Detection
→ Load Navigation
→ Dashboard
→ Quick Actions
→ Protected View
→ Permission Check
→ ORM
→ Database
→ Template
→ Browser

## Key Takeaways

✓ Dashboards should be role-specific.
✓ Navigation should show only relevant features.
✓ Quick actions improve productivity.
✓ Hidden buttons are not security.
✓ Protect every view with authentication and authorization.