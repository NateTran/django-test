from django.shortcuts import render
from .models import testapp
from .forms import testappForm, RawForm

# Create your views here.
def testapp_detail_view(request):
    obj = testapp.objects.get(id=3)
    context = {
            'object': obj
    }
    return render(request, "testapp/testapp_detail.html", context)

def testapp_create_view(request):
    form = testappForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = testappForm()

    context = {
            'form': form
    }
    return render(request, "testapp/testapp_create.html", context)

def testapp_create_view_django(request):
    form = RawForm()
    if request.method == 'POST':
        form = RawForm(request.POST)
        if form.is_valid():
            testapp.objects.create(**form.cleaned_data)
            print(form.cleaned_data)
        else:
            print(form.errors)
    context = {
            'form': form
    }
    return render(request, 'testapp/testapp_create_raw.html', context)
