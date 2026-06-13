# 07. 面向对象的核心特性：多态

多态（Polymorphism）一词源自希腊语，意为“多种形态”。在面向对象编程中，多态指的是不同的对象对同一个函数或方法调用可以表现出不同的行为结果。

## 1 多态的核心意义

多态的本质是**接口的统一与实现的分离**。它允许开发者编写更为通用、健壮的代码。只要对象满足特定的接口规范，系统就能自动根据对象的实际类型调用其对应的逻辑，而无需在主控代码中编写繁琐的 `if-else` 类型判断。

## 2 Python 中的鸭子类型 (Duck Typing)

与 Java、C++ 等静态强类型语言不同，Python 实现多态不强制要求对象之间存在严格的继承关系。Python 秉持“鸭子类型”的哲学：
> “如果它走起来像鸭子，叫起来像鸭子，那么它就是鸭子。”

这意味着，只要对象具有被调用的方法，Python 解释器就会将其视为合法的多态参与者。

```python
class Dog:
    def speak(self):
        return "汪汪！"

class Cat:
    def speak(self):
        return "喵喵！"

class Robot:
    # 机器人不继承任何动物类，但它同样实现了 speak 方法
    def speak(self):
        return "滴滴！系统正常。"

# 通用的多态接口函数
def animal_sound(entity):
    # 只要传入的 entity 对象拥有 speak() 方法即可调用，并不关心它的具体血统
    print(entity.speak())

entities = [Dog(), Cat(), Robot()]

# 相同的接口调用，展现出不同的形态
for e in entities:
    animal_sound(e)
```

## 3 接口与抽象基类 (ABC)

尽管鸭子类型赋予了 Python 极大的灵活性，但在大型工程项目中，过度自由往往会导致接口不明确。为了在 Python 中实现严格的契约精神，我们可以使用 `abc` (Abstract Base Classes) 模块来定义抽象基类。

### 3.1 抽象基类的作用
抽象基类本身不能被实例化，它的唯一使命是作为一套严格的接口规范，强制要求所有继承它的子类必须实现其标记的抽象方法。

```python
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    """支付网关的抽象基类：强制规范所有支付子类的行为"""
    
    @abstractmethod
    def pay(self, amount):
        pass

class WeChatPay(PaymentGateway):
    def pay(self, amount):
        print(f"调用微信支付接口，完成付款 {amount} 元")

class AliPay(PaymentGateway):
    # 如果开发者忘记实现 pay 方法，将在实例化时直接引发 TypeError
    def pay(self, amount):
        print(f"调用支付宝接口，完成付款 {amount} 元")

class ErrorPay(PaymentGateway):
    # 未实现抽象方法 pay
    pass

# 正常的多态表现
gateway1 = WeChatPay()
gateway1.pay(100)

# 强制校验失败的示例
# gateway2 = ErrorPay()  # 抛出 TypeError: Can't instantiate abstract class
```

通过抽象基类，Python 在保持其动态语言灵活性的同时，也具备了静态语言在大型架构设计上的安全感与规范性。
