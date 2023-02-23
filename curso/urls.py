from django.urls import path, reverse_lazy
from .views import Homepage, Courses, DetailCourses, Pesquisa, Paginaperfil, Criarconta
from django.contrib.auth import views as auth_view

app_name = 'curso'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('courses', Courses.as_view(), name='courses'),
    path('courses/<int:pk>', DetailCourses.as_view(), name='DetailCourses'),
    path('pesquisa/', Pesquisa.as_view(), name='PesquisaCurso'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/<int:pk>', Paginaperfil.as_view(), name='editarperfil'),
    path('criarconta/', Criarconta.as_view(), name='criarconta'),
    path('mudarsenha/' , auth_view.PasswordChangeView.as_view(template_name='editarperfil.html' ,
                                                              success_url=reverse_lazy('filme:homefilmes')), name='mudarsenha'),
]


