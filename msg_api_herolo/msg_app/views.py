from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
	LoginRequiredMixin,
	UserPassesTestMixin,
	)
from django.views.generic import (
	CreateView,
	DeleteView,
	)
from django.db import models
from .models import Message

# Create your views here.
def home(request):
	context = {'msgs':[]}
	for msg in Message.objects.all():
		# Checks if the message if the receiver or the sender is the current logged in user - 
		# if the message does not belong to one of the above - it is not included in the context
		if str(request.user) == msg.sender or str(request.user) == msg.receiver:
			context['msgs'].append(msg)
	return render(request=request, 
				  template_name='msg_app/home.html', 
				  context=context)


@login_required
def compose(request):
	return render(request=request,
				  template_name='msg_app/compose.html')


@login_required
def unread(request):
	context = {'msgs':[]}
	for msg in Message.objects.all():
		# Checks if the message was already read and if the receiver is the current logged in user - 
		# if the message was read, or the user is not the current logged in - the message is not included in the context
		if not msg.read and str(request.user) == msg.receiver:
			if str(request.user) == msg.sender or str(request.user) == msg.receiver:
				context['msgs'].append(msg)
	return render(request=request, 
				  template_name='msg_app/home.html', 
				  context=context)


@login_required
def delete_msg(request, pk):
	if request.method == 'POST':
		msg = Message.objects.get(pk=pk)
		msg_sender = msg.sender
		msg_receiver = msg.receiver
		# Deletes the message only if the message is owned by the current logged in user
		if str(request.user) == msg_sender or str(request.user) == msg_receiver:
			msg_subject = msg.subject
			msg_creation_date = msg.creation_date
			msg.delete()
			messages.success(request, f'Message {msg_subject} from {msg_sender} to {msg_receiver} sent on {msg_creation_date} was deleted successfully!')
		else:
			messages.error(request, f'You have no permission to delete the message for {msg_sender} or {msg_receiver} because you are logged in as {request.user}')
	return redirect('msg_app:home')

@login_required
def show_msg(request, pk):
	if request.method == 'GET':
		msg = Message.objects.get(pk=pk)
		msg_sender = msg.sender
		msg_receiver = msg.receiver
		# Shows the message only if the sender or the receiver is the current logged in user
		if str(request.user) == msg_sender or str(request.user) == msg_receiver:
			msg_subject = msg.subject
			msg_creation_date = msg.creation_date
			if str(request.user) == msg_receiver:
				msg.read = True
				msg.save()
			return render(request=request,
						  template_name='msg_app/show_msg.html',
						  context={'msg': msg})


class MessageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Message
	success_url = '/'
	def test_func(self):
		msg = self.get_object()
		if str(self.request.user) == msg.sender or str(self.request.user) == msg.receiver:
			return True
		return False


class MessageCreateView(LoginRequiredMixin, CreateView):
	model = Message
	fields = ['subject', 'receiver', 'content']
	def form_valid(self, form):
		form.instance.sender = self.request.user
		return super().form_valid(form)

