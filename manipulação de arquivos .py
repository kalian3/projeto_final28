with open('entrevistados.txt','w',encoding='utf-8') as arquivos:
    arquivos.write('me chamo joão...estou sendo entrevistado ')

with open('entrevistados.txt','a')as arquivo:
    arquivo.write('\n me chamo kaliane e \n tenho 17 anos.')
    
with open('entrevistados.txt','a',encoding='utf-8')as arquivo:
    arquivo.write('\n me chamo luiz,\n tenho 18 anos e \n faço a faculdade de farmacêutico.')

with open ('entrevistados.txt','r',encoding='utf-8') as arquivos :
    entrevistados= arquivos.readlines()
    print(entrevistados)