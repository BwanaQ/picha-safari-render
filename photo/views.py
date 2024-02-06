from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Photo, Tag, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class PhotoListView(LoginRequiredMixin, ListView):
    model = Photo
    template_name = 'photo_list.html'
    context_object_name = 'photos'
    paginate_by = 10 
    
    def get_queryset(self):
        return Photo.objects.filter(owner=self.request.user)

class PhotoDetailView(LoginRequiredMixin, DetailView):
    model = Photo
    template_name = 'photo/photo_detail.html'  
    context_object_name = 'photo'

class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    template_name = 'photo/photo_form.html'  
    fields = ['title', 'description', 'category', 'tags', 'image','webp_image', 'price'] 
    success_url = reverse_lazy('photo_list')  
    success_message = "The Photo was created successfully!"
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)
        return response

class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    template_name = 'photo/photo_form.html'  
    fields = ['title', 'description', 'category', 'tags', 'price']
    success_url = reverse_lazy('photo_list')  
    success_message = "The Photo was updated successfully!"
    
    def form_valid(self, form):
        response = super().form_valid(form)
        return response
    
class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = 'photo/photo_confirm_delete.html'  
    success_url = reverse_lazy('photo_list')  
    success_message = "The Photo was deleted successfully!"

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return response

# Category Views
class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 10 
    
    def get_queryset(self):
        return Category.objects.all()

class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'photo/category_detail.html'  
    context_object_name = 'category'

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'photo/category_form.html'  
    fields = ['name'] 
    success_url = reverse_lazy('category_list')  
    success_message = "The Category was created successfully!"
    
    def form_valid(self, form):
        response = super().form_valid(form)
        return response

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = 'photo/category_form.html'  
    fields = ['name']
    success_url = reverse_lazy('category_list')  
    success_message = "The Category was updated successfully!"
    
    def form_valid(self, form):
        response = super().form_valid(form)
        return response
    
class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'photo/category_confirm_delete.html'  
    success_url = reverse_lazy('category_list')  
    success_message = "The Category was deleted successfully!"

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return response


# Tag Views
class TagListView(LoginRequiredMixin, ListView):
    model = Tag
    template_name = 'tag_list.html'
    context_object_name = 'tags'
    paginate_by = 10 
    
    def get_queryset(self):
        return Tag.objects.all()

class TagDetailView(LoginRequiredMixin, DetailView):
    model = Tag
    template_name = 'photo/tag_detail.html'  
    context_object_name = 'tag'

class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    template_name = 'photo/tag_form.html'  
    fields = ['name'] 
    success_url = reverse_lazy('tag_list')  
    success_message = "The Tag was created successfully!"
    
    def form_valid(self, form):
        response = super().form_valid(form)
        return response

class TagUpdateView(LoginRequiredMixin, UpdateView):
    model = Tag
    template_name = 'photo/tag_form.html'  
    fields = ['name']
    success_url = reverse_lazy('tag_list')  
    success_message = "The Tag was updated successfully!"
    
    def form_valid(self, form):
        response = super().form_valid(form)
        return response
    
class TagDeleteView(LoginRequiredMixin, DeleteView):
    model = Tag
    template_name = 'photo/tag_confirm_delete.html'  
    success_url = reverse_lazy('tag_list')  
    success_message = "The Tag was deleted successfully!"

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return response


