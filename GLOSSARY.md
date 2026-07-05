# Lesson 1.5 - Glossary

| Term | Definition |
|------|------------|
| Django App | A self-contained module responsible for one specific feature of a Django project. |
| `startapp` | Django command used to create a new app inside an existing project. |
| `INSTALLED_APPS` | A list in `settings.py` containing all apps that Django should load. |
| `admin.py` | File used to register models with the Django Admin Panel. |
| `models.py` | File where database models are defined. |
| `views.py` | File containing business logic that processes requests and returns responses. |
| `apps.py` | Configuration file for a Django app. |
| `migrations` | Directory that stores database migration files. |
| Single Responsibility Principle (SRP) | A design principle stating that a module should have one primary responsibility. |

## 📚 Django Terms

| Term | Definition |
|------|------------|
| View | A Python function or class that receives an HTTP request, processes it, and returns an HTTP response. |
| HttpResponse | A Django class used to create and return HTTP responses to the browser. |
| HttpRequest | The request object automatically created by Django and passed to every View. |

## 🌐 Web Development Terms

| Term | Definition |
|------|------------|
| Business Logic | The application's decision-making and processing code that determines how requests are handled. |
| Response Object | An object containing data that will be sent back to the client as an HTTP response. |

## 📚 Django Terms

| Term | Definition |
|------|------------|
| URL Mapping | The process of connecting a URL to a View. |
| `urlpatterns` | A list containing URL-to-View mappings. |
| `path()` | A Django function used to define URL patterns. |
| `include()` | A Django function that delegates URL routing to another app's `urls.py`. |
| URL Name | A unique name assigned to a URL pattern using the `name` parameter. |

## 📚 Django Terms

| Term | Definition |
|------|------------|
| URL Pattern | A mapping between a URL and a View. |
| Route | The URL path defined using `path()`. |
| URL Configuration | The collection of URL patterns stored in `urls.py`. |

## 🌐 Web Development Terms

| Term | Definition |
|------|------------|
| Request Lifecycle | The complete journey of an HTTP request from the browser to the server and back. |

## 📚 Django Terms

| Term | Definition |
|------|------------|
| Template | An HTML file that defines how a webpage should look. |
| `render()` | A Django helper function that loads a template, creates an `HttpResponse`, and returns it to the browser. |
| `django.shortcuts` | A Django module containing helper functions that simplify common development tasks. |

## 🌐 Web Development Terms

| Term | Definition |
|------|------------|
| Presentation Layer | The part of an application responsible for displaying information to the user (HTML, CSS, UI). |

## 📚 Django Terms

| Term | Definition |
|------|------------|
| Template Directory | The folder where Django searches for HTML templates. |
| Template Path | The relative path passed to `render()`, such as `blog/home.html`. |
| TemplateDoesNotExist | A Django exception raised when the requested template cannot be found. |

## 🌐 Web Development Terms

| Term | Definition |
|------|------------|
| Convention | A standard practice or recommended way of organizing code that frameworks expect developers to follow. |