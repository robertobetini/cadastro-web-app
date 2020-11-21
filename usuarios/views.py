from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.db.models import Q
from .models import Usuario

from .forms import FormCriar

# Create your views here.

class Lista(View):
  model = Usuario
  template_name = 'usuarios/lista.html'
  # Se fosse uma ListView, poderiamos utilizar o atributo paginate_by
  # para criar um objeto page_obj automaticamente e passá-lo ao contexto.
  # Porém, como há busca, achei melhor fazer manualmente dentro do método
  # get.

  def get(self, request):
    lista = list()
    pesquisa = request.GET.get('pesquisa', False)

    if pesquisa:
      query = Q(nome__contains=pesquisa)
      lista = Usuario.objects.filter(query)
    else:
      lista = Usuario.objects.all()

    obj_per_page = 2 # número de objetos por página
    # o valor 1 é utilizado apenas para fins de teste e demonstração
    
    paginator = Paginator(lista, obj_per_page) # objeto que facilita a paginação de uma view
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num) # lista dos objetos da página

    ctx = {"lista_usuarios": lista, "pesquisa": pesquisa, "page_obj": page_obj}
    return render(request, self.template_name, ctx)


class Criar(CreateView):
  model = Usuario
  fields = '__all__'
  template_name = 'usuarios/form.html'
  success_url = reverse_lazy('usuarios:lista')

  def get(self, request, pk=None):
    form = FormCriar()
    ctx = {"form": form}
    return render(request, self.template_name, ctx)

  def post(self, request, pk=None):
    form = FormCriar(request.POST)

    if not form.is_valid():
      ctx = {'form': form}
      return render(request, self.template_name, ctx)
    
    usuario = form.save(commit=False)
    usuario.save()
    return redirect(self.success_url)
    

class Visualizar(DetailView):
  model = Usuario
  template_name = 'usuarios/visual.html'

  def get(self, request, pk):
    usuario = Usuario.objects.get(id=pk)
    ctx = {"usuario": usuario}
    return render(request, self.template_name, ctx)


class Atualizar(UpdateView):
  template_name= 'usuarios/form.html'
  success_url = reverse_lazy('usuarios:lista')

  def get(self, request, pk):
    usuario = get_object_or_404(Usuario, id=pk)
    form = FormCriar(instance=usuario)
    ctx = {"form": form}
    return render(request, self.template_name, ctx)

  def post(self, request, pk=None):
    usuario = get_object_or_404(Usuario, id=pk)
    form = FormCriar(request.POST, instance=usuario)

    if not form.is_valid():
      ctx = {'form': form}
      return render(request, self.template_name, ctx)

    usuario = form.save(commit=False)
    usuario.save()

    return redirect(self.success_url)

class Deletar(DeleteView):
  model = Usuario
  template_name = 'usuarios/deletar.html'
  success_url = reverse_lazy('usuarios:lista')

  def get(self, request, pk):
    usuario = get_object_or_404(Usuario, id=pk)
    ctx = {'usuario': usuario}
    return render(request, self.template_name, ctx)