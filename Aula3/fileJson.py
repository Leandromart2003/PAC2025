import os as operating
import json 

objecto={}

filename=R"C:\DEV\Ciseg_0925\Aulas\A4\Data\textoJason.json"

if operating.path.exists(filename):
    with open(filename,'r',encoding='utf-8') as manipfile:
        objecto=json.load(manipfile) # tenta carregar o file json

print(objecto)
# no final salvar o novo file

with open(filename,'w',encoding='utf-8') as manipfile:
    # json.dump salva o dicionário no arquivo como texto JSON
    # indent=4 deixa o JSON formatado
    # f: é o file handler, o arquivo aberto em modo escrita "w".
    # ensure_ascii=False permite acentos e caracteres especiais
    json.dump(objecto,manipfile,indent=4,ensure_ascii=False)