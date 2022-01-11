from django import forms
from form_lead.models import Leads
from datetime import datetime

class LeadForm(forms.ModelForm):
    data_cadastro = forms.DateField(label='Data do Cadastro', disabled=True, initial=datetime.today)
    class Meta:
        model = Leads
        fields = '__all__'
        exclude = ('cliente_ativado',)
        labels = {
            'nome' :'Nome',
            'fone_celular': 'Telefone Celular',
            'fone_whatsapp': 'WhatsApp',
            'email': 'E-mail',
            'cidade' : 'Cidade',
            'uf' : 'UF',
            'obs' :  'Obs.',
            'cupon': 'Cupon',
            'data_cadastro':'Data',
        }