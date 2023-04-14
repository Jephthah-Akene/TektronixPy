# TektronixPy

TektronixPy is a lightweight, user-friendly Python library designed for controlling a variety of Tektronix oscilloscopes using the PyVISA library. The codebase is structured as a template, allowing future engineers to easily build upon and extend its functionality. Whether you're working with digital, mixed signal, or portable oscilloscopes, TektronixPy provides a solid foundation for your projects.

For questions or feature requests, please contact **Jephthah Akene** at 0xtachi@gmail.com. As an independent researcher, I built this project purely for the joy of creating something both enjoyable and practical. If you love to tinker and build innovative control systems, feel free to email me!

## Table of Contents
- [TektronixPy](#tektronixpy)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [How it works and how to build on it](#how-it-works-and-how-to-build-on-it)
    - [Overview](#overview)
    - [oscilloscope.py](#oscilloscopepy)
    - [tektronix.py](#tektronixpy-1)
    - [main.py](#mainpy)
    - [Further Improvements and Expansion](#further-improvements-and-expansion)
  - [Contributing](#contributing)
  - [License](#license)

## Features

- Generic Oscilloscope class for easy inheritance and extension
- Predefined classes for Digital, Mixed Signal, and Portable Tektronix oscilloscopes
- Simple connection and disconnection management
- Designed as a template for future development

## Installation

1. Install the required dependencies: `pip install pyvisa`
2. Clone the TektronixPy repository: `git clone https://github.com/yourusername/TektronixPy.git`
3. Navigate to the TektronixPy folder and install the package:`cd TektronixPy` `pip install` .

## Usage

```python
import pyvisa
from tektronix import TektronixDSO, TektronixMSO, TektronixPortable

def main():
    rm = pyvisa.ResourceManager()

    # Replace 'Your_VISA_Resource_Name' with the VISA resource name of your oscilloscope
    resource_name = 'Your_VISA_Resource_Name'

    # Choose the appropriate oscilloscope class for your device
    oscilloscope = TektronixDSO(rm, resource_name)

    oscilloscope.connect()
    print(oscilloscope.get_idn())
    oscilloscope.disconnect()

if __name__ == '__main__':
    main()
```

## How it works and how to build on it

### Overview

TektronixPy is a Python library designed to control a variety of Tektronix oscilloscopes using the PyVISA library. The project is organized into three main files: `oscilloscope.py`, `tektronix.py`, and `main.py`.

### oscilloscope.py

This file contains the generic `Oscilloscope` class, which provides basic functionality for connecting to and disconnecting from oscilloscope devices. The class also includes a `get_idn()` method to query the device's identification information.

```python
class Oscilloscope:
    def __init__(self, resource_manager, resource_name):
        self.resource_manager = resource_manager
        self.resource_name = resource_name
        self.instrument = None

    def connect(self):
        self.instrument = self.resource_manager.open_resource(self.resource_name)

    def disconnect(self):
        if self.instrument is not None:
            self.instrument.close()

    def get_idn(self):
        if self.instrument is not None:
            return self.instrument.query('*IDN?')
        return None
```

### tektronix.py

This file contains the Tektronix-specific oscilloscope classes that inherit from the generic Oscilloscope class. You can add specific methods for different types of Tektronix oscilloscopes in these classes, such as Digital Storage Oscilloscope (DSO), Mixed Signal Oscilloscope (MSO), and Portable Oscilloscope.
``` python
from oscilloscope import Oscilloscope

class TektronixDSO(Oscilloscope):
    # Add DSO-specific methods here

class TektronixMSO(Oscilloscope):
    # Add MSO-specific methods here

class TektronixPortable(Oscilloscope):
    # Add portable-specific methods here
```
### main.py
This file serves as the entry point for your application and contains the code for connecting to a specific Tektronix oscilloscope using the appropriate class from tektronix.py.

``` python
import pyvisa
from tektronix import TektronixDSO, TektronixMSO, TektronixPortable

def main():
    rm = pyvisa.ResourceManager()

    # Replace 'Your_VISA_Resource_Name' with the VISA resource name of your oscilloscope
    resource_name = 'Your_VISA_Resource_Name'

    # Choose the appropriate oscilloscope class for your device
    oscilloscope = TektronixDSO(rm, resource_name)

    oscilloscope.connect()
    print(oscilloscope.get_idn())
    oscilloscope.disconnect()

if __name__ == '__main__':
    main()

```

### Further Improvements and Expansion

Here are some additional suggestions to improve and expand your TektronixPy project:

1. Add more methods to the Tektronix-specific classes (e.g., TektronixDSO, TektronixMSO, and TektronixPortable) to provide oscilloscope-specific controls and measurements. For example:
``` python
class TektronixDSO(Oscilloscope):
    def set_timebase(self, scale):
        self.instrument.write(f"horizontal:scale {scale}")

    def set_vertical_scale(self, channel, scale):
        self.instrument.write(f"channel{channel}:scale {scale}")

    # Add more DSO-specific methods here
```

2. Add error handling and logging to improve code robustness and assist with troubleshooting.
3. Create examples or tutorials demonstrating the use of TektronixPy with various Tektronix oscilloscopes to help users get started quickly.
4. Implement unit tests and continuous integration to ensure code quality and compatibility with future changes.
5. Create comprehensive documentation for



## Contributing

Contributions welcome! If you'd like to improve TektronixPy or add support for additional Tektronix oscilloscope models, please follow these steps:
1. Fork the repository
2. Create a new branch for your changes
3. Implement your changes and test them
4. Submit a pull request with a clear description of your changes

## License

TektronixPy is released under the MIT License. See the LICENSE file for details.
