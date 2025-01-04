from django.test import TestCase

from Tools.Mailer.mailer import Mailer


class MailerTestCase(TestCase):
    def setUp(self):
        pass

    def test_format_email_text(self):
        """Format mail into text"""
        assert Mailer().format_email_text() == 1