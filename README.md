# 🎰 Mega Sena JR - Sistema de Probabilidade Otimizada

Sistema inteligente para geração de números da Mega Sena com análise estatística e múltiplas estratégias de otimização de probabilidade.

## 📋 Descrição

O **Mega Sena JR** é um sistema profissional desenvolvido para auxiliar jogadores da Mega Sena através de:

- ✨ Análise estatística de padrões históricos
- 🎯 Múltiplas estratégias de geração de números
- 📊 Análise detalhada de combinações
- 🔥 Identificação de números "quentes" e "frios"
- ⚖️ Balanceamento de pares/ímpares e distribuição de faixas
- 🧮 Estratégias baseadas em Fibonacci e outras sequências matemáticas

## 🚀 Instalação

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Passos de Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/juniorcosta-win/mega-sena-jr.git
cd mega-sena-jr
```

2. **Instale as dependências (opcional):**
```bash
pip install -r requirements.txt
```

3. **Execute o sistema:**
```bash
python mega_sena.py
```

## 💡 Como Usar

### Modo Interativo

Execute o programa e escolha uma das estratégias disponíveis:

```bash
python mega_sena.py
```

### Estratégias Disponíveis

1. **Balanceada** - Combina números quentes, frios e aleatórios
2. **Números Quentes** - Usa os números mais sorteados historicamente
3. **Números Frios** - Estratégia contrária, números menos sorteados
4. **Completamente Aleatório** - Geração puramente aleatória
5. **Baseado em Fibonacci** - Usa a sequência de Fibonacci
6. **Par/Ímpar Balanceado** - Equilibra números pares e ímpares
7. **Múltiplos Jogos** - Gera jogos usando todas as estratégias

### Exemplo de Uso

```
╔════════════════════════════════════════════════════════════╗
║     MEGA SENA JR - Sistema de Probabilidade Otimizada     ║
║              Gerador Inteligente de Números                ║
╚════════════════════════════════════════════════════════════╝

Escolha uma estratégia:
1. Balanceada (Hot + Cold + Random)
2. Números Quentes (Mais sorteados)
3. Números Frios (Menos sorteados)
4. Completamente Aleatório
5. Baseado em Fibonacci
6. Par/Ímpar Balanceado
7. Gerar Múltiplos Jogos (todas estratégias)

Digite sua escolha (1-7): 1
Quantos jogos gerar? (1-20): 5

============================================================
Estratégia: BALANCED
Data/Hora: 26/12/2024 18:00:00
============================================================

Jogo  1: 05 - 12 - 18 - 33 - 41 - 52
Jogo  2: 04 - 10 - 25 - 30 - 47 - 58
Jogo  3: 03 - 07 - 20 - 35 - 46 - 54
Jogo  4: 12 - 18 - 23 - 26 - 38 - 58
Jogo  5: 05 - 12 - 27 - 34 - 35 - 52

============================================================
```

## 📊 Recursos do Sistema

### Análise Estatística
- Rastreamento de frequência de números
- Identificação de padrões históricos
- Cálculo de distribuição (baixos, médios, altos)
- Análise de soma e média das combinações

### Estratégias Inteligentes
- **Hot Numbers**: Prioriza números frequentemente sorteados
- **Cold Numbers**: Aposta em números "devidos"
- **Balanced**: Mix otimizado de diferentes análises
- **Mathematical**: Baseado em sequências matemáticas
- **Random**: Para quem acredita na sorte pura

### Análise de Combinações
Cada jogo gerado inclui:
- Contagem de números pares e ímpares
- Distribuição por faixas (1-20, 21-40, 41-60)
- Soma total e média dos números
- Padrões e estatísticas relevantes

## 🎯 Funcionalidades Programáticas

### Uso como Biblioteca Python

```python
from mega_sena import MegaSenaGenerator

# Criar instância do gerador
generator = MegaSenaGenerator()

# Carregar dados históricos (opcional)
historical_data = [
    [4, 5, 30, 33, 41, 52],
    [10, 18, 25, 35, 47, 58],
    # ... mais resultados
]
generator.load_historical_data(historical_data)

# Gerar jogos com diferentes estratégias
balanced_games = generator.generate_multiple_games(5, 'balanced')
hot_games = generator.generate_multiple_games(5, 'hot')
random_games = generator.generate_multiple_games(5, 'random')

# Analisar uma combinação
analysis = generator.analyze_combination([5, 12, 23, 34, 45, 56])
print(analysis)

# Obter estatísticas
stats = generator.get_statistics()
print(stats['hot_numbers'])
```

## 📈 Melhorando as Probabilidades

Este sistema foi projetado para:

1. **Análise de Padrões**: Identifica tendências em resultados anteriores
2. **Diversificação**: Oferece múltiplas estratégias para diferentes perfis
3. **Balanceamento**: Otimiza distribuição de números (pares/ímpares, faixas)
4. **Matemática**: Aplica conceitos estatísticos e sequências matemáticas

### Dicas para Uso Profissional

- 📅 Use a estratégia **Balanceada** para melhor equilíbrio
- 🔥 Combine **Números Quentes** com análise de padrões
- 💰 Jogue múltiplos jogos com estratégias diferentes
- 📊 Acompanhe seus resultados e ajuste sua estratégia
- 🎲 Lembre-se: loteria é probabilidade, não certeza

## ⚠️ Aviso Legal e Responsabilidade

**IMPORTANTE**: Este sistema é uma ferramenta de análise estatística e geração de combinações para entretenimento e estudo de probabilidades. 

- ❌ **NÃO GARANTE ganhos** na loteria
- ❌ **NÃO aumenta matematicamente** suas chances de ganhar
- ✅ **Fornece análise estatística** de padrões históricos
- ✅ **Gera combinações otimizadas** baseadas em diferentes estratégias
- ✅ **Ajuda a diversificar** suas apostas de forma inteligente

### Jogue com Responsabilidade

- 🎰 A Mega Sena é um jogo de azar
- 💸 Nunca gaste mais do que pode perder
- 📚 Use este sistema como ferramenta educacional
- ⚖️ As probabilidades de ganhar permanecem as mesmas para qualquer combinação
- 🔞 Jogue apenas se tiver idade legal

## 🛠️ Tecnologias Utilizadas

- Python 3.7+
- Algoritmos de análise estatística
- Geração de números pseudoaleatórios otimizada
- Estruturas de dados eficientes para análise

## 📝 Licença

Este projeto está licenciado sob a Apache License 2.0 - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Junior Costa**
- GitHub: [@juniorcosta-win](https://github.com/juniorcosta-win)

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fork o projeto
2. Criar uma branch para sua feature (`git checkout -b feature/NovaEstrategia`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova estratégia'`)
4. Push para a branch (`git push origin feature/NovaEstrategia`)
5. Abrir um Pull Request

## 📞 Suporte

Para questões, sugestões ou suporte:
- Abra uma [Issue](https://github.com/juniorcosta-win/mega-sena-jr/issues)
- Entre em contato através do GitHub

## 🎁 Versão Comercial

Interessado em uma versão profissional com:
- 📱 Interface gráfica moderna
- 🌐 Aplicativo web responsivo
- 📊 Dashboard com análises avançadas
- 🔄 Atualização automática de resultados
- 💾 Histórico completo de todos os sorteios
- 🤖 Machine Learning para predição de padrões
- 📧 Alertas e notificações
- 👥 Suporte dedicado

Entre em contato para mais informações sobre a versão premium!

---

**Desenvolvido com ❤️ para a comunidade de apostadores da Mega Sena**
