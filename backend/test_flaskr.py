import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format("localhost:5432", self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {
            "question": "What is the name of the first programmable computer invented by Konrad Zuse, and in what year was it completed?",
            "answer": " Z3, 1941",
            "difficulty": 3,
            "category": 1
        }
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
            
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    
    # test pagination implementation
    def test_get_paginated_questions(self):
        res = self.client.get("/questions")
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_questions"])
        self.assertTrue(len(data["questions"]))
        
    def test_404_sent_requesting_beyond_valid_page(self):
        res = self.client.get("/questions?page=1000", json={"difficulty": 1})
        data = json.loads(res.data)
        
        self.assertEqual(res.result_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Resource Not Found")
        
        
    # test retrieve categories
    def test_retrieve_categories(self):
        res = self.client().get("/categories")
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["categories"])
        self.assertTrue(len(data["categories"]))
        
    def test_404_retrieve_categories_fail(self):
        res = self.client().get("/categories")
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["message"], "Resource Not Found")
        
        
    # test retrieve all question
    def test_retrieve_questions(self):
        res = self.client().get("/questions")
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["questions"])
        self.assertTrue(data["categories"])
        self.assertTrue(len(data["questions"]))
        
    def test_404_retrieve_questions(self):
        res = self.client().get("/questions")
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["message"], "Resource Not Found")
        
        
    # test delete a question
    def test_delete_question(self):
        res = self.client.delete("/book/1")
        data = json.loads(res.data)
        
        question = Question.query.filter(Question.id == 1).one_or_none()
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["deleted"], 1)
        self.assertTrue(data["total_questions"])
        self.assertTrue(len(data["questions"]))
        self.assertEqual(question, None)
        
    def test_404_if_question_does_not_exist(self):
        res = self.client.delete("/questions/1000")
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Resource Not Found")
        
        
    # test create and search question for a question
    # test create question
    def test_create_question(self):
        res = self.client().post("/questions", json=self.new_question)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertequal(data["success"], True)
        self.assertTrue(data["created"])
        self.assertTrue(data["total_questions"])
        
    def test_422_create_question_fails(self):
        res = self.client().post("/questions", json=self.new_question)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertequal(data["success"], False)
        self.assertEqual(data["message"], "Unprocessable")
        
    # test search question
    def test_search_question(self):
        res = self.client().post("/questions", json={"searchTerm": "question"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["question"], True)
        
    def test_422_search_question_fail(self):
        res = self.client().post("/questions", json={"searchTerm": "not_existent_content"})
        data = json.loads(res.data)
        
        self.assertEqual(res.stTus_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Unprocessable")
        
        
    # test retrieve question by category
    def test_retrieve_questions_by_category(self):
        res = self.client().get("categories/1/questions")
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["questions"])
        self.assertTrue(data["categories"])
    
    def test_404_retrieve_question_by_category(self):
        res = self.client().get("/categories/1000/question")
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Resource Not Found")


    # test retrieve quizzes
    def test_retrieve_quizzes(self):
        res = self.client().post("/quizzes", json= {"previous_question": [1,2,3], "quiz_category": {id: 1, type: "Science"}})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["question"])
        
    def test_422_retrieve_quizzes_fail(self):
        res = self.client().post("/quizzes", json= {"previous_question": []})
        data = json.loads(res.data)
        
        self.assertEqual(res.stTus_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Unprocessable")

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()