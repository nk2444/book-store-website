from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.contrib.auth.models import User
from home.models import Product, Author


# Create your views here.
def index(request):
    products=Product.objects.all()
    for a in products:
      print(a.book_title, a.image, a.price)
#     print(products)
      params={'products':products}
    return render(request,'index.html', params)

def about(request):
     return render(request,'about.html')
    # return HttpResponse("This is about page")

def product(request):
     if request.method == "POST":
          book_id = request.POST.get('book_id')
          book_title = request.POST.get('book_title')
          authors = request.POST.get('authors')
          email= request.POST.get('email')
          pub_date = request.POST.get('pub_date')
          
          em = Product(book_id= book_id, book_title = book_title, pub_date = datetime())
          em.save()
          john = Author.objects.create(name="John")
          product.authors.add(john)
          # return redirect('/')
     else:
            products=Product.objects.all()
     for a in products:
      print(a.book_title, a.image, a.price)
#     print(products)
      params={'products':products}
      return render(request,'product.html',params)
          # return HttpResponse("This is books page")



def contact(request):
     if request.method == "POST":
          name = request.POST.get('name')
          phone = request.POST.get('phone')
          email = request.POST.get('email')
          em = Contact(name = name, phone = phone, email = email, date = datetime.today())
          em.save()
          messages.success(request, "Yor message has been send!.")     
     return render(request,'Contact.html')
    # return HttpResponse("This is contact page")


def search(request):    
           products=Product.objects.all()
           if request.method=="GET":
                 vr=request.GET.get('query')     
                 if vr!= None:
                  products=Product.objects.filter(book_title__icontains=vr)
                  params={'products':products}
           return render(request,"search.html",params)

def Signup(request):
     if request.method == 'POST':
          # Get the post perameters
          username= request.POST['username']
          email= request.POST['email']
          password1 = request.POST['password1']
          password2 = request.POST['password2']
          # checks for errorneou input
          if len(username)>10:
               messages.error(request,"username must be under 10 characters")
          return redirect('/')
     
     if password1 != password2:
          messages.error(request,"password must be match")
          return redirect('/')
     
          #  create the user:
          myuser = User.objects.create_user(username, email, password1)
          myuser.save()
          messages.success(request,"your account has been succesfully created")
          return redirect('/')
     else:
          return HttpResponse('Not allowed')
          
def handlelogin(request):
     if request.method == 'POST':
          loginusername= request.POST['loginusername']
          loginpassword= request.POST['loginpassword']
          user = authenticate(username=loginusername, password=loginpassword)
        
          if user is not None:
               login(request, user)
               messages.success(request,"you are sucessfully logged in")
          return redirect('/') 
     else:
          messages.error("invalid credantials, please try again")

          return redirect("/")  
     
     return HttpResponse("not found") 
     
def handlelogout(request):
          logout(request)
          messages.success(request,"successfuly logged out")
          return redirect("/")
         
    