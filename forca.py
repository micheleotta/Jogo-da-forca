# ESCOLHA DA PALAVRA #
import random 

palavrasaleatorias = ['GIRAFA', 'GATO', 'ESMALTE', 'MIOJO', 'MORANGO', 'CHOCOLATE', 'VERDE', 'CINZA', 'PYTHON', 'ABELHA', 'PUCPR', 'ALEGRIA','ESTUDAR', 'PROGRAMA', 'PIMENTA']
# escolha de maneira randômica
escolhida = palavrasaleatorias[random.randint(0,14)]
# conta o número de letras da palavra escolhida, que será usada para preencher o vetor
numeroletras = len(escolhida)
palavrasecreta = [0] * numeroletras

# preenche o vetor, letra a letra
i = 0
while i < numeroletras:
  for char in escolhida:
    palavrasecreta[i] = char
    i += 1

# INÍCIO JOGO #
tentativa = numeroletras + 5
palpite = 'A'
palavra = ["_"] * numeroletras # o que é impresso à medida dos acertos

print("₊˚ʚᗢ₊˚✧ﾟ。JOGO DA FORCA ₊˚ʚᗢ₊˚✧ﾟ。\n")

print(" ".join(palavra))

# repete enquanto ainda há tentativas restantes e a palavra ainda não foi descoberta
while (tentativa > 0) and (palavrasecreta != palavra):
  
  print(f'\n\nTentativas restantes: {tentativa}')
  palpite = input("\nDigite uma letra: ")
  palpite = palpite.upper(); # para o jogo funcionar tanto com letras minúsculas, quanto maiúsculas

  # checa se a letra inserida está presente na palavra
  for posicao in range(numeroletras):
    if palpite == palavrasecreta[posicao]:
      palavra[posicao] = palpite

  # ao final do palpite, imprime a palavra atualizada: se há a ocorrência da letra, ela preenche as posições. caso contrário, continua vazia
  print(f'\n{" ".join(palavra)}')
  tentativa -= 1

# caso o jogador perca, ou seja, a palavra não foi adivinhada e o número de tentativas acabou
if (tentativa <= 0) and (palavrasecreta != palavra):
  print("\n\n₊˚ʚᗢ₊˚✧ﾟ。GAME OVER ₊˚ʚᗢ₊˚✧ﾟ。\n")
  print(f'Puxa! Você perdeu :P\nA palavra era: {" ".join(palavrasecreta)}')

# quando o jogador ganha, acertou a palavra dentro do número de tentativas!
elif palavrasecreta == palavra:
  print("\n\n₊˚ʚᗢ₊˚✧ﾟ。VENCEDOR ₊˚ʚᗢ₊˚✧ﾟ。\n")
  print("Oba! Parabéns! Você acertou a palavra! :D\n\n")
