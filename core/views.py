from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Item Has Been Added To List!'))
            # redirect('home')
            return render(request, 'home.html', {'all_items':all_items})
        else:
            messages.success(request, ('Item Invalid: Your Submission was Blank!'))
            render(request, 'home.html',  {'all_items':all_items})
            return

    else:
        all_items = List.objects.all
        #__________________________________________
        context =  {'all_items':all_items}
        return render(request, 'home.html', context)

def about(request):
    #__________________________________________
    context =  {}
    return render(request, 'about.html', context)


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item Has Been Deleted!'))
    return redirect('home')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    messages.success(request, ('Item Crossed Off From Your To-Do list!'))
    return redirect('home')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    messages.success(request, ('Item Re-added To Your To-Do list!'))
    return redirect('home')

def edit(request, list_id):
    if request.method == "POST":
        # getting the specific item from the list with the list_id
        item = List.objects.get(pk=list_id)

        # Telling form to use the 'item' instance we just grabbed from the list
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item Has Been Edited!'))
            return redirect('home')
        else:
            messages.success(request, ('Edit Invalid: Your Submission was Blank!'))
            return redirect('home')
    else:
        item = List.objects.get(pk=list_id)
        #__________________________________________
        # context =  {'item':item}
        return render(request, 'edit.html', {'item':item})
