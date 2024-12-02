from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


def home(request):
    return HttpResponse("<h1>Welcome to Coffee Shop!</h1>")


class StaticInfoView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        static_info = {
            "location": "ул. Амир Темур, 45, Ташкент, Узбекистан",
            "working_hours": {
                "monday_friday": "8:00 - 22:00",
                "saturday": "9:00 - 20:00",
                "sunday": "9:00 - 18:00"
            },
            "contacts": {
                "phone": "+998-90-123-45-67",
                "email": "info@coffee-takeaway.uz"
            },
            "additional_info": "Все напитки только на вынос. Доступен предварительный заказ через приложение."
        }
        return Response(static_info)
