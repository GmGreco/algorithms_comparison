import random
import time
import matplotlib.pyplot as plt
import numpy as np

def busca_sequencial(lista, elemento):
    comparacoes = 0
    for i in range(len(lista)):
        comparacoes += 1
        if lista[i] == elemento:
            return i, comparacoes
    return -1, comparacoes

def busca_binaria(lista, elemento):
    comparacoes = 0
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        comparacoes += 1
        meio = (inicio + fim) // 2
        
        if lista[meio] == elemento:
            return meio, comparacoes
        elif lista[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1
    
    return -1, comparacoes

def gerar_dados(tamanho):
    return list(range(1, tamanho + 1))

def executar_teste_com_dados(lista, elemento):
    inicio = time.time()
    indice_seq, comp_seq = busca_sequencial(lista, elemento)
    tempo_seq = time.time() - inicio
    
    inicio = time.time()
    indice_bin, comp_bin = busca_binaria(lista, elemento)
    tempo_bin = time.time() - inicio
    
    return {
        'sequencial': {'tempo': tempo_seq, 'comparacoes': comp_seq, 'indice': indice_seq},
        'binaria': {'tempo': tempo_bin, 'comparacoes': comp_bin, 'indice': indice_bin}
    }

def executar_teste(lista, elemento, nome_caso):
    print(f"\n--- {nome_caso} ---")
    print(f"Lista com {len(lista)} elementos")
    print(f"Procurando elemento: {elemento}")
    
    resultado = executar_teste_com_dados(lista, elemento)
    
    print(f"  Índice encontrado: {resultado['sequencial']['indice']}")
    print(f"  Comparações: {resultado['sequencial']['comparacoes']}")
    print(f"  Tempo: {resultado['sequencial']['tempo']:.8f} segundos")
    
    print(f"\nBusca Binária:")
    print(f"  Índice encontrado: {resultado['binaria']['indice']}")
    print(f"  Comparações: {resultado['binaria']['comparacoes']}")
    print(f"  Tempo: {resultado['binaria']['tempo']:.8f} segundos")
    
    if resultado['sequencial']['tempo'] > 0:
        melhoria_tempo = resultado['sequencial']['tempo'] / resultado['binaria']['tempo'] if resultado['binaria']['tempo'] > 0 else float('inf')
        print(f"\nMelhoria da busca binária:")
        print(f"  Tempo: {melhoria_tempo:.2f}x mais rápida")
        print(f"  Comparações: {resultado['sequencial']['comparacoes'] / resultado['binaria']['comparacoes'] if resultado['binaria']['comparacoes'] > 0 else float('inf'):.2f}x menos comparações")
    
    return resultado

def criar_graficos(dados_coletas):
 
    tamanhos = list(dados_coletas.keys())
    
    tempo_seq_medio = [dados_coletas[t]['caso_medio']['sequencial']['tempo'] for t in tamanhos]
    tempo_bin_medio = [dados_coletas[t]['caso_medio']['binaria']['tempo'] for t in tamanhos]
    comp_seq_medio = [dados_coletas[t]['caso_medio']['sequencial']['comparacoes'] for t in tamanhos]
    comp_bin_medio = [dados_coletas[t]['caso_medio']['binaria']['comparacoes'] for t in tamanhos]
    
    tempo_seq_pior = [dados_coletas[t]['pior_caso']['sequencial']['tempo'] for t in tamanhos]
    tempo_bin_pior = [dados_coletas[t]['pior_caso']['binaria']['tempo'] for t in tamanhos]
    comp_seq_pior = [dados_coletas[t]['pior_caso']['sequencial']['comparacoes'] for t in tamanhos]
    comp_bin_pior = [dados_coletas[t]['pior_caso']['binaria']['comparacoes'] for t in tamanhos]
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    ax1.plot(tamanhos, tempo_seq_medio, 'r-o', label='Busca Sequencial', linewidth=2, markersize=8)
    ax1.plot(tamanhos, tempo_bin_medio, 'b-s', label='Busca Binária', linewidth=2, markersize=8)
    ax1.set_xlabel('Tamanho da Lista')
    ax1.set_ylabel('Tempo (segundos)')
    ax1.set_title('Tempo de Execução - Caso Médio')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_yscale('log')
    
    ax2.plot(tamanhos, tempo_seq_pior, 'r-o', label='Busca Sequencial', linewidth=2, markersize=8)
    ax2.plot(tamanhos, tempo_bin_pior, 'b-s', label='Busca Binária', linewidth=2, markersize=8)
    ax2.set_xlabel('Tamanho da Lista')
    ax2.set_ylabel('Tempo (segundos)')
    ax2.set_title('Tempo de Execução - Pior Caso')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_yscale('log')
    
    ax3.plot(tamanhos, comp_seq_medio, 'r-o', label='Busca Sequencial', linewidth=2, markersize=8)
    ax3.plot(tamanhos, comp_bin_medio, 'b-s', label='Busca Binária', linewidth=2, markersize=8)
    ax3.set_xlabel('Tamanho da Lista')
    ax3.set_ylabel('Número de Comparações')
    ax3.set_title('Número de Comparações - Caso Médio')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    ax3.set_yscale('log')
    
    ax4.plot(tamanhos, comp_seq_pior, 'r-o', label='Busca Sequencial', linewidth=2, markersize=8)
    ax4.plot(tamanhos, comp_bin_pior, 'b-s', label='Busca Binária', linewidth=2, markersize=8)
    ax4.set_xlabel('Tamanho da Lista')
    ax4.set_ylabel('Número de Comparações')
    ax4.set_title('Número de Comparações - Pior Caso')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    ax4.set_yscale('log')
    
    plt.tight_layout()
    plt.savefig('comparacao_algoritmos.png', dpi=300, bbox_inches='tight')
    plt.show()

def main():
 
    print("=" * 60)
    print("COMPARAÇÃO: BUSCA SEQUENCIAL vs BUSCA BINÁRIA")
    print("=" * 60)
    
    tamanhos = [1000, 10000, 100000]
    dados_coletas = {}
    
    for tamanho in tamanhos:
        print(f"\n{'=' * 40}")
        print(f"TESTANDO COM {tamanho} ELEMENTOS")
        print(f"{'=' * 40}")
        
        lista = gerar_dados(tamanho)
        dados_coletas[tamanho] = {}
        
        elemento_caso_medio = random.choice(lista)
        resultado_medio = executar_teste(lista, elemento_caso_medio, f"CASO MÉDIO - {tamanho} elementos")
        dados_coletas[tamanho]['caso_medio'] = resultado_medio
        
        elemento_pior_caso = tamanho + 1000 
        resultado_pior = executar_teste(lista, elemento_pior_caso, f"PIOR CASO - {tamanho} elementos")
        dados_coletas[tamanho]['pior_caso'] = resultado_pior
    
    print(f"\n{'=' * 60}")
    print("GERANDO GRÁFICOS COMPARATIVOS...")
    print("=" * 60)
    
    criar_graficos(dados_coletas)
    
    print("\nGráfico salvo como:")
    print("- comparacao_algoritmos.png")

if __name__ == "__main__":
    main()
