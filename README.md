# FastAPI CRUD with PostgreSQL

A simple CRUD project built using **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.  
This API manages a `Person` database with the following fields: `id`, `first_name`, `last_name`, and `is_male`.  
The project demonstrates **RESTful API design**, database operations, and error handling. It can be tested using **Postman** or any API client.

---

## 🚀 Features
- Create a new person (POST)
- Fetch all persons (GET)
- Fetch a person by ID (GET)
- Update person details (PUT)
- Delete a person (DELETE)
- Error handling with appropriate HTTP status codes

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **FastAPI**
- **SQLAlchemy**
- **PostgreSQL**
- **Pydantic**
- **Postman** (for testing)

---

## 📂 Project Structure 
├── main.py # FastAPI app and CRUD routes 
<br>
├── models.py # SQLAlchemy models and table creation
<br>
├── database.py # Database configuration (engine, session)
<br>
└── requirements.txt # Project dependencies

---

📬 **API Endpoints**
<br>

| Method | Endpoint                 | Description            |
| ------ | ------------------------ | ---------------------- |
| GET    | `/`                      | Fetch all persons      |
| GET    | `/persons/{person_id}` | Fetch person by ID     |
| POST   | `/persons`            | Add a new person       |
| PUT    | `/persons/{id}`    | Update existing person |
| DELETE | `/persons/{id}`    | Delete a person        |

