from django.shortcuts import render

users = set()

def home(request):
    if request.method=="POST":
        username = request.POST["name"]
        if not username in users:
            users.add(username)
            print(username)
            print(users)
            return render(request, 'index.html',{'user':username})
        if username in users:
            return render(request, 'login.html',{'error':'user with this name already exist'})
    return render(request, 'login.html')
