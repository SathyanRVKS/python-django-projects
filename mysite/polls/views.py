from django.shortcuts import get_object_or_404, render
#from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.views import generic
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

 # Create your views here.
def index(request):
	if not request.user.is_authenticated:
		context = {
			"message" : "not logged in",
		}
		return redirect("/polls/login/", context)
	else:
		question_list = Question.objects.order_by('-pub_date')
		#template = loader.get_template("polls/index.html")
		context = {
			'question_list' : question_list
		}
		return render(request, "polls/index.html", context)
	#output = ', '.join([q.question_text for q in question_list])
	#return HttpResponse(template.render(context, request))
	

def detail(request, question_id):
	if not request.user.is_authenticated:
		context = {
			"message" : "not logged in",
		}
		return redirect("/polls/login/", context)
	else:
		question = get_object_or_404(Question, pk=question_id)
		# try:
		# 	question = Question.objects.get(pk=question_id)
		# except Question.DoesNotExist:
		# 	raise Http404("Question does not exist")
		context = {
			'question' : question
		}
		return render(request, "polls/detail.html", context)

def results(request, question_id):
	if not request.user.is_authenticated:
		context = {
			"message" : "not logged in",
		}
		return redirect("/polls/login/", context)
	else:
		question = get_object_or_404(Question, pk=question_id)
		context = {
			'question' : question,
		}
		return render(request, 'polls/results.html', context)

# class IndexView(generic.ListView):
# 	template_name = 'polls/index.html'
# 	context_object_name = 'question_list'
# 	def get_queryset(self):
# 		return Question.objects.order_by('-pub_date')

# class DetailView(generic.DetailView):
# 	model = Question
# 	template_name = "polls/detail.html"

# class ResultsView(generic.DetailView):
# 	model = Question
# 	template_name = "polls/results.html"

def vote(request, question_id):
	if not request.user.is_authenticated:
		context = {
			"message" : "not logged in",
		}
		return redirect("/polls/login/", context)
	else:	
		question = get_object_or_404(Question, pk=question_id)
		try:
			selected_choice = question.choice_set.get(pk=request.POST['choice'])
		except (KeyError, Choice.DoesNotExist):
			context = {
				'question' : question,
				'error_message' : "Nothing selected",
			}
			return render(request, 'polls/detail.html', context)
		else:
			selected_choice.votes += 1
			selected_choice.save()
			return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))

def logout_view(request):
	logout(request)
	context = {
		'message' : 'test',
	}
	return render(request, "polls/logout.html", context)

class SignUpView(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'registration/signup.html'