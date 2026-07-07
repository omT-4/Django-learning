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