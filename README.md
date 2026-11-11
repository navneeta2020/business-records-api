

\# Business Records API



A REST API built using Python, FastAPI and SQLAlchemy

to manage business records.



\## Features



\- Create business records

\- Retrieve all business records

\- Retrieve records by ID

\- Update existing records

\- Delete business records

\- SQLite database integration

\- Interactive Swagger API documentation

\- HTTP error handling



\## Technologies



\- Python 3.10

\- FastAPI

\- SQLAlchemy

\- SQLite

\- Uvicorn

\- Pydantic

\- Swagger UI



\## Installation



1\. Clone or download this project.



2\. Create a virtual environment:



&#x20;  python -m venv venv



3\. Activate it on Windows:



&#x20;  venv\\Scripts\\activate



4\. Install dependencies:



&#x20;  pip install -r requirements.txt



5\. Start the application:



&#x20;  uvicorn main:app --reload



6\. Open Swagger documentation:



&#x20;  http://127.0.0.1:8000/docs



\## API Endpoints



| Method | Endpoint | Description |

|--------|----------|-------------|

| POST | /records/ | Create record |

| GET | /records/ | Get all records |

| GET | /records/{record\_id} | Get one record |

| PUT | /records/{record\_id} | Update record |

| DELETE | /records/{record\_id} | Delete record |



\## Database



SQLite is used for persistent local storage.

The database file is created automatically

when the application starts.



\## Author



Navneeta Sinha



