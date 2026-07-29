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



## 4 私有成员全景解析

在 Python 中，通过双下划线 `__` 实现的私有化机制，不仅适用于实例，也适用于类本身。下面我们将私有成员分为四个维度进行详细拆解，并明确它们各自的访问权限。

### 4.1 实例私有属性 (Instance Private Attribute)

实例私有属性依附于具体的对象，用于存储对象不应对外公开的核心状态。通常在 `__init__` 方法中定义。

**代码示例：**
```python
class SecretBox:
    def __init__(self, content):
        self.__content = content  # 实例私有属性

    def open_box(self):
        # 内部访问实例私有属性
        return f"秘密内容是：{self.__content}"

box = SecretBox("机密文件")
print(box.open_box())      # 输出: 秘密内容是：机密文件
# print(box.__content)     # 报错: AttributeError
```

**访问权限详细划分：**

| 访问场景 (访问主体与途径) | 允许情况 | 底层机制与代码说明 |
| :--- | :--- | :--- |
| **当前类的实例方法** (通过 `self`) | ✅ 允许 | 处于同一类的作用域内，名称重整一致，可直接通过 `self.__content` 访问。 |
| **当前类的类方法 / 静态方法** | ⚠️ 条件允许 | 方法本身无 `self`。但若在内部获取到了该类的**具体实例对象**，则可以通过该实例访问（如 `obj.__content`），因为处于同类作用域。 |
| **类的外部代码** (通过实例访问) | ❌ 禁止 | 实例级的外部直接访问被重整机制拦截（实际引发 `AttributeError`）。 |
| **类的外部代码** (通过类名访问) | ❌ 禁止 | 该属性绑定在具体的实例内存中而非类的命名空间，类本身并不持有此数据。 |
| **子类的任意方法内部** | ❌ 禁止 | 子类的名称重整规则变更为 `_ChildClass__content`，无法匹配父类中已被重整为 `_SecretBox__content` 的真实属性名。 |

### 4.2 实例私有方法 (Instance Private Method)

实例私有方法同样依附于对象，通常用于执行内部的辅助计算或敏感逻辑，不希望被外部直接触发。

**代码示例：**
```python
class AlarmSystem:
    def trigger_alarm(self):
        print("检测到异常！")
        self.__call_police()  # 内部调用实例私有方法

    def __call_police(self):
        print("正在自动拨打报警电话...")

alarm = AlarmSystem()
alarm.trigger_alarm()  
# 依次输出: 
# 检测到异常！ 
# 正在自动拨打报警电话...

# alarm.__call_police()  # 报错: AttributeError
```

**访问权限详细划分：**

| 访问场景 (访问主体与途径) | 允许情况 | 底层机制与代码说明 |
| :--- | :--- | :--- |
| **当前类的实例方法** (通过 `self`) | ✅ 允许 | 处于同一类作用域，可直接通过 `self.__call_police()` 触发。 |
| **当前类的类方法 / 静态方法** | ⚠️ 条件允许 | 若方法内部持有了该类的**具体实例对象**，可通过该实例调用（如 `obj.__call_police()`）。 |
| **类的外部代码** (通过实例访问) | ❌ 禁止 | 外部对私有方法的直接调用被拦截。 |
| **类的外部代码** (通过类名访问) | ❌ 禁止 | 实例方法必须绑定具体的实例对象，无法直接通过类名去凭空调用。 |
| **子类的任意方法内部** | ❌ 禁止 | 受名称重整机制严格隔离，子类即使通过 `self` 也找不到父类的私有方法。 |

### 4.3 类私有属性 (Class Private Attribute)

类私有属性依附于类本身，被所有实例共享，但不允许外部直接读取或修改。必须直接定义在类体内部、方法之外。

**代码示例：**
```python
class ServerConfig:
    __max_connections = 100  # 类私有属性

    @classmethod
    def get_max_connections(cls):
        # 内部访问类私有属性
        return cls.__max_connections

print(ServerConfig.get_max_connections())  # 输出: 100

# print(ServerConfig.__max_connections)    # 报错: AttributeError
s1 = ServerConfig()
# print(s1.__max_connections)              # 报错: AttributeError
```

**访问权限详细划分：**

| 访问场景 (访问主体与途径) | 允许情况 | 底层机制与代码说明 |
| :--- | :--- | :--- |
| **当前类的类方法** (通过 `cls`) | ✅ 允许 | 最标准的设计范式，通过 `cls.__max_connections` 安全访问和修改全类共享状态。 |
| **当前类的实例方法** (通过 `self`) | ✅ 允许 | 实例在自身的字典中找不到该属性时，会通过 MRO 向上查找到类的命名空间，从而通过 `self.__max_connections` 成功读取。 |
| **类的外部代码** (通过类名访问) | ❌ 禁止 | 类级别的直接外部访问被名称重整机制拦截。 |
| **类的外部代码** (通过实例访问) | ❌ 禁止 | 虽然公有类属性可通过实例从外部读取，但私有的类属性依然对外严格屏蔽。 |
| **子类的任意方法内部** | ❌ 禁止 | 子类无论通过 `cls` 还是 `self`，其重整后的名称均与父类原始私有属性名不符。 |

### 4.4 类私有方法 (Class Private Method)

类私有方法与类私有属性类似，通常结合 `@classmethod` 装饰器使用，用于执行全类共享的内部敏感核心逻辑。

**代码示例：**
```python
class DatabaseManager:
    
    @classmethod
    def connect(cls):
        print("准备连接数据库...")
        cls.__verify_credentials()  # 内部调用类私有方法
        print("连接成功。")

    @classmethod
    def __verify_credentials(cls):
        print("验证底层全局配置的安全证书...")

DatabaseManager.connect()
# 依次输出: 
# 准备连接数据库... 
# 验证底层全局配置的安全证书... 
# 连接成功。

# DatabaseManager.__verify_credentials()  # 报错: AttributeError
```

**访问权限详细划分：**

| 访问场景 (访问主体与途径) | 允许情况 | 底层机制与代码说明 |
| :--- | :--- | :--- |
| **当前类的类方法** (通过 `cls`) | ✅ 允许 | 最标准的调用方式，通过 `cls.__verify_credentials()` 触发。 |
| **当前类的实例方法** (通过 `self`) | ✅ 允许 | 实例方法可通过 `self.__verify_credentials()` 解析到绑定在类上的私有方法并执行。 |
| **类的外部代码** (通过类名访问) | ❌ 禁止 | 外部通过类名的直接调用被拦截。 |
| **类的外部代码** (通过实例访问) | ❌ 禁止 | 外部通过实例对象的调用同样被拦截。 |
| **子类的任意方法内部** | ❌ 禁止 | 名称重整隔离，子类内部无法触发父类的类私有方法。 |

> **核心解析：为什么子类无法访问父类的私有成员？**
> 
> 这是因为 Python 在处理双下划线 `__` 变量时，其名称重整（Name Mangling）机制是硬编码与**当前定义该成员的类名**绑定的。父类的 `__attr` 在底层会被重命名为 `_Father__attr`，而子类内部若尝试访问 `__attr`，Python 解释器会去寻找 `_Child__attr`，由于名称不一致，这就实现了物理层面上的严格隔离与封装。
