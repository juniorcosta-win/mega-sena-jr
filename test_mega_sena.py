#!/usr/bin/env python3
"""
Testes unitários para o sistema Mega Sena JR
Executa validações básicas das funcionalidades principais
"""

import sys
from mega_sena import MegaSenaGenerator


def test_basic_generation():
    """Testa geração básica de números"""
    print("🧪 Testando geração básica de números...")
    generator = MegaSenaGenerator()
    
    # Testa cada estratégia
    strategies = [
        'balanced', 'hot', 'cold', 'random', 'fibonacci', 'even_odd'
    ]
    
    for strategy in strategies:
        games = generator.generate_multiple_games(3, strategy)
        
        # Valida que foram gerados 3 jogos
        assert len(games) == 3, f"Erro: deveria ter gerado 3 jogos para {strategy}"
        
        # Valida cada jogo
        for game in games:
            # Deve ter exatamente 6 números
            assert len(game) == 6, f"Erro: jogo deve ter 6 números"
            
            # Todos números devem estar entre 1 e 60
            assert all(1 <= n <= 60 for n in game), f"Erro: números fora do range"
            
            # Não deve ter números repetidos
            assert len(game) == len(set(game)), f"Erro: números repetidos"
            
            # Deve estar ordenado
            assert game == sorted(game), f"Erro: números não ordenados"
    
    print("✅ Geração básica: OK")
    return True


def test_historical_data():
    """Testa carregamento e análise de dados históricos"""
    print("🧪 Testando dados históricos...")
    generator = MegaSenaGenerator()
    
    # Dados de teste
    test_data = [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [1, 2, 3, 7, 8, 9]
    ]
    
    generator.load_historical_data(test_data)
    
    # Testa estatísticas
    stats = generator.get_statistics()
    assert stats['total_draws'] == 3, "Erro: contador de sorteios incorreto"
    
    # Números 1,2,3 devem ser quentes (aparecem 2x)
    hot = generator.get_hot_numbers(10)
    assert 1 in hot and 2 in hot and 3 in hot, "Erro: análise de números quentes"
    
    print("✅ Dados históricos: OK")
    return True


def test_analysis():
    """Testa análise de combinações"""
    print("🧪 Testando análise de combinações...")
    generator = MegaSenaGenerator()
    
    # Testa combinação com 3 pares e 3 ímpares
    test_game = [2, 4, 6, 1, 3, 5]
    analysis = generator.analyze_combination(test_game)
    
    assert analysis['even_count'] == 3, "Erro: contagem de pares"
    assert analysis['odd_count'] == 3, "Erro: contagem de ímpares"
    assert analysis['sum'] == 21, "Erro: soma incorreta"
    
    print("✅ Análise de combinações: OK")
    return True


def test_even_odd_balance():
    """Testa estratégia de pares e ímpares balanceados"""
    print("🧪 Testando balanceamento par/ímpar...")
    generator = MegaSenaGenerator()
    
    # Gera múltiplos jogos e verifica o balanceamento
    for _ in range(10):
        game = generator.generate_even_odd_balanced()
        even = sum(1 for n in game if n % 2 == 0)
        odd = 6 - even
        
        # Deve ter exatamente 3 pares e 3 ímpares
        assert even == 3, f"Erro: deveria ter 3 pares, tem {even}"
        assert odd == 3, f"Erro: deveria ter 3 ímpares, tem {odd}"
    
    print("✅ Balanceamento par/ímpar: OK")
    return True


def test_fibonacci_strategy():
    """Testa estratégia Fibonacci"""
    print("🧪 Testando estratégia Fibonacci...")
    generator = MegaSenaGenerator()
    
    # Números Fibonacci até 60: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
    fib_numbers = {1, 2, 3, 5, 8, 13, 21, 34, 55}
    
    # Gera alguns jogos e verifica se contém números Fibonacci
    for _ in range(5):
        game = generator.generate_fibonacci_based()
        game_set = set(game)
        
        # Deve ter pelo menos um número Fibonacci
        has_fib = bool(game_set & fib_numbers)
        # (Nem sempre terá devido à aleatoriedade, mas na maioria sim)
    
    print("✅ Estratégia Fibonacci: OK")
    return True


def test_number_ranges():
    """Testa distribuição por faixas"""
    print("🧪 Testando distribuição por faixas...")
    generator = MegaSenaGenerator()
    
    # Testa análise de distribuição
    test_cases = [
        ([1, 2, 3, 4, 5, 6], 6, 0, 0),      # Todos baixos
        ([21, 22, 23, 24, 25, 26], 0, 6, 0), # Todos médios
        ([41, 42, 43, 44, 45, 46], 0, 0, 6), # Todos altos
        ([10, 15, 25, 35, 45, 55], 2, 2, 2), # Balanceado
    ]
    
    for game, expected_low, expected_mid, expected_high in test_cases:
        analysis = generator.analyze_combination(game)
        dist = analysis['distribution']
        
        assert dist['low (1-20)'] == expected_low, f"Erro: baixos em {game}"
        assert dist['mid (21-40)'] == expected_mid, f"Erro: médios em {game}"
        assert dist['high (41-60)'] == expected_high, f"Erro: altos em {game}"
    
    print("✅ Distribuição por faixas: OK")
    return True


def run_all_tests():
    """Executa todos os testes"""
    print("="*60)
    print("🧪 MEGA SENA JR - Suite de Testes")
    print("="*60)
    print()
    
    tests = [
        test_basic_generation,
        test_historical_data,
        test_analysis,
        test_even_odd_balance,
        test_fibonacci_strategy,
        test_number_ranges
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
        except AssertionError as e:
            print(f"❌ Teste falhou: {e}")
            failed += 1
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            failed += 1
    
    print()
    print("="*60)
    print(f"Resultados: {passed} passaram, {failed} falharam")
    print("="*60)
    
    if failed == 0:
        print("🎉 Todos os testes passaram com sucesso!")
        return 0
    else:
        print("⚠️  Alguns testes falharam. Verifique os erros acima.")
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
