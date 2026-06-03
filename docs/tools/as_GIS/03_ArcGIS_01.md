# ArcGIS 的家族产品

---


ArcGIS 不仅仅是一个软件，而是一个涵盖了桌面、服务器、云端、移动和开发的完整 **Web GIS 生态系统**。


## 1. 桌面 GIS (Desktop GIS)

最核心的工作环境，经历了从 32 位到 64 位架构的彻底转型。

| 阶段 | 代表产品 | 核心特征 | 现状建议 |
| :--- | :--- | :--- | :--- |
| **早期** | **ArcView 3.x** | 奠定了 Shapefile 格式标准，仅支持基础制图。 | 永远的历史遗迹。 |
| **经典** | **ArcMap** (ArcGIS Desktop) | 包含 ArcMap, ArcCatalog 等；32 位架构，功能极度成熟。 | 停留在维护阶段，不再更新功能。 |
| **现代** | **ArcGIS Pro** | 64 位、多线程；Ribbon 界面；2D/3D 一体化；深度集成 Python。 | 绝对主流，新项目必选。 |

!!! note
    **Pro 与 Map 的关系**：ArcGIS Pro 是 ArcMap 的继任者。 我们应以 Pro 为主要学习工具，它在处理大规模空间数据和深度学习（GeoAI）方面性能远超 ArcMap。


## 2. 企业级 GIS (Enterprise GIS)
用于在私有环境（服务器/私有云）中部署、管理和共享空间资源。

* **演进路径**：从单一的 **ArcGIS Server** 演进为 **ArcGIS Enterprise**。
* **核心架构 (四大件)**：
    1.  **ArcGIS Server**：将地图发布为 Web 服务（URL）。
    2.  **Portal for ArcGIS**：企业内部的“地图门户”，类似于私有版 ArcGIS Online。
    3.  **ArcGIS Data Store**：存储托管要素和空间大数据的数据库。
    4.  **ArcGIS Web Adaptor**：负责与现有 Web 服务器（如 IIS/Tomcat）整合及负载均衡。



## 3. 在线云 GIS (Cloud GIS)
无需部署服务器，直接在云端进行制图、分析与协作。

* **ArcGIS Online (AGOL)**：
    * **定位**：由 Esri 维护的公有云平台。
    * **能力**：支持地图托管、即插即用的 Web App 构建（如 Dashboard）、空间分析、全球数据共享。
    * **联动**：与 Pro 无缝互通，可一键将桌面端成果“发布到云端”。



## 4. 移动与外业 GIS (Field GIS)
解决“去野外怎么采集数据”以及“如何实时传回办公室”的问题。

* **ArcGIS Field Maps**：**核心整合应用**。取代了旧有的 Collector (采集)、Explorer (浏览) 和 Tracker (轨迹)。
* **Survey123 for ArcGIS**：基于表格逻辑的智能表单采集，适合社会调查、灾害统计。
* **QuickCapture**：快速采集，适合高速运动场景（如车巡、机巡）。


## 5. 开发平台 (Developer & SDKs)
对于开发者来说，这是将 GIS 能力集成到自定义系统中的钥匙。

* **ArcPy (Python)**：**important** 用于 ArcGIS Pro 内部的自动化脚本、批处理和地理处理模型建模。
* **ArcGIS Maps SDK for JavaScript**：构建高性能 Web GIS 网页应用的事实标准。
* **ArcGIS Runtime SDKs**：用于在 .NET, Java, Android, iOS 等原生环境下构建跨平台 GIS 应用。
* **无代码/低代码工具**：Experience Builder 和 Dashboards，适合快速搭建专业展示界面。


## 6. 扩展模块 (Extensions)
在通用 GIS 基础上，针对特定分析需求提供的专业扩展。

* **Spatial Analyst**：栅格数据分析、水文分析、地形建模。
* **3D Analyst**：点云处理 (LiDAR)、视域分析、真三维建模。
* **Network Analyst**：最短路径搜索、物流配送、服务区计算。
* **Geostatistical Analyst**：空间插值（克里金插值等）与统计预测。


---


### 💡 学习路径建议
1.  **基础工具**：掌握 **ArcGIS Pro**。
2.  **自动化**：深入 **ArcPy**（结合你的 Python 学习背景）。
3.  **分发与Web**：理解 **ArcGIS Online/Enterprise** 的发布逻辑，并尝试 **JavaScript API**。







