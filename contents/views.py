from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ContentCreateForm
from .models import Content
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def content_create(request):
    if request.method=='POST':
        form=ContentCreateForm(data=request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            new_item=form.save(commit=False)
            new_item.user=request.user
            new_item.save()
            messages.success(request, 'Question added successfully')
            return redirect(new_item.get_absolute_url())
    else:
        form=ContentCreateForm(data=request.GET)
    return render(request, 'contents/content/create.html',
                    {'section': 'contents', 'form': form})

def content_detail(request, id, slug):
    content=get_object_or_404(Content, id=id, slug=slug)
    return render(request, 'contents/content/detail.html',
                    {'section': 'contents', 'content': content})

@login_required
@require_POST
def content_like(request):
    content_id=request.POST.get('id')
    action=request.POST.get('action')
    if content_id and action:
        try:
            content=Content.objects.get(id=content_id)
            if action=='like':
                content.users_like.add(request.user)
            else:
                content.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status': 'error'})

@login_required
def content_list(request):
    contents=Content.objects.all()
    paginator=Paginator(contents, 8)
    page=request.GET.get('page')
    try:
        contents=paginator.page(page)
    except PageNotAnInteger:
        contents=paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            return HttpResponse('')
        contents=paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request, 'contents/content/list_ajax.html',
                    {'section': 'contents', 'contents': contents})
    return render(request, 'contents/content/list.html',
                    {'section': 'contents', 'contents': contents})
