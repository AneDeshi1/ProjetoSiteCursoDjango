from .models import Curso


def lista_cursos_recentes(request):

    lista_cursos = Curso.objects.all().order_by('data_criacao')
    if lista_cursos:
        curso_destaque = lista_cursos
    else:
        curso_destaque = None
    return {"lista_cursos_recentes": lista_cursos, "curso_destaque": curso_destaque}



def lista_cursos_emalta(request):

    lista_cursos = Curso.objects.all().order_by('visualizacoes')
    return {"lista_cursos_emalta": lista_cursos}


