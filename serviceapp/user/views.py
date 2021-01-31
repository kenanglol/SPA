from django.shortcuts import render, redirect
from .UserController import UserController
from django.http import HttpResponseRedirect
from .UserForm import UserForm
from django.views.decorators.csrf import csrf_exempt
from home.views import home_view2


@csrf_exempt
def login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm()
        form.email = request.POST['email']
        form.password = request.POST['password']

        islog = UserController.login(request.POST['email'],
                                     request.POST['password'])

        # check whether it's valid:
        if islog:
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect(home_view2)
    # if a GET (or any other method) we'll create a blank form
    else:
        print('35')
        form = UserForm()

    return render(request, 'login.html', {'form': form})
