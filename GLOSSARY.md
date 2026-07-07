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