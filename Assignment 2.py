# Question 1
# Base class for vehicles
class Vehicle:
    def __init__(self, brand: str, model: str, year: int):
        """
        Initialize a Vehicle with basic attributes
        Args:
            brand (str): The manufacturer of the vehicle
            model (str): The model name of the vehicle
            year (int): The manufacturing year
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False

    def start_engine(self) -> str:
        """
        Base method to start the vehicle engine
        Returns:
            str: Description of the engine starting
        """
        self.is_running = True
        return f"{self.brand} {self.model}'s engine is starting..."

    def stop_engine(self) -> str:
        """
        Method to stop the vehicle engine
        Returns:
            str: Description of the engine stopping
        """
        self.is_running = False
        return f"{self.brand} {self.model}'s engine is stopping..."

    def get_description(self) -> str:
        """
        Base method to get vehicle description
        Returns:
            str: Basic description of the vehicle
        """
        return f"This is a {self.year} {self.brand} {self.model} vehicle"
# Car subclass inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand: str, model: str, year: int, num_doors: int):
        """
        Initialize a Car with additional door attribute
        Args:
            brand (str): The manufacturer of the car
            model (str): The model name of the car
            year (int): The manufacturing year
            num_doors (int): Number of doors in the car
        """
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def start_engine(self) -> str:
        """
        Override start_engine to provide car-specific behavior
        Returns:
            str: Car-specific engine start description
        """
        self.is_running = True
        return f"{self.brand} {self.model}'s V6 engine roars to life!"

    def get_description(self) -> str:
        """
        Override get_description to include car-specific details
        Returns:
            str: Detailed description of the car
        """
        return f"This is a {self.year} {self.brand} {self.model} car with {self.num_doors} doors"
# Bike subclass inheriting from Vehicle
class Bike(Vehicle):
    def __init__(self, brand: str, model: str, year: int, has_sidecar: bool):
        """
        Initialize a Bike with sidecar attribute
        Args:
            brand (str): The manufacturer of the bike
            model (str): The model name of the bike
            year (int): The manufacturing year
            has_sidecar (bool): Whether the bike has a sidecar
        """
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def start_engine(self) -> str:
        """
        Override start_engine to provide bike-specific behavior
        Returns:
            str: Bike-specific engine start description
        """
        self.is_running = True
        return f"{self.brand} {self.model}'s motorcycle engine revs up!"

    def get_description(self) -> str:
        """
        Override get_description to include bike-specific details
        Returns:
            str: Detailed description of the bike
        """
        sidecar_status = "with" if self.has_sidecar else "without"
        return f"This is a {self.year} {self.brand} {self.model} motorcycle {sidecar_status} a sidecar"
# Demonstration of the class hierarchy
def main():
    # Create instances of Car and Bike
    my_car = Car("Toyota", "Camry", 2023, 4)
    my_bike = Bike("Harley-Davidson", "Sportster", 2022, True)

    # Demonstrate method calls for Car
    print("Car Demonstration:")
    print(my_car.get_description())
    print(my_car.start_engine())
    print(my_car.stop_engine())
    print()

    # Demonstrate method calls for Bike
    print("Bike Demonstration:")
    print(my_bike.get_description())
    print(my_bike.start_engine())
    print(my_bike.stop_engine())
    print()

    # Demonstrate polymorphism
    vehicles = [my_car, my_bike]
    print("Polymorphic Behavior:")
    for vehicle in vehicles:
        print(f"{vehicle.__class__.__name__}: {vehicle.get_description()}")
        print(f"{vehicle.__class__.__name__}: {vehicle.start_engine()}")
        print()
if __name__ == "__main__":
    main()


#Question 2
from abc import ABC, abstractmethod
import math
from typing import List

# Abstract base class for shapes
class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        """
        Abstract method to calculate the area of a shape
        Returns:
            float: The area of the shape
        """
        pass

    def get_description(self) -> str:
        """
        Abstract method to get shape description
        Returns:
            str: Description of the shape
        """
        pass

# Circle class inheriting from Shape
class Circle(Shape):
    def __init__(self, radius: float):
        """
        Initialize a Circle with radius
        Args:
            radius (float): The radius of the circle
        """
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def calculate_area(self) -> float:
        """
        Calculate the area of the circle (πr²)
        Returns:
            float: Area of the circle
        """
        return math.pi * self.radius ** 2

    def get_description(self) -> str:
        """
        Get description of the circle
        Returns:
            str: Description including radius
        """
        return f"Circle with radius {self.radius:.2f}"

# Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        """
        Initialize a Rectangle with width and height
        Args:
            width (float): The width of the rectangle
            height (float): The height of the rectangle
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        """
        Calculate the area of the rectangle (width * height)
        Returns:
            float: Area of the rectangle
        """
        return self.width * self.height

    def get_description(self) -> str:
        """
        Get description of the rectangle
        Returns:
            str: Description including width and height
        """
        return f"Rectangle with width {self.width:.2f} and height {self.height:.2f}"

# Function to calculate total area of all shapes
def calculate_total_area(shapes: List[Shape]) -> float:
    """
    Calculate the total area of all shapes in the list using polymorphism
    Args:
        shapes (List[Shape]): List of shape objects
    Returns:
        float: Sum of areas of all shapes
    """
    total_area = 0.0
    for shape in shapes:
        total_area += shape.calculate_area()
    return total_area

# Demonstration of the shape hierarchy and total area calculation
def main():
    try:
        # Create a list of different shapes
        shapes = [
            Circle(5.0),           # Circle with radius 5
            Rectangle(4.0, 6.0),   # Rectangle with width 4, height 6
            Circle(2.5),           # Circle with radius 2.5
            Rectangle(3.0, 8.0)    # Rectangle with width 3, height 8
        ]

        # Print individual shape information and areas
        print("Individual Shape Details:")
        print("-" * 50)
        for shape in shapes:
            print(f"{shape.get_description()}")
            print(f"Area: {shape.calculate_area():.2f} square units")
            print()

        # Calculate and display total area
        total = calculate_total_area(shapes)
        print("-" * 50)
        print(f"Total Area of All Shapes: {total:.2f} square units")

        # Demonstrate error handling
        print("\nTesting Error Handling:")
        try:
            invalid_circle = Circle(-1)  # Should raise ValueError
        except ValueError as e:
            print(f"Error: {e}")

        try:
            invalid_rectangle = Rectangle(0, 5)  # Should raise ValueError
        except ValueError as e:
            print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()


#Question 3
from abc import ABC, abstractmethod
from typing import Optional


# Abstract base class for shapes
class Shape(ABC):
    def __init__(self, color: str = "Unknown", border_width: float = 1.0):
        """
        Initialize a Shape with common attributes
        Args:
            color (str): The color of the shape (default: "Unknown")
            border_width (float): The width of the shape's border (default: 1.0)
        Raises:
            ValueError: If border_width is negative
        """
        if border_width < 0:
            raise ValueError("Border width cannot be negative")
        self.color = color
        self.border_width = border_width

    @abstractmethod
    def calculate_area(self) -> float:
        """
        Abstract method to calculate the area of the shape
        Returns:
            float: The area of the shape (0.0 in base class as it's abstract)
        """
        # Base implementation does nothing but can be called by subclasses
        return 0.0

    def get_description(self) -> str:
        """
        Get description of the shape
        Returns:
            str: Description including color and border width
        """
        return f"Shape with color {self.color} and border width {self.border_width:.2f}"


# Derived Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, width: float, height: float, color: str = "Unknown", border_width: float = 1.0):
        """
        Initialize a Rectangle with width, height, and inherited attributes
        Args:
            width (float): The width of the rectangle
            height (float): The height of the rectangle
            color (str): The color of the rectangle (passed to base class)
            border_width (float): The border width (passed to base class)
        Raises:
            ValueError: If width or height is non-positive
        """
        # Call the parent class's __init__ using super()
        super().__init__(color, border_width)

        # Validate rectangle-specific attributes
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        """
        Calculate the area of the rectangle, utilizing the base class method
        Returns:
            float: Area of the rectangle (width * height)
        """
        # Call the parent class's calculate_area method
        # Note: In this case, it returns 0.0 but demonstrates the use of super()
        base_area = super().calculate_area()

        # Calculate rectangle-specific area
        rect_area = self.width * self.height

        # Return the rectangle's area (base_area is 0.0 but included for demonstration)
        return base_area + rect_area

    def get_description(self) -> str:
        """
        Get detailed description of the rectangle
        Returns:
            str: Description including width, height, color, and border width
        """
        return (f"Rectangle with width {self.width:.2f}, height {self.height:.2f}, "
                f"color {self.color}, and border width {self.border_width:.2f}")


# Demonstration of the Shape and Rectangle classes
def main():
    try:
        # Create instances of Rectangle with different parameters
        rect1 = Rectangle(5.0, 3.0, "Blue", 2.0)
        rect2 = Rectangle(4.0, 6.0, "Red")

        # Demonstrate the functionality
        print("Rectangle 1 Demonstration:")
        print(rect1.get_description())
        print(f"Area: {rect1.calculate_area():.2f} square units")
        print()

        print("Rectangle 2 Demonstration:")
        print(rect2.get_description())
        print(f"Area: {rect2.calculate_area():.2f} square units")
        print()

        # Demonstrate error handling
        print("Testing Error Handling:")
        try:
            invalid_rect = Rectangle(-1, 5, "Green")  # Should raise ValueError
        except ValueError as e:
            print(f"Error creating rectangle: {e}")

        try:
            invalid_rect = Rectangle(2, 3, "Yellow", -1)  # Should raise ValueError
        except ValueError as e:
            print(f"Error creating rectangle: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()



#Question 4

from abc import ABC, abstractmethod
from typing import List

# Abstract base class to ensure make_sound method is implemented
class Animal(ABC):
    def __init__(self, name: str, age: int):
        """
        Initialize an Animal with basic attributes
        Args:
            name (str): The name of the animal
            age (int): The age of the animal
        Raises:
            ValueError: If age is negative or name is empty
        """
        if not name.strip():
            raise ValueError("Name cannot be empty")
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self) -> str:
        """
        Abstract method to make animal-specific sound
        Returns:
            str: The sound made by the animal
        """
        pass

    def get_description(self) -> str:
        """
        Get description of the animal
        Returns:
            str: Description including name and age
        """
        return f"{self.__class__.__name__} named {self.name}, age {self.age}"

# Dog class inheriting from Animal
class Dog(Animal):
    def make_sound(self) -> str:
        """
        Implement make_sound for Dog
        Returns:
            str: Dog-specific sound
        """
        return f"{self.name} says: Woof! Woof!"

# Cat class inheriting from Animal
class Cat(Animal):
    def make_sound(self) -> str:
        """
        Implement make_sound for Cat
        Returns:
            str: Cat-specific sound
        """
        return f"{self.name} says: Meow!"

# Function to process sound of any animal
def process_sound(sound_object: Animal) -> str:
    """
    Process the sound of an animal object using polymorphism
    Args:
        sound_object (Animal): Object that implements make_sound method
    Returns:
        str: Formatted string describing the animal and its sound
    Raises:
        AttributeError: If the object doesn't have make_sound method
    """
    try:
        sound = sound_object.make_sound()
        return f"{sound_object.get_description()} makes sound: {sound}"
    except AttributeError:
        raise AttributeError("Object must have a make_sound method")

# Demonstration of polymorphic sound processing
def main():
    try:
        # Create instances of Dog and Cat
        animals: List[Animal] = [
            Dog("Rex", 5),
            Cat("Whiskers", 3),
            Dog("Buddy", 2),
            Cat("Luna", 4)
        ]

        # Process sounds for all animals
        print("Processing Animal Sounds:")
        print("-" * 50)
        for animal in animals:
            print(process_sound(animal))
        print()

        # Demonstrate error handling with invalid input
        print("Testing Error Handling:")
        class InvalidAnimal:
            pass

        try:
            invalid_animal = InvalidAnimal()
            process_sound(invalid_animal)  # Should raise AttributeError
        except AttributeError as e:
            print(f"Error: {e}")

        try:
            invalid_dog = Dog("", 3)  # Should raise ValueError (empty name)
        except ValueError as e:
            print(f"Error: {e}")

        try:
            invalid_cat = Cat("Misty", -1)  # Should raise ValueError (negative age)
        except ValueError as e:
            print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()



#Question 5
from abc import ABC, abstractmethod
import os
from typing import Any


# Abstract base class for file handlers
class FileHandler(ABC):
    def __init__(self, filename: str):
        """
        Initialize a FileHandler with a filename
        Args:
            filename (str): The name of the file to handle
        Raises:
            ValueError: If filename is empty
        """
        if not filename.strip():
            raise ValueError("Filename cannot be empty")
        self.filename = filename

    @abstractmethod
    def read(self) -> Any:
        """
        Abstract method to read content from the file
        Returns:
            Any: The content read from the file
        """
        pass

    @abstractmethod
    def write(self, content: Any) -> None:
        """
        Abstract method to write content to the file
        Args:
            content (Any): The content to write to the file
        """
        pass

    def get_file_info(self) -> str:
        """
        Get information about the file
        Returns:
            str: Description of the file and its handler
        """
        return f"{self.__class__.__name__} handling file: {self.filename}"


# Concrete class for handling text files
class TextFileHandler(FileHandler):
    def read(self) -> str:
        """
        Read content from a text file
        Returns:
            str: The content of the text file
        Raises:
            FileNotFoundError: If the file does not exist
            IOError: If there's an error reading the file
        """
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Text file {self.filename} not found")
        except IOError as e:
            raise IOError(f"Error reading text file {self.filename}: {str(e)}")

    def write(self, content: str) -> None:
        """
        Write content to a text file
        Args:
            content (str): The text content to write
        Raises:
            TypeError: If content is not a string
            IOError: If there's an error writing to the file
        """
        if not isinstance(content, str):
            raise TypeError("Content must be a string for TextFileHandler")
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                file.write(content)
        except IOError as e:
            raise IOError(f"Error writing to text file {self.filename}: {str(e)}")


# Concrete class for handling binary files
class BinaryFileHandler(FileHandler):
    def read(self) -> bytes:
        """
        Read content from a binary file
        Returns:
            bytes: The content of the binary file
        Raises:
            FileNotFoundError: If the file does not exist
            IOError: If there's an error reading the file
        """
        try:
            with open(self.filename, 'rb') as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Binary file {self.filename} not found")
        except IOError as e:
            raise IOError(f"Error reading binary file {self.filename}: {str(e)}")

    def write(self, content: bytes) -> None:
        """
        Write content to a binary file
        Args:
            content (bytes): The binary content to write
        Raises:
            TypeError: If content is not bytes
            IOError: If there's an error writing to the file
        """
        if not isinstance(content, bytes):
            raise TypeError("Content must be bytes for BinaryFileHandler")
        try:
            with open(self.filename, 'wb') as file:
                file.write(content)
        except IOError as e:
            raise IOError(f"Error writing to binary file {self.filename}: {str(e)}")


# Demonstration of the file handler system
def main():
    try:
        # Create temporary files for demonstration
        text_file = "example.txt"
        binary_file = "example.bin"

        # Create instances of file handlers
        text_handler = TextFileHandler(text_file)
        binary_handler = BinaryFileHandler(binary_file)

        # Demonstrate text file handling
        print("Text File Handler Demonstration:")
        print(text_handler.get_file_info())

        # Write to text file
        text_content = "Hello, this is a text file!"
        text_handler.write(text_content)
        print(f"Written to text file: {text_content}")

        # Read from text file
        text_read = text_handler.read()
        print(f"Read from text file: {text_read}")
        print()

        # Demonstrate binary file handling
        print("Binary File Handler Demonstration:")
        print(binary_handler.get_file_info())

        # Write to binary file
        binary_content = b"Binary data \x00\x01\x02"
        binary_handler.write(binary_content)
        print(f"Written to binary file: {binary_content}")

        # Read from binary file
        binary_read = binary_handler.read()
        print(f"Read from binary file: {binary_read}")
        print()

        # Demonstrate error handling
        print("Testing Error Handling:")

        # Try to create handler with empty filename
        try:
            invalid_handler = TextFileHandler("")
        except ValueError as e:
            print(f"Error: {e}")

        # Try to write wrong content type
        try:
            text_handler.write(123)  # Should raise TypeError
        except TypeError as e:
            print(f"Error: {e}")

        try:
            binary_handler.write("Not bytes")  # Should raise TypeError
        except TypeError as e:
            print(f"Error: {e}")

        # Try to read non-existent file
        try:
            invalid_text_handler = TextFileHandler("nonexistent.txt")
            invalid_text_handler.read()
        except FileNotFoundError as e:
            print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Clean up temporary files
        for file in [text_file, binary_file]:
            if os.path.exists(file):
                os.remove(file)
                print(f"Cleaned up file: {file}")


if __name__ == "__main__":
    main()