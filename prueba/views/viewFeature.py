from rest_framework import generics
from rest_framework.response import Response
from ..models import Feature
from ..serializers import FeatureSerializer
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'data': data,
            "pagination": {
                "current_page": self.page.number,
                'total': self.page.paginator.count,
                "per_page": self.page.paginator.per_page,
            },     
        })

class FeatureListAPIView(generics.ListAPIView):
    serializer_class = FeatureSerializer
    queryset = Feature.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        mag_type = self.request.query_params.getlist('filters[mag_type]')
        if mag_type:
            queryset = queryset.filter(mag_type__in=mag_type)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = request.query_params.get('page')
        per_page = request.query_params.get('per_page')
        paginator = CustomPagination()
        paginator.page_size = per_page if per_page and int(per_page) <= 1000 else 1000
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = self.get_serializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)
