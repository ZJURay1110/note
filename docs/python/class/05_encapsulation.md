# 05. 面向对象的核心特性：封装

封装（Encapsulation）是面向对象编程的三大核心特性之一。它的核心思想是将对象的数据（属性）和操作数据的方法（行为）绑定在一起，并对外隐藏内部的实现细节。

## 1 封装的核心意义

在实际工程中，封装主要解决以下两个问题：
1. **数据安全**：防止外部代码随意篡改对象内部的核心状态，确保数据的合法性和一致性。
2. **降低耦合**：对外仅暴露必要的接口。当类的内部实现发生改变时，只要对外的接口保持不变，调用该类的外部代码就无需修改。

## 2 私有属性与私有方法

Python 并没有像 Java 或 C++ 那样严格的 `public`, `protected`, `private` 关键字限制。它主要通过命名约定来实现访问控制。

### 2.1 单下划线 `_`（受保护的约定）
以单下划线开头的属性或方法（如 `_balance`），在 Python 社区的约定俗成中表示“受保护的”。这是一种强烈的警告，告知外部使用者：这是类的内部实现细节，请不要在类的外部直接访问。但这仅仅是约定，Python 解释器层面并不会阻止你访问它。

### 2.2 双下划线 `__`（私有属性名称重整）
以双下划线开头的属性或方法（如 `__password`），Python 会触发名称重整（Name Mangling）机制。在底层，Python 会自动将其重命名为 `_类名__属性名`，从而在语法层面上使其难以在类外部被直接访问。

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # 公有属性
        self._currency = "CNY"      # 受保护属性（约定）
        self.__balance = balance    # 私有属性（名称重整）

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__record_transaction()

    def __record_transaction(self):
        # 私有方法，仅限类内部调用
        print("交易已记录至内部账本")

    def get_balance(self):
        # 通过公有方法安全地暴露私有数据
        return self.__balance

account = BankAccount("Alice", 1000)

print(account.owner)         # 正常访问
print(account._currency)     # 可以访问，但极其不推荐（破坏了约定）
# print(account.__balance)   # 抛出 AttributeError，无法直接访问
print(account.get_balance()) # 输出: 1000，推荐的访问方式
```

## 3 属性装饰器 `@property`

为了更优雅地解决私有属性的读写问题，Python 提供了 `@property` 装饰器。它可以将类的方法伪装成属性进行访问，从而在不改变对象对外使用方式的前提下，在内部无缝植入类型检查或逻辑校验。

### 3.1 Getter 与 Setter 的实现

通过 `@property` 定义读取逻辑，通过 `@属性名.setter` 定义写入逻辑。

```python
class User:
    def __init__(self, username, age):
        self.username = username
        self.__age = age  # 私有属性

    @property
    def age(self):
        """Getter: 伪装成属性读取"""
        return self.__age

    @age.setter
    def age(self, value):
        """Setter: 在赋值时进行严格的合法性校验"""
        if not isinstance(value, int):
            raise TypeError("年龄必须是整数")
        if value < 0 or value > 150:
            raise ValueError("年龄数值不合法")
        self.__age = value

user = User("Bob", 25)

# 像访问普通属性一样触发 @property 的 getter 方法
print(user.age)  # 输出: 25

# 像普通赋值一样触发 @age.setter 方法，内部自动进行合法性校验
user.age = 30    
print(user.age)  # 输出: 30

# user.age = -5  # 抛出 ValueError: 年龄数值不合法
```

这种机制完美兼顾了数据操作的安全性与代码的可读性，是 Pythonic 风格中实现封装的标准范式。
