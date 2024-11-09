# arrays.py

class Array:
    def __init__(self, capacity, fill_value=None):
        self.items = [fill_value] * capacity

    def insert(self, index, value):
        if 0 <= index <= len(self.items):
            self.items = self.items[:index] + [value] + self.items[index:]
        else:
            print(f"Error: Index {index} out of bounds")

    def delete(self, index):
        if 0 <= index < len(self.items):
            self.items = self.items[:index] + self.items[index+1:]
        else:
            print(f"Error: Index {index} out of bounds")

    def increase_size(self, new_capacity):
        self.items += [None] * (new_capacity - len(self.items))

    def decrease_size(self, new_capacity):
        self.items = self.items[:new_capacity]

    def display(self):
        return str(self.items)

# Full Test for Array
if __name__ == "__main__":
    # Initialize array with capacity 5, filled with zeros
    arr = Array(5, 0)
    print("Initial Array:", arr.display())  

    # Insert elements
    arr.insert(2, 100)
    print("After Insert at index 2:", arr.display()) 

    # Delete element
    arr.delete(3)
    print("After Delete at index 3:", arr.display())  

    # Increase array size
    arr.increase_size(8)
    print("After Increase Size to 8:", arr.display())  

    # Decrease array size
    arr.decrease_size(4)
    print("After Decrease Size to 4:", arr.display())  

