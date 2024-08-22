# stories/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from .models import Story, Contribution
from .serializers import StorySerializer, ContributionSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

class StoryListCreate(generics.ListCreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    @extend_schema(
        summary="List all stories",
        description="Returns a list of all existing stories.",
        responses={200: StorySerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Create a new story",
        description="Create a new story instance.",
        request={
            'multipart/form-data': {
                'type': 'object',
                'properties': {
                    'title': {'type': 'string'},
                    'image': {'type': 'string', 'format': 'binary'}
                }
            }
        },
        responses={201: StorySerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    summary="Retrieve a specific story",
    description="Get details of a specific story by its ID.",
    responses={200: StorySerializer}
)
class StoryDetail(generics.RetrieveAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def get(self, request, *args, **kwargs):
        story = get_object_or_404(Story, pk=kwargs['pk'])
        serializer = self.get_serializer(story)
        return Response(serializer.data)
    
    
@extend_schema(
    summary="Add a contribution to a story",
    description="Add a new contribution to a specific story.",
    parameters=[
        OpenApiParameter(name='pk', description='ID of the story', required=True, type=int)
    ],
    request=ContributionSerializer,
    responses={
        201: ContributionSerializer,
        400: OpenApiTypes.OBJECT
    }
)
class AddContribution(generics.CreateAPIView):
    serializer_class = ContributionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def create(self, request, *args, **kwargs):
        story = get_object_or_404(Story, pk=kwargs['pk'])
        if story.contributions.count() >= 4:
            return Response({"detail": "Story is already completed."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, story=story)
            if story.contributions.count() == 4:
                story.completed = True
                story.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
