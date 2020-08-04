from django.shortcuts import render, get_object_or_404, redirect
from apply.models  import ApplyInformation
from user.models import CustomUser

def apply_create(request) :
    if request.method == 'POST' and request.session.get('user', False) :
        reason = request.POST['reason']
        user = get_object_or_404(CustomUser, username=request.session['user'])
        makeweb = request.POST['makeweb']
        solution = request.POST['solution']
        gain = request.POST['gain']

        apply = ApplyInformation(
            reason = reason,
            makeweb = makeweb,
            solution = solution,
            gain = gain,
            user = user
            )
        apply.save()
        return redirect('apply_read')
    else:
        return render(request, 'apply/create.html')

def apply_read(request) :
    applys = ApplyInformation.objects.all()
    context = {'applys': applys}
    return render(request,'apply/read.html',context)

