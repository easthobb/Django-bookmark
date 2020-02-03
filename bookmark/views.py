from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy
from .models import Bookmark

# Create your views here.

class BookmarkListView(ListView):
    model = Bookmark #모든 뷰는 클랙스 뷰로 문듭니당

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name','url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create' #사용할 템플릿의 접미사만 변경 CreateView와 UpdateView는 form이 접미사인데 이결 변경해서 bookmark_create로 사용하도록

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update' #bookmark_update.html 이 탬플릿이 된다닌 이야기입니다~

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6

