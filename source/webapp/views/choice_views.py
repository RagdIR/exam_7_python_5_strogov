from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, TemplateView
from webapp.models import Choice, Poll
from webapp.forms import ChoiceForm


class ChoiceView(DetailView):
    template_name = 'choice/choice_view.html'
    model = Choice
    form_class = ChoiceForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context) #отладка
        return context

# class ChoiceView(TemplateView):
#     template_name = 'choice/choice_view.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         pk = self.kwargs.get('pk')
#         choice = get_object_or_404(Choice, pk=pk)
#         context['choice'] = choice
#         print(context)
#         return context


class PollChoiceCreateView(CreateView):
    model = Choice
    template_name = 'choice/choice_create.html'
    form_class = ChoiceForm

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.poll = poll
        choice.save()
        return redirect('poll_view', pk=poll.pk)


class ChoiceUpdateView(UpdateView):
    model = Choice
    template_name = 'choice/choice_update.html'
    form_class = ChoiceForm
    context_key = 'choice'

    def get_success_url(self):
        return reverse('choice_view', kwargs={'pk': self.object.pk})


class ChoiceDeleteView(DeleteView):
    template_name = 'choice/choice_delete.html'
    model = Choice
    context_object_name = 'choice'
    success_url = reverse_lazy('index')


