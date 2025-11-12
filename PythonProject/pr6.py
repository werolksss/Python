import psutil
import time
import statistics


class MemoryMonitor:
    def __init__(self):
        self.process = psutil.Process()
        self.memory_readings = []
        self.start_time = time.time()
        self.max_memory = 0

    def get_memory_usage(self):
        memory_info = self.process.memory_info()
        return memory_info.rss / (1024 * 1024)

    def monitor(self, duration=60, interval=2, memory_limit=1024):
        print("Запуск мониторинга памяти...")
        print("Время\t\tТекущая (MB)\tМакс. (MB)\tСредняя (MB)\tСкорость прироста (MB/с)")
        print("-" * 80)

        end_time = time.time() + duration
        prev_memory = self.get_memory_usage()

        while time.time() < end_time:
            current_memory = self.get_memory_usage()
            self.memory_readings.append(current_memory)
            self.max_memory = max(self.max_memory, current_memory)

            time_diff = interval
            memory_diff = current_memory - prev_memory
            growth_rate = memory_diff / time_diff

            elapsed = time.time() - self.start_time
            avg_memory = statistics.mean(self.memory_readings[-10:]) if len(
                self.memory_readings) >= 10 else current_memory

            print(
                f"{elapsed:6.1f}c\t{current_memory:8.1f}\t{self.max_memory:8.1f}\t{avg_memory:8.1f}\t{growth_rate:8.2f}")

            if current_memory > memory_limit:
                print(f"ПРЕДУПРЕЖДЕНИЕ: Память превысила лимит {memory_limit} MB!")

            prev_memory = current_memory
            time.sleep(interval)

    def get_statistics(self):
        if not self.memory_readings:
            return {}

        return {
            'max_memory': self.max_memory,
            'avg_memory': statistics.mean(self.memory_readings),
            'min_memory': min(self.memory_readings),
            'total_time': time.time() - self.start_time
        }


def create_memory_load():
    data_list = []
    for i in range(50000):
        data_list.append([j for j in range(1000)])
        if i % 1000 == 0:
            print(f"Создано {i} элементов...")
        time.sleep(0.001)
    return data_list

monitor = MemoryMonitor()

import threading

load_thread = threading.Thread(target=create_memory_load)
load_thread.start()

monitor.monitor(duration=30, interval=1, memory_limit=500)

stats = monitor.get_statistics()
print("\n=== СТАТИСТИКА ===")
print(f"Максимальная нагрузка на память: {stats['max_memory']:.2f} MB")
print(f"Средняя нагрузка на память: {stats['avg_memory']:.2f} MB")
print(f"Минимальная нагрузка на память: {stats['min_memory']:.2f} MB")
print(f"Общее время мониторинга: {stats['total_time']:.2f} секунд")

load_thread.join()
print("Мониторинг завершен.")