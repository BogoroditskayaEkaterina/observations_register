from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm, PatientCreateForm, QuestionnaireCreateForm
from django.views.generic import RedirectView, ListView
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView 
from .models import Patient, Questionnaire
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from csv_export.views import CSVExportView

class AccountLoginView(LoginView):
    ''' Display the login form '''
    form_class = LoginForm
    template_name = f'login.html'
    redirect_authenticated_user = True


class AccountLogoutView(LogoutView):
    ''' Logout '''
    pass


class PatientsRedirectView(RedirectView):
    ''' Redirect user to list of patients '''
    def get_redirect_url(self, *args, **kwargs):
        return reverse('patients-detail')


class PatientsDetailView(SuccessMessageMixin, CreateView, ListView):
    ''' Display patients information '''
    model = Patient
    template_name = f'patients.html'
    context_object_name = 'patients'
    form_class = PatientCreateForm

    def form_valid(self, form):
        return super(PatientsDetailView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('patients-detail')


def delete_patient(request, patient_id=None):
    ''' Patient deletion function '''
    patient_to_delete = Patient.objects.get(id=patient_id)
    patient_to_delete.delete()
    return HttpResponseRedirect(reverse('patients-detail'))


class MedicalCardDetailView(TemplateView):
    ''' Display medical card of patient '''
    template_name = f'medical-card.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        patient_id = self.kwargs['patient_id']
        patient = get_object_or_404(Patient, id=patient_id)
        context['patient'] = patient
        return context

class PatientUpdateView(SuccessMessageMixin, UpdateView):
    ''' Display the patient update form '''
    model = Patient
    form_class = PatientCreateForm
    template_name = f'patient-update.html'

    def form_valid(self, form):
        return super(PatientUpdateView, self).form_valid(form)
    
    def get_success_url(self):
        patient_id = self.kwargs['patient_id']
        return reverse_lazy('medical-card', args=[patient_id])

    def get_object(self):
        patient_id = self.kwargs['patient_id']
        patient = get_object_or_404(Patient, id=patient_id)
        return patient

class CreateQuestionnaire(SuccessMessageMixin, CreateView):
    ''' Display patients information '''
    model = Questionnaire
    template_name = f'create-questionnaire.html'
    form_class = QuestionnaireCreateForm

    def form_valid(self, form):
        return super(CreateQuestionnaire, self).form_valid(form)

    def get_success_url(self):
        patient_id = self.kwargs['patient_id']
        return reverse_lazy('medical-card', args=[patient_id])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        patient_id = self.kwargs['patient_id']
        patient = get_object_or_404(Patient, id=patient_id)
        context['patient'] = patient
        return context

def delete_questionnaire(request, patient_id=None, questionnaire_id=None):
    ''' Patient deletion function '''
    questionnaire_to_delete = Questionnaire.objects.get(id=questionnaire_id)
    questionnaire_to_delete.delete()
    return HttpResponseRedirect(reverse('medical-card', args=[patient_id]))


class PatientExportView(CSVExportView):
    model = Patient
    fields = ('id','gender', 'birthday', 'eyes_col', 'hair_col')
    header = True
    specify_separator = False
    filename = 'Patient-export.csv'

class QuestionnaireExportView(CSVExportView):
    model = Questionnaire
    fields = ("date_of_visit", "patient", "weight",
                  "growth", "freckles", "skin_col",
                  "redness_during_sunburn", "tanning_character", "rest_in_south",
                  "sunscreen_using", "neoplasm_appearance", "neoplasm_location",
                  "skin_tumors_in_fam", "elem_size", "elem_area",
                  "elem_borders", "elem_color", "inclusions", "elem_symmetry",
                  "doc_decision", "reappearance")
    header = True
    specify_separator = False
    filename = 'Questionnaire-export.csv'
