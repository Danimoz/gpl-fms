from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Folder, File
from .forms import  UploadFileForm

# Create your views here.
@login_required
def FolderList(request):
    u = User.objects.get(username = request.user)
    is_superuser = request.user.is_superuser
    if is_superuser:
        folder = Folder.objects.all()
    else:
        dept = u.staff_user.department
        folder = Folder.objects.filter(department=dept)
    context = {'folder':folder}
    return render(request, 'pages/folderview.html', context)

class FolderCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Folder
    fields = ['name', 'folder']
    template_name = 'pages/folder_form.html'
    permission_required = 'dept.can_add_folder'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.department = self.request.user.staff_user.department
        return super().form_valid(form)

def is_valid_queryparam(param):
    return param != '' and param is not None

# Folder with files in it
@login_required
def folderfiles(request, pk):
    curr_folder = Folder.objects.get(id=pk)
    files = File.objects.filter(folder=curr_folder).order_by('-uploaded_at')
    
    #Search
    nameFile = request.GET.get('nameFile')
    description = request.GET.get('description')
    startdate = request.GET.get('startdate')
    enddate = request.GET.get('enddate')

    if is_valid_queryparam(nameFile):
        files = files.filter(name_of_file__icontains=nameFile)
    if is_valid_queryparam(description):
        files = files.filter(description__icontains=description)
    if is_valid_queryparam(startdate):
        files = files.filter(uploaded_at__gte=startdate)
    if is_valid_queryparam(enddate):
        files = files.filter(uploaded_at__lt=enddate)

    # Paginator
    filelist = list(files)
    paginator = Paginator(filelist, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context={'pk':pk, 'files':files, 'curr_folder':curr_folder, 'page_obj':page_obj}
    return render(request, 'pages/fileview.html', context)


@login_required
def FileUploadForm(request, pk):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            u = User.objects.get(username=request.user)
            form.instance.fileuser = u
            folder = Folder.objects.get(id=pk)
            form.instance.folder = folder
            department = u.staff_user.department
            form.instance.department = department
            form.save()
            messages.success(request, f'File Successfully uploaded to {folder} in {department}!')
            return redirect('home')
    else:
        form = UploadFileForm()

    context = {'pk':pk, 'form':form}
    return render(request, "pages/fileup_form.html", context)