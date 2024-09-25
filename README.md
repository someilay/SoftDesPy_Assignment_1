# Assignment 1 for Software Design with Python

This is a basic extendable web application built using **FastAPI** and **Uvicorn**, where you can dynamically add and load plugins to provide new functionality.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [Adding New Plugins](#adding-new-plugins)

## Prerequisites

- Python 3.11 or above
- [Poetry](https://python-poetry.org/) for dependency management

## Project Structure

```
├── plugins                 # Directory containing plugin modules
│   └── toy_example.py       # Example plugin
├── poetry.lock              # Poetry lock file for package versions
├── pyproject.toml           # Poetry configuration file
├── README.md                # This README file
└── src
    ├── app.py               # Main application runner
    ├── op.py                # Operator class that defines plugin logic
    ├── plugin.py            # Base Plugin class
    └── runner.py            # Core app logic for handling FastAPI and plugins
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install dependencies with Poetry:**
   If you don't have Poetry installed, you can install it by following the [official guide](https://python-poetry.org/docs/#installation).

   Once installed, run:
   ```bash
   poetry install
   ```

3. **Activate the virtual environment:**
   ```bash
   poetry shell
   ```

4. **Verify that all dependencies are installed properly:**
   ```bash
   poetry show
   ```

## Running the Application

Once the setup is complete, you can run the web application using the following command:

```bash
poetry run app
```

This will start the FastAPI server using Uvicorn, which listens on `localhost:8000` by default. You can change the host and port in the `ExtendableWebApp` class if necessary.

### Access the API

1. **Main Endpoint:**  
   Open your browser or use a tool like `curl` or Postman to navigate to:
   ```
   http://localhost:8000/
   ```
   This will show a simple message directing you to the `/list` endpoint.

2. **List of Available Plugins:**  
   You can get a list of all available plugins via the `/list` endpoint:
   ```
   http://localhost:8000/list
   ```

3. **Plugin Endpoint:**  
   Once a plugin is loaded, it will create a unique route. For example, for the `add` plugin, it will be available at:
   ```
   http://localhost:8000/plugins/add?a=5&b=10
   ```

## Adding New Plugins

To add a new plugin, follow these steps:

1. **Create a new Python file inside the `plugins` directory:**  
   Each plugin must implement a specific logic using the `make_operator` and `Plugin` classes. For example, let's create a new plugin that multiplies two numbers.

   Create a new file called `plugins/multiply.py`:
   ```python
   from op import make_operator
   from plugin import Plugin

   @make_operator("Multiply two numbers", a="first number", b="second number")
   def multiply(a: int, b: int):
       return a * b

   plugin = Plugin("multiply", multiply)
   ```

2. **Run the application again:**  
   If the server is already running, restart it to load the new plugin.

3. **Access the new plugin's endpoint:**  
   After restarting, you should be able to access the new plugin via the following endpoint:
   ```
   http://localhost:8000/plugins/multiply?a=5&b=3
   ```

4. **View all available plugins:**
   After adding your new plugin, visit the `/list` endpoint again to see it listed along with other plugins:
   ```
   http://localhost:8000/list
   ```

## Plugin Example

Here is an example of how the `add` plugin is implemented (found in `plugins/toy_example.py`):

```python
from op import make_operator
from plugin import Plugin

@make_operator("Sum of a and b", a="first number", b="second number")
def add(a: int, b: int):
    return a + b

plugin = Plugin("add", add)
```

You can create plugins in a similar manner by defining a function, annotating it with `make_operator`, and then wrapping it in a `Plugin` class. The function will automatically be exposed as a FastAPI route.
