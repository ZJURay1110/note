# 04. 魔术方法 (Magic Methods)

在 Python 的面向对象编程中，魔术方法（Magic Methods，也被称为 Dunder Methods，因其被双下划线 Double Underscore 包围而得名）是极为重要的一环。它们允许开发者自定义类的行为，使其能够与 Python 的内置函数（如 `len()`, `print()`）和运算符（如 `+`, `==`）无缝交互。

---

## 1 魔术方法的核心意义

Python 崇尚“鸭子类型” (Duck Typing) 和统一的接口协议。魔术方法就是这些协议的底层实现。  
如果你希望自定义的类能够像 Python 内置类型一样使用加法运算、支持 `len()` 函数或能够直接被迭代，你就需要在类中实现对应的魔术方法。当进行特定操作时，Python 解释器会自动在底层调用这些方法。

## 2 对象的生命周期：构造与初始化

对象的诞生经历了两个关键阶段，分别由 `__new__` 和 `__init__` 负责。

### 2.1 构造方法 `__new__`
- **调用时机**：在对象被创建时最先被调用，负责在内存中分配空间并返回对象的引用。
- **特点**：它是一个属于类级别的静态方法（尽管不需要加装饰器）。首个参数通常是 `cls`。
- **主要用途**：极少被重写，通常仅在实现单例模式或继承不可变内置类型（如 `tuple`, `str`）时使用。

### 2.2 初始化方法 `__init__`
- **调用时机**：在 `__new__` 返回实例对象后自动被调用。
- **特点**：首个参数是 `self`，它不返回任何值（隐式返回 `None`）。
- **主要用途**：为已创建的实例对象绑定初始属性。

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        # 如果尚未创建实例，则调用父类的 __new__ 分配内存
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value

# 测试单例模式
obj1 = Singleton(10)
obj2 = Singleton(20)

print(obj1 is obj2)      # 输出: True (两者指向同一内存地址)
print(obj1.value)        # 输出: 20 (后一次初始化覆盖了先前的属性)
```

## 3 字符串表示：`__str__` 与 `__repr__`

当我们尝试打印一个自定义对象时，默认输出的是包含内存地址的泛型字符串。通过重写以下两个方法，可以提供具备可读性的输出。

### 3.1 开发者视图 `__repr__`
- **作用**：返回对象的官方字符串表示，主要用于调试和日志记录。理想情况下，`eval(repr(obj)) == obj` 应当成立。
- **调用方式**：通过 `repr(obj)` 或交互式环境直接回车触发。

### 3.2 用户视图 `__str__`
- **作用**：返回对象的非正式、易读的字符串表示，面向最终用户。
- **调用方式**：通过 `str(obj)` 或 `print(obj)` 触发。如果在类中仅定义了 `__repr__` 而未定义 `__str__`，Python 在执行 `print()` 时会隐式调用 `__repr__` 作为后备替代方案。

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # 提供足够的信息以明确对象状态
        return f"Point(x={self.x}, y={self.y})"

    def __str__(self):
        # 提供简洁的终端呈现形式
        return f"({self.x}, {self.y})"

p = Point(3, 4)
print(p)         # 隐式调用 __str__，输出: (3, 4)
print(repr(p))   # 显式调用 __repr__，输出: Point(x=3, y=4)
```

## 4 运算符重载

通过实现相应的魔术方法，可以赋予自定义对象使用算术和比较运算符的能力。

### 4.1 算术运算符重载
例如，重写 `__add__` 使得两个对象可以使用 `+` 号相加。

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # 判断类型，确保安全相加
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("只能与 Vector 类型相加")

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 1)
print(v1 + v2)  # 底层等价于 v1.__add__(v2)，输出: Vector(6, 4)
```

### 4.2 比较运算符重载
常用的比较方法包括 `__eq__` (==), `__lt__` (<), `__gt__` (>)。

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __eq__(self, other):
        return self.score == other.score

    def __lt__(self, other):
        return self.score < other.score

s1 = Student("Alice", 90)
s2 = Student("Bob", 85)

print(s1 == s2)  # 底层执行 s1.__eq__(s2)，输出: False
print(s1 > s2)   # 因为实现了 __lt__，Python 可推断 > 的逻辑，输出: True
```

## 5 容器化接口：使对象具有序列特性

如果希望对象像列表或字典那样可以通过索引访问或支持计算长度，需实现容器魔术方法。

- `__len__(self)`: 返回容器长度，通过 `len(obj)` 触发。
- `__getitem__(self, key)`: 支持索引访问，通过 `obj[key]` 触发。
- `__setitem__(self, key, value)`: 支持索引赋值，通过 `obj[key] = value` 触发。

```python
class CustomList:
    def __init__(self):
        self._data = []

    def add(self, item):
        self._data.append(item)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

my_list = CustomList()
my_list.add("Apple")
my_list.add("Banana")

print(len(my_list))       # 输出: 2
print(my_list[1])         # 输出: Banana
```

## 6 可调用对象：`__call__`

实现了 `__call__` 方法的类的实例，可以像普通函数一样使用括号 `()` 直接被调用。它常被用于创建保持内部状态的高阶函数或设计模式中。

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

# 实例化并固化 factor 的状态
double = Multiplier(2)
triple = Multiplier(3)

print(double(5))  # 底层执行 double.__call__(5)，输出: 10
print(triple(5))  # 底层执行 triple.__call__(5)，输出: 15
```

## 7 常见魔术方法分类总结参考

| 方法分类 | 方法名 | 触发条件 / 操作符 | 核心作用说明 |
| :--- | :--- | :--- | :--- |
| **生命周期** | `__new__` | 实例化前 | 在内存中分配对象空间并返回实例引用 |
| | `__init__` | 实例化时 | 对分配好空间的对象进行属性绑定 |
| **字符串表现** | `__str__` | `str()`, `print()` | 面向用户的非正式、高可读性格式输出 |
| | `__repr__` | `repr()` | 面向开发者的正式、详细表达，通常用于调试 |
| **算术运算** | `__add__` | `+` | 实现加法行为 |
| | `__sub__` | `-` | 实现减法行为 |
| **比较运算** | `__eq__` | `==` | 实现等值判断机制 |
| | `__lt__` | `<` | 实现小于号判定，通常结合排序使用 |
| **容器访问** | `__len__` | `len()` | 响应内置长度查询函数 |
| | `__getitem__` | `obj[key]` | 使对象支持基于索引或键的数据访问机制 |
| **可调用行为** | `__call__` | `obj()` | 允许对象表现出如同函数一般的调用行为 |
