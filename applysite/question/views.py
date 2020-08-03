from django.shortcuts import render


def question_read(request):
    questions = question.objects.all()
    context = {'question', questions }
    return render(request, 'question/read.html', context)

def question_read_one(request, pk):
    question = get_object_or_404(Question, pk = pk)
    context = {'question' : question }
    return render(request, 'board/read_one.html')