import psutil


class HardwareDetails:

    def __init__(self):
        self.get_cpu_information()
        self.get_gpu_information()
        self.get_memory_information()

    def get_cpu_information(self):
        self.cpu_cores = psutil.cpu_count()

        from cpuinfo import get_cpu_info

        cpu = get_cpu_info()
        cpu_model = cpu.get("brand_raw") or "Unknown CPU"
        self.cpu_model = cpu_model

        import platform

        architecture = platform.machine()
        self.cpu_architecture = architecture

        # print(self.cpu_cores)
        # print(self.cpu_model)
        # print(self.cpu_architecture)

    def get_gpu_information(self):
        # Check the GPU of system
        import pynvml

        pynvml.nvmlInit()

        try:
            for i in range(pynvml.nvmlDeviceGetCount()):
                gpu = pynvml.nvmlDeviceGetHandleByIndex(i)
                memory = pynvml.nvmlDeviceGetMemoryInfo(gpu)
                self.gpu_name = pynvml.nvmlDeviceGetName(gpu)
                self.total_gpu_memory = float(memory.total) / 1024**3
                self.used_gpu_memory = float(memory.used) / 1024**3
                self.free_gpu_memory = float(memory.free) / 1024**3
        finally:
            pynvml.nvmlShutdown()
            # print(self.gpu_name)
            # print(self.total_gpu_memory)
            # print(self.used_gpu_memory)
            # print(self.free_gpu_memory)

    def get_memory_information(self):
        # Check the Memory of system
        self.available_memory = psutil.virtual_memory().available / 1024**3
        self.total_memory = psutil.virtual_memory().total / 1024**3

        # print(self.available_memory / 1024**3)
        # print(self.total_memory / 1024**3)


hardwaredetails = HardwareDetails()
