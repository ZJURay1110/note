# 06. 面向对象的核心特性：继承

继承（Inheritance）是面向对象编程中实现代码复用的核心机制。它允许我们基于已有的类（父类/基类）创建一个新的类（子类/派生类）。子类会自动继承父类的属性和方法，并可以进行扩展或修改。

## 1 继承的核心意义

继承主要描述了对象之间 **"是一个" (Is-A)** 的关系。例如，“狗”是一个“动物”，“汽车”是一个“交通工具”。
通过继承，可以将多个类中共有的属性和行为提取到父类中，消除冗余代码，建立清晰的层级结构。

## 2 单继承与方法重写 (Override)

在 Python 中，定义继承关系的语法非常简单：在子类名称后面的括号中指定父类即可。

### 2.1 基础继承与重写
子类不仅可以直接使用父类的方法，还可以通过定义同名方法来覆盖（Override）父类的默认行为。

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} 发出了未知的叫声。")

class Dog(Animal):
    # 重写父类的 speak 方法
    def speak(self):
        print(f"{self.name} 汪汪叫！")

class Cat(Animal):
    # 重写父类的 speak 方法
    def speak(self):
        print(f"{self.name} 喵喵叫！")

dog = Dog("旺财")
cat = Cat("小黑")

dog.speak()  # 输出: 旺财 汪汪叫！
cat.speak()  # 输出: 小黑 喵喵叫！
```

## 3 深入解析 `super()` 函数

在子类中重写方法时，如果并非要完全丢弃父类的逻辑，而是要在父类逻辑的基础上进行扩展，就必须调用父类的原生方法。此时需要使用 `super()` 函数。

### 3.1 扩展父类的初始化逻辑
`super()` 最常见的使用场景是在子类的 `__init__` 方法中调用父类的 `__init__`，以确保父类的属性得到正确的初始化。

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        # 显式调用父类的 __init__ 方法完成 name 和 salary 的初始化
        super().__init__(name, salary)
        # 子类专属的扩展属性
        self.department = department

m = Manager("张三", 15000, "研发部")
print(m.name, m.department)  # 输出: 张三 研发部
```

## 4 多继承与 MRO

Python 支持多继承，即一个子类可以同时拥有多个直接父类。这为代码组合提供了极大的灵活性，但也可能引入复杂的命名冲突问题。

### 4.1 方法解析顺序 (MRO)
为了解决多继承中的冲突问题（如著名的菱形继承问题），Python 内部采用了一种名为 C3 线性化算法的机制，为每个类计算出一个严格的方法解析顺序（Method Resolution Order，简称 MRO）。

当调用一个方法时，Python 解释器会严格按照 `__mro__` 属性元组中列出的类顺序进行查找，找到第一个匹配的方法即刻执行并停止搜索。

```python
class A:
    def process(self):
        print("执行 A 类的 process")

class B(A):
    def process(self):
        print("执行 B 类的 process")

class C(A):
    def process(self):
        print("执行 C 类的 process")

class D(B, C):
    pass

d = D()
d.process()  # 输出: 执行 B 类的 process

# 查看 D 类的严格解析顺序
print(D.__mro__)
# 输出顺序为: D -> B -> C -> A -> object
```

在工程实践中，尽管多继承非常强大，但为避免系统复杂度失控，推荐使用 **Mixin (混入)** 模式作为多继承的主要应用场景。
