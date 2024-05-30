# Back-End 🚀

## Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
- [Author](#author)

## About

The `Django` 🚀 project follows a RESTful API architectural style, emphasizing the principles of statelessness, resource identification, and uniform interface. By adhering to RESTful principles, the project aims to provide a clear and consistent approach to designing web services, promoting scalability, flexibility, and ease of maintenance.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Create the environment (creates a folder in your current directory)

```bash
virtualenv .venv
```

In Linux or Mac, activate the new python environment

```bash
source .venv/bin/activate
```

Or in Windows

```bash
source .venv/Scripts/activate
```

### Installing

Install `requirements.txt` file

```bash
pip install -r requirements.txt
```

Run server

```bash
py manage.py runserver
```

Run migrate again to create those model tables in database:

```bash
py manage.py migrate
```

Create super user

```bash
py manage.py createsuperuser --email="admin@gmail.com" --username="admin"
```

## Author

Copyright &copy; 2024 by [ZIN](http://www.github.com/zinitdev)
