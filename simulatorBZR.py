import pandas as pd
import numpy as np
from typing import List, Tuple

# Definindo os parâmetros do cenário
token_bzr_supply = 1000
weth_liquidity_1 = 0.01
weth_liquidity_2 = 0.02
fee_tier = 0.0003  # Taxa de negociação de 0.03%

# Criando o pool de liquidez
def create_pool(token_amount: float, weth_amount: float) -> Tuple[float, float]:
    total_value = token_amount + weth_amount
    token_share = token_amount / total_value
    weth_share = weth_amount / total_value
    return token_share, weth_share

token_share_1, weth_share_1 = create_pool(token_bzr_supply, weth_liquidity_1)
token_share_2, weth_share_2 = create_pool(token_bzr_supply, weth_liquidity_2)

# Definindo as funções de simulação
def simulate_trade(
    token_amount: float,
    weth_amount: float,
    trade_amount: float,
    is_buy: bool
) -> Tuple[float, float]:
    if is_buy:
        new_token_amount = token_amount + trade_amount
        new_weth_amount = weth_amount - (trade_amount / (1 - fee_tier))
    else:
        new_weth_amount = weth_amount + trade_amount
        new_token_amount = token_amount - (trade_amount * (1 - fee_tier))
    return new_token_amount, new_weth_amount

def simulate_liquidity_provision(
    token_amount: float,
    weth_amount: float,
    added_token: float,
    added_weth: float
) -> Tuple[float, float]:
    new_token_amount = token_amount + added_token
    new_weth_amount = weth_amount + added_weth
    return new_token_amount, new_weth_amount

# Simulando as operações
# Primeira rodada com 0.01 WETH
token_amount_1 = token_bzr_supply
weth_amount_1 = weth_liquidity_1
print(f"Pool 1: Token BZR = {token_amount_1}, WETH = {weth_amount_1}")

# Segunda rodada com 0.02 WETH 
token_amount_2 = token_bzr_supply
weth_amount_2 = weth_liquidity_2
print(f"Pool 2: Token BZR = {token_amount_2}, WETH = {weth_amount_2}")

# Exibindo os resultados
print("Resultado da Simulação:")
print(f"Pool 1: Token BZR = {token_amount_1}, WETH = {weth_amount_1}")
print(f"Pool 2: Token BZR = {token_amount_2}, WETH = {weth_amount_2}")