from rest_framework import generics, status
from rest_framework.response import Response
from ..models import Comment, Feature
from ..serializers import CommentSerializer

class CreateCommentAPIView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def create(self, request, *args, **kwargs):
        print(self.kwargs)
        feature_id = self.kwargs.get('feature_id', False)
        body = request.data.get('body', False)

        if not feature_id:
            return Response({'error': 'Feature id is required'}, status=status.HTTP_404_NOT_FOUND)

        if not body:
            return Response({'error': 'Comment body cannot be empty'}, status=status.HTTP_404_NOT_FOUND)

        try:
            feature = Feature.objects.get(id=int(feature_id))
            
        except Feature.DoesNotExist:
            return Response({'error': f'Feature with id {feature_id} does not exist'}, status=status.HTTP_404_NOT_FOUND)

        comment = Comment.objects.create(feature=feature, body=body)
        serializer = self.get_serializer(comment)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
