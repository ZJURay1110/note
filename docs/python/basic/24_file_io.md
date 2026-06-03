# 文件的读写

*Python 中基于流式处理的本地文件交互机制*

---

## 1 文件操作基础 (File I/O Basics)

在 Python 中，文件操作的核心是内置函数 `open()`，它会在内存和外部存储介质之间建立一个数据流通道（File Object）。  

!!! info "上下文管理器 (Context Manager)"
    在进行任何文件读写操作时，**强烈建议**使用 `with` 语句。它可以保证即使在处理数据流时发生异常（如磁盘空间不足或编码错误），文件句柄也会在退出代码块时被自动且安全地关闭，避免内存泄漏或文件被系统持续锁定。

### 1.1 `open()` 核心函数与完整参数

```python
open(file, mode='r', buffering=-1, encoding=None, errors=None,\
newline=None, closefd=True, opener=None)

```

| 参数 | 说明 | 默认值 | 常用场景 |
| --- | --- | --- | --- |
| **`file`** | 文件路径（字符串或类路径对象 `Path`） | - | `D:\data\points.csv` |
| **`mode`** | 读写模式（见 1.2 节） | `'r'` | `'w'`, `'rb'`, `'a'` |
| **`buffering`** | 缓冲策略（0关闭，1行缓冲，>1指定字节） | `-1` (系统默认) | 处理极大数据流时优化 I/O 性能 |
| **`encoding`** | 字符编码（仅文本模式有效） | 依赖系统平台 | `'utf-8'` (强烈推荐显式指定以防乱码) |
| **`errors`** | 编解码报错处理策略 | `'strict'` | 遇到非标准字符时使用 `'ignore'` 或 `'replace'` |
| **`newline`** | 换行符控制 | `None` | 跨平台处理 `\r\n` (Windows) 与 `\n` |

### 1.2 核心模式 (Modes) 矩阵

| 模式字符 | 操作类型 | 指针初始位置 | 文件不存在时 | 文件已存在时 |
| --- | --- | --- | --- | --- |
| **`'r'`** | **读 (Read)** | 文件开头 | **报错 `FileNotFoundError**` | 正常打开 |
| **`'w'`** | **写 (Write)** | 文件开头 | 创建新文件 | **清空原文件内容 (覆盖)** |
| **`'x'`** | **创 (Create)** | 文件开头 | 创建新文件 | **报错 `FileExistsError**` |
| **`'a'`** | **增 (Append)** | 文件末尾 | 创建新文件 | 在末尾追加数据 |

*(附加修饰符：`'b'` 表示二进制流模式，`'t'` 表示文本模式（默认），`'+'` 表示开启读写双向更新。)*



## 2 读操作 (Read)

文件打开后，Python 提供了不同粒度的读取方法，用于将外部数据载入内存。

| 方法 | 说明 | 返回值 | 适用场景与复杂度 |
| --- | --- | --- | --- |
| **`.read(size=-1)`** | 读取整个文件，若指定 $size$ 则读取对应字节/字符数 | 字符串 / 字节串 | 小文件全量加载。$O(n)$ |
| **`.readline(size=-1)`** | 读取单行（遇到换行符或 EOF 停止） | 字符串 / 字节串 | 逐行逻辑判断，内存友好 |
| **`.readlines(hint=-1)`** | 读取所有行并返回列表。$hint$ 控制读取的近似字节数 | 列表 (List) | 需要对所有行进行切片或索引操作 |

!!! warning "大文件内存陷阱 (Memory Trap)"
    当处理海量数据（如几十 GB 的空间坐标记录或遥感日志）时，**绝对不要**使用 `.read()` 或 `.readlines()`，这会立刻导致内存溢出 (OOM)。

**最佳实践**是直接迭代文件对象，这利用了底层生成器机制，在内存中始终只保留当前的一行数据：
`python with open("D:\\data\\large_dataset.csv", "r", encoding="utf-8") as f: for line in f: process(line) # 恒定内存占用 O(1) `



## 3 写操作 (Write)

写操作会将内存中的数据流式推送到物理硬盘上。

!!! warning
    注意：写操作只能写入字符串的数据类型

| 方法 | 说明 | 返回值 | 行为特性 |
| --- | --- | --- | --- |
| **`.write(s)`** | 将字符串 $s$（或字节串）写入文件流 | 成功写入的字符/字节数 | 不会自动添加换行符，需手动拼接 `\n` |
| **`.writelines(lines)`** | 接收一个可迭代对象（如列表），将其所有元素依次写入 | `None` | 同样**不会**自动为元素添加换行符 |
| **`.flush()`** | 强制将内存缓冲区中的数据立即同步到物理硬盘 | `None` | 避免程序意外崩溃导致缓冲区数据丢失 |

```python
lines = ["Latitude,Longitude\n", "30.27,120.15\n"]
with open("output.csv", "w", encoding="utf-8") as f:
    f.writelines(lines)
    # f.flush() # 退出 with 语句块时会自动触发 flush 并 close

```



## 4 创与增操作 (Create & Append)

### 4.1 安全创建 (Exclusive Creation: `'x'`)

使用 `'x'` 模式是创建文件的最安全方式。它被称为“独占创建”。在处理重要的实验数据或配置文件时，它可以严格防止代码意外覆盖已存在的同名文件。

```python
try:
    with open("D:\\workspace\\devgis\\new_config.json", "x", encoding="utf-8") as f:
        f.write('{"status": "initialized"}')
except FileExistsError:
    print("配置文件已存在，跳过初始化。")

```

### 4.2 尾部追加 (Append: `'a'`)

使用 `'a'` 模式打开文件时，系统的文件指针会直接锁定在文件末尾。所有的 `.write()` 操作都会在现有数据之后无缝拼接，而不会破坏原有数据。极度适合日志记录器（Logger）或长期运行脚本的状态输出。



## 5 删与路径操作 (Delete & Path Management)

Python 的内置 `open()` 并不包含删除功能。文件的删除属于**操作系统级别**的 API 调度，必须依赖标准库 `os` 或更具现代化的 `pathlib`。

| 库分类 | 方法/操作 | 说明 | 异常处理 |
| --- | --- | --- | --- |
| **`os`** | `os.remove(path)` | 删除指定路径的文件 | 若文件不存在抛出 `FileNotFoundError`；若是目录抛出 `IsADirectoryError` |
|  | `os.unlink(path)` | 与 `remove()` 逻辑完全等同（Unix 语义风格） | 同上 |
| **`pathlib`** | `Path(path).unlink(missing_ok=True)` | 面向对象的删除方式 | `missing_ok=True` (Python 3.8+) 可静默忽略文件不存在的错误，极为优雅 |
| **`shutil`** | `shutil.rmtree(path)` | **递归删除**整个目录树及其内部所有文件 | 破坏性极强，常用于彻底清理废弃的虚拟环境 |

!!! warning "删除操作的不可逆性 (Irreversibility)"
    通过 Python 脚本执行的 `os.remove()` 或 `pathlib.Path.unlink()` 删除的文件**不会**进入 Windows 的回收站，而是直接从文件分配表中抹除（底层释放簇空间）。

在执行自动化清理脚本（如为了腾出 C 盘或 D 盘空间而执行批量删除）时，务必先进行严谨的路径断言，或提供打印路径的空跑（Dry-run）模式进行测试。

```python
from pathlib import Path

target_file = Path("D:\\temp_data\\cache.tmp")

# 推荐的现代 Python 文件删除写法
target_file.unlink(missing_ok=True) 

```

## 6 查找与定位操作 (Lookup & Positioning)

在处理文件流时，“查找”与字典中 $O(1)$ 的哈希索引完全不同。文件本质上是一串连续的字节序列（Sequential Stream），因此针对文件的查找操作通常分为两个维度：**物理位置的游标移动**，以及**内容数据的线性扫描**。

### 6.1 文件指针控制 (File Pointer Manipulation)

当我们对文件进行读写时，Python 内部维护了一个“游标”（文件指针），记录当前操作所在的绝对字节位置。

| 方法 | 说明 | 返回值 |
| --- | --- | --- |
| **`.tell()`** | 获取当前文件指针所在的字节位置 | 整数 (当前字节偏移量) |
| **`.seek(offset, whence=0)`** | 移动文件指针到指定位置 | 整数 (移动后的绝对字节位置) |

#### 关于 `.seek()` 的 `whence` 参数

`whence` 决定了偏移量 `offset` 的参考基准点：

| `whence` 值 | 常量别名 (`os` 模块) | 参考基准点 | 适用模式 |
| --- | --- | --- | --- |
| **`0`** (默认) | `os.SEEK_SET` | 文件开头 | 文本模式 / 二进制模式 |
| **`1`** | `os.SEEK_CUR` | 当前指针位置 | **仅限二进制模式** (`'rb'`, `'wb'`) |
| **`2`** | `os.SEEK_END` | 文件末尾 | **仅限二进制模式** (`'rb'`, `'wb'`) |

!!! warning "文本模式的 `seek` 陷阱"
    在默认的文本模式 (`'r'`) 下，由于多字节字符编码（如 UTF-8 中一个汉字占 3 字节）的复杂性，除了 `f.seek(0, 2)`（跳到文件末尾）之外，**严禁**使用非 `0` 的 `whence` 参数，否则会抛出 `io.UnsupportedOperation` 异常，或者导致截断多字节字符引发解码崩溃。如果需要精准定位和切片，请务必使用二进制模式 (`'rb'`)。

```python
with open("data.bin", "rb") as f:
    f.seek(1024, 0)  # 直接跳转到第 1024 个字节
    print(f.tell())  # 输出: 1024

```

#### 对比表


| 写法 | 文本模式 | 二进制模式 |
|---|---|---|
| `f.seek(0)` | ✅ 回到开头 | ✅ |
| `f.seek(n, 0)` | ✅ 从头跳 n 字节 | ✅ |

| 写法 | 文本模式 | 二进制模式 |
|---|---|---|
| `seek(0, 1)` | ✅（原地不动） | ✅ |
| `seek(1, 1)` | ❌ | ✅ **往下跳 1 字节** |
| `seek(-1, 1)` | ❌ | ✅ **往回退 1 字节** |



| 写法 | 文本模式 | 二进制模式 |
|---|---|---|
| `f.seek(0, 2)` | ✅ **跳到末尾**（offset 必须为 0） | ✅ |
| `f.seek(2, 2)` | ❌ **会报错** | ✅ |


