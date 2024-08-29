# Redis Basic Operations with Python Ì∑ë‚ÄçÌ≤ª

## Project Overview

This project demonstrates how to leverage Redis for basic operations and as a simple cache using Python. The project is divided into several tasks, each focusing on different functionalities of Redis, including storing and retrieving data, counting method calls, logging method history, and more.

## Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run this project, you'll need to have Redis and Python 3.7 installed on your Ubuntu 18.04 LTS system.

1. **Install Redis**:
    ```bash
    $ sudo apt-get -y install redis-server
    ```

2. **Install Python Dependencies**:
    ```bash
    $ pip3 install redis
    ```

3. **Configure Redis**:
    Update your Redis configuration to bind only to `127.0.0.1`:
    ```bash
    $ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
    ```

## Project Structure

```plaintext
0x02-redis_basic/
‚îÇ
‚îú‚îÄ‚îÄ exercise.py   # Core implementation of the Cache class and decorators
‚îú‚îÄ‚îÄ main.py       # Entry-point for testing the Cache class (not provided, create your own)
‚îî‚îÄ‚îÄ web.py        # Implementation of the web caching mechanism (separate task)
```

## Usage

### 1. **Basic Cache Operations**

You can use the `Cache` class to store and retrieve data from Redis. Below is an example:

```python
from exercise import Cache

cache = Cache()

# Store data
key = cache.store("Hello, Redis!")
print(f"Stored key: {key}")

# Retrieve data
value = cache.get_str(key)
print(f"Retrieved value: {value}")
```

### 2. **Counting Method Calls**

The `store` method in the `Cache` class tracks the number of times it has been called using a decorator.

```python
cache.store("Data 1")
cache.store("Data 2")

# Check the number of times store was called
calls = cache.get_int("Cache.store")
print(f"Store method was called {calls} times.")
```

### 3. **Logging Method History**

You can also log the input and output history of the `store` method:

```python
from exercise import replay

cache.store("Data 1")
cache.store("Data 2")

# Replay the history
replay(cache.store)
```

## Features

- **Basic Redis Operations**: Store and retrieve data using a randomly generated key.
- **Data Type Preservation**: Automatically convert data back to its original type after retrieval.
- **Method Call Counting**: Count the number of times a method is called.
- **Call History Logging**: Log the history of inputs and outputs for any method.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any feature additions or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
