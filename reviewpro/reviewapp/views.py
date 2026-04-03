from django.shortcuts import render
from . models import Review

def add_review(request):
    if request.method =="POST":
        product=request.POST.get('product')
        user=request.POST.get('user')
        rating=request.POST.get('rating')
        comment=request.POST.get('comment')

        Review.objects.create(
            product=product,
            user=user,
            rating=rating,
            comment=comment
        )
        return render(request,'add.html',{'msg':'Review Taken Successfully....'})
    return render(request,'add.html')
def display_review(request):
    reviews=Review.objects.all()
    return render(request,'display.html',{'reviews':reviews})


# Create your views here.
