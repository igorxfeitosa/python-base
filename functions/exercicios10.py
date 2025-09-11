def student_status(*notas, situacao = False):
    """
    -> Função para analisar notas e situação de alunos.
    :param notas: recebe varias notas do aluno.
    :param situação: (opcional) indicando se deve ou não mostrar a situação do aluno.
    :return: retorna um dicionario com as notas, média, e situação do aluno.
    """
    
    status = dict()
    
    status['total'] = len(notas)
    status['maior'] = max(notas)
    status['menor'] = min(notas)
    status['média'] = round(sum(notas) / len(notas), 1)
    
    if situacao:
        if status['média'] >=7:
            status['situacao'] = 'BOA'
            
        elif status['média'] >=5:
            status['situacao'] = 'RAZOÁVEL'
            
        else: status['situacao'] = 'RUIM'
        
    return status

igor = student_status(4.5, 6.2, 7.0, 9.0, situacao=True)
print(igor)
help(student_status)