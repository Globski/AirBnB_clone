# Tasks

## 0. README, AUTHORS

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

---

## 5: Store first object

Now we can recreate a `BaseModel` from another one by using its dictionary representation:

`<class 'BaseModel'>` → `to_dict()` → `<class 'dict'>` → `<class 'BaseModel'>`

This works, but it’s not persistent: every time you launch the program, you lose all objects created before. To make it persistent, we will save these objects to a file.

However, writing the dictionary representation to a file won’t be effective because:
- Python doesn’t easily convert a string back to a dictionary.
- The file is not human-readable.
- It is hard to use this file with another program in Python or other languages.

Instead, we'll convert the dictionary representation into a JSON string. JSON is a standard representation of a data structure that is human-readable, and most programming languages have a JSON reader and writer.

### Serialization-Deserialization flow:

`<class 'BaseModel'>` → `to_dict()` → `<class 'dict'>` → JSON dump → `<class 'str'>` → FILE → `<class 'str'>` → JSON load → `<class 'dict'>` → `<class 'BaseModel'>`

### Implementation Details:

You need to write a `FileStorage` class that will serialize instances to a JSON file and deserialize them back to instances:

#### `models/engine/file_storage.py`

##### Private class attributes:
- `__file_path`: A string representing the path to the JSON file (e.g., `file.json`).
- `__objects`: A dictionary that will store all objects by `<class name>.id`. For example, to store a `BaseModel` object with `id=12121212`, the key will be `BaseModel.12121212`.

##### Public instance methods:
- `all(self)`: Returns the dictionary `__objects`.
- `new(self, obj)`: Sets in `__objects` the object `obj` with the key `<obj class name>.id`.
- `save(self)`: Serializes `__objects` to the JSON file (using the `__file_path`).
- `reload(self)`: Deserializes the JSON file to `__objects` (only if the JSON file exists; otherwise, do nothing). If the file doesn’t exist, no exception should be raised.

#### `models/__init__.py`
- Create a unique instance of `FileStorage` for your application.
- Initialize the `storage` variable, an instance of `FileStorage`.
- Call the `reload()` method on the `storage` variable.

#### `models/base_model.py`
- Link your `BaseModel` to `FileStorage` by using the `storage` variable.
- In the `save(self)` method, call the `save()` method of the `storage` instance.
- In `__init__(self, *args, **kwargs)`, if it's a new instance (not from a dictionary), call the `new(self)` method of `storage`.

### Example test case:

```python
guillaume@ubuntu:~/AirBnB$ cat test_save_reload_base_model.py
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
guillaume@ubuntu:~/AirBnB$ cat file.json
cat: file.json: No such file or directory
guillaume@ubuntu:~/AirBnB$ 
```

#### Expected Output:

```bash
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
-- Create a new object --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d'}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"my_number": 89, "__class__": "BaseModel", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372)}
-- Create a new object --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'name': 'My_First_Model', 'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301)}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301), 'name': 'My_First_Model', 'my_number': 89}
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'my_number': 89}
-- Create a new object --
[BaseModel] (e79e744a-55d4-45a3-b74a-ca5fae74e0e2) {'id': 'e79e744a-55d4-45a3-b74a-ca5fae74e0e2', 'updated_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151750), 'created_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151711), 'name': 'My_First_Model', 'my_number': 89}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.e79e744a-55d4-45a3-b74a-ca5fae74e0e2": {"__class__": "BaseModel", "id": "e79e744a-55d4-45a3-b74a-ca5fae74e0e2", "updated_at": "2017-09-28T21:08:06.151750", "created_at": "2017-09-28T21:08:06.151711", "name": "My_First_Model", "my_number": 89}, "BaseModel.080cce84-c574-4230-b82a-9acb74ad5e8c": {"__class__": "BaseModel", "id": "080cce84-c574-4230-b82a-9acb74ad5e8c", "updated_at": "2017-09-28T21:07:51.973308", "created_at": "2017-09-28T21:07:51.973301", "name": "My_First_Model", "my_number": 89}, "BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"__class__": "BaseModel", "id": "ee49c413-023a-4b49-bd28-f2936c95460d", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "my_number": 89}}
guillaume@ubuntu:~/AirBnB$ 
```

---

### Repo:
- GitHub repository: `AirBnB_clone`
- Files: `models/engine/file_storage.py`, `models/engine/__init__.py`, `models/__init__.py`, `models/base_model.py`, `tests/`

## 7: Console 0.1

Update your command interpreter (`console.py`) to have these commands:

1. **create**: Creates a new instance of `BaseModel`, saves it (to the JSON file), and prints the `id`. 
   - Ex: `$ create BaseModel`
   - If the class name is missing, print **class name missing** (Ex: `$ create`)
   - If the class name doesn’t exist, print **class doesn't exist** (Ex: `$ create MyModel`)

2. **show**: Prints the string representation of an instance based on the class name and `id`.
   - Ex: `$ show BaseModel 1234-1234-1234`
   - If the class name is missing, print **class name missing** (Ex: `$ show`)
   - If the class name doesn’t exist, print **class doesn't exist** (Ex: `$ show MyModel`)
   - If the `id` is missing, print **instance id missing** (Ex: `$ show BaseModel`)
   - If the instance of the class name doesn’t exist for the `id`, print **no instance found** (Ex: `$ show BaseModel 121212`)

3. **destroy**: Deletes an instance based on the class name and `id` (saves the change into the JSON file).
   - Ex: `$ destroy BaseModel 1234-1234-1234`
   - If the class name is missing, print **class name missing** (Ex: `$ destroy`)
   - If the class name doesn’t exist, print **class doesn't exist** (Ex: `$ destroy MyModel`)
   - If the `id` is missing, print **instance id missing** (Ex: `$ destroy BaseModel`)
   - If the instance of the class name doesn’t exist for the `id`, print **no instance found** (Ex: `$ destroy BaseModel 121212`)

4. **all**: Prints all string representation of all instances based or not on the class name.
   - Ex: `$ all BaseModel` or `$ all`
   - The printed result must be a list of strings (like the example below)
   - If the class name doesn’t exist, print **class doesn't exist** (Ex: `$ all MyModel`)

5. **update**: Updates an instance based on the class name and `id` by adding or updating an attribute (saves the change into the JSON file).
   - Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`
   - Usage: `update <class name> <id> <attribute name> "<attribute value>"`
   - Only one attribute can be updated at a time.
   - You can assume the attribute name is valid (exists for this model).
   - The attribute value must be cast to the attribute type.
   - If the class name is missing, print **class name missing** (Ex: `$ update`)
   - If the class name doesn’t exist, print **class doesn't exist** (Ex: `$ update MyModel`)
   - If the `id` is missing, print **instance id missing** (Ex: `$ update BaseModel`)
   - If the instance of the class name doesn’t exist for the `id`, print **no instance found** (Ex: `$ update BaseModel 121212`)
   - If the attribute name is missing, print **attribute name missing** (Ex: `$ update BaseModel existing-id`)
   - If the value for the attribute name doesn’t exist, print **value missing** (Ex: `$ update BaseModel existing-id first_name`)
   - All other arguments should not be used (Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty"` = `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`).
   - `id`, `created_at`, and `updated_at` can’t be updated. You can assume they won’t be passed in the update command.
   - Only “simple” arguments can be updated: string, integer, and float. You can assume nobody will try to update lists of ids or datetime.

### Error Management:
- Arguments are always in the right order.
- Each argument is separated by a space.
- A string argument with a space must be between double quotes.
- The error management starts from the first argument to the last one.

### Example Interaction:

```bash
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb)
```

No unittests needed

---

### Repo:
- GitHub repository: `AirBnB_clone`
- Files: `console.py`

## 8. First User

1. **Create a class `User`** that inherits from `BaseModel` in `models/user.py`.
   
   **Public class attributes**:
   - `email: string` - empty string
   - `password: string` - empty string
   - `first_name: string` - empty string
   - `last_name: string` - empty string

2. **Update `FileStorage`** to manage the correct serialization and deserialization of the `User` class.

3. **Update your command interpreter (`console.py`)** to allow:
   - `show`
   - `create`
   - `destroy`
   - `update`
   - `all`
   
   These commands should work for the `User` class as they do for `BaseModel`.

---

### Example:

```bash
guillaume@ubuntu:~/AirBnB$ cat test_save_reload_user.py
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)

guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"__class__": "BaseModel", "id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "updated_at": "2017-09-28T21:11:14.333862", "created_at": "2017-09-28T21:11:14.333852"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"__class__": "BaseModel", "id": "a42ee380-c959-450e-ad29-c840a898cfce", "updated_at": "2017-09-28T21:11:15.504296", "created_at": "2017-09-28T21:11:15.504287"}, "BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"__class__": "BaseModel", "id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "updated_at": "2017-09-28T21:11:12.971544", "created_at": "2017-09-28T21:11:12.971521"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"__class__": "BaseModel", "id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "updated_at": "2017-09-28T21:11:13.753347", "created_at": "2017-09-28T21:11:13.753337"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"__class__": "BaseModel", "id": "9bf17966-b092-4996-bd33-26a5353cccb4", "updated_at": "2017-09-28T21:11:14.963058", "created_at": "2017-09-28T21:11:14.963049"}}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_user.py
-- Reloaded objects --
[BaseModel] (38a22b25-ae9c-4fa9-9f94-59b3eb51bfba) {'id': '38a22b25-ae9c-4fa9-9f94-59b3eb51bfba', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753337), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753347)}
[BaseModel] (9bf17966-b092-4996-bd33-26a5353cccb4) {'id': '9bf17966-b092-4996-bd33-26a5353cccb4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963049), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963058)}
[BaseModel] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {'id': '2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333852), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333862)}
[BaseModel] (a42ee380-c959-450e-ad29-c840a898cfce) {'id': 'a42ee380-c959-450e-ad29-c840a898cfce', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504287), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504296)}
[BaseModel] (af9b4cbd-2ce1-4e6e-8259-f578097dd15f) {'id': 'af9b4cbd-2ce1-4e6e-8259-f578097dd15f', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971521), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971544)}
-- Create a new User --
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'id': '38f22813-2753-4d42-b37c-57a17f1e4f88', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'email': 'airbnb@mail.com', 'first_name': 'Betty', 'last_name': 'Bar', 'password': 'root'}
-- Create a new User 2 --
[User] (d0ef8146-4664-4de5-8e89-096d667b728e) {'id': 'd0ef8146-4664-4de5-8e89-096d667b728e', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848280), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848294), 'email': 'airbnb2@mail.com', 'first_name': 'John', 'password': 'root'}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "updated_at": "2017-09-28T21:11:12.971544", "created_at": "2017-09-28T21:11:12.971521", "__class__": "BaseModel"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "updated_at": "2017-09-28T21:11:13.753347", "created_at":

 "2017-09-28T21:11:13.753337", "__class__": "BaseModel"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"id": "9bf17966-b092-4996-bd33-26a5353cccb4", "updated_at": "2017-09-28T21:11:14.963058", "created_at": "2017-09-28T21:11:14.963049", "__class__": "BaseModel"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"id": "a42ee380-c959-450e-ad29-c840a898cfce", "updated_at": "2017-09-28T21:11:15.504296", "created_at": "2017-09-28T21:11:15.504287", "__class__": "BaseModel"}, "BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "updated_at": "2017-09-28T21:11:14.333862", "created_at": "2017-09-28T21:11:14.333852", "__class__": "BaseModel"}, "User.38f22813-2753-4d42-b37c-57a17f1e4f88": {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at": "2017-09-28T21:11:42.848279", "updated_at": "2017-09-28T21:11:42.848291", "email": "airbnb@mail.com", "first_name": "Betty", "last_name": "Bar", "password": "root", "__class__": "User"}, "User.d0ef8146-4664-4de5-8e89-096d667b728e": {"id": "d0ef8146-4664-4de5-8e89-096d667b728e", "created_at": "2017-09-28T21:11:42.848280", "updated_at": "2017-09-28T21, 11:42.848294", "email": "airbnb2@mail.com", "first_name": "John", "password": "root", "__class__": "User"}}
guillaume@ubuntu:~/AirBnB$ 
```

No unittests needed for the console

--- 

### Repo:
- GitHub repository: `AirBnB_clone`
- Files: `models/user.py`, `models/engine/file_storage.py`, `console.py`, `tests/`

---

## 9. More Classes!

Write all the following classes that inherit from `BaseModel`:

1. **State** (`models/state.py`):
   - **Public class attribute**:
     - `name: string` - empty string

2. **City** (`models/city.py`):
   - **Public class attributes**:
     - `state_id: string` - empty string (will reference the `State.id`)
     - `name: string` - empty string

3. **Amenity** (`models/amenity.py`):
   - **Public class attribute**:
     - `name: string` - empty string

4. **Place** (`models/place.py`):
   - **Public class attributes**:
     - `city_id: string` - empty string (will reference the `City.id`)
     - `user_id: string` - empty string (will reference the `User.id`)
     - `name: string` - empty string
     - `description: string` - empty string
     - `number_rooms: integer` - 0
     - `number_bathrooms: integer` - 0
     - `max_guest: integer` - 0
     - `price_by_night: integer` - 0
     - `latitude: float` - 0.0
     - `longitude: float` - 0.0
     - `amenity_ids: list of string` - empty list (to later reference the `Amenity.id`)

5. **Review** (`models/review.py`):
   - **Public class attributes**:
     - `place_id: string` - empty string (will reference the `Place.id`)
     - `user_id: string` - empty string (will reference the `User.id`)
     - `text: string` - empty string

---

### Repo:

- GitHub repository: `AirBnB_clone`
- Files:
  - `models/state.py`
  - `models/city.py`
  - `models/amenity.py`
  - `models/place.py`
  - `models/review.py`
  - `tests/`

---

## 10. Console 1.0

1. **Update `FileStorage`**:
   - Modify the `FileStorage` class to handle the correct serialization and deserialization of the newly created classes:
     - `Place`
     - `State`
     - `City`
     - `Amenity`
     - `Review`

2. **Update the command interpreter (`console.py`)**:
   - Modify the command interpreter to allow the following actions for all previously created classes:
     - `show`
     - `create`
     - `destroy`
     - `update`
     - `all`

3. **No unittests needed for the console**.

---

### Repo:

- GitHub repository: `AirBnB_clone`
- Files:
  - `console.py`
  - `models/engine/file_storage.py`
  - `tests/`

---

## 11. All instances by class name

- Update your command interpreter (`console.py`) to enable retrieving all instances of a class by using the following command syntax:

  ```bash
  <class_name>.all()
  ```

  For example:

  ```bash
  (hbnb) User.all()
  ```

  This should display all instances of the `User` class stored in memory.

### Example:

```bash
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.all()
[[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@mail.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}, [User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}]
```

### No unittests needed.

---

### Repo:

- GitHub repository: `AirBnB_clone`
- File: `console.py`

---

## 12. Count instances

- Update your command interpreter (`console.py`) to allow retrieving the number of instances of a class using the following syntax:

  ```bash
  <class_name>.count()
  ```

  For example:

  ```bash
  (hbnb) User.count()
  ```

  This should return the number of instances of the `User` class.

### Example:

```bash
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.count()
2
```

This command will display the number of `User` instances stored in memory.

### No unittests needed.

---

### Repo:

- GitHub repository: `AirBnB_clone`
- File: `console.py`

---

## 13. Show

- Update your command interpreter (`console.py`) to retrieve an instance based on its ID using the following syntax:

  ```bash
  <class_name>.show(<id>)
  ```

  For example:

  ```bash
  (hbnb) User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
  ```

  This should display the instance of the class with the specified ID.

- Error management must behave as it has for previous commands. If an invalid ID is provided (e.g., an ID not found), the interpreter should return an error message like:

  ```bash
  ** no instance found **
  ```

### Example:

```bash
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@mail.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}
(hbnb) User.show("Bar")
** no instance found **
```

### No unittests needed.

---

### Repo:

- GitHub repository: `AirBnB_clone`
- File: `console.py`

---

