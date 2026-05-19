class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # Resize if array is full
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        value = self.arr[self.size - 1]
        self.size -= 1
        return value

    def resize(self) -> None:
        # Double the capacity
        self.capacity *= 2

        # Create new array
        new_arr = [0] * self.capacity

        # Copy old elements
        for i in range(self.size):
            new_arr[i] = self.arr[i]

        # Replace old array
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size
        
    def getCapacity(self) -> int:
        return self.capacity