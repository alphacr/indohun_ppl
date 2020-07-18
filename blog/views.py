from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse
from .forms import ContactUsForm, QuestionnaireForm
from . import constants
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    FormView
)
from .models import (
    Questionnaire,
)
from users.models import Profile

# Create your views here.
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'May 4, 2020',
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'May 5, 2020',
    },
]


@login_required
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


class ReportListView(LoginRequiredMixin, ListView):
    model = Questionnaire
    template_name = 'blog/report_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'reports'
    ordering = ['-date_posted']


class ReportDetailView(LoginRequiredMixin, DetailView):
    model = Questionnaire  # <app>/<model>_<viewtype>.html
    context_object_name = 'report'


def get_questionnaire_from_hash(session_hash):
    return Questionnaire.objects.filter(
        session_hash=session_hash,
    ).exclude(
        stage=constants.COMPLETE
    ).first()


class ReportCreateView(LoginRequiredMixin, FormView):
    template_name = 'blog/questionnaire_form.html'  # <app>/<model>_<viewtype>.html
    questionnaire = None
    form_class = None

    def dispatch(self, request, *args, **kwargs):
        session_hash = request.session.get("session_hash", None)
        self.questionnaire = get_questionnaire_from_hash(
            session_hash)
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        self.request.session['session_hash'] = form.instance.session_hash
        current_stage = form.cleaned_data.get('stage')
        new_stage = constants.STAGE_ORDER[constants.STAGE_ORDER.index(
            current_stage)+1]
        form.instance.stage = new_stage
        form.save()
        if new_stage == constants.COMPLETE:
            return redirect(reverse('questionnaire:blog-home'))
        else:
            return redirect(reverse('questionnaire:report-create'))

    def get_form_class(self):
        stage = self.questionnaire.stage if self.questionnaire else constants.STAGE_1
        fields = Questionnaire.get_fields_by_stage(stage)
        return modelform_factory(Questionnaire, QuestionnaireForm, fields)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.questionnaire
        return kwargs


class ReportUpdateView(LoginRequiredMixin, FormView):
    template_name = 'blog/questionnaire_form.html'  # <app>/<model>_<viewtype>.html
    questionnaire = None
    form_class = None

    def dispatch(self, request, *args, **kwargs):
        session_hash = request.session.get("session_hash", None)
        self.questionnaire = get_questionnaire_from_hash(
            session_hash)
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        self.request.session['session_hash'] = form.instance.session_hash
        current_stage = form.cleaned_data.get('stage')
        new_stage = constants.STAGE_ORDER[constants.STAGE_ORDER.index(
            current_stage)+1]
        form.instance.stage = new_stage
        form.save()
        if new_stage == constants.COMPLETE:
            return redirect(reverse('questionnaire:blog-home'))
        else:
            return redirect(reverse('questionnaire:report-create'))

    def get_form_class(self):
        stage = self.questionnaire.stage if self.questionnaire else constants.STAGE_1
        fields = Questionnaire.get_fields_by_stage(stage)
        return modelform_factory(Questionnaire, QuestionnaireForm, fields)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.questionnaire
        return kwargs


def about(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Terima kasih telah menghubungi One Health Laboratory')
    else:
        form = ContactUsForm()
    return render(request, 'blog/about.html', {'form': form})

def tentang_manajement(request):
    return render(request, 'blog/tentang_manajement.html')

def tentang_biorisiko(request):
    return render(request, 'blog/tentang_biorisiko.html')

def tentang_SMBL(request):
    return render(request, 'blog/tentang_SMBL.html')

