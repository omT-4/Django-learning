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

