from .models import Post

def validatePost():

    posts = Post.objects.all()

    for post in posts:
        if '&' in post.content:
            print(post.id, 'has error')
            post.content = post.content.replace('&', '')
            post.save()
        
        if post.modifiedAt < post.createdAt:
            print(post.id, 'modified date error')
            post.save()