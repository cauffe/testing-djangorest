#django basic testing imports
from django.test import TestCase
from task.models import Task, Category, Tag

#django rest framework testing imports
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .serializers import *

class TaskTestCase(TestCase):
    def setUp(self):
    	test_category = Category.objects.create(name="weekly", description="weekly task")
        Task.objects.create(name="task1", description="task one", priority=5, due_date='2015-05-27 01:51:06', category=test_category )
        Task.objects.create(name="task2", description="task two", priority=5, due_date='2015-05-27 01:51:06', category=test_category )

    def test_task_creation(self):
        """Testing Task Names"""
        task1 = Task.objects.get(name="task1")
        task2 = Task.objects.get(name="task2")
        self.assertEqual(task1.name, 'task1')
        self.assertEqual(task2.name, 'task2')



class AccountTests(APITestCase):
    def test_create_task(self):
        """
        Ensure we can create a new Category object.
        """
        test_category = Category.objects.create(name="weekly", description="weekly task")
        test_tag = Tag.objects.create(name="Test Tag")

        url = '/tasks' #reverse('tasks')
        data = {'category': 1, 'due_date': '2010-06-15 05:05', 'name': '12345', 'tags': [1], 'priority': '9', 'description': '1237'}
        response = self.client.post(url, data, format='json')

        print "the raw response"
        print response
        print "- response.data output -"
        print response.data
        print "- response.rendered_content output-"
        print response.rendered_content
        print "---"
        print dir(response)
        print "---"

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.rendered_content, data)
        #self.assertEqual(response.data, data)