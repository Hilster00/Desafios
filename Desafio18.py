#https://curso.grupysanca.com.br/pt/latest/exercicios.html
#desafio 18
from functools import reduce
q_leds={
    "0":6,
    "1":2,
    "2":5,
    "3":5,
    "4":4,
    "5":5,
    "6":6,
    "7":3,
    "8":7,
    "9":6,
}
def quantidade_leds(palavra):
    return reduce(lambda sm,c:q_leds[c]+sm, palavra, 0)

print(quantidade_leds("115380"))
print(quantidade_leds("2819311"))
print(quantidade_leds("23456"))
print(quantidade_leds("000"))
