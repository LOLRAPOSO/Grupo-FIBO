class MiniCPU:
    def __init__(self):
        self.mem = [0] * 256          # memória
        self.reg = [0, 0, 0, 0]       # R0-R3
        self.pc = 0                   # Program Counter
        self.zf = 0                   # Zero Flag
        self.running = True
        self.ciclo = 0

    def load_program(self):
        # Salta para o início do código em 0x40
        self.mem[0x00] = 0x07; self.mem[0x01] = 0x40; self.mem[0x02] = 0x00  # JMP 0x40

        # Dados
        self.mem[0x08] = 0    # zero
        self.mem[0x09] = 1    # um
        self.mem[0x0A] = 7    # N = 7

        # Código a partir de 0x40
        # MOV R0, 0        ; a = 0
        self.mem[0x40] = 0x05; self.mem[0x41] = 0x00; self.mem[0x42] = 0x00
        # MOV R1, 1        ; b = 1
        self.mem[0x43] = 0x05; self.mem[0x44] = 0x01; self.mem[0x45] = 0x01
        # LOAD R2, 0x0A    ; R2 = N = 7
        self.mem[0x46] = 0x01; self.mem[0x47] = 0x02; self.mem[0x48] = 0x0A
        # LOAD R3, 0x09    ; R3 = 1
        self.mem[0x49] = 0x01; self.mem[0x4A] = 0x03; self.mem[0x4B] = 0x09
        # SUB R2, R3       ; R2 = N - 1 = 6 (contador)
        self.mem[0x4C] = 0x04; self.mem[0x4D] = 0x02; self.mem[0x4E] = 0x03

        # loop: (0x4F)
        # LOAD R3, 0x08    ; R3 = 0
        self.mem[0x4F] = 0x01; self.mem[0x50] = 0x03; self.mem[0x51] = 0x08
        # CMP R2, R3       ; compara contador com 0
        self.mem[0x52] = 0x06; self.mem[0x53] = 0x02; self.mem[0x54] = 0x03
        # JZ done (0x76)
        self.mem[0x55] = 0x08; self.mem[0x56] = 0x76; self.mem[0x57] = 0x00

        # temp = a + b
        # MOV R3, 0
        self.mem[0x58] = 0x05; self.mem[0x59] = 0x03; self.mem[0x5A] = 0x00
        # ADD R3, R0
        self.mem[0x5B] = 0x03; self.mem[0x5C] = 0x03; self.mem[0x5D] = 0x00
        # ADD R3, R1
        self.mem[0x5E] = 0x03; self.mem[0x5F] = 0x03; self.mem[0x60] = 0x01

        # a = b
        # MOV R0, 0
        self.mem[0x61] = 0x05; self.mem[0x62] = 0x00; self.mem[0x63] = 0x00
        # ADD R0, R1
        self.mem[0x64] = 0x03; self.mem[0x65] = 0x00; self.mem[0x66] = 0x01

        # b = temp
        # MOV R1, 0
        self.mem[0x67] = 0x05; self.mem[0x68] = 0x01; self.mem[0x69] = 0x00
        # ADD R1, R3
        self.mem[0x6A] = 0x03; self.mem[0x6B] = 0x01; self.mem[0x6C] = 0x03

        # contador--
        # LOAD R3, 0x09
        self.mem[0x6D] = 0x01; self.mem[0x6E] = 0x03; self.mem[0x6F] = 0x09
        # SUB R2, R3
        self.mem[0x70] = 0x04; self.mem[0x71] = 0x02; self.mem[0x72] = 0x03
        # JMP loop (0x4F)
        self.mem[0x73] = 0x07; self.mem[0x74] = 0x4F; self.mem[0x75] = 0x00

        # done: (0x76)
        # STORE R1, 0x20   ; mem[0x20] = resultado
        self.mem[0x76] = 0x02; self.mem[0x77] = 0x01; self.mem[0x78] = 0x20
        # HALT
        self.mem[0x79] = 0x0A; self.mem[0x7A] = 0x00; self.mem[0x7B] = 0x00

    def fetch(self):
        op = self.mem[self.pc]
        a = self.mem[self.pc + 1]
        b = self.mem[self.pc + 2]
        self.pc += 3
        return op, a, b

    def decode_execute(self, op, a, b):
        if op == 0x01:   # LOAD
            self.reg[a] = self.mem[b]
        elif op == 0x02: # STORE
            self.mem[b] = self.reg[a]
        elif op == 0x03: # ADD
            self.reg[a] = (self.reg[a] + self.reg[b]) & 0xFF
        elif op == 0x04: # SUB
            self.reg[a] = (self.reg[a] - self.reg[b]) & 0xFF
        elif op == 0x05: # MOV
            self.reg[a] = b
        elif op == 0x06: # CMP
            self.zf = 1 if self.reg[a] == self.reg[b] else 0
        elif op == 0x07: # JMP
            self.pc = a
        elif op == 0x08: # JZ
            if self.zf:
                self.pc = a
        elif op == 0x09: # JNZ
            if not self.zf:
                self.pc = a
        elif op == 0x0A: # HALT
            self.running = False

    def trace(self, op, a, b):
        nomes = {1:'LOAD', 2:'STORE', 3:'ADD', 4:'SUB',
                 5:'MOV', 6:'CMP', 7:'JMP', 8:'JZ', 9:'JNZ', 10:'HALT'}
        nome = nomes.get(op, '???')
        print(f'Ciclo {self.ciclo}: {nome:5s} {a},{b} |'
              f' R0={self.reg[0]:3d} R1={self.reg[1]:3d}'
              f' R2={self.reg[2]:3d} R3={self.reg[3]:3d}'
              f' | PC={self.pc:3d} ZF={self.zf}')

    def run(self):
        while self.running and self.pc < 256:
            self.ciclo += 1
            op, a, b = self.fetch()
            self.decode_execute(op, a, b)
            self.trace(op, a, b)
        print(f'\nResultado em 0x20 = {self.mem[0x20]} (esperado: 13)')

if __name__ == '__main__':
    cpu = MiniCPU()
    cpu.load_program()
    cpu.run()