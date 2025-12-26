#!/usr/bin/env python3
"""
Exemplo de uso programático do Mega Sena JR
Este arquivo demonstra como usar o sistema como biblioteca Python
"""

from mega_sena import MegaSenaGenerator

def main():
    print("="*70)
    print("DEMO - Uso Programático do Mega Sena JR")
    print("="*70)
    print()
    
    # Criar instância do gerador
    generator = MegaSenaGenerator()
    
    # Exemplo 1: Dados históricos simulados
    print("📊 Carregando dados históricos simulados...")
    historical_data = [
        [4, 5, 30, 33, 41, 52],
        [10, 18, 25, 35, 47, 58],
        [3, 12, 23, 25, 38, 54],
        [7, 12, 18, 26, 35, 46],
        [5, 12, 20, 27, 34, 58],
        [8, 15, 22, 29, 36, 43],
        [2, 9, 16, 23, 30, 37],
        [11, 18, 25, 32, 39, 46],
        [6, 13, 20, 27, 34, 41],
        [14, 21, 28, 35, 42, 49]
    ]
    generator.load_historical_data(historical_data)
    print(f"✅ {len(historical_data)} sorteios carregados\n")
    
    # Exemplo 2: Obter estatísticas
    print("📈 Estatísticas dos dados históricos:")
    stats = generator.get_statistics()
    print(f"   Total de sorteios: {stats['total_draws']}")
    print(f"   Números quentes (top 10): {stats['hot_numbers'][:10]}")
    print(f"   Números frios (top 10): {stats['cold_numbers'][:10]}")
    print()
    
    # Exemplo 3: Gerar jogos com diferentes estratégias
    print("🎲 Gerando jogos com diferentes estratégias:")
    print("-"*70)
    
    strategies = {
        'balanced': 'Balanceada (Hot + Cold + Random)',
        'hot': 'Números Quentes',
        'cold': 'Números Frios',
        'random': 'Completamente Aleatório',
        'fibonacci': 'Baseado em Fibonacci',
        'even_odd': 'Par/Ímpar Balanceado'
    }
    
    for strategy_key, strategy_name in strategies.items():
        games = generator.generate_multiple_games(2, strategy_key)
        print(f"\n📍 {strategy_name}:")
        for i, game in enumerate(games, 1):
            numbers_str = ' - '.join(f'{n:02d}' for n in game)
            print(f"   Jogo {i}: {numbers_str}")
    
    # Exemplo 4: Análise detalhada de uma combinação
    print("\n" + "="*70)
    print("🔍 Análise Detalhada de Combinação")
    print("="*70)
    
    sample_game = generator.generate_balanced_combination()
    numbers_str = ' - '.join(f'{n:02d}' for n in sample_game)
    print(f"\nCombinação: {numbers_str}")
    
    analysis = generator.analyze_combination(sample_game)
    print(f"\n📊 Análise:")
    print(f"   • Números Pares: {analysis['even_count']}")
    print(f"   • Números Ímpares: {analysis['odd_count']}")
    print(f"   • Soma Total: {analysis['sum']}")
    print(f"   • Média: {analysis['average']:.1f}")
    print(f"   • Distribuição:")
    print(f"     - Baixos (1-20): {analysis['distribution']['low (1-20)']}")
    print(f"     - Médios (21-40): {analysis['distribution']['mid (21-40)']}")
    print(f"     - Altos (41-60): {analysis['distribution']['high (41-60)']}")
    
    # Exemplo 5: Gerar múltiplos jogos para bolão
    print("\n" + "="*70)
    print("👥 Exemplo: Gerando 10 jogos para um bolão")
    print("="*70)
    print()
    
    bolao_games = generator.generate_multiple_games(10, 'balanced')
    for i, game in enumerate(bolao_games, 1):
        numbers_str = ' - '.join(f'{n:02d}' for n in game)
        analysis = generator.analyze_combination(game)
        print(f"Jogo {i:2d}: {numbers_str} | "
              f"Pares:{analysis['even_count']} Ímpares:{analysis['odd_count']} | "
              f"Soma:{analysis['sum']}")
    
    print("\n" + "="*70)
    print("✅ Demo concluída!")
    print("="*70)
    print("\nUse este código como base para criar suas próprias aplicações!")
    print()


if __name__ == "__main__":
    main()
