from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Choice
from webapp.forms import ChoiceForm


class ChoiceView(DetailView):
    template_name = 'choice/choice_view.html'
    model = Choice
    paginate_choice_by = 3
    paginate_choice_orphans = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        choice, page, is_paginated = self.paginate_choice(self.object)
        context['choice'] = choice
        context['page_obj'] = page
        context['is_paginated'] = is_paginated
        print(context)
        return context

    def paginate_choice(self, choice):
        choice = choice.choice.all()
        if choice.count() > 0:
            paginator = Paginator(choice, self.paginate_choice_by, orphans=self.paginate_choice_orphans)
            page_number = self.request.GET.get('page', 1)
            page = paginator.get_page(page_number)
            is_paginated = paginator.num_pages > 1
            return page.object_list, page, is_paginated
        else:
            return choice, None, False
        
class PollChoiceCreateView(CreateView):
    template_name = 'choice/choice_create.html'
    form_class = ChoiceForm
    model = Choice

    def get_success_url(self):
        return reverse('choice_view', kwargs={'pk': self.object.pk})


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