from re import I
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins, generics
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, Http404
from django.contrib.auth.models import User
from activity.models import Activity
from activity.serializers import ActivitySerializer
from rest_framework.permissions import IsAuthenticated 
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)
#######################################################################

@api_view(['GET', 'POST'])
def list_or_create_activity(request, *args, **kwargs):
    '''
    This is an implementation of 
    activity manager using 
    function based api view
    '''
    if request.method == 'GET':
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ActivitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#######################################################################

class ActivityListCreate(APIView):
    '''
    This is an implementation of 
    activity manager using 
    class based api view
    '''
    def get(self,request, *args, **kwargs):
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = ActivitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#######################################################################

class ActivityListCreateMixin(mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              generics.GenericAPIView):
    '''
    This is an implementation of 
    activity manager using mixins
    '''
    queryset=Activity.objects.all()
    serializer_class = ActivitySerializer

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

#######################################################################

class ActivityListCreateGenericAPIView(generics.ListCreateAPIView):
    '''
    This is an implementation of 
    activity manager using generic api view
    '''
    logger.info("Have a great day")
    permission_classes = [IsAuthenticated,]
    queryset=Activity.objects.all()
    serializer_class = ActivitySerializer

#######################################################################