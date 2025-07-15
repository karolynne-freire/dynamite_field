# 🎮 Campo Minado - Acione seu raciocínio (e evite as bombas!)

🚀 Bem-vindo ao campo de batalha da **lógica**! Este projeto é um **jogo de Campo Minado**, desenvolvido com **Python puro**, como atividade prática da disciplina de **Lógica de Programação**.

Aqui, cada célula pode esconder uma explosão 💥 ou te dar pistas valiosas para vencer. Prepare seu raciocínio, mire nas posições certas... e tente sair ileso!

---

## 🔍 Sobre o Projeto

Inspirado no clássico jogo de estratégia, o **Campo Minado** desafia o jogador a descobrir células seguras sem ativar nenhuma bomba. Este projeto tem como foco:

- Praticar lógica de programação e pensamento estratégico
- Implementar listas, funções e controle de fluxo em Python
- Simular um jogo completo via terminal com menus, histórico e estatísticas
- Trabalhar com leitura e gravação de arquivos (.txt)
- Utilizar cores e emojis para uma melhor experiência visual

---

## 💡 Funcionalidades

✅ Jogo funcional via terminal (modo texto)  
✅ Níveis de dificuldade: Fácil (4x4) e Médio (6x6)  
✅ Geração aleatória de bombas a cada partida  
✅ Contador de bombas ao redor de cada célula clicada  
✅ Salvamento e carregamento de partidas  
✅ Registro de histórico, vitórias e derrotas  
✅ Visual com cores e emojis no terminal  
✅ Estatísticas gerais e Top 5 melhores tempos  

---

## 🛠️ Tecnologias e Conceitos Utilizados

- Python (sem bibliotecas externas)
- Listas e matrizes bidimensionais
- Funções e modularização
- Manipulação de arquivos (`open()`, `.txt`)
- Estruturas condicionais (`if`, `elif`, `else`)
- Laços de repetição (`for`, `while`)
- Códigos ANSI para colorir o terminal
- Controle de exceções (`try`, `except`)
- `pickle` e `ast` para leitura segura de dados salvos

---

## 📁 Arquivos Gerados

Durante o jogo, são gerados automaticamente:

- `tempovitoria4bombas.txt` e `tempovitoria6bombas.txt`: registros de vitórias
- `historico_partidas.txt`: log completo de partidas
- `vitorias.txt` / `derrotas.txt`: placar geral
- `ultimojogo4x4.txt` / `ultimojogo6x6.txt`: progresso salvo por dificuldade

---

## 🧪 Como Executar o Projeto

Siga os passos abaixo para rodar o jogo localmente em seu terminal:

### ✅ Pré-requisitos

- Ter o **Python** instalado (recomendado: versão 3.8 ou superior)
- Ter o **VS Code** (ou qualquer editor) instalado

### 💻 Instruções


# 1. Clone o repositório
```bash
git clone https://github.com/karolynne-freire/dynamite_field.git
```
# 2. Acesse a pasta do projeto
```bash
cd dynamite_field
```
# 3. Entre na subpasta back
```bash
cd back
```
# 4. Execute o jogo principal
```bash
python dynamite.py
```
Obs: No Windows, use python ou py, dependendo da sua configuração.

### 👥 Time de Desenvolvimento
Este projeto foi desenvolvido por estudantes da disciplina de Lógica de Programação:

- Karolynne Freire  
- Ruth Lima  
- Erwin Fernandes

Para detalhes sobre as contribuições individuais, acesse o histórico de commits no repositório:  
[Ver histórico de commits](https://github.com/karolynne-freire/dynamite_field/commits/main/)



### 🚧 Status do Projeto
🟢 Fase atual:
Jogo totalmente funcional em modo terminal com menus interativos, persistência de dados e estatísticas.

### 🔜 Fase futura (planejada):
Desenvolvimento de uma interface web com Flask + HTML/CSS.

### 📜 Licença
Projeto desenvolvido com fins educacionais.
Inspirado no clássico Campo Minado, com um toque de 💣 estratégia e 💻 lógica computacional.

