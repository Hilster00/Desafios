#https://curso.grupysanca.com.br/pt/latest/exercicios.html
#desafio 21

def letras_e_quantidades(palavra={}):
    q={}
    for letra in palavra:
        q[letra]=q.get(letra,0)+1
    return q

print(letras_e_quantidades("casa"))
print(letras_e_quantidades("abracadabra"))
