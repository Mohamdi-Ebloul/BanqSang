from http import client
from urllib import response
from django.test import TestCase,Client
from django.urls import reverse
from donor.models import BloodDonate,Donor
import json
# Create your tests here.


class TestViews(TestCase):
    def test_Myapp(self):
        client=Client()

        response = client.get(reverse('donor-dashboard'))


        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'donor/donor_dashboard.htmls')