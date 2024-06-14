from django.shortcuts import render
from django.http import HttpResponse
from .models import Item  
from django.template import loader  
from .forms import ItemForm
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
# def index(request):
#     item_list=Item.objects.all()
#     # template=loader.get_template('food/index.html')
#     context={
#         'item_list':item_list,
#     }
#     # return HttpResponse(template.render(context,request)) 
#     return render(request,'food/index.html',context)

# ABOVE IS FUNCTION BASED VIEWS,ITS CLASS BASED VIEWS WRITTEN BELOW.

class IndexClassView(ListView):
    model=Item
    template_name='food/index.html'
    context_object_name='item_list'


def item(request):
    return HttpResponse('<h1>This is item page</h1>')

# def detail(request,item_id):
#     item=Item.objects.get(pk=item_id)
#     context={
#         'item':item,
#     }
#     return render(request,'food/detail.html',context)
#     # return HttpResponse("This is item No./Id: %s" % item_id)

class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'


# def create_item(request):
#     # context{}
#     form=ItemForm(request.POST or None)

#     if form.is_valid():
#         form.save()
#         return redirect('food:index')
#         # After form is saved we want to take the user to our index page
#     return render(request,'food/item-form.html',{'form':form})

# class CreateItem(CreateView):
class CreateItem(CreateView):
    model = Item
    # we want to add description feilds and name ,here we don't add username feilds ,because we want that if we add item details then username update automatically and add in a admin panel
    fields=['item_name','item_desc','item_price','item_image']
    template_name='food/item-form.html'

    def form_valid(self,form):
        form.instance.User_name=self.request.user

        return super().form_valid(form)
    # Now user_name is automaticaly save in admin panel ,if new user register ittself and add new item


def update_item(request,id):
    item=Item.objects.get(id=id)
    form=ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
        # After form is saved we want to take the user to our index page
    return render(request,'food/item-form.html',{'form':form,'item':item})


def delete_item(request,id):
    item=Item.objects.get(id=id)

    if request.method == "POST":
        item.delete()
        return redirect('food:index')
    # We also pass the item ,so that page know that which item is deleted
    return render(request,'food/item-delete.html',{'item':item})
        