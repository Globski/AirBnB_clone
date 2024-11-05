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
