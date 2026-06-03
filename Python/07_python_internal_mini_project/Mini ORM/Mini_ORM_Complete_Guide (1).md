# Mini ORM in Python — Complete Beginner Guide

## What You Will Learn
- What ORM is
- Why ORMs exist
- SQL fundamentals
- Object Relational Mapping
- Class Introspection
- __dict__
- setattr()
- getattr()
- Dynamic Attribute Handling
- SQL Generation
- How Django ORM Works Internally
- How SQLAlchemy Works Internally
- How Prisma Works Internally

## Problem Statement

Build a Mini ORM that can:
1. Define database fields using Python classes.
2. Define database tables using Python models.
3. Generate CREATE TABLE SQL.
4. Generate INSERT SQL.
5. Convert Python objects into database rows.

## Core Idea

Python Class → Database Table

```python
class User(Model):
    table_name = "users"
    name = StringField()
    age = IntegerField()
```

becomes:

```sql
CREATE TABLE users (name TEXT, age INTEGER);
```

Python Object → Database Row

```python
user = User(name="Neelam", age=24)
```

becomes:

```sql
INSERT INTO users (name, age) VALUES ('Neelam', 24);
```

## Algorithm

1. Create Field class to store SQL datatype.
2. Create StringField and IntegerField.
3. Create Model base class.
4. Store object values using kwargs and setattr().
5. Read model fields using cls.__dict__.
6. Generate CREATE TABLE SQL.
7. Read object values using getattr().
8. Generate INSERT SQL.

## Complete Code

```python
class Field:
    def __init__(self, field_type):
        self.field_type = field_type


class StringField(Field):
    def __init__(self):
        super().__init__("TEXT")


class IntegerField(Field):
    def __init__(self):
        super().__init__("INTEGER")


class Model:
    table_name = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def create_table_sql(cls):
        columns = []

        for name, value in cls.__dict__.items():
            if isinstance(value, Field):
                columns.append(f"{name} {value.field_type}")

        table = cls.table_name or cls.__name__.lower()

        return f"CREATE TABLE {table} ({', '.join(columns)});"

    def insert_sql(self):
        fields = []
        values = []

        for name, value in self.__class__.__dict__.items():
            if isinstance(value, Field):
                fields.append(name)
                values.append(repr(getattr(self, name)))

        table = self.table_name or self.__class__.__name__.lower()

        return f"INSERT INTO {table} ({', '.join(fields)}) VALUES ({', '.join(values)});"


class User(Model):
    table_name = "users"

    name = StringField()
    age = IntegerField()
```

## Working of Each Part

### Field Class
Represents one database column and stores SQL datatype.

### StringField
Represents TEXT column.

### IntegerField
Represents INTEGER column.

### Model Class
Provides ORM functionality to all models.

### setattr()
Converts:

```python
User(name="Neelam")
```

into:

```python
self.name = "Neelam"
```

### create_table_sql()
Reads field definitions from the class and generates CREATE TABLE SQL.

### insert_sql()
Reads object values and generates INSERT INTO SQL.

### __dict__
Used to inspect class attributes.

Example:

```python
User.__dict__
```

contains:

```python
table_name
name
age
```

### getattr()
Used to dynamically fetch values.

```python
getattr(user, "name")
```

returns:

```python
"Neelam"
```

## Dry Run

1. User.create_table_sql()
2. Read fields: name, age
3. Generate:

```sql
CREATE TABLE users (name TEXT, age INTEGER);
```

4. Create object:

```python
user = User(name="Neelam", age=24)
```

5. Generate:

```sql
INSERT INTO users (name, age) VALUES ('Neelam', 24);
```

## Workflow Diagram

Python Class
↓
ORM Reads Fields
↓
CREATE TABLE SQL

Python Object
↓
ORM Reads Values
↓
INSERT SQL

## Time Complexity

create_table_sql() → O(number_of_fields)

insert_sql() → O(number_of_fields)

## Resume Bullet

Built a Mini ORM in Python using class introspection, dynamic attributes, and SQL generation to map Python classes to database tables and objects to SQL INSERT statements.
