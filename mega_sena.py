#!/usr/bin/env python3
"""
Mega Sena Number Generator with Probability Optimization
Sistema de geração de números para Mega Sena com otimização de probabilidade

This system analyzes patterns and generates optimized number combinations
for the Brazilian Mega Sena lottery.
"""

import random
from collections import Counter
from typing import List, Set, Tuple
from datetime import datetime


class MegaSenaGenerator:
    """Generator for Mega Sena lottery numbers with probability optimization"""
    
    # Mega Sena rules: pick 6 numbers from 1 to 60
    MIN_NUMBER = 1
    MAX_NUMBER = 60
    NUMBERS_PER_GAME = 6
    
    def __init__(self):
        self.historical_data = []
        self.frequency_map = Counter()
        
    def load_historical_data(self, data: List[List[int]]):
        """Load historical lottery results for analysis"""
        self.historical_data = data
        for draw in data:
            self.frequency_map.update(draw)
    
    def get_hot_numbers(self, top_n: int = 15) -> List[int]:
        """Get the most frequently drawn numbers (hot numbers)"""
        if not self.frequency_map:
            return list(range(self.MIN_NUMBER, self.MIN_NUMBER + top_n))
        return [num for num, _ in self.frequency_map.most_common(top_n)]
    
    def get_cold_numbers(self, bottom_n: int = 15) -> List[int]:
        """Get the least frequently drawn numbers (cold numbers)"""
        if not self.frequency_map:
            return list(range(self.MAX_NUMBER - bottom_n + 1, self.MAX_NUMBER + 1))
        
        # Get all numbers sorted by frequency (ascending)
        all_numbers_by_freq = sorted(
            range(self.MIN_NUMBER, self.MAX_NUMBER + 1),
            key=lambda n: self.frequency_map.get(n, 0)
        )
        
        # Return the least frequent ones
        return all_numbers_by_freq[:bottom_n]
    
    def generate_balanced_combination(self) -> List[int]:
        """Generate a balanced combination using statistical analysis"""
        numbers = []
        
        # Strategy: Mix hot and cold numbers
        hot_numbers = self.get_hot_numbers(20)
        cold_numbers = self.get_cold_numbers(20)
        
        # Ensure no overlap between hot and cold
        cold_numbers = [n for n in cold_numbers if n not in hot_numbers]
        
        # Pick 3 hot numbers
        numbers.extend(random.sample(hot_numbers, min(3, len(hot_numbers))))
        
        # Pick 2 cold numbers (or fewer if not enough available)
        if cold_numbers:
            numbers.extend(random.sample(cold_numbers, min(2, len(cold_numbers))))
        
        # Fill remaining slots with random numbers
        while len(numbers) < self.NUMBERS_PER_GAME:
            remaining = set(range(self.MIN_NUMBER, self.MAX_NUMBER + 1)) - set(numbers)
            numbers.append(random.choice(list(remaining)))
        
        return sorted(numbers)
    
    def generate_hot_strategy(self) -> List[int]:
        """Generate combination using only hot numbers"""
        hot_numbers = self.get_hot_numbers(25)
        return sorted(random.sample(hot_numbers, self.NUMBERS_PER_GAME))
    
    def generate_cold_strategy(self) -> List[int]:
        """Generate combination using cold numbers (contrarian strategy)"""
        cold_numbers = self.get_cold_numbers(25)
        return sorted(random.sample(cold_numbers, self.NUMBERS_PER_GAME))
    
    def generate_random_combination(self) -> List[int]:
        """Generate a completely random combination"""
        numbers = random.sample(range(self.MIN_NUMBER, self.MAX_NUMBER + 1), 
                               self.NUMBERS_PER_GAME)
        return sorted(numbers)
    
    def generate_fibonacci_based(self) -> List[int]:
        """Generate combination based on Fibonacci sequence"""
        # Fibonacci numbers up to 60 (unique values only)
        fib = [1, 2, 3, 5, 8, 13, 21, 34, 55]
        fib_in_range = [f for f in fib if f <= self.MAX_NUMBER]
        
        # Add some Fibonacci numbers
        count = min(4, len(fib_in_range))
        numbers = random.sample(fib_in_range, count)
        
        # Fill remaining with random numbers
        remaining = set(range(self.MIN_NUMBER, self.MAX_NUMBER + 1)) - set(numbers)
        numbers.extend(random.sample(list(remaining), self.NUMBERS_PER_GAME - count))
        
        return sorted(numbers)
    
    def generate_even_odd_balanced(self) -> List[int]:
        """Generate combination with balanced even/odd numbers"""
        even_numbers = list(range(2, self.MAX_NUMBER + 1, 2))
        odd_numbers = list(range(1, self.MAX_NUMBER + 1, 2))
        
        # Pick 3 even and 3 odd
        numbers = random.sample(even_numbers, 3) + random.sample(odd_numbers, 3)
        
        return sorted(numbers)
    
    def generate_multiple_games(self, count: int, strategy: str = 'balanced') -> List[List[int]]:
        """Generate multiple game combinations using specified strategy"""
        games = []
        strategy_map = {
            'balanced': self.generate_balanced_combination,
            'hot': self.generate_hot_strategy,
            'cold': self.generate_cold_strategy,
            'random': self.generate_random_combination,
            'fibonacci': self.generate_fibonacci_based,
            'even_odd': self.generate_even_odd_balanced
        }
        
        generator = strategy_map.get(strategy, self.generate_balanced_combination)
        
        for _ in range(count):
            games.append(generator())
        
        return games
    
    def analyze_combination(self, numbers: List[int]) -> dict:
        """Analyze a combination and provide statistics"""
        if len(numbers) != self.NUMBERS_PER_GAME:
            return {"error": "Invalid number of numbers"}
        
        even_count = sum(1 for n in numbers if n % 2 == 0)
        odd_count = self.NUMBERS_PER_GAME - even_count
        
        # Range distribution
        low = sum(1 for n in numbers if n <= 20)
        mid = sum(1 for n in numbers if 20 < n <= 40)
        high = sum(1 for n in numbers if n > 40)
        
        # Sum of numbers
        total_sum = sum(numbers)
        
        analysis = {
            'numbers': numbers,
            'even_count': even_count,
            'odd_count': odd_count,
            'distribution': {
                'low (1-20)': low,
                'mid (21-40)': mid,
                'high (41-60)': high
            },
            'sum': total_sum,
            'average': total_sum / self.NUMBERS_PER_GAME
        }
        
        return analysis
    
    def get_statistics(self) -> dict:
        """Get overall statistics from historical data"""
        if not self.frequency_map:
            return {"message": "No historical data loaded"}
        
        stats = {
            'total_draws': len(self.historical_data),
            'most_common': self.frequency_map.most_common(10),
            'least_common': self.frequency_map.most_common()[-10:],
            'hot_numbers': self.get_hot_numbers(15),
            'cold_numbers': self.get_cold_numbers(15)
        }
        
        return stats


def print_banner():
    """Print system banner"""
    banner = """
    ╔════════════════════════════════════════════════════════════╗
    ║     MEGA SENA JR - Sistema de Probabilidade Otimizada     ║
    ║              Gerador Inteligente de Números                ║
    ╚════════════════════════════════════════════════════════════╝
    """
    print(banner)


def print_combinations(games: List[List[int]], strategy: str):
    """Print generated combinations in a formatted way"""
    print(f"\n{'='*60}")
    print(f"Estratégia: {strategy.upper()}")
    print(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"{'='*60}\n")
    
    for i, game in enumerate(games, 1):
        numbers_str = ' - '.join(f'{n:02d}' for n in game)
        print(f"Jogo {i:2d}: {numbers_str}")
    
    print(f"\n{'='*60}\n")


def main():
    """Main CLI interface"""
    print_banner()
    
    generator = MegaSenaGenerator()
    
    # Sample historical data (simulated for demonstration)
    # In a real system, this would be loaded from actual Mega Sena results
    sample_historical = [
        [4, 5, 30, 33, 41, 52],
        [10, 18, 25, 35, 47, 58],
        [3, 12, 23, 25, 38, 54],
        [7, 12, 18, 26, 35, 46],
        [5, 12, 20, 27, 34, 58],
    ]
    
    generator.load_historical_data(sample_historical)
    
    print("\nEscolha uma estratégia:")
    print("1. Balanceada (Hot + Cold + Random)")
    print("2. Números Quentes (Mais sorteados)")
    print("3. Números Frios (Menos sorteados)")
    print("4. Completamente Aleatório")
    print("5. Baseado em Fibonacci")
    print("6. Par/Ímpar Balanceado")
    print("7. Gerar Múltiplos Jogos (todas estratégias)")
    
    try:
        choice = input("\nDigite sua escolha (1-7): ").strip()
        
        if choice == '7':
            num_games = int(input("Quantos jogos por estratégia? (1-10): "))
            num_games = max(1, min(10, num_games))
            
            strategies = ['balanced', 'hot', 'cold', 'random', 'fibonacci', 'even_odd']
            for strategy in strategies:
                games = generator.generate_multiple_games(num_games, strategy)
                print_combinations(games, strategy)
        else:
            strategy_map = {
                '1': 'balanced',
                '2': 'hot',
                '3': 'cold',
                '4': 'random',
                '5': 'fibonacci',
                '6': 'even_odd'
            }
            
            strategy = strategy_map.get(choice, 'balanced')
            num_games = int(input("Quantos jogos gerar? (1-20): "))
            num_games = max(1, min(20, num_games))
            
            games = generator.generate_multiple_games(num_games, strategy)
            print_combinations(games, strategy)
            
            # Show analysis for first game
            if games:
                print("\nAnálise do primeiro jogo:")
                analysis = generator.analyze_combination(games[0])
                print(f"  Pares: {analysis['even_count']} | Ímpares: {analysis['odd_count']}")
                print(f"  Soma: {analysis['sum']} | Média: {analysis['average']:.1f}")
                print(f"  Distribuição: Baixos={analysis['distribution']['low (1-20)']} "
                      f"Médios={analysis['distribution']['mid (21-40)']} "
                      f"Altos={analysis['distribution']['high (41-60)']}")
    
    except (ValueError, KeyboardInterrupt):
        print("\n\nOperação cancelada.")
    
    print("\n" + "="*60)
    print("IMPORTANTE: Este sistema é apenas uma ferramenta de análise.")
    print("A loteria é um jogo de azar. Jogue com responsabilidade.")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
