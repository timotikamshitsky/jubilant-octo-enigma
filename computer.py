from component.cpu import CPU
from component.gpu import GPU
from component.motherboard import Motherboard
from component.data import Component


class Computer(CPU, GPU, Motherboard):
    cpu: CPU
    gpu: GPU
    motherboard: Motherboard

    def __init__(self, cpu, gpu, motherboard):
        self.cpu = cpu
        self.gpu = gpu
        self.motherboard = motherboard

    def set_cpu(self, cpu):
        self.cpu = cpu

    def set_gpu(self, gpu):
        self.gpu = gpu

    def set_motherboard(self, motherboard):
        self.motherboard = motherboard

    def get_cpu(self):
        return self.cpu

    def get_gpu(self):
        return self.gpu

    def get_motherboard(self):
        return self.motherboard

    def get_computer_data(self):
        self.cpu.get_specs()
        self.gpu.get_specs()
        self.motherboard.get_specs()


if __name__ == '__main__':
    cpu = CPU("Jetson TX2", 2017, "AMD")
    gpu = GPU("TitanX", 2019, "Nivida")
    motherboards = Motherboard("Asus 200 pro", 2009, "Asus")
    computer = Computer(cpu, gpu, motherboards)
    computer.get_computer_data()



























