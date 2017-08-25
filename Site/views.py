from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Person
from django.views.generic import ListView,DetailView
from Site.serializers import UserSerializer, GroupSerializer, PersonSerializer


class PersonView(ListView):
    model = Person

class PersonDetailView(DetailView):
    model = Person

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = (SearchFilter,)
    filter_fields = ('first_name',)

    def list(self, request, *args, **kwargs):
        it = request.query_params.dict()
        if 'search' not in request.query_params:
            lol = {}
            for i in it:
                if i not in ('format'):
                    lol[i+''] = it[i]
            queryset = Person.objects.filter(**lol)
        else:
            queryset = Person.objects.filter(**dict(filter(lambda x: x!='search' and x!='format',it)))
        serializer = PersonSerializer(queryset, many=True)
        return Response(serializer.data)