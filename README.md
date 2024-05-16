# Airbnb Clone Project - hbnb

![Python](https://img.shields.io/badge/language-python-blue.svg)
![HTML/CSS](https://img.shields.io/badge/language-HTML%2FCSS-orange.svg)
![JavaScript](https://img.shields.io/badge/language-JavaScript-yellow.svg)
![SQL](https://img.shields.io/badge/language-SQL-red.svg)

![License](https://img.shields.io/badge/license-MIT-green.svg)

## Table of Contents

- [Introduction](#introduction)
- [Objective](#objective)
- [Project Overview](#project-overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Command Interpreter](#command-interpreter)
  - [Usage](#usage)
- [Tasks](#tasks)
  - [Task 0: Create a Python script that starts a Flask web application](#task-0-create-a-python-script-that-starts-a-flask-web-application)
  - [Task 1: Create a basic Flask app](#task-1-create-a-basic-flask-app)
  - [Task 2: Display "Hello HBNB!" on the web app](#task-2-display-hello-hbnb-on-the-web-app)
  - [Task 3: Display specified route](#task-3-display-specified-route)
  - [Task 4: Display "HBNB" if no specified route found](#task-4-display-hbnb-if-no-specified-route-found)
  - [Task 5: Display template for HTML](#task-5-display-template-for-html)
  - [Task 6: Add additional route and template](#task-6-add-additional-route-and-template)
  - [Task 7: Display specified status code](#task-7-display-specified-status-code)
  - [Task 8: Render dynamic content with Flask](#task-8-render-dynamic-content-with-flask)
  - [Task 9: Render dynamic content from storage](#task-9-render-dynamic-content-from-storage)
  - [Task 10: Update state](#task-10-update-state)
  - [Task 11: Add route for /states](#task-11-add-route-for-states)
  - [Task 12: Display cities by state](#task-12-display-cities-by-state)
  - [Task 13: Add route for /cities_by_states](#task-13-add-route-for-cities_by_states)
  - [Task 14: Update routes for /cities_by_states](#task-14-update-routes-for-cities_by_states)
  - [Task 15: Display cities by state with specified storage](#task-15-display-cities-by-state-with-specified-storage)
  - [Task 16: Update states route with place objects](#task-16-update-states-route-with-place-objects)
  - [Task 17: Display places by city](#task-17-display-places-by-city)
- [Advanced Features](#advanced-features)
- [Technologies Used](#technologies-used)
- [Contributors](#contributors)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction
Welcome to the hbnb (Airbnb Clone) Project! This project aims to replicate the core functionality of the Airbnb platform. It includes a command-line interpreter (console) that interacts with JSON files to manage various objects like properties, bookings, and users. These objects are stored in JSON files, representing the backend of an Airbnb-like application. The CLI will allow users to create, retrieve, update, and delete various objects used in the hbnb application.

## Objective

The main objective of this project is to develop a scalable and functional clone of the Airbnb platform, allowing users to manage properties, bookings, and users via a command-line interface.

### Goals:

1. **Create a User-Friendly Airbnb Clone**: Develop a web application similar to Airbnb, providing users with an intuitive interface for listing, discovering, and booking accommodations.

2. **Robust Backend Logic**: Implement backend functionality using Python to handle user authentication, data storage, and business logic effectively.

3. **Efficient Web Development**: Utilize Flask framework to streamline web application development and ensure scalability.

4. **Integration with External Services**: Integrate external APIs for additional features such as mapping services, payment gateways, and recommendation systems.

### Key Features:

- **User Authentication**: Implement user authentication to secure user accounts and provide personalized experiences.
- **User Registration and Login**: Users can create accounts and log in securely to access the platform's features.
- **Search and Discovery**: Enable users to search for accommodations based on location, dates, price range, accommodation type, and amenities.
- **Booking and Payments**: Facilitate the booking process, including secure payment transactions, review booking details, and reservation management.
- **Accommodation Listings**: Allow hosts to create and manage listings, including details such as property descriptions, photos, pricing, and availability calendars.
- **User Reviews and Ratings**: Allow users to leave reviews and ratings for accommodations they've stayed in, contributing to a transparent and trustworthy community.
- **Messaging System**: Built-in messaging system for communication between hosts and guests regarding bookings, inquiries, and special requests.
- **Admin Dashboard**: Implement an admin dashboard to manage user profiles with information such as booking history, saved listings, and reviews.

### Integration with External Services:

1. **Mapping Services**: Integrate mapping services like Google Maps API or Mapbox to provide users with interactive maps for searching accommodations based on location.

2. **Payment Gateways**: Integrate payment gateways like Stripe, PayPal, or Braintree to facilitate secure and seamless transactions between hosts and guests.

3. **Recommendation Systems**: Implement recommendation systems using machine learning algorithms or collaborative filtering techniques to suggest personalized accommodations to users.

4. **External Data Sources**: Utilize external APIs or data sources to enrich the platform with additional information such as local weather forecasts, transportation options, tourist attractions, and events happening in the area.

## Project Overview
The project is structured around a command-line interface (CLI) and a Flask web application.
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
- **Backend Logic:** Develop classes for various objects (users, properties, bookings, etc.) with robust backend logic.
- **Integration with External APIs:** Integrate external APIs for additional functionality (e.g., mapping services).
- **User Authentication and Authorization:** Implement user authentication and authorization.
- **Payment Integration:** Integration with payment gateways for handling transactions.
- **Recommendation Systems:** Implementation of recommendation systems for property suggestions.
- **User Management:** User registration, authentication, profile management, and social authentication.
- **Property Management:** Listing creation, media upload, availability calendar, and booking management.
- **Booking and Reservation:** Search, filter, instant booking, reservation confirmation, and cancellation policy.
- **Admin Dashboard:** Overview of key metrics, user and property management, and booking management.

### User Management

- Registration: Users can easily register for an account by providing necessary details such as username, email, and password.
- Authentication: Secure authentication mechanisms ensure that only authorized users can access the application.
- Profile Management: Users can update their profiles, including adding profile pictures, changing passwords, and updating contact information.
- Social Authentication: Integration with social media platforms allows users to log in using their existing accounts, enhancing convenience and user experience.

### Property Management

- Listing Creation: Property owners can create detailed listings for their accommodations, including property type, location, amenities, and pricing.
- Media Upload: Users can upload multiple images and videos to showcase their properties effectively, attracting potential guests.
- Availability Calendar: A calendar view allows property owners to manage availability dates, block off booked dates, and update availability status easily.
- Booking Management: Property owners can view and manage bookings for their properties, including confirming, modifying, or canceling reservations.

### Booking and Reservation

- Search and Filter: Users can search for properties based on location, dates, price range, number of guests, and amenities, with advanced filtering options for 
personalized results.
- Instant Booking: Instant booking feature allows users to make immediate reservations without waiting for host approval, providing flexibility and convenience.
- Reservation Confirmation: Users receive instant confirmation upon booking, along with details such as booking ID, property information, and payment summary.
- Cancellation Policy: Clear and transparent cancellation policies are provided to users, outlining refund conditions and penalties for cancellations.

### Payment Integration

- Payment Gateways: Integration with popular payment gateways such as Stripe, PayPal, and Square enables users to make secure payments using various methods, including credit/debit cards, digital wallets, and bank transfers.
- SSL Encryption: All payment transactions are encrypted with SSL (Secure Sockets Layer) technology to protect sensitive financial information and ensure data security.
- Payment Confirmation: Users receive payment confirmation and receipts for successful transactions, providing peace of mind and transparency throughout the booking process.

### Admin Dashboard

- Dashboard Overview: An intuitive dashboard provides administrators with an overview of key metrics, including total users, bookings, revenue, and property listings.
- User Management: Administrators can manage user accounts, including creating new accounts, disabling accounts, and resetting passwords.
- Property Management: Comprehensive property management tools allow administrators to review and moderate property listings, ensuring compliance with community guidelines and quality standards.
- Booking Management: Administrators can view and manage all bookings, including reviewing reservations, resolving disputes, and handling cancellations.

##Learning Objectives

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

3. Install Dependencies: Use pip to install the required Python dependencies:
```
pip install -r requirements.txt
```

4. Set Up the Database: Configure the database settings in config.py and run the database migrations:
```
flask db init
flask db migrate
flask db upgrade
```

5. Run the Application: Start the Flask development server to run the application:
```
flask run
```

6. Access the Application: Open a web browser and navigate to http://localhost:5000 to access the Airbnb Clone application.

## Command Interpreter

The command interpreter is a Python-based CLI that provides a shell for interacting with hbnb objects. It allows users to perform various operations on objects, such as creating, retrieving, updating, and deleting them.

## How to Start
To start the command interpreter, simply run the `console.py` script from the terminal:
```
./console.py
```

## Usage
Once the command interpreter is running, you can enter commands to interact with hbnb objects. The available commands include:

- create: Create a new object
- show: Retrieve an object
- update: Update attributes of an object
- destroy: Delete an object
- all: Retrieve all objects of a certain type
- count: Count the number of objects of a certain type
- quit: Exit the command interpreter

### Example
Create a new user:
```
(hbnb) create User
```

Show details of a specific user:
```
(hbnb) show User 1234-5678
```

Update the name attribute of a user:
```
(hbnb) update User 1234-5678 name "John Doe"
```

### Examples
```
$ ./console.py
(hbnb) create User
6f9307b1-1104-4c3c-843c-d1f0ec34f88d
(hbnb) show User 6f9307b1-1104-4c3c-843c-d1f0ec34f88d
[User] (6f9307b1-1104-4c3c-843c-d1f0ec34f88d) {'id': '6f9307b1-1104-4c3c-843c-d1f0ec34f88d'}
(hbnb) update User 6f9307b1-1104-4c3c-843c-d1f0ec34f88d first_name "John"
(hbnb) show User 6f9307b1-1104-4c3c-843c-d1f0ec34f88d
[User] (6f9307b1-1104-4c3c-843c-d1f0ec34f88d) {'id': '6f9307b1-1104-4c3c-843c-d1f0ec34f88d', 'first_name': 'John'}
(hbnb) all User
["[User] (6f9307b1-1104-4c3c-843c-d1f0ec34f88d) {'id': '6f9307b1-1104-4c3c-843c-d1f0ec34f88d', 'first_name': 'John'}"]
(hbnb) quit
$
```

### Sample Usage
Here's a sample session demonstrating the usage of the console:

```
$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) create User
38f22813-2753-4d42-b37c-57a17f1e4f88
(hbnb) all User
["[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'email': 'airbnb@mail.com', 'first_name': 'Betty', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88', 'last_name': 'Bar', 'password': 'root', 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291)}"]
(hbnb) exit
$
```

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

- Task 0: Create a Python script that starts a Flask web application
- Task 1: Create a basic Flask app
- Task 2: Display "Hello HBNB!" on web app
- Task 3: Display specified route
- Task 4: Display "HBNB" if no specified route found
- Task 5: Display template for HTML
- Task 6: Add additional route and template
- Task 7: Display specified status code
- Task 8: Render dynamic content with Flask
- Task 9: Render dynamic content from storage
- Task 10: Update state
- Task 11: Add route for /states
- Task 12: Display cities by state
- Task 13: Add route for /cities_by_states
- Task 14: Update routes for /cities_by_states
- Task 15: Display cities by state with specified storage
- Task 16: Update states route with place objects
- Task 17: Display places by city

### Task 0: Create a Python script that starts a Flask web application
  - Initialize Flask app
  - Run the app
  - Check if everything is set up correctly by accessing the server

### Task 1: Create a basic Flask app
  - Set up Flask app structure
  - Define a basic route
  - Test the route to ensure it returns the expected output

### Task 2: Display "Hello HBNB!" on the web app
  - Update the route to return "Hello HBNB!"
  - Test the route to ensure it displays the correct message

### Task 3: Display specified route
  - Create a new route to display a specified message
  - Test the new route to ensure it displays the specified message

### Task 4: Display "HBNB" if no specified route found
  - Handle cases where no specified route is found
  - Update the app to return "HBNB" in such cases
  - Test to ensure the app displays "HBNB" when accessing an undefined route

### Task 5: Display template for HTML
  - Create an HTML template
  - Render the template using Flask
  - Test to ensure the template is displayed correctly in the browser

### Task 6: Add additional route and template
  - Create a new route in the Flask app
  - Define a new HTML template for the route
  - Test to ensure the new route and template are working correctly

### Task 7: Display specified status code
  - Update the Flask app to return a specified HTTP status code
  - Test to ensure the correct status code is returned when accessing the route

### Task 8: Render dynamic content with Flask
  - Update the Flask app to render dynamic content
  - Pass variables to the HTML template
  - Test to ensure the dynamic content is displayed correctly

### Task 9: Render dynamic content from storage
  - Integrate Flask with a storage system
  - Retrieve dynamic content from the storage system
  - Pass the content to the HTML template
  - Test to ensure the content is displayed correctly

### Task 10: Update state
  - Modify the state of the application
  - Test to ensure the state is updated correctly

### Task 11: Add route for /states
  - Create a route to display information about states
  - Test the route to ensure it returns the expected information

### Task 12: Display cities by state
  - Retrieve information about cities based on a state
  - Display the cities on the web app
  - Test to ensure the correct cities are displayed for a given state

### Task 13: Add route for /cities_by_states
  - Create a route to display cities grouped by states
  - Test the route to ensure it returns the expected information

### Task 14: Update routes for /cities_by_states
  - Modify routes to handle different HTTP methods
  - Test the routes to ensure they handle different requests correctly

### Task 15: Display cities by state with specified storage
  - Integrate Flask with a specified storage system
  - Retrieve cities by state from the specified storage
  - Test to ensure the correct cities are displayed for a given state

### Task 16: Update states route with place objects
  - Modify the states route to handle place objects
  - Test to ensure the correct place objects are displayed for a given state

### Task 17: Display places by city
  - Retrieve places based on a city
  - Display the places on the web app
  - Test to ensure the correct places are displayed for a given city

## Advanced Features

### 0: Implement pagination for /cities_by_states route
  - Paginate the list of cities displayed on the /cities_by_states route
  - Test to ensure pagination works correctly and displays the desired number of cities per page

### 1: Implement pagination for /states route
  - Paginate the list of states displayed on the /states route
  - Test to ensure pagination works correctly and displays the desired number of states per page

### 2: Create API routes
  - Define API routes to expose data in JSON format
  - Test the API routes to ensure they return the expected JSON data

### 3: Implement filters for /states route
  - Add filters to the /states route to allow users to filter states by various criteria (e.g., name, population)
  - Test to ensure the filters work correctly and return the expected results

### 4: Implement filters for /cities_by_states route
  - Add filters to the /cities_by_states route to allow users to filter cities by various criteria (e.g., name, population)
  - Test to ensure the filters work correctly and return the expected results

### 5: Create user authentication system
  - Implement a user authentication system to restrict access to certain routes
  - Test to ensure only authenticated users can access restricted routes

### 6: Implement user permissions
  - Define different levels of user permissions (e.g., admin, regular user)
  - Restrict access to certain routes based on user permissions
  - Test to ensure users can only access routes they have permission to access

### 7: Add support for file uploads
  - Implement functionality to allow users to upload files (e.g., images, documents)
  - Test to ensure file uploads work correctly and files are stored properly

### 8: Implement error handling
  - Add error handling to the Flask app to gracefully handle exceptions and errors
  - Test to ensure error messages are displayed appropriately and the app remains stable

### 9: Implement logging
  - Integrate logging functionality into the Flask app to record events and errors
  - Test to ensure logs are generated correctly and contain useful information for debugging

### 10: Implement caching
  - Add caching functionality to the Flask app to improve performance and reduce server load
  - Test to ensure cached data is served efficiently and accurately

### 11: Implement internationalization (i18n) support
  - Add support for multiple languages in the Flask app
  - Test to ensure the app displays content in the user's preferred language

### 12: Implement session management
  - Manage user sessions securely in the Flask app
  - Test to ensure sessions are created, maintained, and destroyed properly

### 13: Implement CSRF protection
  - Protect against Cross-Site Request Forgery (CSRF) attacks by implementing CSRF tokens
  - Test to ensure CSRF protection is effective and prevents unauthorized requests

### 14: Implement rate limiting
  - Limit the number of requests a user can make to certain routes within a specified time period
  - Test to ensure rate limiting is enforced correctly and prevents abuse

### 15:
- Implement SSL/TLS encryption
  - Secure communication between clients and the Flask app using SSL/TLS encryption
  - Test to ensure data is encrypted properly and transmitted securely over HTTPS

### 16: Implement role-based access control (RBAC)
  - Define roles and permissions for different user types
  - Restrict access to routes based on user roles
  - Test to ensure RBAC is implemented correctly and restricts access as intended

### 17: Implement OAuth authentication
  - Allow users to log in to the Flask app using OAuth providers (e.g., Google, Facebook)
  - Test to ensure OAuth authentication works correctly and users can log in using their OAuth accounts


### 18: Integrate payment gateway
  - Implement functionality to accept online payments using a payment gateway (e.g., Stripe, PayPal)
  - Test to ensure payments are processed securely and successfully, with appropriate handling of payment-related errors and notification

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
