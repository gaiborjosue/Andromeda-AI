from freebible import read_web

web = read_web()

libro = 'John'

capitulo = '2'

versiculo = '6'


output = (web[libro][capitulo][versiculo])

print(output)