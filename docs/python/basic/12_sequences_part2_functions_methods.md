# 序列操作、方法、函数大全
*无需 `import` 直接调用*

---

## 1 序列的操作
序列操作是基于 Python 序列协议（Sequence Protocol）的通用运算，适用于 `list`, `tuple`, `str`, `range`, `bytes` 等类型。

### 1.1 索引与切片
* **索引 (Indexing)**：通过 `s[i]` 访问元素。支持负数索引（`-1` 为末尾）。
* **切片 (Slicing)**：语法为 `s[start:stop:step]`。
    * **逻辑**：从 `start` 开始到 `stop` 前结束（左闭右开），间隔为 `step`。
    * **内存**：切片操作会生成原序列的**浅拷贝 (Shallow Copy)**。



### 1.2 序列运算

| 运算符 | 描述 | 复杂度 | 说明 |
| :--- | :--- | :--- | :--- |
| **`s + t`** | 拼接 | $O(len(s) + len(t))$ | 返回包含两个序列元素的新序列 |
| **`s * n`** | 重复 | $O(n \times len(s))$ | 将序列重复 $n$ 次并拼接 |


下面的运算`range`不可使用

| 运算符 | 描述 | 复杂度 | 说明 |
| :--- | :--- | :--- | :--- |
| **`in`** | 成员判定 | $O(n)$ | 检查元素是否存在于序列中 |
| **`not in`** | 非成员判定 | $O(n)$ | 检查元素是否不存在于序列中 |



## 2 序列的方法
这里列出以下几种方法：
1.  **增加 (2.1)**：涉及向可变序列末尾或指定位置添加新元素。
2.  **删除 (2.2)**：涉及移除特定元素、指定位置元素或清空整个序列。
3.  **替换 (2.3)**：涉及修改元素引用或字符串内容替换。
4.  **分类与排序 (2.4)**：涉及对序列成员进行原地排序或顺序反转。
5.  **其他 (2.5)**：涉及索引查找、元素计数以及创建对象浅拷贝。

### 2.1 增加 (Addition)
#### `.append(x)`：
* **适用于**：可变序列（如 `list`）
* **相应参数**：`x` (欲添加至末尾的单一对象)
* **用法演示**：
```python
nums = [1, 2]
nums.append(3)          # 添加基础类型: [1, 2, 3]
nums.append([4, 5])     # 将列表作为“单个对象”添加: [1, 2, 3, [4, 5]]
print(len(nums))        # 输出 4 (注意嵌套列表仅占 1 个位置)
```

#### `.extend(iterable)`：
* **适用于**：可变序列
* **相应参数**：`iterable` (可迭代对象，如列表、元组、字符串)
* **用法演示**：
```python
nums = [1, 2]
nums.extend([3, 4])     # 拆解列表并追加: [1, 2, 3, 4]
nums.extend("AB")       # 拆解字符串并追加: [1, 2, 3, 4, 'A', 'B']
# 对比: nums.append([5, 6]) 会导致嵌套，而 nums.extend([5, 6]) 会扁平化合并
```



#### `.insert(i, x)`：
* **适用于**：可变序列
* **相应参数**：`i` (索引位置), `x` (待插入对象)
* **用法演示**：
```python
data = ["A", "C"]
data.insert(1, "B")     # 在索引 1 处插入: ['A', 'B', 'C']
data.insert(0, "Start") # 在开头插入: ['Start', 'A', 'B', 'C']
data.insert(100, "End") # 索引超出长度时，默认插在末尾: ['Start', 'A', 'B', 'C', 'End']
```



### 2.2 删除 (Deletion)
#### `.remove(x)`：
* **适用于**：可变序列
* **相应参数**：`x` (待删除的元素值)
* **用法演示**：
```python
colors = ["red", "blue", "red", "green"]
colors.remove("red")    # 仅移除“第一个”匹配的元素: ['blue', 'red', 'green']
# colors.remove("black") # 若值不存在，会抛出 ValueError 错误
```

#### `.pop([i])`：
* **适用于**：可变序列
* **相应参数**：`i` (可选，索引位置，默认为 -1)
* **用法演示**：
```python
stack = [10, 20, 30, 40]
top = stack.pop()       # 默认移除并返回最后一个: 40, 列表变为 [10, 20, 30]
first = stack.pop(0)    # 移除并返回指定索引处元素: 10, 列表变为 [20, 30]
print(f"弹出值: {top}, {first}")
```

#### `.clear()`：
* **适用于**：可变序列
* **功能**：移除序列中的所有元素。
* **用法演示**：
```python
cache = [1, 2, 3, 4, 5]
cache.clear()           # 列表变为 [], 但 id(cache) 保持不变 (原地清空)
```



### 2.3 替换 (Replacement)
#### `.replace(old, new[, count])`：
* **适用于**：仅 `str` (字符串)
* **说明**：字符串不可变，该方法返回新字符串。
* **用法演示**：
```python
path = "C:/users/desktop/notes.txt"
# 1. 全部替换
new_path = path.replace("/", "\\")    # "C:\\users\\desktop\\notes.txt"
# 2. 限制替换次数
text = "one-two-three-four"
half = text.replace("-", " ", 2)      # "one two three-four" (仅前两个替换)
```

#### 索引赋值 (Index Assignment)：
* **适用于**：可变序列
* **说明**：通过索引直接修改引用的指向。
* **用法演示**：
```python
# 1. 单个替换
nums = [1, 0, 3]
nums[1] = 2               # [1, 2, 3]

# 2. 切片批量替换
nums[0:2] = [8, 9]        # [8, 9, 3]
nums[0:2] = [10, 11, 12]  # 甚至可以用不等长的序列替换切片: [10, 11, 12, 3]
```



### 2.4 分类与排序 (Sorting & Ordering)
#### `.sort(key=None, reverse=False)`：
* **适用于**：仅 `list`
* **功能**：原地排序。
* **用法演示**：
```python
# 1. 基础排序
vals = [3, 1, 4, 2]
vals.sort(reverse=True)   # 降序: [4, 3, 2, 1]

# 2. 键函数排序 (按字符串长度)
names = ["Python", "C", "Java"]
names.sort(key=len)       # ['C', 'Java', 'Python']
```

#### `.reverse()`：
* **适用于**：可变序列
* **功能**：将序列中的元素原地反转。
* **用法演示**：
```python
items = [1, "A", 2, "B"]
items.reverse()           # 原地反转: ['B', 2, 'A', 1]
# 注意: 这不是排序，仅仅是位置掉头
```



### 2.5 其他 (Other)
#### `.index(x[, start[, end]])`：
* **适用于**：所有序列
* **功能**：查找第一个匹配项的索引。
* **用法演示**：
```python
letters = ["a", "b", "c", "b", "d"]
pos1 = letters.index("b")          # 返回 1
pos2 = letters.index("b", 2)       # 从索引 2 开始找，返回 3
# pos3 = letters.index("z")        # 找不到会报 ValueError
```

#### `.count(x)`：
* **适用于**：所有序列
* **功能**：统计元素出现的频次。
* **用法演示**：
```python
dna = "ATCGATTG"
a_count = dna.count("A")           # 返回 2
tag_count = dna.count("TAG")       # 返回 0 (找不到返回 0 而不是报错)
```

#### `.copy()`：
* **适用于**：可变序列
* **功能**：返回浅拷贝副本。
* **用法演示**：
```python
original = [1, [2, 3]]
new_copy = original.copy() 

new_copy[0] = 99                   # 修改一级元素，不影响原件
new_copy[1].append(4)              # 修改嵌套可变对象，会影响原件 (浅拷贝特性)
print(original)                    # 输出 [1, [2, 3, 4]]
```




## 3 序列的函数
这里列出以下几种函数：
* **基础属性函数**：用于获取序列的元数据（如长度）。
* **统计运算函数**：用于对序列内容进行数值汇总或极值查找。
* **排序与转换函数**：用于生成排序副本或反向迭代器，不修改原序列。
* **迭代增强函数**：用于在循环或处理流程中提供索引绑定与多序列并行功能。
* **逻辑判定函数**：用于对序列成员的整体布尔状态进行评估。

### 3.1 基础属性 (Basic Meta-data)
#### `len(s)`：
* **用法演示**：
```python
print(len([1, 2, 3]))    # 列表长度: 3
print(len("Hello"))      # 字符串长度: 5
print(len(range(0, 10))) # range 长度: 10
```



### 3.2 统计运算 (Statistics)
#### `min(s)` / `max(s)`：
* **用法演示**：
```python
# 1. 数字比较
nums = [4, 1, 8, 2]
print(min(nums), max(nums)) # 1, 8

# 2. 字符串比较 (按 ASCII/Unicode)
chars = ["a", "Z", "b"]
print(min(chars))           # 'Z' (大写字母编码小于小写)

# 3. 指定 key 比较
words = ["apple", "go", "banana"]
print(max(words, key=len))  # 'banana' (长度最长)
```

#### `sum(iterable[, start])`：
* **用法演示**：
```python
nums = [1, 2, 3, 4]
print(sum(nums))            # 默认从 0 开始加: 10
print(sum(nums, 100))       # 从 100 开始加: 110
# print(sum(["a", "b"]))    # 报错: sum 只能用于数值累加
```



### 3.3 排序与转换 (Sorting & Transformation)
#### `sorted(iterable, key=None, reverse=False)`：
* **用法演示**：
```python
# 1. 对元组进行排序 (返回列表)
tup = (5, 1, 9)
new_list = sorted(tup)      # [1, 5, 9]

# 2. 对字典键排序
d = {'b': 1, 'a': 2}
print(sorted(d))            # ['a', 'b']
```

#### `reversed(seq)`：
* **用法演示**：
```python
s = "Python"
# reversed 返回的是迭代器，常用于循环
for char in reversed(s):
    print(char, end="")     # "nohtyP"
# 或者转为列表
print(list(reversed([1, 2, 3]))) # [3, 2, 1]
```


### 3.4 迭代增强 (Iteration Enhancement)
#### `enumerate(iterable, start=0)`：
* **用法演示**：
```python
fruits = ["apple", "banana", "cherry"]

# 默认从 0 开始
for i, name in enumerate(fruits):
    print(f"Index {i}: {name}")

# 自定义起始索引 (例如从 1 开始计数)
for i, name in enumerate(fruits, start=1):
    print(f"No.{i}: {name}")
```

#### `zip(*iterables)`：
* **用法演示**：
```python
names = ["Alice", "Bob"]
scores = [85, 92, 78] # scores 较长，zip 会以最短的为准

# 1. 组合成对
for name, score in zip(names, scores):
    print(f"{name}: {score}") # 仅打印 Alice 和 Bob

# 2. 解压 (Unzip)
pairs = [('A', 1), ('B', 2)]
letters, numbers = zip(*pairs) # letters=('A', 'B'), numbers=(1, 2)
```





### 3.5 逻辑判定 (Logical Evaluation)
#### `all(iterable)` / `any(iterable)`：
* **用法演示**：
```python
# 1. all: 全部为真才为真
print(all([True, 1, "text"]))  # True
print(all([True, 0, "text"]))  # False (0 是假)

# 2. any: 有一个为真就为真
print(any([False, 0, ""]))     # False (全部是假)
print(any([False, 0, "Hi"]))   # True ("Hi" 是真)

# 3. 空序列测试
print(all([]))                 # True (特殊逻辑: 空序列 all 为真)
print(any([]))                 # False
```