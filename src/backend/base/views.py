from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import renderers, viewsets
from .models import Ticket
from .serializers import TicketSerializer
from .permissions import IsSafeOrReadOnly


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    permission_classes = (IsSafeOrReadOnly, )
    serializer_class = TicketSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        ticket = get_object_or_404(queryset, pk=kwargs['pk'])

        serializer = self.get_serializer(ticket, context={'request': request})
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer()(queryset, many=True, context={'request': request})
        return Response(serializer.data)




