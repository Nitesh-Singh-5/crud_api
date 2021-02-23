from django.shortcuts import render, HttpResponsePermanentRedirect
from .forms import StudentRegistration
from .models import User



# This Function will add new item and show all item
def add_show(request):
    if request.method == 'POST':
        fm= StudentRegistration(request.POST)
        if fm.is_valid():
            nm= fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pas=fm.cleaned_data['password']

            reg= User(name=nm, email=em, password=pas)
            reg.save()
            fm= StudentRegistration()

    else:
        fm=StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html',{'form':fm,'stu':stud} )

# This Function will delete
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id) 
        pi.delete()
        return HttpResponsePermanentRedirect('/')


# This Function will Edit
def update_data(request,id):
    if request.method == 'POST':
        pi= User.objects.get(pk=1)
        fm= StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi= User.objects.get(pk=1)
        fm= StudentRegistration(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})








