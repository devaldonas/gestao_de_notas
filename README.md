# gestao_de_notas
sSstema simples de gestão de notas de alunos. O sistema deve permitir que o usuário adicione notas, calcule a média das notas, determine a situação do aluno (aprovado ou reprovado), e exiba um relatório final. Utilize estruturas condicionais, de repetição e funções.
1. Estrutura Principal do Programa
main()
Função: Ponto de entrada da versão simplificada
Fluxo: Sequência linear que chama todas as funções na ordem correta
Saída: Executa cadastro → cálculo → situação → relatório automaticamente
sistema_completo()
Função: Versão interativa com menu
Fluxo: Loop contínuo com opções até o usuário escolher sair
Vantagem: Permite executar operações específicas sem recomeçar
2. Cadastro de Notas (cadastrar_notas(notas))
Validações Implementadas:
Intervalo: Aceita apenas notas entre 0 e 10
Tipo de dado: Apenas números (float)
Finalização: -1 para terminar o cadastro
Mínimo: Exige pelo menos uma nota antes de finalizar
Processamento:
python
# Armazenamento em lista
notas = [] # Lista vazia inicial
notas.append(8.5) # Adição de notas válidas
Tratamento de Erros:
ValueError: Captura entradas não numéricas
Mensagens claras de erro para o usuário
3. Cálculo da Média (calcular_media(notas))
Algoritmo:
python
soma = sum(notas) # Soma todos os elementos
media = soma / len(notas) # Divide pelo número de elementos
return round(media, 2) # Retorna com 2 casas decimais
Características:
Precisão: Arredondamento para melhor legibilidade
Segurança: Verifica se a lista não está vazia
Eficiência: Usa funções built-in do Python
4. Determinação da Situação (determinar_situacao(media))
Lógica Condicional:
python
if media >= 7:
return "APROVADO"
else:
return "REPROVADO"
Critérios:
Aprovação: Média ≥ 7.0 - Reprovação: Média < 7.0
Simplicidade: Regra direta sem complicações
