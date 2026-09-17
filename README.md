# MiniCPU Simulator – Grupo 1: Fibonacci

Simulador da MiniCPU implementado em Python como parte da atividade Torneio de Processadores (Infraestrutura de Hardware). O simulador executa o ciclo Fetch -> Decode -> Execute e resolve o cálculo do enésimo número de Fibonacci (N=7), gravando o resultado no endereço 0x20. Resultado esperado: fib(7) = 13.

## Equipe

Ana Beatriz
Daniel Andrade
Eduardo Boxwell
Gustavo Rezende
Juan Riquelme
Matheus Lima
Rafael Pimentel
Victor Carraly
Walter Maia

## Como executar

Requisito: Python 3.x

```
python fibo.py
```

A saída mostra o trace ciclo a ciclo com o estado dos registradores R0–R3, PC e ZF, seguido do resultado final em 0x20.
