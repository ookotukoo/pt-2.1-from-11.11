# Модели с отношением один-ко-многим

Отношение один-ко-многим `one-to-many` представляет ситуацию, когда одна модель хранит ссылку на один объект другой модели, а вторая модель может ссылаться на коллекцию объектов первой модели. 

Например, в одной компании может работать несколько пользователей, а каждый пользователь в свою очередь может официально работать только в одной компании:

```python
class Person(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    company_id = Column(Integer, ForeignKey("companies.id"))  # one-to-many
    company = relationship("Company", back_populates="users")  # one-to-many

    def __repr__(self):
        return f"Person(id={self.id}, name={self.name}, age={self.age})"

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    users = relationship("Person", back_populates="company")

    def __repr__(self):
        return f"Company(id={self.id}, name={self.name})"

Base.metadata.create_all(bind=engine)
```

Здесь пользователи представлены моделью `User`, а компании - моделью `Company`. 

Оба класса имеют обычные атрибуты-столбцы - `id` и `name`. 

Но кроме того, они имеют атрибуты, которые позволяют установить отношения между моделями

Для установки отношений между моделями применяется функция `relationship()`.

Она принимает множество параметров, из которых самый первый параметр указывает на связанную модель. 

А параметр back_populates представляет атрибут связанной модели, с которой будет сопоставляться текущая модель. Например, в классе `Company` атрибут

```python
users = relationship("Person", back_populates="company")
```
указывает, что он будет связан с моделью Person через ее атрибут `"company"`.

В классе `Person` мы имеем обратную ситуацию
```python
 company = relationship("Company", back_populates="users")  # one-to-many
```

здесь атрибут `company` связан с моделью Company через ее атрибут `"users"`. 

То есть получается связь `User.company -- Company.users`.

Но какая из этих моделей будет главной и хранить список объектов, а какая будет подчиненной и хранить ссылку на один объект связанной модели?

Для этого в подчиненной модели `User` определяем атрибут-столбец, который будет представлять внешний ключ:

```python
 company_id = Column(Integer, ForeignKey("companies.id"))
```

То есть атрибут `company_id` будет представлять числовой внешний ключ на столбец `id` из таблицы `"companies"`


## Добавление данных 

Для добавления данных моделей, связанных отношением один ко многим, используются уже ранее рассмотренные методы добавления в бд. 

При этом, при добавлении одного объекта все связанные с ним объекты добавляются автоматически:



```python

def add_test_date_db():
    with Session(autoflush=False, bind=engine) as db:
        
        microsoft = Company(name="Microsoft")
        google = Company(name="Google")
        db.add_all([microsoft, google])

        db.commit()

        user1 = Person(name="Сергей", age=28)
        user2 = Person(name="Владимир", age=32)
        user1.company = microsoft
        user2.company = google
        db.add_all([user1, user2])

        db.commit()
```
### Получение данных

```python
def get_users_from_db():
    with Session(autoflush=False, bind=engine) as db:      
        users = db.query(Person).all()
        for u in users:
            try:
                print(f"{u.name} ({u.company.name if u.company.name else ''})")
            except:
                ...
        print(users[0].as_dict()) #сериализация
get_users_from_db()

```

### Получение пользователей у компаний:

```python
def get_users_from_companies():
    with Session(autoflush=False, bind=engine) as db:
        # получение всех объектов
        companies = db.query(Company).all()
        for c in companies:
            print(f"{c.name}")
            for u in c.users: print(f"{u.name}")
            print()
```

### Редактирование данных

```python

def edit_bd():
    with Session(autoflush=False, bind=engine) as db:
        user = db.query(Person).filter(Person.name == "Сергей").first()
        google = db.query(Company).filter(Company.name == "Google").first()

        if user != None and google != None:
            user.name = 'Ростислав'
            user.company = google
            db.commit()

        users = db.query(Person).all()
        for u in users:
            try:
                print(f"{u.name} ({u.company.name if u.company.name else ''})")
            except:
                ...
```


## Удаление

```python
def del_user():
    with Session(autoflush=False, bind=engine) as db:
        user = db.query(Person).filter(Person.name == "Станислав").first()
        microsoft = db.query(Company).filter(Company.name == "Microsoft").first()

        if user != None and microsoft != None:
            microsoft.users.remove(user)
            db.commit()

        # # проверяем изменение
        users = db.query(Person).all()
        for u in users:
            try:
                print(f"{u.name} ({u.company.name if u.company.name else ''})")
            except:
                ...
```


## Удаление объекта зависимой модели `(User)` из базы данных

проиходит как и в общем случае
```python
with Session(autoflush=False, bind=engine) as db:   
    user = db.query(User).filter(User.name=="Владимир").first()
    db.delete(user)
    db.commit()
```


Удаление объекта главной модели `(Company)` из базы данных зависит от настройки выражения `ON DELETE`.

Например, для выше определенных моделей `User` и `Company` отношение установливалось следующим образом:

```python
# User
company_id = Column(Integer, ForeignKey("companies.id"))
company = relationship("Company", back_populates="users")
 
#class Company
users = relationship("Person", back_populates="company")
```

В данном случае атрибут `company_id` в модели `User` может принимать значение `None` (на уровне базы данных столбец может принимать значение `NULL`). 

При удалении объекта главной модели, этот столбец `company_id` получит значение `NULL` (то есть компания для пользователя не установлена)

```python
with Session(autoflush=False, bind=engine) as db:   
    google = db.query(Company).filter(Company.name=="Google").first()
    db.delete(google)
    db.commit()
```

Однако нередко применяется каскадное удаление, при котором при удалении объекта главной модели также удаляются все связанные с ней объекты зависимой модели.

```python
cascade="all, delete-orphan" 
cascade="save-update"
cascade="all, delete"
```


* `cascade="none"` - значение по умолчанию, будет игнорировать ассоциации, поэтому разруливать зависимости придется самостоятельно.

* `cascade="save-update"`  разруливать зависимости необходимо при комите транзакции в которой делается `save()` или `update()` объекта. 
Суть разруливания заключается в том, что новые объекты, с которыми есть ассоциации у нашего, будут сохранены до него. Это позволяет обойти `constraint-violations`.

* `cascade="delete"`  надо разруливать зависимости при удалении объекта.

* `cascade="all"` обозначает выполнение каскадных операций при `save-update` и `delete`.

* `cascade="all-delete-orphan"` обозначает то же самое, что и `cascade="all"`, но к тому же  удаляет любые связанные сущности, удаленные из ассоциации (например, из коллекции).

* `cascade="delete-orphan"` будет удалять любые сущности, которые были удалены из ассоциации.



Для установки каскадного удаления в функции `relationship()` применяется параметр `cascade`, которая получает значение `"all, delete-orphan"`. 

Например, создадим новую базу данных с подобной настройкой:

```python
class Base(DeclarativeBase): pass
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    company_id = Column(Integer, ForeignKey("companies.id"))
    company = relationship("Company", back_populates="users")
 
class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    users = relationship("User", back_populates="company", cascade="all, delete-orphan")
 
Base.metadata.create_all(bind=engine)
 
with Session(autoflush=False, bind=engine) as db:
    google = Company(name="Google")
    tom = User(name="Tom")
    bob = User(name="Bob")

    google.users=[tom, bob]
    db.add(google)
    db.commit()

```

Ключевой момент здесь - установка атрибута `users` в классе `Company`:

Удалим компанию, и вместе с ней будут удалены все связанные с ней пользователи:

```python
with Session(autoflush=False, bind=engine) as db:   
    google = db.query(Company).filter(Company.name=="Google").first()   
    db.delete(google)
    db.commit()

```