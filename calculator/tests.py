from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
