# Music-Api-FlaskRestful
This is a simple project with python using FlaskRestful and other libraries, where you can update, delete, add and view  different songs  registered by users.

## Features

- **GET /music**: Return all musics stored in database.

- **GET /music/{id}**: Returns one music by `id`.

- **POST /music**: Add one new music to database.

- **PUT /music/{id}**: Update data of a existing music `id`.

- **DELETE /music/{id}**: Delete a specif music by `id`.

## Libraries Used

- **Flask**: Development framework.

- **Flask-RESTful**: Flask extension to create RESTful Apis quickly and in an organized way.

- **Flask-SQLAlchemy**: Flask extension to integrate with SQL databases using SQLalchemy.

- **python-dotenv**: To load environment variables from a  `.env` file.

## Database creation

The creation of database is done in the config.py file, where de SQLite database URI is defined.

## Database initialization

The database will be automatically created when the aplication is run, if the tables do not already exist. This occurs in the code where the initialization is done within app.py

## How to install Dependencies 

1. **Clone the repository**

```bash
git clone https://github.com/RicardoNardaoBelmonte/ApiFlask.git
```

2. **Active the virtual environment**

```bash
.\flask\Scripts\activate
```

3. **Download dependencies**

```bash
pip install -r requirements.txt
```

4. **Run app.py**

```bash
python app.py
``` 