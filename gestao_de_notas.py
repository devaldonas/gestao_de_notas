def main():
print("=== SISTEMA DE GESTÃO DE NOTAS DE ALUNOS ===")
print()
# Lista para armazenar as notas
notas = []
# Cadastro de notas
cadastrar_notas(notas)
# Cálculo da média
media = calcular_media(notas)
# Determinação da situação
situacao = determinar_situacao(media)
# Exibir relatório final
exibir_relatorio(notas, media, situacao)
def cadastrar_notas(notas):
"""Função para cadastrar as notas dos alunos"""
print("CADASTRO DE NOTAS")
print("Digite as notas do aluno (digite -1 para finalizar):")
print()
while True:
try:
nota = float(input("Digite uma nota (0-10): "))
if nota == -1:
if len(notas) == 0:
print("É necessário cadastrar pelo menos uma nota!")
continue
break
if 0 <= nota <= 10:
notas.append(nota)
print(f"Nota {nota} adicionada com sucesso!")
else:
print("Nota inválida! Digite um valor entre 0 e 10.")
except ValueError:
print("Erro! Digite um número válido.")
print(f"\nTotal de notas cadastradas: {len(notas)}")
print()
def calcular_media(notas):
"""Função para calcular a média das notas"""
if len(notas) == 0:
return 0
soma = sum(notas)
media = soma / len(notas)
return round(media, 2)
def determinar_situacao(media):
"""Função para determinar a situação do aluno"""
if media >= 7:
return "APROVADO"
else:
return "REPROVADO"
def exibir_relatorio(notas, media, situacao):
"""Função para exibir o relatório final"""
print("=" * 50)
print("RELATÓRIO FINAL DO ALUNO")
print("=" * 50)
print(f"Notas cadastradas: {notas}")
print(f"Quantidade de notas: {len(notas)}")
print(f"Média final: {media}")
print(f"Situação: {situacao}")
# Informações adicionais
print("\nDETALHES:")
print(f"Maior nota: {max(notas) if notas else 'N/A'}")
print(f"Menor nota: {min(notas) if notas else 'N/A'}")
print("=" * 50)
# Função adicional para menu interativo
def sistema_completo():
"""Sistema completo com menu interativo"""
notas = []
while True:
print("\n" + "=" * 50)
print("SISTEMA DE GESTÃO DE NOTAS - MENU PRINCIPAL")
print("=" * 50)
print("1. Cadastrar notas")
print("2. Calcular média")
print("3. Ver situação")
print("4. Exibir relatório completo")
print("5. Limpar todas as notas")
print("6. Sair")
print("=" * 50)
opcao = input("Escolha uma opção (1-6): ")
if opcao == "1":
cadastrar_notas(notas)
elif opcao == "2":
if notas:
media = calcular_media(notas)
print(f"\nMédia calculada: {media}")
else:
print("\nNenhuma nota cadastrada!")
elif opcao == "3":
if notas:
media = calcular_media(notas)
situacao = determinar_situacao(media)
print(f"\nSituação do aluno: {situacao}")
else:
print("\nNenhuma nota cadastrada!")
elif opcao == "4":
if notas:
media = calcular_media(notas)
situacao = determinar_situacao(media)
exibir_relatorio(notas, media, situacao)
else:
print("\nNenhuma nota cadastrada!")
elif opcao == "5":
notas.clear()
print("\nTodas as notas foram removidas!")
elif opcao == "6":
print("\nObrigado por usar o sistema!")
break
else:
print("\nOpção inválida! Digite um número de 1 a 6.")
# Execução do programa
if __name__ == "__main__":
# Para executar a versão simples:
# main()
# Para executar a versão completa com menu:
sistema_completo()