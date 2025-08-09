from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .models import Post
from django.http import HttpResponse
from django.core.management import call_command

def migrate_view(request):
    try:
        call_command('migrate')
        return HttpResponse("✅ Migration tamamlandı.")
    except Exception as e:
        return HttpResponse(f"❌ Migration hatası: {str(e)}")

def showAllPosts(req):
    post_list = Post.objects.filter(is_public=True).order_by('-released_at')
    paginator = Paginator(post_list, 6)

    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj
    }

    return render(req, 'blog.html', context)


def showPost(req, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(req, 'post.html', {'post': post})
