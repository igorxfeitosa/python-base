
def situacao_voto(ano_nascimento):
    from datetime import date
    idade = date.today().year - ano_nascimento
    
    if idade >= 18 and idade <= 65:
        
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
        
    elif 16 <= idade < 18  or idade > 65:
        
        return f'Com {idade} anos: VOTO OPCIONAL'
        
    else:
    
        return f'Com {idade} anos: NÃO VOTA'





print(situacao_voto(1956))