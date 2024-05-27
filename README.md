# Airbnb Clone Project - hbnb

![Python](https://img.shields.io/badge/language-python-blue.svg)
![HTML/CSS](https://img.shields.io/badge/language-HTML%2FCSS-orange.svg)
![JavaScript](https://img.shields.io/badge/language-JavaScript-yellow.svg)
![SQL](https://img.shields.io/badge/language-SQL-red.svg)

![License](https://img.shields.io/badge/license-MIT-green.svg)

## Table of Contents

- [Introduction](#introduction)
- [Objective](#objective)
- [Project Structure](#project-structure)
- [Features](#features)
- [Learning Objectives](#learning-objectives)
- [Command Interpreter](#command-interpreter)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [Tasks](#tasks)
- [Advanced Features](#advanced-features)
- [Technologies Used](#technologies-used)
- [Contributors](#contributors)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction
Welcome to the hbnb (Airbnb Clone) Project! This project aims to replicate the core functionality of the Airbnb platform. It includes a command-line interpreter (console) that interacts with JSON files to manage various objects like properties, bookings, and users. These objects are stored in JSON files, representing the backend of an Airbnb-like application. The CLI will allow users to create, retrieve, update, and delete various objects used in the hbnb application. 

Web static development involves creating static HTML pages and applying styles using CSS. Building the front end step-by-step by creating simple HTML static pages, style guides, and fake contents without using JavaScript. The main goal is to learn how to manipulate HTML and CSS languages.

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

##
| Task | Description | File |
|------|-------------|------|
| 0. Inline styling | Write an HTML page that displays a header and a footer with inline styling. | [0-index.html](web_static/0-index.html) |
| 1. Head styling | Write an HTML page that displays a header and a footer using the style tag in the head tag. | [1-index.html](web_static/1-index.html) |
| 2. CSS files | Write an HTML page that displays a header and a footer using CSS files. | [2-index.html](web_static/2-index.html), [styles/2-common.css](web_static/styles/2-common.css), [styles/2-header.css](web_static/styles/2-header.css), [styles/2-footer.css](web_static/styles/2-footer.css) |
| 3. Zoning done! | Write an HTML page that displays a header and a footer using CSS files with specific styling. | [3-index.html](web_static/3-index.html), [styles/3-common.css](web_static/styles/3-common.css), [styles/3-header.css](web_static/styles/3-header.css), [styles/3-footer.css](web_static/styles/3-footer.css), [images/](web_static/images/) |
| 4. Search! | Write an HTML page that displays a header, footer, and a filters box with a search button. | [4-index.html](web_static/4-index.html), [styles/4-common.css](web_static/styles/4-common.css), [styles/4-header.css](web_static/styles/4-header.css), [styles/4-footer.css](web_static/styles/4-footer.css), [styles/4-filters.css](web_static/styles/4-filters.css), [images/](web_static/images/) |
| 5. More filters | Write an HTML page that displays a header, footer, and a filters box with additional filters. | [5-index.html](web_static/5-index.html), [styles/5-common.css](web_static/styles/5-common.css), [styles/5-header.css](web_static/styles/5-header.css), [styles/5-footer.css](web_static/styles/5-footer.css), [styles/5-filters.css](web_static/styles/5-filters.css), [images/](web_static/images/) |
| 6. It's (h)over | Write an HTML page that displays a header, footer, and a filters box with a contextual dropdown. | [6-index.html](web_static/6-index.html), [styles/6-common.css](web_static/styles/6-common.css), [styles/6-header.css](web_static/styles/6-header.css), [styles/6-footer.css](web_static/styles/6-footer.css), [styles/6-filters.css](web_static/styles/6-filters.css), [images/](web_static/images/) |
| 7. Display results | Write an HTML page that displays a header, footer, filters box with dropdown, and results. | [7-index.html](web_static/7-index.html), [styles/7-common.css](web_static/styles/7-common.css), [styles/7-header.css](web_static/styles/7-header.css), [styles/7-footer.css](web_static/styles/7-footer.css), [styles/7-filters.css](web_static/styles/7-filters.css), [styles/7-places.css](web_static/styles/7-places.css), [images/](web_static/images/) |
| 8. More details | Write an HTML page that displays a header, footer, filter box, and the result of the search with additional details. | [8-index.html](web_static/8-index.html), [styles/8-common.css](web_static/styles/8-common.css), [styles/8-header.css](web_static/styles/8-header.css), [styles/8-footer.css](web_static/styles/8-footer.css), [styles/8-filters.css](web_static/styles/8-filters.css), [styles/8-places.css](web_static/styles/8-places.css), [images/](web_static/images/) |
| 9. Full details | Write an HTML page that displays a header, footer, filter box, results, and additional details. | [9-index.html](web_static/9-index.html), [styles/9-common.css](web_static/styles/9-common.css), [styles/9-header.css](web_static/styles/9-header.css), [styles/9-footer.css](web_static/styles/9-footer.css), [styles/9-filters.css](web_static/styles/9-filters.css), [styles/9-places.css](web_static/styles/9-places.css), [images/](web_static/images/) |
| 10. Flex (Advanced) | Improve the Places section by using Flexible boxes for all Place articles. | [10-index.html](web_static/10-index.html), [styles/10-common.css](web_static/styles/10-common.css), [styles/10-header.css](web_static/styles/10-header.css), [styles/10-footer.css](web_static/styles/10-footer.css), [styles/10-filters.css](web_static/styles/10-filters.css), [styles/10-places.css](web_static/styles/10-places.css), [images/](web_static/images/) |
| 11. Responsive design (Advanced) | Improve the page by adding responsive design for mobile or small screens. | [11-index.html](web_static/11-index.html), [styles/11-common.css](web_static/styles/11-common.css), [styles/11-header.css](web_static/styles/11-header.css), [styles/11-footer.css](web_static/styles/11-footer.css), [styles/11-filters.css](web_static/styles/11-filters.css), [styles/11-places.css](web_static/styles/11-places.css), [images](web_static/images/) |
| 12. Accessibility (Advanced) | Improve accessibility by adding semantic tags to the HTML structure. |  [12-index.html](web_static/12-index.html), [styles/12-common.css](web_static/styles/12-common.css), [styles/12-header.css](web_static/styles/12-header.css), [styles/12-footer.css](web_static/styles/12-footer.css), [styles/12-filters.css](web_static/styles/12-filters.css), [styles/12-places.css](web_static/styles/12-places.css), [images](web_static/images/) |

## Features

- **CRUD Operations:** Implement CRUD (Create, read, update, and delete) operations for managing various objects (users, properties, bookings, etc.).
- **Command-line Interface (CLI):** Implement a command-line interface (CLI) for easy interaction and management.
- **JSON File Storage:** Integrate JSON file storage for data persistence.
- **Backend Logic:** Develop classes for various objects (users, properties, bookings, etc.).
- **Integration with External APIs:** Integrate external APIs for additional functionality (e.g., mapping services).
- **User Authentication and Authorization:** Implement user authentication and authorization.
- **Payment Integration:** Integration with payment gateways for handling transactions.
- **Recommendation Systems:** Implementation of recommendation systems for property suggestions.
- **User Management:** User registration, authentication, profile management, and social authentication.
- **Property Management:** Listing creation, media upload, availability calendar, and booking management.
- **Booking and Reservation:** Search, filter, instant booking, reservation confirmation, and cancellation policy.
- **Admin Dashboard:** Overview of key metrics, user and property management, and booking management.

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

##
HTML, CSS, and front-end development:
- What is HTML
- How to create an HTML page
- What is a markup language
- What is the DOM
- What is an element / tag
- What is an attribute
- How does the browser load a webpage
- What is CSS
- How to add style to an element
- What is a class
- What is a selector
- How to compute CSS Specificity Value
- What are Box properties in CSS

## Command Interpreter

The command interpreter is a Python-based CLI that provides a shell for interacting with hbnb objects. It allows users to perform various operations on objects, such as creating, retrieving, updating, and deleting them. It supports the following functionalities:

- create: Create a new object (e.g., User, Place)
- show: Retrieve an object from storage
- update: Update attributes of an object
- destroy: Delete an object
- all: Retrieve all objects of a certain type
- count: Count the number of objects of a certain type
- quit: Exit the command interpreter


## Getting Started
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

## Requirements

- Python 3.8.
- Ubuntu 20.04 LTS

##
- W3C compliant HTML code
 
## Supported Classes
The application supports the following classes:

- BaseModel
- User
- State
- City
- Amenity
- Place
- Review

## Tasks

### More classes!
- Write classes that inherit from BaseModel:
  - State (models/state.py)
    - Public class attributes:
      - name: string (empty string)
  - City (models/city.py)
    - Public class attributes:
      - state_id: string (empty string)
      - name: string (empty string)
  - Amenity (models/amenity.py)
    - Public class attributes:
      - name: string (empty string)
  - Place (models/place.py)
    - Public class attributes:
      - city_id: string (empty string)
      - user_id: string (empty string)
      - name: string (empty string)
      - description: string (empty string)
      - number_rooms: integer (0)
      - number_bathrooms: integer (0)
      - max_guest: integer (0)
      - price_by_night: integer (0)
      - latitude: float (0.0)
      - longitude: float (0.0)
      - amenity_ids: list of string (empty list)
  - Review (models/review.py)
    - Public class attributes:
      - place_id: string (empty string)
      - user_id: string (empty string)
      - text: string (empty string)

### Console 1.0

- Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review
- Update command interpreter (console.py) to allow those actions: show, create, destroy, update and all with all classes created previously.

## Advanced Features

### All instances by class name
- Update command interpreter (console.py) to retrieve all instances of a class by using `<class name>.all()`

### Count instances
- Update command interpreter (console.py) to retrieve the number of instances of a class using `<class name>.count()`

### Show
- Update command interpreter (console.py) to retrieve an instance based on its ID using `<class name>.show(<id>)`

### Destroy
- Update command interpreter (console.py) to destroy an instance based on its ID using `<class name>.destroy(<id>)`

### Update
- Update command interpreter (console.py) to update an instance based on its ID using `<class name>.update(<id>, <attribute name>, <attribute value>)`

### Update from dictionary
- Update command interpreter (console.py) to update an instance based on its ID with a dictionary using `<class name>.update(<id>, <dictionary representation>)`

### Unittests for the Console!
- Write unit tests for all features in console.py
- Ensure tests pass in both interactive and non-interactive mode

## Technologies Used

### Frontend
- **HTML/CSS**: Used to create the structure and style of the web pages.
- **JavaScript**: Implemented for client-side scripting to enhance interactivity and user experience.

### Backend
- **Python**: Utilized for backend development, including server-side logic, API integration, and recommendation systems.
- **Flask**: Employed as the Python framework for building the web application.
- **SQLAlchemy**: Utilized for interacting with the database to store and retrieve data efficiently.
- **Jinja**: Used as the Python templating engine to dynamically generate HTML pages.

### Authentication
- **OAuth**: Implemented for user authentication, enhancing security and enabling social authentication.

### Database
- **SQL**: Used for database management and querying to store and retrieve property and user information.

### Additional Tools
- **APIs**: Integrated external APIs for functionalities such as mapping services and payment gateways.

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
