from django.shortcuts import render, redirect
from .models import User, Author
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'loginReg/index.html')
def addBook(request):
    viewsAuthor = Author.objects.add_author(request.POST)
    if viewsAuthor['isRegistered']:
        request.session['authorList'] = viewsAuthor['author'].author
        return redirect('users:dashboard')
    else:
        for error in viewsAuthor['errors']:
            messages.error(request, error)
    print request.session['authorList']
    return render(request, 'wishlist/index.html')
def register(request):
    viewsResponse = User.objects.add_user(request.POST)
    if viewsResponse['isRegistered']:
        request.session['user_id'] = viewsResponse['user'].id
        request.session['user_fname'] = viewsResponse['user'].first_name
        return redirect('users:dashboard')
    else:
        for error in viewsResponse['errors']:
            messages.error(request, error)
        return redirect('users:index')
def dashboard(request):
    context = {
        'all_courses': Author.objects.all()
    }
    return render(request, 'loginReg/dashboard.html', context)
def add(request):
    return render(request, 'wishlist/index.html')
def login(request):
    viewsResponse = User.objects.login_user(request.POST)
    if viewsResponse['isLoggedIn']:
        request.session['user_id'] = viewsResponse['user'].id
        request.session['user_fname'] = viewsResponse['user'].first_name
        return redirect('users:dashboard')
    else:
        for error in viewsResponse['errors']:
            messages.error(request, error)
        return redirect('users:index')
def logout(request):
    request.session.clear()
    return redirect('users:index')
def delete(request, author_id):
    # pseudo
    # if clicked while logged in:
    #     then add to other's wish list and delete from your wishlist
    Author.objects.get(id = author_id).delete()
    return redirect('users:dashboard')
def wish_items(request, author_id):
    context = {
        'course': Author.objects.get(id=author_id),
    }

    return render(request, 'wishlist/wish_list.html', context)
