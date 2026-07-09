# Lesson 1.4 Commands

## Create Virtual Environment

```bash
python -m venv venv
```

Creates a new virtual environment.

---

## Activate Virtual Environment (Windows CMD)

```cmd
venv\Scripts\activate
```

Activates the virtual environment.

---

## Activate Virtual Environment (PowerShell)

```powershell
venv\Scripts\Activate.ps1
```

Activates the virtual environment in PowerShell.

---

## Activate Virtual Environment (Linux/macOS)

```bash
source venv/bin/activate
```

Activates the virtual environment.

---

## Install Django

```bash
pip install django
```

Installs Django inside the active virtual environment.

---

## Check Django Version

```bash
python -m django --version
```

Displays the installed Django version.

---

## Run Development Server

```bash
python manage.py runserver
```

Starts Django's built-in development server.

---

## Stop Development Server

```text
CTRL + C
```

Stops the running development server.

# Lesson 1.5 - Commands

## Create a Django App

### Syntax

```bash
python manage.py startapp <app_name>
```

### Purpose

Creates a new Django application (app) inside the current Django project.

### Example

```bash
python manage.py startapp blog
```

### Command Breakdown

| Component | Meaning |
|-----------|---------|
| `python` | Runs the Python interpreter |
| `manage.py` | Executes Django commands for the current project |
| `startapp` | Creates a new Django app |
| `<app_name>` | Name of the app to be created |

### Output

Creates the following directory structure:

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

### When to Use

- Creating a new feature/module.
- Organizing a project into separate responsibilities.
- Starting development of a reusable Django app.

### Common Mistakes

❌ Running the command outside the Django project directory.

✔ Navigate to the directory containing `manage.py` before running the command.

---

❌ Creating one huge app for every feature.

✔ Create separate apps for different functionalities (e.g., `clients`, `employees`, `billing`, `reports`).

### Interview Tip

`startproject` creates the entire Django project, whereas `startapp` creates a single feature module inside that project.

# Lesson 1.6 - Commands

**No new Django commands were introduced in this lesson.**

# Lesson 1.7 - Commands

**No new Django commands were introduced in this lesson.**

# Lesson 1.8 - Commands

## Start Development Server

### Syntax

```bash
python manage.py runserver
```

### Purpose

Starts Django's built-in development server.

### Example

```bash
python manage.py runserver
```

### Output

Runs the application locally at:

```text
http://127.0.0.1:8000/
```

### Common Mistakes

❌ Running the command outside the project directory.

✔ Run it from the directory containing `manage.py`.

### Interview Tip

`runserver` is intended for development only. It should not be used as the production web server.

# Lesson 2.1 - Commands

**No new Django commands were introduced in this lesson.**

# Lesson 2.2 - Commands

**No new Django commands were introduced in this lesson.**

# Lesson 2.3 - Commands

**No new Django commands were introduced in this lesson.**

# Lesson 2.4 - Commands

**No new Django commands were introduced in this lesson.**

# Lesson 2.5 - Commands

**No new Django commands were introduced in this lesson.**

# Lesson 2.6 - Commands

**No new Django commands were introduced in this lesson.**

# Lesson 2.7 - Commands

**No new Django commands were introduced in this lesson.**

# Module 3.1 - Commands

**No Django commands were introduced in this lesson.**

# Module 3.2 - Commands

**No Django commands were introduced in this lesson.**

# Module 3.3 - Commands

## Create Migration Files

```bash
python manage.py makemigrations
```

**Purpose:** Detect changes in Models and generate migration files.

---

## Apply Migrations

```bash
python manage.py migrate
```

**Purpose:** Execute pending migration files and update the database schema.

# Module 3.4 - Commands

## Create Superuser

```bash
python manage.py createsuperuser
```

**Purpose:** Creates an administrator account with full permissions.

---

## Start Development Server

```bash
python manage.py runserver
```

**Purpose:** Starts Django's development server so the Admin Panel can be accessed.

---

## Admin URL

```
http://127.0.0.1:8000/admin/
```

**Purpose:** Opens the Django Admin login page.

# Module 3.5 - Commands

## Start Development Server

```bash
python manage.py runserver
```

Starts Django's development server.

---

## Admin URL

```
http://127.0.0.1:8000/admin/
```

Opens the Django Admin interface.

# Module 3.6 - Commands

**No new terminal commands were introduced in this module.**

## Common ORM Retrieval

```python
Pet.objects.all()
```

**Purpose:** Retrieves all records from the `Pet` table as a QuerySet.

# Module 3.7 - Commands

**No new terminal commands were introduced in this module.**

## Common ORM Retrieval

```python
Pet.objects.all()
```

**Purpose:** Retrieves all records.

---

## DTL Loop

```html
{% for pet in pets %}
    {{ pet.name }}
{% endfor %}
```

**Purpose:** Iterates through a QuerySet and displays each object's data.

# Module 3.8 - Commands

python manage.py makemigrations
Purpose: Create migration files.

python manage.py migrate
Purpose: Apply migrations to the database.

python manage.py createsuperuser
Purpose: Create an administrator account.

python manage.py runserver
Purpose: Start the development server.

# ==========================================================
# Module 4.1 - Filtering Data (filter())
# ==========================================================

## 1. Retrieve All Records

### Syntax

```python
Model.objects.all()
```

### Example

```python
Pet.objects.all()
```

### Purpose

- Retrieves every record from the database table.
- Returns a QuerySet.

### SQL Equivalent

```sql
SELECT * FROM Pet;
```

### Returns

QuerySet

---

## 2. Filter Records

### Syntax

```python
Model.objects.filter(field_name="value")
```

### Example

```python
Pet.objects.filter(species="Dog")
```

### Purpose

Retrieves only the records matching the specified condition.

### SQL Equivalent

```sql
SELECT *
FROM Pet
WHERE species='Dog';
```

### Returns

Filtered QuerySet

---

## 3. Filter Using Multiple Conditions

### Syntax

```python
Model.objects.filter(
    field1="value1",
    field2="value2"
)
```

### Example

```python
Pet.objects.filter(
    species="Dog",
    age=2
)
```

### Purpose

Retrieves records satisfying all specified conditions (AND).

### SQL Equivalent

```sql
SELECT *
FROM Pet
WHERE species='Dog'
AND age=2;
```

### Returns

Filtered QuerySet

---

# Quick Comparison

| Command | Purpose | Returns |
|---------|---------|----------|
| Model.objects.all() | Retrieve every record | QuerySet |
| Model.objects.filter() | Retrieve matching records | Filtered QuerySet |

---

# Notes

✓ filter() never modifies the database.

✓ filter() always returns a QuerySet.

✓ If no record matches, an empty QuerySet is returned.

✓ Let the database perform filtering instead of filtering in Python.

# ==========================================================
# Module 4.2 - Retrieving a Single Record (get())
# ==========================================================

## Retrieve a Single Record by ID

### Syntax

```python
Model.objects.get(id=value)
```

### Example

```python
Pet.objects.get(id=1)
```

### Purpose

Retrieves exactly one Model object using a unique field.

### SQL Equivalent

```sql
SELECT *
FROM Pet
WHERE id=1;
```

### Returns

Single Model Object

---

## Retrieve by Another Field

### Syntax

```python
Model.objects.get(field_name="value")
```

### Example

```python
Pet.objects.get(name="Bruno")
```

### Note

Use this only if the field is unique. Otherwise, `MultipleObjectsReturned` may be raised.

---

# Quick Comparison

| Command | Returns | Best Use |
|---------|---------|----------|
| `Model.objects.filter()` | QuerySet | Multiple matching records |
| `Model.objects.get()` | Single Model object | Exactly one expected record |

---

# Notes

✓ `get()` returns a single object.

✓ `get()` does not return a QuerySet.

✓ Raises `Model.DoesNotExist` if no record matches.

✓ Raises `MultipleObjectsReturned` if multiple records match.

# ==========================================================
# Module 4.3 - Ordering Data (order_by())
# ==========================================================

# Command Overview

The order_by() method is used to sort records returned by the Django ORM.

It does NOT modify the database.

It only changes the order in which records are retrieved.

Return Type:
Ordered QuerySet

==========================================================

# 1. Sort Records in Ascending Order

## Syntax

```python
Model.objects.order_by("field_name")
```

## Example

```python
Pet.objects.order_by("name")
```

## Syntax Breakdown

Model
↓

Database Table

objects
↓

Default ORM Manager

order_by()
↓

Sorting Method

"name"
↓

Field used for sorting

## Purpose

Sorts records in ascending order.

## SQL Equivalent

```sql
SELECT *
FROM Pet
ORDER BY name ASC;
```

## Returns

Ordered QuerySet

## Notes

Ascending order is the default behavior.

==========================================================

# 2. Sort Records in Descending Order

## Syntax

```python
Model.objects.order_by("-field_name")
```

## Example

```python
Pet.objects.order_by("-age")
```

## Syntax Breakdown

-
↓

Descending Order Indicator

age
↓

Sort Field

## Purpose

Sorts records in descending order.

## SQL Equivalent

```sql
SELECT *
FROM Pet
ORDER BY age DESC;
```

## Returns

Ordered QuerySet

## Notes

The minus (-) sign tells Django to reverse the sorting order.

==========================================================

# 3. Sort Using Multiple Fields

## Syntax

```python
Model.objects.order_by(
    "field1",
    "field2"
)
```

## Example

```python
Pet.objects.order_by(
    "species",
    "name"
)
```

## Purpose

Sort by the first field.

If multiple records have the same value,

sort those records using the second field.

## SQL Equivalent

```sql
SELECT *
FROM Pet
ORDER BY species ASC,
         name ASC;
```

## Returns

Ordered QuerySet

==========================================================

# 4. Filter Then Sort

## Syntax

```python
Model.objects.filter(
    condition
).order_by("field")
```

## Example

```python
Pet.objects.filter(
    species="Dog"
).order_by("age")
```

## Purpose

Retrieve matching records first.

Then sort those records.

## SQL Equivalent

```sql
SELECT *
FROM Pet
WHERE species='Dog'
ORDER BY age ASC;
```

## Returns

Filtered Ordered QuerySet

==========================================================

# Command Comparison

| Command | Purpose | Returns |
|----------|---------|----------|
| all() | Retrieve every record | QuerySet |
| filter() | Retrieve matching records | QuerySet |
| get() | Retrieve one record | Model Object |
| order_by() | Sort retrieved records | Ordered QuerySet |

==========================================================

# Best Practices

✓ Perform sorting inside the database.

✓ Combine filter() with order_by() whenever necessary.

✓ Use meaningful fields for sorting.

✓ Avoid manual sorting in Python.

==========================================================

# Common Mistakes

❌ Sorting manually in Python.

✔ Use order_by().

----------------------------------------------------------

❌ Forgetting "-" for descending order.

Ascending

```python
Pet.objects.order_by("age")
```

Descending

```python
Pet.objects.order_by("-age")
```

----------------------------------------------------------

❌ Assuming order_by() changes the database.

✔ It only changes the retrieval order.

==========================================================

# Important Notes

✓ order_by() never modifies database records.

✓ Default sorting is ascending.

✓ "-" indicates descending order.

✓ Multiple fields can be used.

✓ Returns an Ordered QuerySet.

# ==========================================================
# Module 4.4 - Excluding Records (exclude())
# ==========================================================

# Command Overview

exclude() retrieves every record except those matching one or more conditions.

Return Type

QuerySet

==========================================================

# 1. Exclude Records

## Syntax

```python
Model.objects.exclude(field_name="value")
```

## Example

```python
Pet.objects.exclude(species="Dog")
```

## Syntax Breakdown

Model
↓

Database Table

objects
↓

Default ORM Manager

exclude()
↓

Exclude matching records

field_name
↓

Field used for comparison

"value"
↓

Condition Value

## Purpose

Retrieve every record except those matching the specified condition.

## SQL Equivalent

```sql
SELECT *
FROM Pet
WHERE NOT species='Dog';
```

## Returns

QuerySet

==========================================================

# 2. Exclude Multiple Conditions

## Syntax

```python
Model.objects.exclude(
    field1="value1",
    field2="value2"
)
```

## Example

```python
Pet.objects.exclude(
    species="Dog",
    age=2
)
```

## Purpose

Exclude records matching all specified conditions.

==========================================================

# 3. Filter Then Exclude

## Syntax

```python
Model.objects.filter(...).exclude(...)
```

## Example

```python
Pet.objects.filter(
    species="Dog"
).exclude(age=1)
```

## Purpose

Retrieve matching records first, then remove unwanted records.

==========================================================

# 4. Exclude Then Order

## Syntax

```python
Model.objects.exclude(...).order_by("field")
```

## Example

```python
Client.objects.exclude(
    status="Completed"
).order_by("deadline")
```

## Purpose

Exclude records first, then sort the remaining records.

==========================================================

# Command Comparison

| Command | Purpose | Returns |
|---------|---------|----------|
| all() | Retrieve all records | QuerySet |
| filter() | Retrieve matching records | QuerySet |
| get() | Retrieve one record | Model Object |
| order_by() | Sort records | Ordered QuerySet |
| exclude() | Retrieve records except matching ones | QuerySet |

==========================================================

# Best Practices

✓ Use exclude() instead of removing records in Python.

✓ Chain filter(), exclude() and order_by() when needed.

✓ Keep queries readable.

==========================================================

# Important Notes

✓ exclude() never deletes records.

✓ exclude() never modifies the database.

✓ SQL equivalent uses WHERE NOT.

✓ Always returns a QuerySet.

# ==========================================================
# Module 4.6 - Relationship Fields
# ==========================================================

## OneToOneField

### Syntax

```python
field_name = models.OneToOneField(
    RelatedModel,
    on_delete=models.CASCADE
)
```

### Example

```python
user = models.OneToOneField(
    User,
    on_delete=models.CASCADE
)
```

### Purpose

Creates a One-to-One relationship.

### Syntax Breakdown

- field_name → Relationship field
- OneToOneField → One-to-One relation
- RelatedModel → Connected model
- on_delete → Deletion behavior
- CASCADE → Delete related record

### Returns

Relationship Field

---

## ForeignKey

### Syntax

```python
field_name = models.ForeignKey(
    RelatedModel,
    on_delete=models.CASCADE
)
```

### Purpose

Creates a One-to-Many relationship.

---

## ManyToManyField

### Syntax

```python
field_name = models.ManyToManyField(RelatedModel)
```

### Example

```python
courses = models.ManyToManyField(Course)
```

### Purpose

Creates a Many-to-Many relationship.

### Syntax Breakdown

- field_name → Relationship field
- ManyToManyField → Many-to-Many relation
- RelatedModel → Connected model

---

## Command Comparison

| Field | Relationship |
|--------|--------------|
| OneToOneField | One-to-One |
| ForeignKey | One-to-Many |
| ManyToManyField | Many-to-Many |

---

## Notes

✓ OneToOneField requires on_delete.

✓ ForeignKey requires on_delete.

✓ ManyToManyField automatically creates a junction table.

✓ Relationships improve database normalization and reduce redundancy.

# ==========================================================
# Module 4.7 - Database Design
# ==========================================================

## Relationship Fields

### ForeignKey

```python
models.ForeignKey(RelatedModel, on_delete=models.CASCADE)
```

Purpose: One-to-Many relationship.

---

### OneToOneField

```python
models.OneToOneField(RelatedModel, on_delete=models.CASCADE)
```

Purpose: One-to-One relationship.

---

### ManyToManyField

```python
models.ManyToManyField(RelatedModel)
```

Purpose: Many-to-Many relationship.

---

## Relationship Summary

| Field | Relationship |
|--------|--------------|
| ForeignKey | One-to-Many |
| OneToOneField | One-to-One |
| ManyToManyField | Many-to-Many |

---

## Design Workflow

Requirements → Entities → Relationships → Models → Database

# ==========================================================
# Day 4 ORM Commands Summary
# ==========================================================

## Retrieve All

```python
Model.objects.all()
```

Returns: QuerySet

---

## Filter Records

```python
Model.objects.filter(field=value)
```

Returns: QuerySet

---

## Retrieve One Record

```python
Model.objects.get(field=value)
```

Returns: Model Object

---

## Exclude Records

```python
Model.objects.exclude(field=value)
```

Returns: QuerySet

---

## Sort Records

```python
Model.objects.order_by("field")
Model.objects.order_by("-field")
```

Returns: Ordered QuerySet

---

## Relationship Fields

```python
models.ForeignKey(RelatedModel, on_delete=models.CASCADE)
```

One-to-Many

```python
models.OneToOneField(RelatedModel, on_delete=models.CASCADE)
```

One-to-One

```python
models.ManyToManyField(RelatedModel)
```

Many-to-Many

# ==========================================================
# Module 5.1 - CRUD Overview
# ==========================================================

## Read Operations

```python
Model.objects.all()
```

Retrieve all records.

---

```python
Model.objects.filter(...)
```

Retrieve matching records.

---

```python
Model.objects.get(...)
```

Retrieve one record.

---

```python
Model.objects.exclude(...)
```

Retrieve records except matching ones.

---

```python
Model.objects.order_by(...)
```

Retrieve ordered records.

---

## CRUD Summary

| CRUD | Purpose |
|------|---------|
| Create | Add new records |
| Read | Retrieve records |
| Update | Modify records |
| Delete | Remove records |

# ==========================================================
# Module 5.2 - Creating Records
# ==========================================================

## create()

```python
Model.objects.create(
    field=value
)
```

Purpose:
Create and immediately save a record.

Returns:
Model Object.

---

## save()

```python
object = Model(field=value)
object.save()
```

Purpose:
Save an existing model object to the database.

Returns:
None.

---

## Comparison

| Method | Saves Immediately |
|---------|-------------------|
| create() | Yes |
| save() | Only after calling save() |

# ==========================================================
# Module 5.3 - Updating Records
# ==========================================================

## Retrieve Record

```python
Model.objects.get(id=value)
```

Returns:
Model Object

Purpose:
Retrieve one record.

---

## Modify Field

```python
object.field = value
```

Purpose:
Modify the Python object.

---

## Save Changes

```python
object.save()
```

Purpose:
Update the existing database record.

---

## Update Workflow

get() → Modify Fields → save()

---

## SQL Mapping

| ORM | SQL |
|-----|-----|
| get() | SELECT |
| save() (existing object) | UPDATE |

# ==========================================================
# Module 5.4 - Deleting Records
# ==========================================================

## Delete One Record

```python
object = Model.objects.get(id=value)
object.delete()
```

Example:

```python
client = Client.objects.get(id=5)
client.delete()
```

---

## Delete Multiple Matching Records

```python
Model.objects.filter(condition).delete()
```

Example:

```python
Client.objects.filter(status="Inactive").delete()
```

---

## SQL Mapping

| ORM | SQL |
|---|---|
| get() | SELECT |
| delete() | DELETE |

---

## CRUD Summary

| CRUD | Django ORM | SQL |
|---|---|---|
| Create | create() / save() | INSERT |
| Read | all() / filter() / get() | SELECT |
| Update | get() + modify + save() | UPDATE |
| Delete | get() + delete() | DELETE |

# ==========================================================
# Module 5.5 - Django Forms Introduction
# ==========================================================

## Import Forms

```python
from django import forms