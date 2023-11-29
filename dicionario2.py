# cadastro de produto

# apresentação

print('\n\t\t\t------informações do produto------')
nm = input('nome: ')
dic = input('descrição: ')
vlr = float(input('valor R$: '))
qtd = int(input('estoque: '))
qtdtotal = float(vlr*qtd)

# processamento

produto = {'nome': 'informe o nome...','descrição': 'insira a dic','valor': 0.0,'estoque': 'quantos produtos','valor total':0.0}

produto['nome'] = nm
produto['descrição'] = dic
produto['valor'] = vlr
produto['estoque'] = qtd
produto['valor total'] = qtdtotal

# saida

print('\n\t\t\t-----produto cadastrado com sucesso------ ')
print(f'Nome.................{produto["nome"]}')
print(f'descrição............{produto["descrição"]}')
print(f'valor................{produto["valor"]}')
print(f'estoque..............{produto["estoque"]}')
print(f'valor total..........{produto["valor total"]}')