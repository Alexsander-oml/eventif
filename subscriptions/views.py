from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from subscription.forms import SubscriptionForm
from django.core import mail
# Create your views here.

def subscribe(request):
    if request.method == 'POST'
       email = mail.send_mail('Confirmação de inscrição!', Message, 'contato@eventif.com.br', ['contato@eventif.com.br', 'profceleberfonseca@gmail.com'])
       return HttpResponseRedirect('/inscricao/')
    else:  
    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)


Message = '''
Olá! Tudo bem?

Muito obrigado por se inscrever no Eventif.

Estes foram os dados que você enviou na sua
inscrição.

Nome: Cleber Fonseca
CPF: 12345678901
Email: profcleberfonseca@gmail.com
Telefone: 53-12345-6789

Em até 48h úteis alguem da nossa equipe entrará
em contato com você para concluirmos a sua 
inscrição.

Atenciosamente,
Equipe EventIF
'''