from django.shortcuts import render, redirect
from .models import Curso, Students
from django.contrib import messages
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse


# Create your views here.
def home(request):
    cursosListados = Curso.objects.all()
    messages.success(request, '¡Cursos listados!')
    return render(request, "setup_course.html", {"cursos": cursosListados})


def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, '¡Curso registrado!')
    return redirect('/')


def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edit_course.html", {"curso": curso})


def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    messages.success(request, '¡Curso actualizado!')

    return redirect('/')


def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

    messages.success(request, '¡Curso eliminado!')

    return redirect('/')


def report_create(request):
    cursos = Curso.objects.all()
    template_path = 'Reports/report.html'
    context = { 'cursos': cursos }
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'filename="result_report.pdf"'
    response['Content-Disposition'] = 'attachment; filename="result_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)

    #if(pisa_status.error):
    #    return HttpResponse('Hay errores en la plantilla <pre>' + html + '</pre>')
    return response


def generate_bar_chart(request):
    cs_no = Students.objects.filter(course='Computer Science').count()
    cs_no = int(cs_no)
    #print('Number of Computer Science Students Are',cs_no)

    ce_no = Students.objects.filter(course='Computer Engineering').count()
    ce_no = int(ce_no)
    #print('Number of Computer Engineering Students Are',ce_no)

    se_no = Students.objects.filter(course='Software Engineering').count()
    se_no = int(se_no)
    #print('Number of Software Engineering Students Are',se_no)

    sec_no = Students.objects.filter(course='Computer Security').count()
    sec_no = int(sec_no)
    #print('Number of Computer Security Students Are',sec_no)

    male_no = Students.objects.filter(gender='Male').count()
    male_no = int(male_no)
    #print('Number of Male Are',male_no)

    female_no = Students.objects.filter(gender='Female').count()
    female_no = int(female_no)
    #print('Number of Female Are',female_no)

    gender_list = ['Male', 'Female']
    gender_number = [male_no, female_no]

    course_list = ['Computer Science', 'Computer Engineering', 'Software Engineering', 'Computer Security']
    number_list = [cs_no, ce_no, se_no, sec_no]
    context = {'course_list':course_list, 'number_list':number_list, 'gender_list':gender_list, 'gender_number':gender_number}
    return render(request, 'graphics/graphics.html', context)