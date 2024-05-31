from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register_view(request):
    if request.method == "POST": 
        form = UserCreationForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect("posts:list")
    else:
        form = UserCreationForm()

        # Add Tailwind CSS to the template  
        form.fields['username'].widget.attrs['class'] = 'text-md block px-3 py-2  rounded-lg w-full bg-white border-2 border-gray-300 placeholder-gray-600 shadow-md focus:placeholder-gray-500 focus:bg-white focus:border-gray-600 focus:outline-none'
        
        form.fields['password1'].widget.attrs['class'] = 'text-md block px-3 py-2 rounded-lg w-full bg-white border-2 border-gray-300 placeholder-gray-600 shadow-md focus:placeholder-gray-500 focus:bg-white  focus:border-gray-600 focus:outline-none'

        form.fields['password2'].widget.attrs['class'] = 'text-md block px-3 py-2 rounded-lg w-full bg-white border-2 border-gray-300 placeholder-gray-600 shadow-md focus:placeholder-gray-500 focus:bg-white  focus:border-gray-600 focus:outline-none'
    return render(request, "users/register.html", { "form": form })