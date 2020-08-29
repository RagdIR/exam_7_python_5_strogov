from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Poll
from webapp.forms import PollForm


class IndexView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'polls'
    model = Poll
    paginate_by = 5
    paginate_orphans = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        return super().get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        data = Poll.objects.all()
        return data.order_by('-created_at')

class PollView(DetailView):
    template_name = 'poll/poll_view.html'
    model = Poll

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        return context

    # def paginate_choice(self, poll):
    #     choice = poll.poll.all()
    #     if choice.count() > 0:
    #         paginator = Paginator(choice, self.paginate_choice_by, orphans=self.paginate_choice_orphans)
    #         page_number = self.request.GET.get('page', 1)
    #         page = paginator.get_page(page_number)
    #         is_paginated = paginator.num_pages > 1
    #         return page.object_list, page, is_paginated
    #     else:
    #         return choice, None, False
    #
    # def paginate_choice(self, poll):
    #     choice = poll.poll.all()
    #     return choice, None, False
        
        
class PollCreateView(CreateView):
    template_name = 'poll/poll_create.html'
    form_class = PollForm
    model = Poll

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollUpdateView(UpdateView):
    model = Poll
    template_name = 'poll/poll_update.html'
    form_class = PollForm
    context_key = 'poll'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):
    template_name = 'poll/poll_delete.html'
    model = Poll
    context_object_name = 'poll'
    success_url = reverse_lazy('index')
