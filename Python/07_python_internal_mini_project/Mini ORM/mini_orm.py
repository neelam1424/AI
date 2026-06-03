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

    #create object
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


print(User.create_table_sql())

user = User(name="Neelam", age=24)
print(user.insert_sql())