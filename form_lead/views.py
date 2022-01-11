from django.db.models import fields
from django.shortcuts import render
from django.http import HttpResponse
from form_lead.forms import LeadForm
import requests
import base64
import json

def index(request):
    leads = LeadForm()
    contexto = {
        'leads':leads,
    }
    return render(request, 'index.html', contexto)

def enviaDados(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            contexto = {
                'form':form,
            }
            
            host = '45.224.183.52'
            url = "https://{}/webservice/v1/contato".format(host)
            token = "14:1994cb27c48d1759b83259f4090fe3f7ccfd45ef9761cf9b68210b0dbfda0f7c".encode('utf-8')

            payload = json.dumps({
                'principal': 'N',
                'id_cliente': '',
                'nome': f'{form.cleaned_data.get("nome")}',
                'tipo_pessoa': 'F',
                'cnpj_cpf': '',
                'data_nascimento': '',
                'razao': '',
                'id_filial': '',
                'id_contato_tipo': '',
                'id_candidato_tipo': '',
                'id_responsavel': '',
                'data_cadastro': f'{form.cleaned_data.get("data_cadastro")}',
                'data': '',
                'id_vd_contrato': '',
                'id_tipo_elemento': '',
                'velocidade_calculada': '',
                'id_fornecedor': '',
                'lead': 'S',
                'ativo': 'S',
                'id_caixa_ftth': '',
                'distancia_caixa_mais_proxima': '',
                'id_prospeccao': '',
                'ultima_atualizacao': 'CURRENT_TIMESTAMP',
                'fone_residencial': '',
                'fone_comercial': '',
                'fone_celular': f'{form.cleaned_data.get("fone_celular")}',
                'fone_whatsapp': f'{form.cleaned_data.get("fone_whatsapp")}',
                'email': f'{form.cleaned_data.get("email")}',
                'skype': '',
                'facebook': '',
                'website': '',
                'cep': '',
                'endereco': '',
                'numero': '',
                'bairro': '',
                'complemento': '',
                'cidade': '',
                'uf': '',
                'referencia': '',
                'latitude': '',
                'longitude': '',
                'pipe_id_pessoa': '',
                'cadastro_site': 'N',
                'status_viabilidade': '',
                'data_ult_verificacao_viab': '',
                'caixa_mais_proxima': '',
                'data_cadastro_lead': '',
                'velocidade_calculada_lead': '',
                'quantidade_pessoas_lead': '',
                'quantidade_smart_lead': '',
                'frequencia_smart_lead': '',
                'quantidade_celular_lead': '',
                'frequencia_celular_lead': '',
                'quantidade_computador_lead': '',
                'frequencia_computador_lead': '',
                'quantidade_console_lead': '',
                'frequencia_console_lead': '',
                'obs': '',
                'alerta': ''
            })

            headers = {
                'ixcsoft': '',
                'Authorization': 'Basic {}'.format(base64.b64encode(token).decode('utf-8')),
                'Content-Type': 'application/json'
            }

            response = requests.post(url, data=payload, headers=headers, verify=False)

            print(response.text)
    return render(request, 'index.html', contexto)            


# Create your views here.
