class MiniCPU:
    def __init__(self):
        self.mem = [0] * 256
        self.reg = [0, 0, 0, 0]
        self.pc = 0
        self.zf = 0
        self.running = True
        self.ciclo = 0

    def load_program(self):
        self.mem[0x00] = 0x07; self.mem[0x01] = 0x40; self.mem[0x02] = 0x00

        self.mem[0x08] = 0
        self.mem[0x09] = 1
        self.mem[0x10] = 7

        self.mem[0x40] = 0x05; self.mem[0x41] = 0x00; self.mem[0x42] = 0x00
        self.mem[0x43] = 0x05; self.mem[0x44] = 0x01; self.mem[0x45] = 0x01
        self.mem[0x46] = 0x01; self.mem[0x47] = 0x02; self.mem[0x48] = 0x10
        self.mem[0x49] = 0x01; self.mem[0x4A] = 0x03; self.mem[0x4B] = 0x09
        self.mem[0x4C] = 0x04; self.mem[0x4D] = 0x02; self.mem[0x4E] = 0x03

        self.mem[0x4F] = 0x01; self.mem[0x50] = 0x03; self.mem[0x51] = 0x08
        self.mem[0x52] = 0x06; self.mem[0x53] = 0x02; self.mem[0x54] = 0x03
        self.mem[0x55] = 0x08; self.mem[0x56] = 0x76; self.mem[0x57] = 0x00

        self.mem[0x58] = 0x05; self.mem[0x59] = 0x03; self.mem[0x5A] = 0x00
        self.mem[0x5B] = 0x03; self.mem[0x5C] = 0x03; self.mem[0x5D] = 0x00
        self.mem[0x5E] = 0x03; self.mem[0x5F] = 0x03; self.mem[0x60] = 0x01

        self.mem[0x61] = 0x05; self.mem[0x62] = 0x00; self.mem[0x63] = 0x00
        self.mem[0x64] = 0x03; self.mem[0x65] = 0x00; self.mem[0x66] = 0x01

        self.mem[0x67] = 0x05; self.mem[0x68] = 0x01; self.mem[0x69] = 0x00
        self.mem[0x6A] = 0x03; self.mem[0x6B] = 0x01; self.mem[0x6C] = 0x03

        self.mem[0x6D] = 0x01; self.mem[0x6E] = 0x03; self.mem[0x6F] = 0x09
        self.mem[0x70] = 0x04; self.mem[0x71] = 0x02; self.mem[0x72] = 0x03
        self.mem[0x73] = 0x07; self.mem[0x74] = 0x4F; self.mem[0x75] = 0x00

        self.mem[0x76] = 0x02; self.mem[0x77] = 0x01; self.mem[0x78] = 0x20
        self.mem[0x79] = 0x0A; self.mem[0x7A] = 0x00; self.mem[0x7B] = 0x00

    def fetch(self):
        op = self.mem[self.pc]
        a = self.mem[self.pc + 1]
        b = self.mem[self.pc + 2]
        self.pc += 3
        return op, a, b

    def decode_execute(self, op, a, b):
        if op == 0x01:
            self.reg[a] = self.mem[b]
        elif op == 0x02:
            self.mem[b] = self.reg[a]
        elif op == 0x03:
            self.reg[a] = (self.reg[a] + self.reg[b]) & 0xFF
        elif op == 0x04:
            self.reg[a] = (self.reg[a] - self.reg[b]) & 0xFF
        elif op == 0x05:
            self.reg[a] = b
        elif op == 0x06:
            self.zf = 1 if self.reg[a] == self.reg[b] else 0
        elif op == 0x07:
            self.pc = a
        elif op == 0x08:
            if self.zf:
                self.pc = a
        elif op == 0x09:
            if not self.zf:
                self.pc = a
        elif op == 0x0A:
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
        assert self.mem[0x20] == 13
        print('Teste passou! Fibonacci(7) = 13')

if __name__ == '__main__':
    cpu = MiniCPU()
    cpu.load_program()
    cpu.run()