# Python Newsfeed Refactor

**[Python](https://www.python.org/)** is an interpreted, high-level, open-source, general-purpose programming language that supports procedural, object-oriented, and some functional programming constructs.

The Python programming language is a popular alternative to Node.js. Python's many benefits include the following:

* An intentionally simple syntax
* An active community that boasts many libraries
* A wide range of uses, from machine learning to standalone software

## Contents

1. [Project Overview](#project-overview)
2. [Set Up The Python Environment](#set-up-the-python-environment)
   1. [Verify Python Version](#verify-python-version)
   2. [Create Virtual Environment](#create-virtual-environment)
      1. [Active Virtual Environment](#activate-the-virtual-environment)
      2. [Deactive Virtual Environment](#deactivate-the-virtual-environment)
3. [Python Dependencies](#python-dependencies)
   1. [pip Python Package Manager](#pip-python-package-manager)
   2. [Python Packages](#python-packages)
   3. [Flask](#flask)
   4. [SQLAlchemy](#sqlalchemy)
   5. [PyMySQL](#pymysql)
   6. [bcrypt](#bcrypt)
   7. [python-dotenv](#python-dotenv)
   8. [Gunicorn](#gunicorn)

## Project Overview

This application will use Python as the basis for a web server. Instead of building it from scratch, the project refactors the back end of an app that was originally built using Node.js. The app, called Just Tech News, lets users submit links to tech-related articles, comment on other users' articles, and upvote articles for points.

## Set Up The Python Environment

In order to begin coding in Python, the environment must first be set up.

### Verify Python Version

To verify that the latest version of Python is installed on the machine, run the following command from the command line:

```Python
python --version

# RETURNS
> Python 3.12.4 # Or The Latest Version
```

> [!NOTE]
> In the context of Python, **print** usually refers to displaying a response in the console window.

Python provides a feature called a **virtual environment**, which is a self-contained directory that maintains its own version of Python and its own library dependencies. This allows multiple Python projects to reside on the same machine without interfering with each other.

### Create Virtual Environment

In the root directory of the project, run the following command:

```Python
# Create Virtual Environment Named `VEnv`
python<3> -m venv VEnv
```

The `VEnv` directory holds all the files that make a virtual environment possible.

#### Activate The Virtual Environment

On macOS, run the following command from the root directory of the project:

```Python
. VEnv/Bin/activate

# RETURNS
> (venv) <Username> <Project-Name> %
```

As long as the virtual environment is active, installing Python dependencies puts them in this local `VEnv` directory instead of globally installing them for the entire operating system.

#### Deactivate The Virtual Environment

To deactivate the virtual environment, run the following command from any directory within the project:

```Python
deactivate
```

## Python Dependencies

Throughout refactoring the back end of Just Tech News, this application will take advantage of some of the numerous useful libraries that Python has to offer.

### pip Python Package Manager

**pip** is the default package manager for Python, similar to how npm is the default package manager for Node.js. It is distributed with Python, meaning that there is no further setup required beyond installing Python itself. Pip is used from the command line to add packages from the **[Python Package Index (PyPI)](https://pypi.org/)**, a repository of software for the Python programming language, to Python applications. Make sure to [active the virtual environment](#activate-the-virtual-environment) before installing any packages to ensure that the project's dependencies get installed in the right place.

### Python Packages

In Python, a **package** is a directory that can contain other packages or modules. The presence of an `__Init__.py` file designates the directory as a package, but the file can also contain logic to consolidate submodules, perform startup tasks, and more.

>[!NOTE] Connect The Dots
> The `__Init__.py` file of a Python package corresponds to the `Index.js` file of a Node.js module.

### Flask

**[Flask](https://palletsprojects.com/p/flask/)** is a lightweight web application framework written in Python. It's designed to make getting started quick and easy, with the ability to scale up to complex applications. It has become one of the most popular Python web application frameworks. In this project, the **[Flask PyPI Package](https://pypi.org/project/Flask/)** will be used.

**Installation:**

Once the virtual environment activates, run the following command to install Flask:

```Python
pip install flask
```

**Create The Flask Application Object:**

In the root directory of the project, create a new directory called `App`. Inside this directory, create a new file called `__Init__.py` with two underscores on each side. Once this is completed, start the Flask server by running the following command:

**Set The FLASK_APP Environment Variable:**

Because this directory name differs from the default entry point of the app, which uses the default name of **`app`**, it is necessary to specify the name of the Python file containing the Flask application object. This is accomplished through using the FLASK_APP environment variable, which can be set to point to the Python file containing the Flask application object by running the following command:

```Python
export FLASK_APP=App.__Init__.py
```

**Start The Flask Server:**

Once the FLASK_APP environment variable has been set, start the Flask server by running the following command:

```Python
python -m flask run
```

### SQLAlchemy

**[SQLAlchemy](https://www.sqlalchemy.org/)** is the Python SQL toolkit and object-relational mapper that gives Python developers the full power and flexibility of SQL. It provides a full suite of well-known, enterprise-level persistence patterns that are designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language. In this project, the **[SQLAlchemy PyPI Package](https://pypi.org/project/SQLAlchemy/)** will be used.

### PyMySQL

**[PyMySQL](https://pymysql.readthedocs.io/en/latest/)** is a pure Python MySQL driver that connects a Python application to a MySQL database. In this project, the **[PyMySQL PyPI Package](https://pypi.org/project/PyMySQL/)** will be used.

### bcrypt

**[bcrypt](https://pypi.org/project/bcrypt/)** is a PyPI library for Python that allows for password hashing. **Hashing** is the process of taking input and using a mathematical formula to chop and mix it up to produce an output of a specific length. Hashing is a one-way function, meaning that it can easily convert input to a fixed-size output, but it is difficult to revert, or convert in the opposite direction. This attribute allows developers to secure passwords when authenticating users for their applications. The **[Cryptography PyPI Package](https://pypi.org/project/cryptography/)** is a dependency of `bcrypt` that will be required to install in order to use it in this project application.

### python-dotenv

**[python-dotenv](https://pypi.org/project/python-dotenv/)** is a PyPI dotenv package that is used to manage environment variables inside Python's native virtual environment, or `venv`. This virtual environment is a self-contained directory that can maintain its own version of Python as well as its own library of dependencies so that multiple Python projects can reside on the same machine without interfering with each other.

### Gunicorn

**[Gunicorn](https://docs.gunicorn.org/en/stable/)**, or Green Unicorn, is a Python HTTP Server for UNIX that is broadly compatible with various web frameworks (including Python and Flask), simply implemented, light on server resources, and fast. In this project, the **[Gunicorn PyPI Package](https://pypi.org/project/gunicorn/)** will be used.