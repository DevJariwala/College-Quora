from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Question, Response
from .forms import NewQuestionForm, NewResponseForm


# Create your views here.

def homePage(request):
    questions = Question.objects.all().order_by('-created_at')
    stuff_for_frontend = {
        'questions': questions,
    }
    return render(request, 'main/homePage.html', stuff_for_frontend)


def questionPage(request, id):
    response_form = NewResponseForm()
  

    if request.method == 'POST':
        try:
            response_form = NewResponseForm(request.POST)
            if response_form.is_valid():
                response = response_form.save(commit=False)
                response.user = request.user
                response.question = Question(id=id)
                response.save()
                return redirect('/main/question/'+str(id)+'#'+str(response.id))
        except Exception as e:
            print(e)
            raise

    question = Question.objects.get(id=id)
    stuff_for_frontend = {
        'question': question,
        'response_form': response_form,
    }
    return render(request, 'main/question.html', stuff_for_frontend)


# if person want to ask the question it runs this and it require the login that's why we put @login_required
@login_required(login_url='home')
def newQuestionPage(request):
    form = NewQuestionForm()
    # here we are using the form made form our model
    # if we save this then it will always save in our database
    if request.method == "POST":
        try:
            form = NewQuestionForm(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                question.author = request.user
                question.save()
                return redirect('homePage')
        except Exception as e:
            print(e)
            raise

    stuff_for_frontend = {
        'form': form,
    }
    return render(request, 'main/newQuestion.html', stuff_for_frontend)


@login_required(login_url='home')
def deleteQuestion(request,id):
    Question.objects.filter(id=id).delete()
    return render(request,'main/questionIsDeleted.html')


def search(request):

    query = request.GET['query']

    if len(query)>78:
        all_questions = []
    else:
        all_questionsTitle = Question.objects.filter(title__icontains=query)
        all_questionsAuthor = Question.objects.filter(author__username__icontains=query)
        all_questionAUthorAndTitle = all_questionsAuthor.union(all_questionsTitle)
        all_questionsBody =  Question.objects.filter(body__icontains=query)
        all_questions= all_questionAUthorAndTitle.union(all_questionsBody)

    stuff_for_frontend ={
        'all_questions':all_questions,
        'query':query,
    }

    return render(request,'main/search.html',stuff_for_frontend)





