from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageForm, VideoForm, Blog_post_form
from .models import Image_list, Video_list, Post_Blog
from django.contrib.auth.decorators import login_required


def user_blog_ui(request):
    blog_list = Post_Blog.objects.all()
    context = {'blog_list': blog_list,
               }
    return render(request, 'Multimedia/user_blog_ui.html', context)


@login_required(login_url="user_login")
def blog_post_ui(request):
    blog_list = Post_Blog.objects.all()
    count = Post_Blog.objects.count()
    print('This is our Blog post count', count)
    context = {'blog_list': blog_list}
    return render(request, 'Multimedia/blog_post_ui.html', context)


@login_required(login_url="user_login")
def blog_post_upload(request):
    if request.method == "POST":
        form = Blog_post_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_post_ui')
    else:
        form = Blog_post_form()
    context = {'form': form, }
    return render(request, 'Multimedia/blog_post_upload.html', context)


def img_list(request):
    images = Image_list.objects.all()
    return render(request, 'Multimedia/img_list.html', {'images': images})


def vid_list(request):
    videos = Video_list.objects.all()
    context = {'videos': videos}
    return render(request, 'Multimedia/vid_list.html', context)


@login_required(login_url="user_login")
def upload_img(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('img_list')
    else:
        form = ImageForm()
    return render(request, 'Multimedia/upload_img.html', {'form': form})


@login_required(login_url="user_login")
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vid_list')
    else:
        form = VideoForm()
    return render(request, 'Multimedia/upload_video.html', {'form': form})


@login_required(login_url="user_login")
def delete_blog(request, id):
    del_blog = get_object_or_404(Post_Blog, id=id)
    if request.method == "POST":
        del_blog.delete()
        return redirect('blog_post_ui')
    return render(request, 'Multimedia/blog_del_confirm.html', {'del_blog': del_blog})


@login_required(login_url="user_login")
def update_blog(request, id):
    blog = get_object_or_404(Post_Blog, id=id)
    form = Blog_post_form(request.POST or None, request.FILES or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('blog_post_ui')
    return render(request, 'Multimedia/blog_post_upload.html', {'form': form, 'blog': blog})
