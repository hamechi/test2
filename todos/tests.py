from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from todos.models import Todo


class TodosAPITestCase(APITestCase):

    def authenticated(self):
        self.client.post(
            "/dj-rest-auth/registration/", {"username": "username",
                                  "email": "email@gmail.com",
                                  "password1": "password49",
                                  "password2": "password49"})

        response = self.client.post(
            "/dj-rest-auth/login/", {"username": "username",
                               "password": "password49"})

        self.client.credentials(HTTP_AUTHORIZATION =
                                f"Bearer {response.data['access_token']}")

    def create_todo(self):
        sample_todo = {"title": "Hello", "desc": "Test"}
        response = self.client.post(reverse("todos"), sample_todo)
        return response


class TestListCreateTodos(TodosAPITestCase):

    def test_should_create_todo(self):
        previous_todo_count = Todo.objects.all().count()
        self.authenticated()

        response = self.create_todo()
        self.assertEqual(Todo.objects.all().count(),
                         previous_todo_count+1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Hello')
        self.assertEqual(response.data['desc'], 'Test')

    def test_retrieves_all_todos(self):
        self.authenticated()
        response = self.client.get(reverse("todos"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['results'], list)

        self.create_todo()
        res = self.client.get(reverse("todos"))
        self.assertIsInstance(res.data['count'], int)
        self.assertEqual(res.data['count'], 1)


class TestDetailTodos(TodosAPITestCase):

    def test_retrieves_one_item(self):
        self.authenticated()
        response = self.create_todo()

        res = self.client.get(reverse("todo",
                                      kwargs={'id': response.data['id']}))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        todo = Todo.objects.get(id=response.data['id'])
        self.assertEqual(todo.title, res.data['title'])

    def test_update_one_item(self):
        self.authenticated()
        response = self.create_todo()

        res = self.client.patch(reverse("todo", kwargs={'id': response.data['id']}),
                                    {"title": "Happy",
                                     "desc": "Feel Good",
                                     "is_complete": True})
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        update_todo = Todo.objects.get(id=response.data['id'])
        self.assertEqual(update_todo.title, 'Happy')
        self.assertEqual(update_todo.desc, 'Feel Good')
        self.assertEqual(update_todo.is_complete, True)

    def test_deletes_one_item(self):
        self.authenticated()
        res = self.create_todo()
        prev_db_count = Todo.objects.all().count()

        self.assertGreater(prev_db_count, 0)
        self.assertEqual(prev_db_count, 1)

        response = self.client.delete(
            reverse("todo", kwargs={'id': res.data['id']})
            )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
