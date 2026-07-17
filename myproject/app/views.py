from django.shortcuts import render,redirect

# Create your views here.
from .models import Petshop

def pet_list(request):
    pets=Petshop.objects.all()
    return render(request,'pet_list.html',{'pets':pets})

def pet_add(request):
    if request.method == 'POST':
        pet_name=request.POST.get('pet_name')
        pet_image=request.FILES.get('pet_image')
        Petshop.objects.create(pet_name=pet_name,pet_image=pet_image)
        return redirect('pet_list')
    return render(request,'form.html')

def del_pet(request,pet_id):
    pet=Petshop.objects.filter(id=pet_id).first()
    if pet:
        pet.delete()
    return redirect('pet_list')
def edit_pet(request,pet_id):
    pet=Petshop.objects.filter(id=pet_id).first()
    if request.method == 'POST':
        
        pet_name=request.POST.get('pet_name')
        pet_image=request.FILES.get('pet_image')
        pet.pet_name=pet_name
        if pet_image:
            pet.pet_image=pet_image
        pet.save()
        return redirect('pet_list')
    return render(request,'edit.html',{'pet':pet})