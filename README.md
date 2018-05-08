# projeto1 Tratamento de Dados Astronômicos
Autor: João Gabriel Macedo
Email: joao15@astro.ufrj

Pacotes necessarios: astropy.io, glob, numpy

ATENCAO! -> É necessário definir o x assim que vc abrir o programa, em que o x deve ser igual ao caminho da sua pasta principal,
e dentro dela deve haver 3 pastas com os nomes 
science -> APENAS IMAGENS DE CIENCIA
flat -> APENAS COM IMAGENS FLAT 
bias -> APENAS COM IMAGENS BIAS

Caso vc defina o x errado, vai dar erro nas suas funções!

O programa consiste em 4 funções:

bias(y): que retorna uma array masterbias se y for igual a 1, ou cria no endereço x
uma imagem fits master_bias se y for diferente de 1

flat(d): que retorna uma array masterflatbias se d for igual a 1, ou cria no endereço x
uma imagem fits master_flat_bias se d for diferente de 1

science(): faz as reducoes em cada imagem de ciencia e as salva na mesma pasta science

test(): cria uma imagem residual da imagem de ciencia xo2b.0006 - xo2b.0006_clean e a salva na pasta science, 
com a finalidade de ver se as imagems foram bem reduzidas. Essa função só funciona como teste após vc ja ter criado
a imagem xo2b.0006_clean
