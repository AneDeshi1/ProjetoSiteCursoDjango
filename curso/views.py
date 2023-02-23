from django.shortcuts import render, redirect, reverse
from .models import Curso, Usuario
from .forms import CriarContaForm, FormHomepage
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
#def homepage(request):
#    return render(request, "homepage.html")

class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHomepage


    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('curso:courses')
        else:
            return super().get(request, *args, **kwargs)

    def get_success_url(self):
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('curso:login')
        else:
            return reverse('curso:criarconta')

#def courses(request):
    #context = {}
    #lista_cursos = Curso.objects.all()
    #context['lista_cursos'] = lista_cursos
    #return render(request, "courses.html", context)

class Courses(LoginRequiredMixin, ListView):
    template_name = "courses.html"
    model = Curso

class DetailCourses(LoginRequiredMixin, DetailView):
    template_name = "DetailCourses.html"
    model = Curso

    def get(self, request, *args, **kwargs):
        curso = self.get_object()
        curso.visualizacoes += 1
        curso.save()
        usuario = request.user
        usuario.cursos_vistos.add(curso)
        return super().get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(DetailCourses, self).get_context_data(**kwargs)
        cursos_relacionados = Curso.objects.filter(category=self.get_object().category)[0:5]
        context["cursos_relacionados"] = cursos_relacionados
        return context

class Pesquisa(ListView):
    template_name = "PesquisaCurso.html"
    model = Curso

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = Curso.objects.filter(title__icontains=termo_pesquisa)
            return object_list
        else:
            return None

class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = "editarperfil.html"
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('curso:courses')


class Criarconta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('curso:login')