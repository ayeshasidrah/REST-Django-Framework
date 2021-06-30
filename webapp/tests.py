from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from . models import mobiles
from . serializers import mobilesSerializer
import requests
import pytest
import json

def test_get_name():
    response = requests.get("http://localhost:8000/mobiles/")
    assert response.status_code == 200


def test_get_performances():
    response = requests.get("http://localhost:8000/mobiles/")
    response_body = response.json()
    assert response_body["performance"] == "excellent"

