# Tasks

## 0. README, AUTHORS
**mandatory**

- **Write a `README.md`:**
  - Description of the project
  - Description of the command interpreter:
    - How to start it
    - How to use it
    - Examples

- **You should have an `AUTHORS` file at the root of your repository**, listing all individuals having contributed content to the repository. For format, reference Docker’s [AUTHORS page](https://github.com/docker/docker/blob/master/AUTHORS).

- **You should use branches and pull requests on GitHub** - it will help you as a team to organize your work.

---

### Repo:

- GitHub repository: `AirBnB_clone`
- Files: `README.md`, `AUTHORS`

---
## 1. Be pycodestyle compliant!
**mandatory**

- **Write beautiful code that passes the `pycodestyle` checks.**

---

### Repo:

- GitHub repository: `AirBnB_clone`

---

## 2. Unittests
**mandatory**

- **All your files, classes, and functions must be tested with unit tests.**

Run the following command to verify your unit tests:

```bash
guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
```

- **Note**: This is just an example, the number of tests you create may differ from the example above.

**Warning**: 

Unit tests must also pass in non-interactive mode:

```bash
guillaume@ubuntu:~/AirBnB$ echo "python3 -m unittest discover tests" | bash
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
```

---

### Repo:

- GitHub repository: `AirBnB_clone`
- Files: `tests/`

---

## 3. BaseModel
**mandatory**


Write a class `BaseModel` that defines all common attributes/methods for other classes:

#### `models/base_model.py`

##### Public instance attributes:
- `id`: string - assigned with a unique UUID when an instance is created.
  - You can use `uuid.uuid4()` to generate a unique id, but ensure it is converted to a string.
  - The goal is to have a unique id for each `BaseModel` instance.
- `created_at`: datetime - assigned with the current datetime when an instance is created.
- `updated_at`: datetime - assigned with the current datetime when an instance is created, and it should be updated every time you change the object.

##### Public instance methods:
- `__str__`: should print: `[<class name>] (<self.id>) <self.__dict__>`
- `save(self)`: updates the public instance attribute `updated_at` with the current datetime.
- `to_dict(self)`: returns a dictionary containing all keys/values of `__dict__` of the instance:
  - By using `self.__dict__`, only instance attributes set will be returned.
  - A key `__class__` must be added to this dictionary with the class name of the object.
  - `created_at` and `updated_at` must be converted to string objects in ISO format:
    - Format: `%Y-%m-%dT%H:%M:%S.%f` (example: `2017-06-14T22:31:03.285259`).
    - You can use the `isoformat()` method of the datetime object.

This method will be the first step of the serialization/deserialization process: creating a dictionary representation with "simple object types" of your `BaseModel`.

---

#### Example Test Case:

```python
guillaume@ubuntu:~/AirBnB$ cat test_base_model.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
```

#### Expected Output:

```bash
guillaume@ubuntu:~/AirBnB$ ./test_base_model.py
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
{'my_number': 89, 'name': 'My First Model', '__class__': 'BaseModel', 'updated_at': '2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T21:05:54.119427'}
JSON of my_model:
    my_number: (<class 'int'>) - 89
    name: (<class 'str'>) - My First Model
    __class__: (<class 'str'>) - BaseModel
    updated_at: (<class 'str'>) - 2017-09-28T21:05:54.119572
    id: (<class 'str'>) - b6a6e15c-c67d-4312-9a75-9d084935e579
    created_at: (<class 'str'>) - 2017-09-28T21:05:54.119427

guillaume@ubuntu:~/AirBnB$
```

---

### Repo:

- GitHub repository: `AirBnB_clone`
- Files: `models/base_model.py`, `models/__init__.py`, `tests/`

---

## 4. Create BaseModel from dictionary
**mandatory**

Previously, we created a method (`to_dict()`) to generate a dictionary representation of an instance.

Now, it's time to re-create an instance from this dictionary representation.

The flow should be:
`<class 'BaseModel'>` → `to_dict()` → `<class 'dict'>` → `<class 'BaseModel'>`

#### Update `models/base_model.py`:

##### `__init__(self, *args, **kwargs)`:
- You will use `*args, **kwargs` arguments for the constructor of `BaseModel`.
- `*args` won’t be used.
- If `kwargs` is not empty:
  - Each key in this dictionary is an attribute name (Note: `__class__` from kwargs is the only key that should not be added as an attribute).
  - Each value of this dictionary is the corresponding value of that attribute.
  - **Warning**: `created_at` and `updated_at` are strings in this dictionary. They need to be converted to `datetime` objects. You know the string format of these datetimes, so use `datetime.strptime()` to convert them back.
- Otherwise:
  - Create `id` and `created_at` as you did previously when creating a new instance.

---

#### Example Test Case:

```python
guillaume@ubuntu:~/AirBnB$ cat test_base_model_dict.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
```

#### Expected Output:

```bash
guillaume@ubuntu:~/AirBnB$ ./test_base_model_dict.py
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
<class 'datetime.datetime'>
--
{'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': '2017-09-28T21:03:54.052298', '__class__': 'BaseModel', 'my_number': 89, 'updated_at': '2017-09-28T21:03:54.052302', 'name': 'My_First_Model'}
JSON of my_model:
    id: (<class 'str'>) - 56d43177-cc5f-4d6c-a0c1-e167f8c27337
    created_at: (<class 'str'>) - 2017-09-28T21:03:54.052298
    __class__: (<class 'str'>) - BaseModel
    my_number: (<class 'int'>) - 89
    updated_at: (<class 'str'>) - 2017-09-28T21:03:54.052302
    name: (<class 'str'>) - My_First_Model
--
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
<class 'datetime.datetime'>
--
False

guillaume@ubuntu:~/AirBnB$ 
```

---

### Repo:

- GitHub repository: `AirBnB_clone`
- Files: `models/base_model.py`, `tests/`


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
