from django.test import TestCase

from Tools.Mailer.mailer import Mailer

class Example1TestCase(TestCase):
    def setUp(self):
        pass

    def test_ex1(self):
        """Format mail into text"""
        assert Mailer().format_email_text() == 1