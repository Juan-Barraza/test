from django.urls import path
from .views import viewFeature, viewComment

urlpatterns = [
    path('features/', viewFeature.FeatureListAPIView.as_view(), name='feature-list-create'),
    path('features/<int:feature_id>/comments/', viewComment.CreateCommentAPIView.as_view(), name='create-comment')
 ]
 