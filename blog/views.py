from django.shortcuts import render
from .models import Post ,Tag
from django.shortcuts import get_object_or_404
from .forms import EmailPostForm ,CommentForm
from django.core.mail import send_mail



# Create your views here.

def post_detail(request,year,month,day,post):
	post= get_object_or_404(Post, slug=post,
		status='published',
		publish__year=year,
		publish__month=month,
		publish__day=day)
	comments = post.comments.filter(active = True)
	if request.method == 'POST':
		comment_form = CommentForm(data = request.POST)

		if(comment_form.is_valid()):
			new_comment = comment_form.save(commit=False)
			new_comment.post = post
			new_comment.save()
	else:
		comment_form = CommentForm()

	return render(request, 'blog/post/detail.html',{
		'post':post,
		'comments':comments,
		'comment_form':comment_form

		})
	

def post_list(request,tag=None):
    posts = Post.objects.all()
    if(tag):
    	tag1=Tag.objects.get(name=tag)
    	posts=tag1.posts.all();
    return render(request,'blog/post/list.html',{'posts': posts})


def share_post(request,post_id):
    post=get_object_or_404(Post,id=post_id,status='published')
    sent=False

    if request.method == 'POST':
	    form = EmailPostForm(request.POST)
	    if form.is_valid():
		    cd = form.cleaned_data
		    post_url = request.build_absolute_uri(post.get_absolute_url())
		    send_mail(cd['name']+" recommends you reading ",cd['comments'],
	        'syed.shibli@daffodilsw.com',[cd['to']],fail_silently=False)
            sent = True
    else:
	    form = EmailPostForm()
    return render(request,'blog/post/share.html',{'post':post,'form':form,'sent':sent })	  	
	   
		

