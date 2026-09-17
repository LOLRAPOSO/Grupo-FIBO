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


## Resultado dos testes

````
Ciclo 1: JMP   64,0 | R0=  0 R1=  0 R2=  0 R3=  0 | PC= 64 ZF=0
Ciclo 2: MOV   0,0 | R0=  0 R1=  0 R2=  0 R3=  0 | PC= 67 ZF=0
Ciclo 3: MOV   1,1 | R0=  0 R1=  1 R2=  0 R3=  0 | PC= 70 ZF=0
Ciclo 4: LOAD  2,16 | R0=  0 R1=  1 R2=  7 R3=  0 | PC= 73 ZF=0
Ciclo 5: LOAD  3,9 | R0=  0 R1=  1 R2=  7 R3=  1 | PC= 76 ZF=0
Ciclo 6: SUB   2,3 | R0=  0 R1=  1 R2=  6 R3=  1 | PC= 79 ZF=0
Ciclo 7: LOAD  3,8 | R0=  0 R1=  1 R2=  6 R3=  0 | PC= 82 ZF=0
Ciclo 8: CMP   2,3 | R0=  0 R1=  1 R2=  6 R3=  0 | PC= 85 ZF=0
Ciclo 9: JZ    118,0 | R0=  0 R1=  1 R2=  6 R3=  0 | PC= 88 ZF=0
Ciclo 10: MOV   3,0 | R0=  0 R1=  1 R2=  6 R3=  0 | PC= 91 ZF=0
Ciclo 11: ADD   3,0 | R0=  0 R1=  1 R2=  6 R3=  0 | PC= 94 ZF=0
Ciclo 12: ADD   3,1 | R0=  0 R1=  1 R2=  6 R3=  1 | PC= 97 ZF=0
Ciclo 13: MOV   0,0 | R0=  0 R1=  1 R2=  6 R3=  1 | PC=100 ZF=0
Ciclo 14: ADD   0,1 | R0=  1 R1=  1 R2=  6 R3=  1 | PC=103 ZF=0
Ciclo 15: MOV   1,0 | R0=  1 R1=  0 R2=  6 R3=  1 | PC=106 ZF=0
Ciclo 16: ADD   1,3 | R0=  1 R1=  1 R2=  6 R3=  1 | PC=109 ZF=0
Ciclo 17: LOAD  3,9 | R0=  1 R1=  1 R2=  6 R3=  1 | PC=112 ZF=0
Ciclo 18: SUB   2,3 | R0=  1 R1=  1 R2=  5 R3=  1 | PC=115 ZF=0
Ciclo 19: JMP   79,0 | R0=  1 R1=  1 R2=  5 R3=  1 | PC= 79 ZF=0
Ciclo 20: LOAD  3,8 | R0=  1 R1=  1 R2=  5 R3=  0 | PC= 82 ZF=0
Ciclo 21: CMP   2,3 | R0=  1 R1=  1 R2=  5 R3=  0 | PC= 85 ZF=0
Ciclo 22: JZ    118,0 | R0=  1 R1=  1 R2=  5 R3=  0 | PC= 88 ZF=0
Ciclo 23: MOV   3,0 | R0=  1 R1=  1 R2=  5 R3=  0 | PC= 91 ZF=0
Ciclo 24: ADD   3,0 | R0=  1 R1=  1 R2=  5 R3=  1 | PC= 94 ZF=0
Ciclo 25: ADD   3,1 | R0=  1 R1=  1 R2=  5 R3=  2 | PC= 97 ZF=0
Ciclo 26: MOV   0,0 | R0=  0 R1=  1 R2=  5 R3=  2 | PC=100 ZF=0
Ciclo 27: ADD   0,1 | R0=  1 R1=  1 R2=  5 R3=  2 | PC=103 ZF=0
Ciclo 28: MOV   1,0 | R0=  1 R1=  0 R2=  5 R3=  2 | PC=106 ZF=0
Ciclo 29: ADD   1,3 | R0=  1 R1=  2 R2=  5 R3=  2 | PC=109 ZF=0
Ciclo 30: LOAD  3,9 | R0=  1 R1=  2 R2=  5 R3=  1 | PC=112 ZF=0
Ciclo 31: SUB   2,3 | R0=  1 R1=  2 R2=  4 R3=  1 | PC=115 ZF=0
Ciclo 32: JMP   79,0 | R0=  1 R1=  2 R2=  4 R3=  1 | PC= 79 ZF=0
Ciclo 33: LOAD  3,8 | R0=  1 R1=  2 R2=  4 R3=  0 | PC= 82 ZF=0
Ciclo 34: CMP   2,3 | R0=  1 R1=  2 R2=  4 R3=  0 | PC= 85 ZF=0
Ciclo 35: JZ    118,0 | R0=  1 R1=  2 R2=  4 R3=  0 | PC= 88 ZF=0
Ciclo 36: MOV   3,0 | R0=  1 R1=  2 R2=  4 R3=  0 | PC= 91 ZF=0
Ciclo 37: ADD   3,0 | R0=  1 R1=  2 R2=  4 R3=  1 | PC= 94 ZF=0
Ciclo 38: ADD   3,1 | R0=  1 R1=  2 R2=  4 R3=  3 | PC= 97 ZF=0
Ciclo 39: MOV   0,0 | R0=  0 R1=  2 R2=  4 R3=  3 | PC=100 ZF=0
Ciclo 40: ADD   0,1 | R0=  2 R1=  2 R2=  4 R3=  3 | PC=103 ZF=0
Ciclo 41: MOV   1,0 | R0=  2 R1=  0 R2=  4 R3=  3 | PC=106 ZF=0
Ciclo 42: ADD   1,3 | R0=  2 R1=  3 R2=  4 R3=  3 | PC=109 ZF=0
Ciclo 43: LOAD  3,9 | R0=  2 R1=  3 R2=  4 R3=  1 | PC=112 ZF=0
Ciclo 44: SUB   2,3 | R0=  2 R1=  3 R2=  3 R3=  1 | PC=115 ZF=0
Ciclo 45: JMP   79,0 | R0=  2 R1=  3 R2=  3 R3=  1 | PC= 79 ZF=0
Ciclo 46: LOAD  3,8 | R0=  2 R1=  3 R2=  3 R3=  0 | PC= 82 ZF=0
Ciclo 47: CMP   2,3 | R0=  2 R1=  3 R2=  3 R3=  0 | PC= 85 ZF=0
Ciclo 48: JZ    118,0 | R0=  2 R1=  3 R2=  3 R3=  0 | PC= 88 ZF=0
Ciclo 49: MOV   3,0 | R0=  2 R1=  3 R2=  3 R3=  0 | PC= 91 ZF=0
Ciclo 50: ADD   3,0 | R0=  2 R1=  3 R2=  3 R3=  2 | PC= 94 ZF=0
Ciclo 51: ADD   3,1 | R0=  2 R1=  3 R2=  3 R3=  5 | PC= 97 ZF=0
Ciclo 52: MOV   0,0 | R0=  0 R1=  3 R2=  3 R3=  5 | PC=100 ZF=0
Ciclo 53: ADD   0,1 | R0=  3 R1=  3 R2=  3 R3=  5 | PC=103 ZF=0
Ciclo 54: MOV   1,0 | R0=  3 R1=  0 R2=  3 R3=  5 | PC=106 ZF=0
Ciclo 55: ADD   1,3 | R0=  3 R1=  5 R2=  3 R3=  5 | PC=109 ZF=0
Ciclo 56: LOAD  3,9 | R0=  3 R1=  5 R2=  3 R3=  1 | PC=112 ZF=0
Ciclo 57: SUB   2,3 | R0=  3 R1=  5 R2=  2 R3=  1 | PC=115 ZF=0
Ciclo 58: JMP   79,0 | R0=  3 R1=  5 R2=  2 R3=  1 | PC= 79 ZF=0
Ciclo 59: LOAD  3,8 | R0=  3 R1=  5 R2=  2 R3=  0 | PC= 82 ZF=0
Ciclo 60: CMP   2,3 | R0=  3 R1=  5 R2=  2 R3=  0 | PC= 85 ZF=0
Ciclo 61: JZ    118,0 | R0=  3 R1=  5 R2=  2 R3=  0 | PC= 88 ZF=0
Ciclo 62: MOV   3,0 | R0=  3 R1=  5 R2=  2 R3=  0 | PC= 91 ZF=0
Ciclo 63: ADD   3,0 | R0=  3 R1=  5 R2=  2 R3=  3 | PC= 94 ZF=0
Ciclo 64: ADD   3,1 | R0=  3 R1=  5 R2=  2 R3=  8 | PC= 97 ZF=0
Ciclo 65: MOV   0,0 | R0=  0 R1=  5 R2=  2 R3=  8 | PC=100 ZF=0
Ciclo 66: ADD   0,1 | R0=  5 R1=  5 R2=  2 R3=  8 | PC=103 ZF=0
Ciclo 67: MOV   1,0 | R0=  5 R1=  0 R2=  2 R3=  8 | PC=106 ZF=0
Ciclo 68: ADD   1,3 | R0=  5 R1=  8 R2=  2 R3=  8 | PC=109 ZF=0
Ciclo 69: LOAD  3,9 | R0=  5 R1=  8 R2=  2 R3=  1 | PC=112 ZF=0
Ciclo 70: SUB   2,3 | R0=  5 R1=  8 R2=  1 R3=  1 | PC=115 ZF=0
Ciclo 71: JMP   79,0 | R0=  5 R1=  8 R2=  1 R3=  1 | PC= 79 ZF=0
Ciclo 72: LOAD  3,8 | R0=  5 R1=  8 R2=  1 R3=  0 | PC= 82 ZF=0
Ciclo 73: CMP   2,3 | R0=  5 R1=  8 R2=  1 R3=  0 | PC= 85 ZF=0
Ciclo 74: JZ    118,0 | R0=  5 R1=  8 R2=  1 R3=  0 | PC= 88 ZF=0
Ciclo 75: MOV   3,0 | R0=  5 R1=  8 R2=  1 R3=  0 | PC= 91 ZF=0
Ciclo 76: ADD   3,0 | R0=  5 R1=  8 R2=  1 R3=  5 | PC= 94 ZF=0
Ciclo 77: ADD   3,1 | R0=  5 R1=  8 R2=  1 R3= 13 | PC= 97 ZF=0
Ciclo 78: MOV   0,0 | R0=  0 R1=  8 R2=  1 R3= 13 | PC=100 ZF=0
Ciclo 79: ADD   0,1 | R0=  8 R1=  8 R2=  1 R3= 13 | PC=103 ZF=0
Ciclo 80: MOV   1,0 | R0=  8 R1=  0 R2=  1 R3= 13 | PC=106 ZF=0
Ciclo 81: ADD   1,3 | R0=  8 R1= 13 R2=  1 R3= 13 | PC=109 ZF=0
Ciclo 82: LOAD  3,9 | R0=  8 R1= 13 R2=  1 R3=  1 | PC=112 ZF=0
Ciclo 83: SUB   2,3 | R0=  8 R1= 13 R2=  0 R3=  1 | PC=115 ZF=0
Ciclo 84: JMP   79,0 | R0=  8 R1= 13 R2=  0 R3=  1 | PC= 79 ZF=0
Ciclo 85: LOAD  3,8 | R0=  8 R1= 13 R2=  0 R3=  0 | PC= 82 ZF=0
Ciclo 86: CMP   2,3 | R0=  8 R1= 13 R2=  0 R3=  0 | PC= 85 ZF=1
Ciclo 87: JZ    118,0 | R0=  8 R1= 13 R2=  0 R3=  0 | PC=118 ZF=1
Ciclo 88: STORE 1,32 | R0=  8 R1= 13 R2=  0 R3=  0 | PC=121 ZF=1
Ciclo 89: HALT  0,0 | R0=  8 R1= 13 R2=  0 R3=  0 | PC=124 ZF=1

Resultado em 0x20 = 13 (esperado: 13)
Teste passou! Fibonacci(7) = 13
````