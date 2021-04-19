from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from .forms import NoteForm, SignUpForm, LogInForm, ChangePasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .models import Note


# Create your views here.
def SignUp(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                fm.save()
                fm = SignUpForm()
        else:
            fm = SignUpForm()
        return render(request, 'signup.html', {'form': fm, 'title': 'SignUp Form'})
    else:
        return HttpResponseRedirect('/notebook/')


def LogIn(request):
    try:
        if not request.user.is_authenticated:
            if request.method == 'POST':
                fm = LogInForm(request=request, data=request.POST)
                if fm.is_valid():
                    uname = fm.cleaned_data['username']
                    upass = fm.cleaned_data['password']
                    user = authenticate(username=uname, password=upass)
                    if user is not None:
                        login(request, user)
                        return HttpResponseRedirect('/notebook/')
                    fm = LogInForm()
            else:
                fm = LogInForm()
            return render(request, 'login.html', {'form': fm, 'title': 'Login Form'})
        else:
            return HttpResponseRedirect('/notebook/')
    except Exception as e:
        print(e)


def Notebook(request):
    try:
        if request.user.is_authenticated:
            if request.method == 'POST':
                fm = NoteForm(request.POST)
                if fm.is_valid():
                    # uid = fm.cleaned_data['user']
                    # cat = fm.cleaned_data['categories']
                    # hed = fm.cleaned_data['headline']
                    # txt = fm.cleaned_data['text']
                    # print(cat, hed, txt)
                    # print(uid)
                    fm.save()
                    fm = NoteForm()
                    return render(request, 'notebook.html', {'form': fm, 'title': 'Notebooks',
                                                             'username': request.user.username,
                                                             'first_name': request.user.first_name,
                                                             'last_name': request.user.last_name,
                                                             'email': request.user.email})

            else:
                fm = NoteForm()
                return render(request, 'notebook.html', {'form': fm, 'title': 'Notebooks',
                                                         'username': request.user.username,
                                                         'first_name': request.user.first_name,
                                                         'last_name': request.user.last_name,
                                                         'email': request.user.email})
        else:
            return HttpResponseRedirect('/login/')
    except Exception as e:
        print(e)


def LogOut(request):
    try:
        logout(request)
        return HttpResponseRedirect('/login/')
    except Exception as e:
        print(e)


def PasswordChange(request):
    try:
        if request.user.is_authenticated:
            if request.method == 'POST':
                fm = ChangePasswordForm(user=request.user, data=request.POST)
                if fm.is_valid():
                    fm.save()
                    update_session_auth_hash(request, fm.user)
                    return HttpResponseRedirect('/notebook/')
            else:
                fm = ChangePasswordForm(user=request.user)
            return render(request, 'passwordchange.html', {'form': fm})
        else:
            return HttpResponseRedirect('/login/')
    except Exception as e:
        print(e)


def ShowAllNotes(request):
    try:
        if request.user.is_authenticated:
            edata = Note.objects.all()
            context = {'title': 'All Notes', 'username': request.user.username,
                       'first_name': request.user.first_name,
                       'last_name': request.user.last_name, 'email': request.user.email,
                       'emd': edata}
            for i in edata:
                print(i.id)
            return render(request, 'shownotes.html', context)
        else:
            return HttpResponseRedirect('/login/')
    except Exception as e:
        print(e)


def EditNote(request, id):
    # return render(request, 'editdata.html')
    try:
        if request.user.is_authenticated:
            # return render(request, 'editdata.html')
            if request.method == 'POST':
                pi = Note.objects.get(pk=id)
                fm = NoteForm(request.POST, instance=pi)
                if fm.is_valid():
                    fm.save()
                    # fm = NoteForm()
                    return render(request, 'editdata.html', {'frm_data': fm, 'title': "Edit Data"})

            else:
                pi = Note.objects.get(pk=id)
                fm = NoteForm(instance=pi)
                return render(request, 'editdata.html', {'frm_data': fm, 'title': "Edit Data"})
        else:
            return HttpResponseRedirect('/login/')
    except Exception as e:
        print(e)


def Delete(request, id):
    try:
        if request.user.is_authenticated:
            if request.method == 'POST':
                pi = Note.objects.get(pk=id)
                pi.delete()
                return HttpResponseRedirect('/notebook/showallnotes/')

        else:
            return HttpResponseRedirect('/login/')

    except Exception as e:
        print(e)
