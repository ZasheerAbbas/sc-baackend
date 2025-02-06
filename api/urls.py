from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()

routers.register('roles', views.RoleViewSet, basename='role')
routers.register('users', views.UserViewSet, basename='user')
routers.register('users-unpaginated', views.UserListViewSet, basename='users')

urlpatterns = [
    path('login', views.LoginView.as_view()),
    path('logout', views.LogoutView.as_view()),
    path('refresh', views.RefreshView.as_view()),
    path('current', views.CurrentUserView.as_view()),
    path('permissions', views.PermissionListView.as_view()),
    # path('uploadPetitionApplicationData', views.PetitionApplicationListView.as_view()),
    # path('downloadPetitionApplicationData', views.PetitionApplicationDownloadView.as_view()),
    path('profile/<int:pk>', views.ProfileUpdateView.as_view()),
    path('changepassword',views.UserChangePasswordView.as_view()),
]

urlpatterns += routers.urls
