from django.contrib import admin
from django.urls import include, path

from strawberry.django.views import GraphQLView
from strawberry.django.views import AsyncGraphQLView

from django_project.schema import schema

urlpatterns = [
    path('my_app/', include('my_app.urls')),
    path('admin/', admin.site.urls),
    path("graphql/sync", GraphQLView.as_view(schema=schema)),
    path('graphql/', AsyncGraphQLView.as_view(schema=schema)),
]
