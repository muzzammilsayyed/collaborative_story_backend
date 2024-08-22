
# Collaborative Story Creator API

## Project Overview

The Collaborative Story Creator API is a backend service designed to manage collaborative storytelling. Users can create stories, contribute to ongoing stories, and view completed stories. The API supports JWT-based authentication, image uploads, and includes Swagger documentation for easy exploration of endpoints.

## Installation Instructions

### Prerequisites

- Python 3.x
- pip (Python package installer)
- MySQL (or compatible database)

### Setup

1. **Clone the repository:**
```
git clone [repository-url]
```
2. **Navigate to the project directory:**
```
cd [project-directory]
```
3. **Create and activate a virtual environment:**

On Windows:
```
python -m venv env
   
.\env\Scripts\activate
```
On macOS/Linux:
```
python -m venv env
source env/bin/activate
```
4. Install dependencies:

```
pip install -r requirements.txt
```

5. **Set up environment variables:**

Create a .env file in the project root directory and add the following variables:

```
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=db_name
DB_USER=db_user
DB_PASSWORD=yourpass
DB_HOST=localhost
DB_PORT=3306
```
Apply database migrations:

```
python manage.py migrate
```
Create a superuser (optional, for admin access):

```
python manage.py createsuperuser
```

Start the development server:

```
python manage.py runserver
```

# API Documentation:
 Swagger Documentation:

The API comes with Swagger documentation for easy exploration of all available endpoints. You can access it at:

```
http://localhost:8000/api/schema/swagger-ui/
```
Key Endpoints Overview
Authentication
```
POST /api/auth/register/: Register a new user.
```
```
POST /api/auth/login/: Login and obtain a JWT token.
```
Story Management
```
GET /api/stories/: List all stories.
```
POST /api/stories/: Create a new story (requires authentication).
```
GET /api/stories/{id}/: Retrieve details of a specific story.
```
```
POST /api/stories/{id}/contribute/: Contribute to an ongoing story 
```


Testing
The project includes unit tests for key components. To run the tests, use:

```
python manage.py test
```
This will run all the tests and display the results in the terminal.




