# 03. 类的方法

上一节我们学习了属性（变量），本节重点讲解类中的方法（函数）。
在 Python 中，类的方法主要分为三种：实例方法、类方法和静态方法。它们在底层机制和应用场景上具有显著区别。

---

## 1 实例方法 (Instance Methods)

实例方法是最常规且使用最广泛的方法形式，通常用于处理或修改对象本身的状态。

### 1.1 基本定义与调用
- **特点**：首个参数必须是 `self`，代表当前的实例对象。
- **作用**：用于访问、操作和修改实例属性，或执行高度依赖于实例状态的业务逻辑。
- **调用方式**：通过 `对象.方法名()` 进行调用。

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"存款成功，当前余额: {self.balance}")
        else:
            print("存款金额必须大于零")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"取款成功，当前余额: {self.balance}")
        else:
            print("余额不足或取款金额无效")

account = BankAccount("张三", 100)
account.deposit(50)   # 修改实例内部状态
account.withdraw(30)  # 修改实例内部状态
```

### 1.2 实例方法的底层执行机制
当通过 `account.deposit(50)` 这种方式调用方法时，Python 解释器在底层实际上执行的是 `BankAccount.deposit(account, 50)`。这解释了为何实例方法的定义中必须显式包含 `self` 参数：Python 会自动将发起调用的实例对象作为第一个参数传入函数内部。


## 2 类方法 (Class Methods)

类方法与特定的实例对象解耦，主要用于操作类级别的数据，或者提供与类结构本身高度相关的行为。

### 2.1 基本定义与操作类属性
- **特点**：必须通过 `@classmethod` 装饰器声明。首个参数通常命名为 `cls`，代表当前类本身（并非类的某个实例）。
- **作用**：主要用于读取或修改类属性。对其做出的修改将全局影响到所有属于该类的对象。
- **调用方式**：通过 `类名.方法名()` 进行调用。

```python
class Employee:
    # 类属性
    raise_amount = 1.05
    num_of_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.num_of_employees += 1

    @classmethod
    def set_raise_amount(cls, amount):
        # 通过 cls 修改类属性，影响所有后续的薪水计算
        cls.raise_amount = amount

Employee.set_raise_amount(1.10)
print(Employee.raise_amount)  # 输出: 1.1
```

### 2.2 高级应用：备选构造函数 (Alternative Constructors)
类方法最强大的应用场景之一是充当“备选构造函数”。当类默认的初始化逻辑（`__init__`）无法满足某些特殊数据源，或者输入数据格式较为复杂时，可以通过类方法提供额外的、定制化的实例化途径。

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, emp_str):
        # 负责解析特定的字符串数据格式
        name, salary = emp_str.split('-')
        # 此处的 cls() 等价于 Employee()，并返回一个全新的实例化对象
        return cls(name, float(salary))

# 使用备选构造函数直接从字符串快速创建对象
emp_str_1 = "李四-8000"
new_emp = Employee.from_string(emp_str_1)
print(new_emp.name, new_emp.salary)  # 输出: 李四 8000.0
```

---

## 3 静态方法 (Static Methods)

静态方法在业务逻辑上属于该类，但在技术实现和内存访问级别上，它等同于普通的独立函数。

### 3.1 基本定义与调用
- **特点**：必须通过 `@staticmethod` 装饰器声明。无需强制指定任何特定首个参数（既不需要 `self` 也不需要 `cls`）。
- **作用**：作为独立的工具/辅助函数存在，将其放入类中仅仅是为了借用类的命名空间进行代码组织，从而提升代码的内聚性。静态方法无法访问实例属性和类属性。
- **调用方式**：通过 `类名.方法名()` 调用。

```python
import datetime

class MathUtils:
    
    @staticmethod
    def is_workday(day):
        # 仅执行简单的逻辑判断，它不需要该类的任何状态数据
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

my_date = datetime.date(2023, 10, 15)
print(MathUtils.is_workday(my_date))  # 输出: False
```

---

## 4 总结与对比

通过下表可以严谨且直观地区分这三种方法的特性与限制边界：

| 方法类型 | 装饰器声明 | 必需的首参数 | 访问实例属性 | 访问类属性 | 核心应用场景 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **实例方法** | 无 | `self` | 是 | 是 | 操作具体对象的内部数据和维护对象状态 |
| **类方法** | `@classmethod` | `cls` | 否 | 是 | 修改类级别全局状态；作为备选构造器返回新实例 |
| **静态方法** | `@staticmethod` | 无 | 否 | 否 | 放置与该类业务逻辑相关的独立纯工具函数或辅助计算机制 |




| 属性/方法类型 | 能否被**实例**访问 / 调用 | 能否被**类**访问 / 调用 |
| --- | --- | --- |
| **实例属性** | **可以** (数据绑定在具体对象自身) | **不可以** (类只是模板，不包含具体对象的数据) |
| **类属性** | **可以** (实例会自动向上读取类的共享数据) | **可以** (数据直接存储在类的命名空间中) |
| **实例方法** | **可以** (自动将当前实例作为 `self` 传入) | **可以（需手动传参）** (类不会自动传 `self`，必须显式塞个实例进去) |
| **类方法** | **可以** (自动追踪实例所属的类，并作为 `cls` 传入) | **可以** (自动将类本身作为 `cls` 传入) |
| **静态方法** | **可以** (仅作普通函数执行，不牵扯任何对象/类参数绑定) | **可以** (仅作普通函数执行，不牵扯任何对象/类参数绑定) |




**方法选择的标准原则：**
1. 业务逻辑若需读取或修改具体的对象内部状态 (`self.xxx`)，**必须**使用实例方法。
2. 业务逻辑若无需对象状态，但必须操作类的公共状态，或需要动态生成新的该类实例，**必须**使用类方法。
3. 业务逻辑若既不涉及对象状态，也不涉及类状态，仅为纯粹的输入输出处理或辅助判断，**应当**使用静态方法，以提升代码的模块化和解耦程度。
