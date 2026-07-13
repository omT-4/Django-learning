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

## 📚 Django Terms

| Term | Definition |
|------|------------|
| Migration | A set of instructions describing database schema changes. |
| `makemigrations` | Generates migration files from Model changes. |
| `migrate` | Applies pending migrations to the database. |
| Migration File | A versioned Python file containing database schema operations. |

## 💾 Database Terms

| Term | Definition |
|------|------------|
| Schema | The structure of a database, including tables and columns. |
| Pending Migration | A migration that has been created but not yet applied to the database. |

## 📚 Django Terms

| Term | Definition |
|------|------------|
| Django Admin | Django's built-in administration interface for managing database records. |
| Superuser | A user account with full administrative permissions. |
| Model Registration | The process of making a Model available in the Django Admin Panel using `admin.site.register()`. |

## 🔐 Security Terms

| Term | Definition |
|------|------------|
| Authorization | Determining what actions a user is allowed to perform. |
| Principle of Least Privilege | A security principle stating that users should be given only the minimum permissions required to perform their job. |

## 📚 Django Terms

| Term | Definition |
|------|------------|
| Record (Row) | One complete entry in a database table. |
| Validation | The process of checking whether input data satisfies the Model's field requirements before saving. |
| Admin Form | The automatically generated form used by Django Admin to create or edit records. |

## 💾 Database Terms

| Term | Definition |
|------|------------|
| Auto Increment | A database feature that automatically generates unique IDs for new records. |
| Data Integrity | Ensuring stored data remains accurate, consistent, and reliable. |

## 📚 Django Terms

| Term | Definition |
|------|------------|
| Query | A request made to retrieve data from the database. |
| QuerySet | A collection of Model objects returned by the ORM. |
| Manager (`objects`) | Django's default interface for querying Model records. |

## 💾 Database Terms

| Term | Definition |
|------|------------|
| Retrieval | The process of reading data from the database. |
| SQL Query | A command sent to the database to retrieve or manipulate data. |

## 📚 Django Terms

| Term | Definition |
|------|------------|
| QuerySet | A collection of Model objects returned by the ORM. |
| Context | A dictionary used to send data from a View to a Template. |
| `{% for %}` | A Django Template Language tag used to iterate over collections. |
| `{{ }}` | Displays the value of a variable or Model field in a Template. |

## 🌐 Web Terms

| Term | Definition |
|------|------------|
| Dynamic HTML | HTML generated using data from the database instead of hardcoded values. |

## Day 3 Summary

| Term | Definition |
|------|------------|
| Model | Blueprint of a database table. |
| Record | One row in a database table. |
| Query | A request for data. |
| QuerySet | A collection of Model objects returned by the ORM. |
| ORM | Translates Python operations into SQL and SQL results into Python objects. |
| Migration | Instructions for creating or modifying database tables. |
| Django Admin | Built-in administration interface for managing data. |
| Superuser | User with complete administrative permissions. |
| Context | Dictionary that carries data from Views to Templates. |

# ==========================================================
# Django Glossary
# ==========================================================

## Condition

A rule used to determine which records should be returned from the database.

Example:

species="Dog"

---

## Database Filtering

The process of allowing the database to search and return only matching records instead of retrieving all records and filtering them in Python.

---

## Filtered QuerySet

A QuerySet containing only the Model objects that satisfy the given condition(s).

Example:

Pet.objects.filter(species="Dog")

---

## ORM (Object Relational Mapping)

A translator between Python and SQL.

It converts Python ORM queries into SQL and converts SQL results back into Python Model objects.

---

## Query

A request made to the database to retrieve or manipulate data.

Example:

Retrieve all Dogs.

---

## QuerySet

A collection of Model objects returned by the Django ORM.

Examples:

Pet.objects.all()

Pet.objects.filter(species="Dog")

---

## WHERE Clause

An SQL clause used to retrieve only records matching specified conditions.

Example:

```sql
SELECT *
FROM Pet
WHERE species='Dog';
```

Django ORM automatically generates the WHERE clause when using filter().

---

# Software Engineering Principles

## Database-First Filtering

Always perform filtering inside the database whenever possible instead of retrieving all records and filtering them in Python.

### Benefits

- Better Performance
- Lower Memory Usage
- Lower CPU Usage
- Lower Network Bandwidth
- Better Scalability
- Faster Response Time

---

## Fetch Only What You Need

A backend engineering principle stating that an application should retrieve only the data required for the current operation.

### Example

❌ Bad

```python
Pet.objects.all()
```

then filtering in Python.

✔ Good

```python
Pet.objects.filter(species="Dog")
```

The database performs the filtering before returning results.

---

## Query Optimization

The practice of retrieving only the required records from the database to improve performance, scalability, and user experience.

## DoesNotExist

An exception raised by `get()` when no matching record exists.

Example:

```python
Pet.objects.get(id=100)
```

---

## MultipleObjectsReturned

An exception raised by `get()` when more than one record matches the query.

Example:

```python
Pet.objects.get(species="Dog")
```

---

## Model Object

A Python object created by the ORM that represents one row from a database table.

Example:

```python
pet = Pet.objects.get(id=1)
```

`pet` is a Model object.

---

## Unique Field

A field whose value uniquely identifies one record in the database.

Examples:

- ID
- Email (when marked unique)
- Username (when marked unique)

---

## Detail Page

A webpage that displays information about one specific object, such as a client's profile, product details, or a blog post.

# ==========================================================
# Django Glossary
# Module 4.3
# ==========================================================

# order_by()

## Definition

An ORM method used to sort records returned from the database.

----------------------------------------------------------

## Purpose

Arrange records in a required order before sending them to the application.

----------------------------------------------------------

## Where Used

Views

ORM Queries

QuerySets

----------------------------------------------------------

## Example

```python
Pet.objects.order_by("name")
```

----------------------------------------------------------

## Related Concepts

QuerySet

Database Sorting

Ascending Order

Descending Order

==========================================================

# Ascending Order

## Definition

Sorting from smallest to largest.

For text:

A → Z

For numbers:

Smallest → Largest

----------------------------------------------------------

## Example

```python
Pet.objects.order_by("age")
```

----------------------------------------------------------

## SQL

```sql
ORDER BY age ASC;
```

==========================================================

# Descending Order

## Definition

Sorting from largest to smallest.

For text:

Z → A

For numbers:

Largest → Smallest

----------------------------------------------------------

## Example

```python
Pet.objects.order_by("-age")
```

----------------------------------------------------------

## SQL

```sql
ORDER BY age DESC;
```

==========================================================

# ORDER BY Clause

## Definition

An SQL clause used to sort records returned by a query.

----------------------------------------------------------

## Example

```sql
SELECT *
FROM Pet
ORDER BY name ASC;
```

----------------------------------------------------------

## Generated By

Django ORM

==========================================================

# Ordered QuerySet

## Definition

A QuerySet whose records have been sorted using order_by().

----------------------------------------------------------

## Example

```python
Pet.objects.order_by("name")
```

----------------------------------------------------------

## Related Concepts

QuerySet

order_by()

==========================================================

# Database Sorting

## Definition

Sorting performed directly by the database before returning records.

----------------------------------------------------------

## Advantages

• Faster

• Lower CPU Usage

• Lower Memory Usage

• Better Scalability

• Better User Experience

----------------------------------------------------------

## Example

```python
Pet.objects.order_by("name")
```

==========================================================

# Multiple Field Ordering

## Definition

Sorting records using more than one field.

The database sorts using the first field.

If values are equal,

the next field is used.

----------------------------------------------------------

## Example

```python
Pet.objects.order_by(
    "species",
    "name"
)
```

==========================================================

# Ordered Retrieval

## Definition

Retrieving records in a specific sequence rather than the default database order.

----------------------------------------------------------

## Purpose

Improve readability and user experience.

----------------------------------------------------------

## Example

Newest products first.

Highest marks first.

Alphabetical employee list.

==========================================================

# Software Engineering Principle

## Move Work Closer to the Data

### Definition

Whenever possible, let the database perform searching, filtering and sorting instead of Python.

### Benefits

✓ Better Performance

✓ Lower Memory Usage

✓ Lower CPU Usage

✓ Better Scalability

✓ Faster Response Time

==========================================================

# Related Methods

| Method | Purpose |
|---------|---------|
| all() | Retrieve every record |
| filter() | Retrieve matching records |
| get() | Retrieve one record |
| order_by() | Sort records |

# ==========================================================
# Django Glossary
# Module 4.4
# ==========================================================

# exclude()

Definition

ORM method that retrieves every record except those matching specified conditions.

Purpose

Remove unwanted records during database retrieval.

Example

```python
Pet.objects.exclude(species="Dog")
```

Returns

QuerySet

Related

filter()

order_by()

QuerySet

==========================================================

# WHERE NOT Clause

Definition

SQL clause used to exclude matching records.

Example

```sql
SELECT *
FROM Pet
WHERE NOT species='Dog';
```

Generated By

exclude()

==========================================================

# Excluded Query

Definition

A query that removes matching records before returning the results.

Purpose

Reduce unnecessary data retrieval.

==========================================================

# Database-side Exclusion

Definition

The database excludes unwanted records before sending data to Django.

Benefits

✓ Faster

✓ Memory Efficient

✓ CPU Efficient

✓ Better Scalability

==========================================================

# Remaining Rows

Definition

Database rows left after matching records have been excluded.

These rows are then converted into Model objects by the ORM.

==========================================================

# QuerySet

Definition

A Django object containing zero, one or many Model objects.

Methods Returning QuerySet

✓ all()

✓ filter()

✓ exclude()

✓ order_by()

==========================================================

# Model Object

Definition

A Python object representing one row of a database table.

Returned By

✓ get()

Contained Inside

✓ QuerySet

==========================================================

# Software Engineering Principle

Move Work Closer to the Data

Definition

Allow the database to perform searching, filtering, exclusion and sorting instead of Python.

Benefits

✓ Better Performance

✓ Lower Memory Usage

✓ Lower CPU Usage

✓ Better Maintainability

✓ Better Scalability

# ==========================================================
# Django Glossary - Module 4.6
# ==========================================================

## One-to-One Relationship

One record is connected to exactly one record.

Example:
User ↔ Profile

Related Field:
OneToOneField

---

## One-to-Many Relationship

One record connects to many records.

Example:
Lawyer → Clients

Related Field:
ForeignKey

---

## Many-to-Many Relationship

Many records connect to many records.

Example:
Student ↔ Courses

Related Field:
ManyToManyField

---

## OneToOneField

Django model field representing a One-to-One relationship.

---

## ForeignKey

Django model field representing a One-to-Many relationship.

---

## ManyToManyField

Django model field representing a Many-to-Many relationship.

---

## Junction Table

A hidden table automatically created by Django to store Many-to-Many relationships.

Contains the primary keys of both related models.

---

## Cardinality

The number of relationships between records in different tables.

Types:
- One-to-One
- One-to-Many
- Many-to-Many

---

## Data Redundancy

Storing the same information multiple times.

Relationships reduce redundancy.

---

## Database Normalization

The process of organizing data to reduce duplication and improve consistency.

Relationships are an important part of normalization.

# ==========================================================
# Django Glossary - Module 4.7
# ==========================================================

## Database Design
Planning database tables, stored data and relationships before implementation.

---

## Entity
A real-world object that becomes a Django model and a database table.

Example: Lawyer, Client, Employee.

---

## Relationship
A connection between two entities.

Types:
- One-to-One
- One-to-Many
- Many-to-Many

---

## Database Normalization
Organizing data to reduce redundancy and improve consistency.

---

## Data Redundancy
Storing the same information multiple times unnecessarily.

---

## Data Consistency
Keeping the same information accurate across the database.

---

## Scalability
The ability of a database to efficiently handle increasing amounts of data.

---

## Maintainability
The ease of updating and modifying a database without affecting other parts of the system.

# ==========================================================
# Django Glossary - Day 4 Summary
# ==========================================================

## ORM
Object Relational Mapper. Converts Python ORM operations into SQL and SQL results into Python model objects.

## QuerySet
A collection of one or more model objects returned by the ORM.

## Model Object
A Python object representing a single database row.

## ForeignKey
Represents a One-to-Many relationship.

## OneToOneField
Represents a One-to-One relationship.

## ManyToManyField
Represents a Many-to-Many relationship.

## Junction Table
A table automatically created by Django to manage Many-to-Many relationships.

## Database Normalization
Organizing data to reduce redundancy and improve consistency.

## Data Redundancy
Unnecessary duplication of data.

## Scalability
The ability of a system to efficiently handle increasing amounts of data.

# ==========================================================
# Django Glossary - Module 5.1
# ==========================================================

## CRUD

The four fundamental database operations: Create, Read, Update and Delete.

---

## Create

Adds a new record to the database.

---

## Read

Retrieves data from the database.

---

## Update

Modifies an existing database record.

---

## Delete

Permanently removes a database record.

---

## Interactive Application

An application that allows users to create, view, modify and remove data instead of only displaying it.

---

## Persistent Storage

Data stored permanently in the database until modified or deleted.

# ==========================================================
# Django Glossary - Module 5.2
# ==========================================================

## create()

An ORM method that creates and immediately saves a model object to the database.

---

## save()

A model method that writes a model object to the database.

---

## SQL INSERT

The SQL command used to insert a new row into a database table.

---

## Model Object

A Python object representing one database record.

---

## Flexibility

The ability to modify or validate a model object before storing it in the database.

---

## Record Creation Workflow

View → ORM → SQL INSERT → Database → ORM → Model Object → Response.

# ==========================================================
# Django Glossary - Module 5.3
# ==========================================================

## Update

The process of modifying an existing database record.

---

## SQL UPDATE

The SQL statement used to modify existing rows in a database table.

---

## Existing Object

A model object retrieved from the database.

---

## Data Consistency

Keeping stored information accurate and synchronized across the database.

---

## Duplicate Record

An unnecessary second copy of the same logical entity.

---

## Record Lifecycle

Create → Read → Update → Delete (CRUD)

# ==========================================================
# Django Glossary - Module 5.4
# ==========================================================

## delete()
A Django ORM method that permanently removes the targeted record or records.

## SQL DELETE
The SQL operation used to remove database rows.

## Hard Delete
Permanent removal of a database record.

## Soft Delete
Preserving a record while marking it inactive instead of permanently removing it.

## CASCADE
A deletion behavior where deleting a parent record also deletes related child records.

## Data Integrity
Keeping data accurate, valid and trustworthy.

## Auditability
The ability to trace historical records and past actions.

## Reversibility
The ability to undo or recover from an action.

## Business Rule
A requirement defining how software should behave according to real organizational needs.


# 📚 `GLOSSARY.md`

```markdown
# ==========================================================
# Django Glossary - Module 5.5
# ==========================================================

## Form
An interface used to collect and submit user input.

## ModelForm
A Django form connected to a model that can generate fields, validate input and create or update model instances.

## forms.py
A file commonly created inside a Django app to define forms.

## GET
An HTTP request method generally used to retrieve resources.

## POST
An HTTP request method generally used to submit data to a server.

## Validation
The process of checking whether submitted data follows required rules.

## Bound Form
A Django form containing submitted data.

## Unbound Form
A form without submitted data, usually an empty form displayed initially.

## Form Error
A validation message generated when submitted data is invalid.

## Separation of Concerns
A design principle where different components handle different responsibilities.

# ==========================================================
# Django Glossary - Module 5.6
# ==========================================================

## forms.py
A file commonly created inside a Django app to define form classes.

## Django Form
A system for receiving, validating and processing user input.

## ModelForm
A Django form connected to a model that can generate fields, validate input and create or update model instances.

## Inheritance
A mechanism where one class receives capabilities from another class.

## forms.ModelForm
The Django class from which a custom ModelForm inherits its capabilities.

## Meta
An inner configuration class that tells a ModelForm which model and fields to use.

## model
The Meta option that specifies which Django model the ModelForm is connected to.

## fields
The Meta option that controls which model fields are exposed through the form.

## fields = "__all__"
A configuration that includes all editable model fields in a ModelForm.

## Unbound Form
A form without submitted data, usually created with `ClientForm()`.

## Bound Form
A form containing submitted data, usually created with `ClientForm(request.POST)`.

## request
An HttpRequest object automatically passed by Django to a view.

## request.method
The HTTP method used for the current request, such as GET or POST.

## GET
An HTTP request method generally used to retrieve a resource or page.

## POST
An HTTP request method generally used to submit data to the server.

## request.POST
A QueryDict containing submitted POST form data.

## QueryDict
Django's dictionary-like object used to store request data such as submitted POST form values.

## Validation
The process of checking whether submitted data follows required rules.

## is_valid()
A form method that runs validation and returns `True` or `False`.

## Form Error
A validation error stored inside a bound form when submitted data is invalid.

## form.save()
A ModelForm method that creates or updates and saves a model instance.

## Model Instance
A Python object representing one database record.

## CSRF
Cross-Site Request Forgery, a web attack involving unauthorized requests made using a user's authenticated session.

## csrf_token
A Django template tag used to protect POST forms against CSRF attacks.

## 403 Forbidden
An HTTP response indicating that access to a requested action or resource is forbidden. Django may return it when required CSRF protection fails.

## form.as_p
A form rendering method that displays form fields wrapped in HTML paragraph elements.

## Context Dictionary
A Python dictionary used to send data from a view to a template.

## render()
A Django shortcut that combines a template with context data and returns an HttpResponse.

## redirect()
A Django shortcut that returns a redirect response, causing the browser to make another request.

## POST-Redirect-GET
A web development pattern where a successful POST request is followed by a redirect and then a new GET request.

## Duplicate Submission
Accidentally submitting the same form data more than once, often caused by refreshing a POST response.

## Least Privilege
A security principle where users receive only the access required to perform their responsibilities.

## Role-Based Access
A design where permissions and available actions depend on the user's role.

## Business Rule
A requirement that determines how an application should behave according to organizational needs.

## Relative Import
An import that references modules relative to the current Python package.

## Current-App Import
Using `.` in an import such as `from .models import Client` to refer to a module inside the current app.

## SQL INSERT
The SQL operation used to add a new row to a database table.

## ORM
Object-Relational Mapping; Django's system for translating Python/model operations into database queries.

# ==========================================================
# Django Glossary - Module 5.7
# ==========================================================

## Validation
The process of checking whether submitted data follows application rules.

## Built-in Validation
Validation automatically provided by Django form and model fields.

## Custom Validation
Application-specific validation rules written by the developer.

## is_valid()
A form method that triggers validation and returns `True` or `False`.

## Raw Data
Submitted data that has not yet completed validation and conversion.

## request.POST
A QueryDict containing raw submitted POST form data.

## cleaned_data
A dictionary containing successfully validated and converted form values.

## clean_<fieldname>()
A custom validation method for one specific field.

## clean_phone()
A custom field-level validation method for a field named `phone`.

## clean()
A form-level validation method used when validation involves multiple fields together.

## self
A reference to the current form instance.

## ValidationError
An exception used to signal that submitted data has failed validation.

## Field-Level Validation
Validation applied to one specific field, even if that field has multiple rules.

## Form-Level Validation
Validation involving multiple form fields together.

## Cross-Field Validation
Validation that compares or depends on two or more fields.

## Business Rule
An application-specific requirement that determines valid behavior or data.

## Business Logic
Rules and processes controlling how an application behaves according to real organizational requirements.

## Data Integrity
The accuracy, consistency and reliability of stored data.

## KeyError
An error raised when attempting to access a dictionary key that does not exist using square brackets.

## None
A Python value representing the absence of a value.

## .get()
A dictionary method that returns a value if the key exists and `None` or a specified default if it does not.

## Bound Form
A form containing submitted data.

## Form Error
A validation error stored in a form after validation failure.

## Error Attachment
The association of a validation error with a particular field or the overall form.

## Model Validation
Validation rules associated with a Django model and its fields.

## Permission Check
A check determining whether a user is authorized to perform an action.

## Service Layer
An optional application architecture layer used to organize complex business operations outside views and forms.

## Data Conversion
The transformation of submitted textual data into suitable Python values, such as text `"21"` becoming integer `21`.

## Reporting Accuracy
The reliability of reports generated from stored application data.

# ==========================================================
# Day 6 - Module 6.1 Glossary
# ==========================================================

Authentication
Verifying the identity of a user.

Authorization
Determining what an authenticated user is allowed to do.

User
An object representing someone who can log into the application.

Anonymous User
A user who has not been authenticated.

Authenticated User
A user whose identity has been successfully verified.

Superuser
A Django user with unrestricted administrative privileges.

Session
Temporary identity maintained after successful login.

Session ID
Unique identifier stored by the browser to recognize a logged-in user.

Cookie
Small data stored in the browser containing the Session ID.

Hashing
One-way conversion of data into a secure hash value.

Password Hash
Hashed representation of the original password.

authenticate()
Verifies user credentials.

login()
Creates a session after successful authentication.

logout()
Destroys the current session.

request.user
Represents the current user making the request.

Identity Verification
The process of confirming who a user is.

Permission
An allowed action assigned to a user.

Authentication Framework
Django's built-in system for user authentication and session management.

User Table
Database table storing user information such as username, email and hashed password.

PBKDF2
The password hashing algorithm used by Django by default.

Session Cookie
Browser cookie storing the Session ID after login.

# ==========================================================
# Day 6 - Module 6.2 Glossary
# ==========================================================

User Model
Django's built-in database model for authentication.

username
Unique login name.

password
Hashed user password.

email
User's email address.

first_name
User's first name.

last_name
User's last name.

is_active
Determines whether login is allowed.

is_staff
Determines Django Admin access.

is_superuser
Determines unrestricted administrative privileges.

create_user()
Creates a user and hashes the password automatically.

create()
General ORM creation method that does not hash passwords.

Password Hash
Secure one-way representation of a password.

date_joined
Date the account was created.

last_login
Most recent successful login.

Admin User
User with access to Django Admin.

Superuser
Highest privileged Django user.

PBKDF2
Django's default password hashing algorithm.

# ==========================================================
# Day 6 - Module 6.3 Commands
# ==========================================================

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

## Authenticate

user = authenticate(
    username="om",
    password="abc123"
)

## Login

login(request, user)

## Logout

logout(request)

## Current User

request.user

## Check Authentication

request.user.is_authenticated

## Username

request.user.username

## Email

request.user.email

## Staff Check

request.user.is_staff

## Superuser Check

request.user.is_superuser

# ==========================================================
# Day 6 - Module 6.4 Glossary
# ==========================================================

UserCreationForm
Built-in Django form for securely registering new users.

Registration
Process of creating a new user account.

Unbound Form
Empty form displayed to the user.

Bound Form
Form containing submitted user data.

Password1
Primary password field.

Password2
Confirmation password field.

Username Validation
Checks whether the username is unique.

Password Confirmation
Ensures Password1 and Password2 are identical.

Password Strength Validation
Checks password length, similarity, common passwords, and numeric-only passwords.

form.is_valid()
Runs all built-in validations.

form.save()
Creates a new user, hashes the password, and stores the account in the database.

# ==========================================================
# Day 6 - Module 6.5 Glossary
# ==========================================================

Protected View
A view accessible only to authenticated users.

login_required
Decorator that restricts access to authenticated users.

AnonymousUser
Represents a user who is not logged in.

Authenticated User
A user with a valid authenticated session.

request.user.is_authenticated
Boolean indicating whether the current user is logged in.

LOGIN_URL
URL where unauthenticated users are redirected.

LOGIN_REDIRECT_URL
URL where users are redirected after successful login.

Authentication
Verifies the identity of a user.

Authorization
Determines what an authenticated user is allowed to do.

# ==========================================================
# Day 6 - Module 6.6 Glossary
# ==========================================================

Authorization
Determines what an authenticated user is allowed to do.

Permission
A rule allowing or denying a specific action.

Group
A collection of users sharing the same permissions.

has_perm()
Checks whether the current user has a specific permission.

is_staff
Allows access to Django Admin.

is_superuser
Grants every permission automatically.

Least Privilege Principle
Giving users only the permissions needed to perform their job.

Permission Denied
Response returned when a user lacks the required permission.

# ==========================================================
# Day 6 - Module 6.7 Glossary
# ==========================================================

request.user
Current authenticated User object attached to the request.

AnonymousUser
Represents a visitor who has not logged in.

User Object
The authenticated Django user.

Ownership
Restricting data so users only access records belonging to them.

Personalization
Displaying content specific to the current user.

User-Specific Query
A query filtered using request.user.

Session
Stores the identity of the current logged-in user between requests.

# ==========================================================
# Day 6 Final Glossary
# ==========================================================

Authentication
Verifies the identity of a user.

Authorization
Determines what an authenticated user can do.

UserCreationForm
Built-in Django form for secure user registration.

authenticate()
Verifies user credentials.

login()
Creates an authenticated session.

logout()
Ends the current session.

Session
Stores the authenticated user's identity between requests.

request.user
Represents the current user.

AnonymousUser
Represents a visitor who has not logged in.

login_required
Restricts a view to authenticated users.

Permission
Rule allowing or denying an action.

Group
Collection of users sharing permissions.

has_perm()
Checks if a user has a specific permission.

create_user()
Creates a user with a securely hashed password.

# ==========================================================
# Day 7 - Module 7.1 Glossary
# ==========================================================

Software Architecture
The blueprint defining how an application is organized.

Model
Represents database structure and business data.

View
Processes requests and contains business logic.

Template
Displays data to the user.

URL Dispatcher
Routes browser requests to the appropriate view.

SRP (Single Responsibility Principle)
Each component should have one responsibility.

Multi-App Architecture
Organizing a Django project into separate apps based on features.

Context Dictionary
Data passed from a view to a template.

ORM
Object Relational Mapper used to communicate with the database.

# ==========================================================
# Day 7 - Module 7.2 Glossary
# ==========================================================

Requirement Analysis
Understanding the client's needs before development.

Entity
A real-world object about which the system stores information.

Relationship
A connection between two entities.

ForeignKey
Represents a one-to-many relationship.

Architecture
The overall structure of the application.

Workflow
The sequence of steps used to complete a task.

Role
Defines an employee's responsibility and permissions.

Module
A feature-focused section of the application.

# ==========================================================
# Day 7 - Module 7.3 Glossary
# ==========================================================

Dashboard
The main page users see after login.

Role-Based Navigation
Showing menus based on a user's role.

Sidebar
A persistent navigation panel.

Quick Actions
Shortcuts for frequently used tasks.

Role Detection
Identifying the current user's role to customize the interface.

Least Privilege
Giving users only the permissions required to perform their job.

Dashboard Widget
A small information panel displaying important data.

Notification
A message informing users about important events or tasks.

# ==========================================================
# Day 7 - Module 7.4 Glossary
# ==========================================================

CRUD
Create, Read, Update and Delete operations.

ModelForm
A Django form automatically generated from a model.

Validation
Checking whether submitted data satisfies application rules.

Redirect
Sending the browser to another page after processing a request.

PRG Pattern
Post/Redirect/Get pattern that prevents duplicate form submissions.

Permission Check
Verifying whether a user can perform a specific action.

User-Specific Query
A query filtered using the current logged-in user.

Confirmation Dialog
A prompt asking the user to confirm a destructive action.

# ==========================================================
# Day 7 - Module 7.5 Glossary
# ==========================================================

Application Security
Protecting an application, its users, and its data from unauthorized access and misuse.

Defense in Depth
Using multiple layers of security instead of relying on a single protection mechanism.

Authentication
Verifying a user's identity.

Authorization
Determining what an authenticated user is allowed to do.

Ownership
Ensuring a user can only access resources they are permitted to access.

Validation
Checking whether submitted data satisfies application rules.

Least Privilege
Granting users only the permissions necessary to perform their tasks.

Confirmation
An additional step before executing destructive actions such as deletion.

# ==========================================================
# Day 7 - Module 7.6 Glossary
# ==========================================================

Code Organization
Structuring code so it is easy to understand, maintain, and extend.

Separation of Concerns (SoC)
Giving each component a single, well-defined responsibility.

DRY (Don't Repeat Yourself)
Avoiding duplicated logic or knowledge throughout the project.

Reusability
Designing components so they can be used in multiple places.

Refactoring
Improving code quality without changing its external behavior.

Maintainability
How easily software can be updated, debugged, or improved.

Scalability
The ability of a system to grow without major redesign.

Reusable Component
A function, template, form, or module designed for use in multiple locations.