#  Persistência de dados com ficheiros (txt, json, csv)

#  Passo 1: Abrir o ficheiro para leitura
# - Utiliza-se a função open() com o modo 'r' (read/leitura)
# - Exemplo: open("ficheiro.txt", "r")

#  Passo 2: Realizar ações no ficheiro
# - Modos de abertura:
#   'r' → leitura (read)
#   'w' → escrita (write) - sobrescreve o conteúdo existente
#   'a' → acrescentar (append) - adiciona ao final do ficheiro
#   'b' → modo binário (pode ser combinado com outros, ex: 'rb')
#   'x' → criar novo ficheiro - erro se já existir

#  Passo 3: Fechar o ficheiro
# - Sempre fechar o ficheiro após o uso com close()
# - Exemplo: ficheiro.close()

filename=R"C:\DEV\Ciseg_0925\Aulas\A4\Data\texto.txt"

with open(filename,'r',encoding='utf-8') as manipfile:
   Texto=manipfile.read()

# Não é necessário chamar ficheiro.close() — é feito automaticamente
# no final salvar o novo file

with open(filename,'w',encoding='utf-8') as manipfile:
   manipfile.write(Texto)