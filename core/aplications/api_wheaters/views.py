
from aplications.api_wheaters.api.services import get_cities_data,get_wheater_data

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

# Create your views here.


class Get_Wheaters_Cities(ListAPIView):

    def get(self, request, *args, **kwargs):

        slug_city = request.query_params.get("slug_city", None)

        if not slug_city:

            data = {"Error": "Escriba un nombre de cidad"}
            code = status.HTTP_400_BAD_REQUEST

            return Response(data, code)

        cities = get_cities_data(slug_city)
        wheaters = get_wheater_data(cities)

        return Response(wheaters, status.HTTP_200_OK)
