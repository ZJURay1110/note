# 02. 类与对象的基础

在上一节的介绍中，我们已经对类和对象有了感性认识。本节将深入探讨类的基础语法，重点理解类的定义、对象的实例化，以及 `__init__` 和 `self` 的核心作用。

---

## 1 类的定义与实例化

在 Python 中，使用 `class` 关键字定义类。

### 1.1 定义类
按照 PEP 8 规范，类名采用大驼峰命名法 (CamelCase)，例如 `Student`。

```python
class Student:
    # 空类，pass 表示不执行任何操作
    pass
```

### 1.2 实例化 (Instantiation)
类是模板，对象是具体的实例。通过调用类名即可完成实例化过程。

```python
# 创建两个 Student 对象
stu1 = Student()
stu2 = Student()

print(stu1)  # 输出示例: <__main__.Student object at 0x000001>
```



## 2 深入理解：`__init__`、`self` 与 `cls`

在面向对象编程中，由于类（图纸）和对象（实体）的界限严格，Python 通过特定的参数传递机制来区分当前操作的层级。

### 2.1 构造与初始化：`__init__`
`__init__` 是实例的初始化方法。在进行实例化时（例如执行 `Student("小明", 20)`），Python 会自动调用此方法，用于为刚刚在内存中开辟出的新对象赋予初始属性。

### 2.2 实例级指针：`self`
类中定义的大部分常规方法（即实例方法），其首个参数必须是 `self`。

- **本质**：`self` 始终指向**当前正在被操作的实例化对象本身**。
- **作用**：当不同的对象调用同一个方法时，Python 会在底层将该对象隐式传递给 `self`，让方法知道当前要处理的是哪一个对象的私有数据。

### 2.3 类级别指针：`cls`
当方法不需要操作具体的对象数据，而是需要操作“类”这个整体时，首个参数会使用 `cls`（这通常与 `@classmethod` 装饰器搭配使用，这将在 `03_methods.md` 中深入讲解）。

- **本质**：`cls` 始终指向**类本身**（图纸），而非实例化出的对象（产品）。
- **作用**：通过 `cls`，你可以在不实例化对象的情况下，直接访问或安全地修改全类共享的类级别属性，或者调用类的其他结构。

### 2.4 `self` 与 `cls` 的核心区别对比

通过下表可以直观地建立 `self` 和 `cls` 之间的概念区隔：

| 维度 | `self` | `cls` |
| :--- | :--- | :--- |
| **指向目标** | 具体的**实例化对象**（造出来的车） | **类本身**（设计图纸） |
| **可访问级别** | 实例属性、类属性 | 仅限类属性 |
| **主要应用** | 修改某个具体对象的状态，互不干扰 | 修改全类共享配置，或用作动态构造新对象的入口 |
| **使用位置** | 实例方法的首个参数 | 类方法 (`@classmethod`) 的首个参数 |

**代码演示：**

```python
class Student:
    # 类属性：全类共享的数据
    school_name = "第一中学"

    def __init__(self, name, age):
        # 通过 self 将属性绑定到具体的实例对象上
        self.name = name  
        self.age = age

    def introduce(self):
        # 通过 self 访问属于具体对象的内部数据
        print(f"我是 {self.name}，来自 {self.school_name}。")

    @classmethod
    def change_school(cls, new_name):
        # 通过 cls 修改类属性，这会立刻影响到所有使用该类的对象
        cls.school_name = new_name

# 1. 实例级操作：Python 会自动把 s1 传递给 self
s1 = Student("小明", 20)
s1.introduce()  # 输出: 我是 小明，来自 第一中学。

# 2. 类级别操作：Python 会自动把 Student 类本身传递给 cls
Student.change_school("第二实验中学")
s1.introduce()  # 输出: 我是 小明，来自 第二实验中学。
```

!!! warning
    **命名约定不可逾越**：无论是 `self` 还是 `cls`，从底层语法的层面而言它们都只是普通的参数名称。你可以强行将其命名为 `this` 或 `c` 而解释器不会报错。但这将严重违反 PEP 8 代码规范，导致其他开发者无法阅读或维护你的代码。因此，**必须在工程中严格遵守 `self` 和 `cls` 的命名规范**。



## 3 属性的增删改查操作

类中的变量称为属性。根据作用域和依附对象的不同，属性分为实例属性和类属性。下面分别深入讲解它们的创建、增加、删除、查询和修改操作。

### 3.1 实例属性 (Instance Attribute)
实例属性依附于具体的对象，每个对象的实例属性相互独立。通常在 `__init__` 方法中进行初始化。

**操作示例：**

```python
class Dog:
    def __init__(self, name):
        # 1. 创 (创建/初始化属性)
        self.name = name

dog1 = Dog("旺财")

# 2. 查 (查询/读取属性)
print(dog1.name)  # 输出: 旺财

# 3. 改 (修改已有属性)
dog1.name = "大黄"
print(dog1.name)  # 输出: 大黄

# 4. 增 (在外部动态新增属性)
dog1.age = 3
print(dog1.age)   # 输出: 3

# 5. 删 (删除属性)
del dog1.age
# print(dog1.age)  # 将抛出 AttributeError，因为 age 属性已被删除
```

### 3.2 类属性 (Class Attribute)
类属性依附于类本身。所有该类的实例对象共享同一份数据。类属性直接定义在类体内部、方法之外。

**操作示例：**

```python
class Dog:
    # 1. 创 (定义类属性)
    species = "犬科动物"

    def __init__(self, name):
        self.name = name

# 2. 查 (推荐通过类名查询，也可通过对象查询)
print(Dog.species)      # 输出: 犬科动物
dog1 = Dog("小白")
print(dog1.species)     # 输出: 犬科动物

# 3. 改 (必须通过类名修改)
Dog.species = "哺乳纲犬科"
print(Dog.species)      # 输出: 哺乳纲犬科
print(dog1.species)     # 输出: 哺乳纲犬科

# 注意：如果试图通过实例对象修改同名属性，实际上是为该实例新增了一个实例属性，覆盖了对类属性的访问！
dog1.species = "外星犬"
print(dog1.species)     # 输出: 外星犬 (访问的是新增加的实例属性)
print(Dog.species)      # 输出: 哺乳纲犬科 (类属性未受影响)

# 4. 增 (动态新增类属性)
Dog.leg_count = 4
print(Dog.leg_count)    # 输出: 4
print(dog1.leg_count)   # 输出: 4

# 5. 删 (删除类属性)
del Dog.leg_count
# print(Dog.leg_count)  # 将抛出 AttributeError
```

> **使用原则：** 如果某个属性是所有对象共有的固定值或全局配置项，应定义为类属性，以保持逻辑清晰并节省内存空间。


!!! warning
    如果试图通过实例对象修改同名属性，实际上是为该实例新增了一个实例属性，覆盖了对类属性的访问！
    ```
    dog1.species = "外星犬"
    print(dog1.species)     # 输出: 外星犬 (访问的是新增加的实例属性)
    print(Dog.species)      # 输出: 哺乳纲犬科 (类属性未受影响)
    ```

