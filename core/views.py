from django.shortcuts import render

def index(request):
    # RF01: Busca rápida de assistidos
    query = request.GET.get('q', '').strip()
    pacientes = [
        {"id": 1, "matricula": "PST-2024-0102", "nome": "Lucas Gabriel dos Santos", "diagnostico": "Paralisia Cerebral", "idade": 9},
        {"id": 2, "matricula": "PST-2024-0145", "nome": "Mariana Souza Lima", "diagnostico": "Transtorno do Espectro Autista (TEA)", "idade": 7},
        {"id": 3, "matricula": "PST-2024-0089", "nome": "Arthur Albuquerque Melo", "diagnostico": "Síndrome de Down", "idade": 11}
    ]
    if query:
        pacientes = [p for p in pacientes if query.lower() in p['nome'].lower() or query.lower() in p['matricula'].lower()]

    return render(request, 'index.html', {'pacientes': pacientes, 'query': query})

def atendimento(request):
    # RF02: Formulário com injeção da última conduta e metas do PDI
    mensagem_sucesso = False
    if request.method == 'POST':
       mensagem_sucesso = True

    ultima_conduta = "Sessão anterior (Fisioterapia - 28/09): Paciente demonstrou boa resposta ao treino de marcha com andador anterior. Mantida estabilidade de tronco por 15 minutos sem compensação postural."

    return render(request, 'atendimento.html', {
        'ultima_conduta': ultima_conduta,
        'sucesso': mensagem_sucesso
    })

def historico(request):
    # RF03: Linha do tempo interdisciplinar
    timeline = [
        {"data": "02/10/2026", "especialidade": "Fisioterapia", "prof": "Dra. Rose Mary", "frequencia": "Presente", "meta": "Treino de equilíbrio estático", "texto": "Realizado circuito psicomotor com apoio bipodal. Evolução satisfatória com diminuição da espasticidade."},
        {"data": "29/09/2026", "especialidade": "Fonoaudiologia", "prof": "Dra. Camila Soares", "frequencia": "Presente", "meta": "Comunicação Aumentativa e Alternativa (CAA)", "texto": "Treino de intenção comunicativa utilizando prancha visual de rotina. Paciente apontou 4 símbolos com autonomia."},
        {"data": "25/09/2026", "especialidade": "Terapia Ocupacional", "prof": "Dr. Marcelo Costa", "frequencia": "Falta Justificada", "meta": "Preensão palmar e AVDs", "texto": "Paciente ausente por consulta médica externa pré-agendada."}
    ]
    return render(request, 'historico.html', {'timeline': timeline})
