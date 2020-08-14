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
        return redirect('apply_create')
    else:
        return render(request, 'apply/create.html')

def apply_read(request) :
    applys = ApplyInformation.objects.all()
    context = {'applys': applys}
    return render(request,'apply/read.html',context)

    # if request.session.get('manager_ok', False):    관리자 로그인 기능 주석처리,,ㅎㅎ
    #    applys = ApplyInformation.objects.all()
    #    context = {'applys': applys}
    #    return render(request,'apply/read.html',context)
    # else:
    #    return redirect(apply_create)

def apply_read_one(request, pk) :
    apply = get_object_or_404(ApplyInformation, pk = pk)
    context = { 'apply': apply }
    return render(request, 'apply/read_one.html',context)

def apply_update(request,pk):
    if  request.method == 'POST':
        reason = request.POST['reason']
        makeweb = request.POST['makeweb']
        solution = request.POST['solution']
        gain = request.POST['gain']

        apply = ApplyInformation.objects.get(pk=pk)

        apply.reason = reason
        apply.makeweb = makeweb
        apply.solution = solution
        apply.gain = gain
        apply.save()
        return redirect('apply_read')
    else:
        apply = get_object_or_404(ApplyInformation, pk = pk)
        context = {"apply" : apply}
        return render(request, 'apply/update.html', context)

def apply_delete(request,pk):
    apply = ApplyInformation.objects.get(pk=pk)
    apply.delete()
    return redirect('apply_read')