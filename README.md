# Airbnb Clone Project - hbnb

![Python](https://img.shields.io/badge/language-python-blue.svg)
![HTML/CSS](https://img.shields.io/badge/language-HTML%2FCSS-orange.svg)
![JavaScript](https://img.shields.io/badge/language-JavaScript-yellow.svg)
![SQL](https://img.shields.io/badge/language-SQL-red.svg)
![65f4a1dd9c51265f49d0](https://github.com/user-attachments/assets/0f1f1be0-d23d-4029-83e6-11a17532be61)

## Introduction
Welcome to the **hbnb (Airbnb Clone) Project**! This project aims to replicate the core functionality of the Airbnb platform. It includes a **command-line interpreter (CLI)** **(console)** that allows you to interact with the application’s data(objects). The data is stored in **JSON files** and represents the backend of an Airbnb-like application. The CLI lets you manage various objects in the system, such as **Users**, **Places**, **Cities**, **States**, **Amenities**, and **Reviews**. With this tool, you can **create**, **retrieve**, **update**, and **delete** these objects. This functionality is important for developers to test and manage the application's data as they build and refine the system.

## Objective

The main objective of this project is to develop a scalable and functional clone of the Airbnb 

## Project Structure

| Task | Description | Source Code |
| ---- | ----------- | ----------- |
| **0. README, AUTHORS** | Write a README.md and an AUTHORS file. | [README.md](./README.md), [AUTHORS](./AUTHORS) |
| **1. Be pycodestyle compliant!** | Ensure the code follows PEP8 style guidelines. | [GitHub repository: AirBnB_clone](https://github.com/username/repo) |
| **2. Unittests** | Write unit tests for all files, classes, and functions. | [GitHub repository: AirBnB_clone](https://github.com/username/repo), [File: tests/](https://github.com/username/repo/tests/) |
| **3. BaseModel** | Create a BaseModel class with specified attributes and methods. | [GitHub repository: AirBnB_clone](https://github.com/username/repo), [File: models/base_model.py](https://github.com/username/repo/models/base_model.py), [File: models/__init__.py](https://github.com/username/repo/models/__init__.py), [File: tests/](https://github.com/username/repo/tests/) |
| **4. Create BaseModel from dictionary** | Implement creating BaseModel instances from dictionary representations. | [GitHub repository: AirBnB_clone](https://github.com/username/repo), [File: models/base_model.py](https://github.com/username/repo/models/base_model.py), [File: tests/](https://github.com/username/repo/tests/) |
| **5. Store first object** | Implement storing objects to a JSON file and reloading them. | [GitHub repository: AirBnB_clone](https://github.com/username/repo), [File: models/engine/file_storage.py](https://github.com/username/repo/models/engine/file_storage.py), [File: models/engine/__init__.py](https://github.com/username/repo/models/engine/__init__.py), [File: models/__init__.py](https://github.com/username/repo/models/__init__.py), [File: models/base_model.py](https://github.com/username/repo/models/base_model.py), [File: tests/](https://github.com/username/repo/tests/) |
| **6. Console 0.0.1** | Implement the command interpreter (console.py). | [GitHub repository: AirBnB_clone](https://github.com/username/repo), [File: console.py](https://github.com/username/repo/console.py), [File: tests/test_console.py](https://github.com/username/repo/tests/test_console.py) |
| **7. Console 0.1** | Update the command interpreter (console.py) to have basic operations. | [GitHub repository: AirBnB_clone](https://github.com/username/repo), [File: console.py](https://github.com/username/repo/console.py), [File: tests/test_console.py](https://github.com/username/repo/tests/test_console.py) |
| **8. First User** | Create a User class. | [GitHub repository: AirBnB_clone](https://github.com/username/repo), [File: models/user.py](https://github.com/username/repo/models/user.py), [File: tests/test_models/test_user.py](https://github.com/username/repo/tests/test_models/test_user.py) |
| **9. More classes!** | Create more classes: State, City, Amenity, Place, Review. | [GitHub repository: AirBnB_clone](https://github.com/username/repo), [Files: models/state.py, models/city.py, models/amenity.py, models/place.py, models/review.py](https://github.com/username/repo/models/), [Files: tests/test_models/test_state.py, tests/test_models/test_city.py, tests/test_models/test_amenity.py, tests/test_models/test_place.py, tests/test_models/test_review.py](https://github.com/username/repo/tests/test_models/) |
| **10. Airbnb 0.1** | Update the command interpreter (console.py) to handle all classes. | [GitHub repository: AirBnB_clone](https://github.com/username/repo), [File: console.py](https://github.com/username/repo/console.py), [File: tests/test_console.py](https://github.com/username/repo/tests/test_console.py) |
| **11. All instances by class name** | Update command interpreter to retrieve all instances of a class using `<class name>.all()`. | [GitHub repository: AirBnB_clone](https://github.com/username/repo), [File: console.py](https://github.com/username/repo/console.py), [tests/test_console.py](https://github.com/username/repo/tests/test_console.py) |
| **12. Count instances** | Update command interpreter to retrieve the number of instances of a class using `<class name>.count()`. | [GitHub repository: AirBnB_clone](https://github.com/username/repo), [File: console.py](https://github.com/username/repo/console.py), [tests/test_console.py](https://github.com/username/repo/tests/test_console.py) |
| **13. Show** | Update command interpreter to retrieve an instance based on its ID using `<class name>.show(<id>)`. | [GitHub repository: AirBnB_clone](https://github.com/username/repo), [File: console.py](https://github.com/username/repo/console.py), [tests/test_console.py](https://github.com/username/repo/tests/test_console.py) |
| **14. Destroy** | Update command interpreter to destroy an instance based on its ID using `<class name>.destroy(<id>)`. | [GitHub repository: AirBnB_clone](https://github.com/username/repo), [File: console.py](https://github.com/username/repo/console.py), [tests/test_console.py](https://github.com/username/repo/tests/test_console.py) |
| **15. Update** | Update command interpreter to update an instance based on its ID using `<class name>.update(<id>, <attribute name>, <attribute value>)`. | [GitHub repository: AirBnB_clone](https://github.com/username/repo), [File: console.py](https://github.com/username/repo/console.py), [tests/test_console.py](https://github.com/username/repo/tests/test_console.py) |
| **16. Update from dictionary** | Update command interpreter to update an instance based on its ID with a dictionary using `<class name>.update(<id>, <dictionary representation>)`. | [GitHub repository: AirBnB_clone](https://github.com/username/repo), [File: console.py](https://github.com/username/repo/console.py), [tests/test_console.py](https://github.com/username/repo/tests/test_console.py) |
| **17. Unittests for the Console!** | Write all unittests for console.py, covering all features. | [GitHub repository: AirBnB_clone](https://github.com/username/repo), [File: tests/test_console.py](https://github.com/username/repo)

## Features

- **CRUD Operations:** Implement CRUD (Create, read, update, and delete) operations for managing various objects (users, properties, bookings, etc.).
- **Command-line Interface (CLI):** Implement a command-line interface (CLI) for easy interaction and management.
- **JSON File Storage:** Integrate JSON file storage for data persistence.
- **Backend Logic:** Develop classes for various objects (users, place, city, etc.).
- **Integration with External APIs:** Integrate external APIs for additional functionality.
- **User Authentication and Authorization:** Implement user authentication and authorization.

##
- Write a command interpreter to manage your AirBnB objects.
-  HTML/CSS templating, database storage, API, front-end integration…
-  put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
-  create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
-  create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
-  create the first abstracted storage engine of the project: File storage.
-  create all unittests to validate all our classes and storage engine


## Supported Classes
The application supports the following classes:

- BaseModel
- User
- State
- City
- Amenity
- Place
- Review

## Environment

- Python 3.8.
- Ubuntu 20.04 LTS
- pycodestyle (version 2.8.*)

## Requirements

### Python Scripts
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start by test_
- Your file organization in the tests folder should be the same as your project
- e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
- e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3
- c 'print(__import__("my_module").MyClass.my_function.__doc__)')

## Learning Objectives

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## Command Interpreter

The command interpreter is a Python-based CLI that provides a shell for interacting with hbnb objects. It allows users to perform various operations on objects, such as creating, retrieving, updating, and deleting them. It supports the following functionalities:

- create: Create a new object (e.g., User, Place)
- show: Retrieve an object from storage
- update: Update attributes of an object
- destroy: Delete an object
- all: Retrieve all objects of a certain type
- count: Count the number of objects of a certain type
- quit: Exit the command interpreter


## How to Use
To get started with the Airbnb Clone Project, follow these steps:

## Installation

1. Clone the Repository: Use git clone to clone the project repository to your local machine:
```
git clone https://github.com/yourusername/hbnb-clone.git
```

2. Navigate to the Project Directory: Use cd to move into the project directory:
```
cd hbnb-clone
```

3. How to Start
To start the command interpreter, simply run the `console.py` script from the terminal:
```
./console.py
```

## Usage
Once the command interpreter is running, you can enter commands to interact with hbnb objects. The available commands include:

- help: Display the help men
- quit: Exit the interpreter
- create <ClassName>: Create a new instance of a class
- show <ClassName> <id>: Display the string representation of an instance
- destroy <ClassName> <id>: Delete an instance
- all [<ClassName>]: Display all instances of a class, or all instances if no class is specified
- update <ClassName> <id> <attribute_name> <attribute_value>: Update an instance’s attribute

### Example
Create a new instance of a class:
```
(hbnb) create BaseModel
```

Show all instances of a class:
```
(hbnb) all BaseModel
```

Show a specific instance by ID:
```
(hbnb) show BaseModel 1234-5678-9012
```

Update an instance:
```
(hbnb) update BaseModel 1234-5678-9012 name "New Name"
```

Destroy an instance:
```
(hbnb) destroy BaseModel 1234-5678-9012
```

Retrieve all instances of a class by class name:
```
(hbnb) User.all()
```

Retrieve the number of instances of a class:
```
(hbnb) User.count()
```

Retrieve an instance based on its ID:
```
(hbnb) User.show("1234-5678-9012")
```

Destroy an instance based on its ID:
```
(hbnb) User.destroy("1234-5678-9012")
```

Update an instance based on its ID and attribute name/value:
```
(hbnb) User.update("1234-5678-9012", "first_name", "John")
```

Update an instance based on its ID with a dictionary:
```
(hbnb) User.update("1234-5678-9012", {'first_name': "John", "age": 89})
```

Exit the console:
```
(hbnb) quit
```

### Sample Usage
Here's a sample session demonstrating the usage of the console:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) User.count()
2
(hbnb) User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb) User.count()
1
(hbnb) User.destroy("Bar")
** no instance found **
(hbnb) User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@mail.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}
(hbnb) User.show("Bar")
** no instance found **
(hbnb) exit
$
```
## Unit Testing

Unit testing ensure that individual components of the application work as expected. The unit tests are organized into different modules, each testing specific components of the application. In this project, unit tests are written using the unittest module to cover various functionalities of the application, including the models, storage, and the command interpreter (console).

### Running Unit Tests

To run the unit tests, use the following command from the root directory of the project:

```bash
python3 -m unittest discover tests
```
This command will discover and execute all test cases in the tests directory.

To run the unit tests in non-interactive mode:
```bash
$ echo "python3 -m unittest discover tests" | bash
```

## Technologies Used

### Frontend
- **HTML/CSS**: Used to create the structure and style of the web pages.
- **JavaScript**: Implemented for client-side scripting to enhance interactivity and user experience.

### Backend
- **Python**: Utilized for backend development, including server-side logic, API integration, and recommendation systems.
- **Flask**: Employed as the Python framework for building the web application.
- **SQLAlchemy**: Utilized for interacting with the database to store and retrieve data efficiently.
- **Jinja**: Used as the Python templating engine to dynamically generate HTML pages.

### Database
- **SQL**: Used for database management and querying to store and retrieve user information.

### APIs
- **APIs**: Integrated external APIs for functionalities.

## Additional Notes

### **1. How to create a Python package:**
A Python package is a directory that contains multiple modules or sub-packages. To create one:
- Create a directory with a name for the package.
- Inside that directory, create an `__init__.py` file (this can be empty).
- Add Python modules (files with `.py` extension) inside the package directory.
- To use the package, import it like any other module:
  ```python
  from package_name import module_name
  ```

---

### **2. How to create a command interpreter in Python using the `cmd` module:**
The `cmd` module allows you to create interactive command-line applications. Here’s a basic structure:

- Use `cmdloop()` to start the interactive prompt.

---

### **3. What is Unit Testing and how to implement it in a large project:**
Unit testing involves testing individual components (functions, classes) of a program to ensure they work as expected. In Python, use the `unittest` module:

For large projects:
- Write tests for each function/module.
- Organize tests in separate files (e.g., `test_*.py`).
- Use test runners like `pytest` or `nose` for larger test suites.

---

### **4. How to serialize and deserialize a Class:**
Serialization is converting a class instance to a format (like JSON) for storage, and deserialization is converting it back.

- **Serialization** (Convert to JSON):
- **Deserialization** (Convert from JSON):

---

### **5. How to write and read a JSON file:**
- **Writing to a JSON file**:
- **Reading from a JSON file**:

---

### **6. How to manage datetime:**
The `datetime` module helps manage dates and times.
- Get current date and time:

---

### **7. What is an UUID:**
A **UUID** (Universal Unique Identifier) is a 128-bit value used to uniquely identify information. In Python, use the `uuid` module to generate it:

---

### **8. What is `*args` and how to use it:**
`*args` allows you to pass a variable number of positional arguments to a function. It collects them as a tuple.

---

### **9. What is `**kwargs` and how to use it:**
`**kwargs` allows you to pass a variable number of keyword arguments (named arguments). It collects them as a dictionary.

---

### **10. How to handle named arguments in a function:**
Named arguments (also called keyword arguments) are passed explicitly by their names when calling the function.

---

## Contributors
This project is maintained by the following contributors:

- [Gloria Ogunsemore](https://github.com/globski)
- [Moufida Herchi](https://github.com/contributor1)

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
The "Airbnb Clone" project aims to replicate the functionality of the Airbnb platform, known as "hbnb," thereby emulating its features.
We would like to express our sincere gratitude to [ALX Afica](https://www.alxafrica.com/) for providing the educational environment and guidance that enabled the development of this project.

ALX Africa is a renowned full-stack software engineering program that prepares students for successful careers in the tech industry through project-based peer learning and a dedication to excellence. The project was created as part of the ALX Africa curriculum, and we want to acknowledge the institution for its invaluable support and resources.

For more information about ALX Africa and its programs, please visit this [link](https://www.alxafrica.com/).
