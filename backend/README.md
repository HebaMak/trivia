# Backend - Trivia API

## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `trivia` database:

```bash
createdb trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## To Do Tasks

These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

One note before you delve into your tasks: for each endpoint, you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior.

1. Use Flask-CORS to enable cross-domain requests and set response headers.
2. Create an endpoint to handle `GET` requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.
3. Create an endpoint to handle `GET` requests for all available categories.
4. Create an endpoint to `DELETE` a question using a question `ID`.
5. Create an endpoint to `POST` a new question, which will require the question and answer text, category, and difficulty score.
6. Create a `POST` endpoint to get questions based on category.
7. Create a `POST` endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
8. Create a `POST` endpoint to get questions to play the quiz. This endpoint should take a category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
9. Create error handlers for all expected errors including 400, 404, 422, and 500.

## Documenting your Endpoints

You will need to provide detailed documentation of your API endpoints including the URL, request parameters, and the response body. Use the example below as a reference.

### Endpoints 
#### GET /questions
- General:
  - Retrieves paginated questions with 10 questions per page.
  - Returns a list of question objects, total number of questions, and categories.
  - Supports pagination with a query parameter for the page number.
- Sample: `curl http://127.0.0.1:5000/questions?page=1`

{
  "success": true,
  "questions": [
    {
      "answer": "Cairo",
      "category": 1,
      "difficulty": 1,
      "id": 1,
      "question": "What is the capital of Egypt?"
    },
    {
      "answer": "Africa, North Africa",
      "category": 2,
      "difficulty": 2,
      "id": 2,
      "question": "on which continent is Egypt located?"
    },
    ...
  ],
  "total_questions": 20,
  "categories": {
    "1": "Science",
    "2": "History",
    ...
  }
}


#### GET /categories
- General:
  - Retrieves all available categories.
  - Returns a list of category objects.
- Sample: `curl http://127.0.0.1:5000/categories`
{
  "success": true,
  "categories": [
    {
      "id": 1,
      "type": "Science"
    },
    {
      "id": 2,
      "type": "History"
    },
    {
      "id": 3,
      "type": "Art"
    },
    {
      "id": 4,
      "type": "Geography"
    },
    {
      "id": 5,
      "type": "Entertainment"
    }
  ]
}

#### DELETE /questions/{question_id}
- General:
  - Deletes a question by its ID.
  - Returns the ID of the deleted question, success value, updated question list, and total questions.
- Sample: `curl -X DELETE http://127.0.0.1:5000/questions/5`
{
  "success": true,
  "deleted": 5,
  "questions": [
    {
      "answer": "Cairo",
      "category": 1,
      "difficulty": 1,
      "id": 1,
      "question": "What is the capital of Egypt?"
    },
    ...
  ],
  "total_questions": 19
}


#### POST /questions
- General:
  - Creates a new question.
  - Returns the ID of the created question, success value, updated question list, and total questions.
- Sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":"What is the capital of Egypt?", "answer":"Cairo", "difficulty":3, "category":2}'`

{
  "success": true,
  "created": 21,
  "questions": [
    {
      "answer": "Amsterdam",
      "category": 1,
      "difficulty": 1,
      "id": 3,
      "question": "What is the capital of Netherlands?"
    },
    ...
  ],
  "total_questions": 20
}

#### GET /categories/{category_id}/questions
- General:
  - Retrieves questions by category.
  - Returns a list of question objects filtered by the specified category ID, total number of questions, and category details.
- Sample: `curl http://127.0.0.1:5000/categories/2/questions`

{
  "success": true,
  "questions": [
    {
      "answer": "Africa, North Africa",
      "category": 2,
      "difficulty": 2,
      "id": 2,
      "question": "on which continent is Egypt located?"
    },
    ...
  ],
  "total_questions": 8,
  "category": {
    "id": 2,
    "type": "History"
  }
}

#### POST /quizzes
- General:
  - Retrieves quizzes for playing.
  - Returns a random question within the given category (if provided) and not one of the previous questions.
- Sample: `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_question":[1,2], "quiz_category":{"id":1}}'`

{
  "success": true,
  "question": {
      "answer": "Amsterdam",
      "category": 1,
      "difficulty": 1,
      "id": 3,
      "question": "What is the capital of Netherlands?"
  }
}


### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 404,
    "message": "Resource Not Found"
}
```
The API will return two error types when requests fail:
  - 404: Resource Not Found
  - 422: Unprocessable 


### Documentation Example

`GET '/api/v1.0/categories'`

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, `categories`, that contains an object of `id: category_string` key: value pairs.

```json
{
  "1": "Science",
  "2": "Art",
  "3": "Geography",
  "4": "History",
  "5": "Entertainment",
  "6": "Sports"
}
```

## Testing

Write at least one test for the success and at least one error behavior of each endpoint using the unittest library.

To deploy the tests, run

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
