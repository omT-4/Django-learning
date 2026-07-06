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

## 📚 Django Terms

| Term | Definition |
|------|------------|
| Context | A Python dictionary used to pass data from a View to a Template. |
| Template Variable | A placeholder written using `{{ }}` that Django replaces with data from the Context dictionary. |

## 🌐 Web Development Terms

| Term | Definition |
|------|------------|
| Dynamic Web Page | A webpage whose content changes based on data, user input, or database information. |
| Static Web Page | A webpage that displays the same content to every visitor. |

## 📚 Django Terms

| Term | Definition |
|------|------------|
| Django Template Language (DTL) | Django's template syntax used to display dynamic data and perform simple presentation logic. |
| Template Variable | A placeholder written using `{{ }}` that displays data from the Context dictionary. |
| Template Tag | A command written using `{% %}` that performs template logic such as loops and conditions. |
| Filter | A template feature that changes how data is displayed without modifying the original value. |
| Django Comment | A comment written using `{# #}` that is removed before the page reaches the browser. |

## 💻 Software Design Terms

| Term | Definition |
|------|------------|
| Separation of Concerns (SoC) | A design principle where each part of an application has a single, well-defined responsibility. Views process data, Templates present data, and Models manage the database. |

## 📚 Django Terms

| Term | Definition |
|------|------------|
| Template Tag | A DTL command that performs presentation logic inside a template. |
| `{% if %}` | Displays content conditionally. |
| `{% for %}` | Repeats content for each item in a collection. |
| `{% empty %}` | Displays fallback content when a collection is empty. |

## 💻 Software Design Terms

| Term | Definition |
|------|------------|
| Presentation Logic | Logic that controls how information is displayed to the user, such as loops, conditions, and formatting. |
| Business Logic | Logic that performs calculations, validation, database operations, or application-specific processing. |

## 📚 Django Terms

| Term | Definition |
|------|------------|
| Template Inheritance | A feature that allows templates to reuse a common layout. |
| `base.html` | The parent template containing the shared layout of a website. |
| Child Template | A template that extends another template and provides content for its blocks. |
| `{% extends %}` | A template tag that tells Django to inherit another template. |
| `{% block %}` | A placeholder in a parent template that child templates replace with their own content. |

## 💻 Software Design Terms

| Term | Definition |
|------|------------|
| Reusability | The ability to write code once and use it in multiple places without duplication. |

## 📚 Django Terms

| Term | Definition |
|------|------------|
| Parent Template | The template (usually `base.html`) that defines the common layout. |
| Child Template | A template that extends a parent template and provides content for its blocks. |
| Block Replacement | The process where Django inserts child template content into the matching block of the parent template. |
| Final HTML | The HTML generated after Django processes Template Inheritance, Context, and DTL. |

## 📚 Django Terms

| Term | Definition |
|------|------------|
| Model | A Python class that defines the structure of a database table. |
| ORM (Object Relational Mapper) | Django's layer that translates Python code into SQL and SQL results back into Python objects. |
| Database | A permanent storage system for organized data. |

## 💾 Database Terms

| Term | Definition |
|------|------------|
| Table | A collection of related records in a database. |
| Row (Record) | A single entry in a table. |
| Column (Field) | A specific attribute of each record. |
| CRUD | Create, Read, Update, Delete — the four basic database operations. |

## 📚 Django Terms

| Term | Definition |
|------|------------|
| Model | A Python class that defines the structure of a database table. |
| Field | A model attribute that becomes a column in the database table. |
| `models.Model` | Django's base class that provides database functionality to Models. |
| Metadata | Information Django stores internally about a Model before creating a database table. |

## 💾 Database Terms

| Term | Definition |
|------|------------|
| Schema | The structure or blueprint of a database table, including its fields and data types. |