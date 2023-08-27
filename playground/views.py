from django.shortcuts import render
from rest_framework.views import APIView
import logging
import requests

logger = logging.getLogger(__name__)


class HelloView(APIView):
    def get(self, request):
        try:
            logger.info("Calling httpbun.com/delay/2")
            response = requests.get("https://httpbun.com/delay/2")
            logger.info("Got response from httpbun.com/delay/2")
        except requests.ConnectionError:
            logger.critical("Could not connect to httpbun.com")
        return render(request, "hello.html", {"name": "data"})
