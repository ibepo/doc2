# 中国技术交易所 - 完整API接口文档

> 文档版本: v1.0
> 生成日期: 2026-01-08
> 基准Token: `chinatsi123` ⚠️ **硬编码安全漏洞**

---

## 目录

- [认证机制](#认证机制)
- [API概览](#api概览)
- [策略评估类API](#策略评估类api)
- [历史数据类API](#历史数据类api)
- [价格预测类API](#价格预测类api)
- [图表服务API](#图表服务api)
- [数据字典](#数据字典)
- [错误码说明](#错误码说明)

---

## 认证机制

### Token认证

所有API使用查询参数方式进行Token认证：

```http
GET /api/endpoint?token=chinatsi123
POST /api/endpoint?token=chinatsi123
```

**⚠️ 安全警告**: 当前使用硬编码Token `chinatsi123`，这是一个严重的安全漏洞！

---

## API概览

### 已确认可访问的API

| # | API端点 | 方法 | 数据敏感性 | 状态 |
|---|---------|------|------------|------|
| 1 | `/newjcyj/api/simInterception/checkToken` | GET | 低 | ✅ |
| 2 | `/newjcyj/api/index/jctlIndexDatasAssess` | POST | 🔴 极高 | ✅ |
| 3 | `/newjcyj/api/index/jctlIndexDatas/ts` | POST | 🔴 极高 | ✅ |
| 4 | `/newjycl/api/index/jctlIndexDatas/v3` | POST | 中 | ✅ |
| 5 | `/monthPriceForecast/index` | GET | 高 | ✅ |

### 需要额外认证的API

| # | API端点 | 状态 |
|---|---------|------|
| 6 | `/api_v3/v4/celuejianyi/aiengine` | ⚠️ 需要额外参数 |
| 7 | `/api_v3/iron/hcsj/type/8/mean` | ⚠️ 返回空数据 |
| 8 | `/api_v3/iron/hcsj/type/glv` | ⚠️ 参数错误 |
| 9 | `/api_v3/iron/hcsj/fq/dheizi/aiengine` | ⚠️ 参数错误 |

---

## 策略评估类API

### API-1: Token验证接口

**端点**: `GET /newjcyj/api/simInterception/checkToken`

**完整URL**:
```
http://118.126.142.187:8089/ts-datamanager/newjcyj/api/simInterception/checkToken
```

**请求参数**:

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| token | string | 是 | 认证Token |

**请求示例**:
```bash
curl "http://118.126.142.187:8089/ts-datamanager/newjcyj/api/simInterception/checkToken?token=chinatsi123"
```

**返回示例**:
```json
{
  "code": "0",
  "message": "token is ok",
  "data": null,
  "totalCount": 0
}
```

**字段说明**:

| 字段 | 类型 | 说明 |
|------|------|------|
| code | string | "0"=成功, 其他=失败 |
| message | string | 响应消息 |
| data | object/null | 响应数据 |
| totalCount | number | 数据总数 |

**功能说明**:
> 验证Token是否有效。这是一个认证检查接口，用于确认Token的有效性。

---

### API-2: 价差策略评估接口 ⭐核心

**端点**: `POST /newjycl/api/index/jctlIndexDatasAssess`

**完整URL**:
```
http://118.126.142.187:8089/ts-datamanager/newjcyj/api/index/jctlIndexDatasAssess
```

**请求参数**:

#### Query参数
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| token | string | 是 | 认证Token |

#### Body参数 (JSON)
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| isDisplay | string | 是 | 显示标识 (通常为"T") |
| type | string | 是 | 产品类型 (螺纹钢/热卷/铁矿石/焦炭/焦煤) |

**请求示例**:
```bash
curl -X POST "http://118.126.142.187:8089/ts-datamanager/newjcyj/api/index/jctlIndexDatasAssess?token=chinatsi123" \
  -H "Content-Type: application/json" \
  -d '{"isDisplay":"T","type":"螺纹钢"}'
```

**返回示例**:
```json
{
  "code": "0",
  "message": "获取成功",
  "data": [
    {
      "name": "上海-北京螺纹钢",
      "cl": 0,
      "ccl": [0, 0, 0],
      "enterDate": "2026-01-07",
      "enterData": 140.0,
      "curData": 120.0,
      "diffValue": -20.0,
      "menuPath": "./index_kpz.html?dataId=xxx&dataName=xxx..."
    }
  ],
  "totalCount": 14
}
```

**返回字段说明**:

| 字段 | 类型 | 说明 |
|------|------|------|
| name | string | 策略名称 (如"上海-北京螺纹钢") |
| cl | int | 策略方向: -1=做空, 0=观望, 1=做多 |
| ccl | array[int] | 三星推荐指数: [-1,-1,-1]=三星做空, [1,1,1]=三星做多 |
| enterDate | string | 入场日期 (YYYY-MM-DD) |
| enterData | float | 入场价差 |
| curData | float | 当前价差 |
| diffValue | float | 差值变化 (curData - enterData) |
| menuPath | string | 详情页面路径 |

**策略类型分类**:

#### 1. 跨区域价差策略
不同地区之间的现货价差套利。

**螺纹钢跨区域策略**:
- 上海-北京螺纹钢
- 北京-沈阳螺纹钢
- 唐山-上海螺纹钢
- 太原-上海螺纹钢
- 广州-沈阳螺纹钢
- 成都-上海螺纹钢
- 成都-西安螺纹钢
- 杭州-上海螺纹钢
- 杭州-沈阳螺纹钢

**热卷跨区域策略**:
- 上海-天津热卷
- 上海-沈阳热卷
- 乐从-天津热卷
- 乐从-沈阳热卷
- 武汉-沈阳热卷

#### 2. 跨品种价差策略
不同品种之间的价差套利。

**螺纹钢相关**:
- 螺纹-热卷_唐山
- 螺纹钢-钢坯_唐山
- 螺纹钢主力-热卷主力

**热卷相关**:
- 中板-热卷_唐山
- 热卷-带钢_唐山
- 热卷-螺纹钢_唐山
- 热卷-钢坯_唐山
- 热卷主力-螺纹钢主力

#### 3. 期现基差策略
期货与现货之间的价差。

**螺纹钢**:
- 螺纹钢主力基差

#### 4. 盘面利润策略
期货合约的盘面利润计算。

**螺纹钢**:
- 螺纹钢主力盘面利润

#### 5. 铁矿石策略
- 66铁精粉_唐山-62PB粉_曹妃甸港
- PB块-PB粉_日照港
- PB粉-超特粉_日照港
- 卡粉-PB粉_日照港
- 带钢现货/铁矿石现货
- 钢坯/铁矿石主力
- 钢坯现货/铁矿石现货

#### 6. 焦炭策略
- 带钢现货/焦炭现货
- 焦炭01/热卷01
- 焦炭01/螺纹钢01
- 焦炭01/铁矿石01
- 焦炭01基差
- 焦炭05/螺纹钢05
- 焦炭05基差

#### 7. 焦煤策略
- 带钢现货/焦煤现货
- 焦煤主力/热卷主力
- 焦煤主力/焦炭主力
- 焦煤主力/螺纹钢主力
- 焦煤主力/铁矿石主力
- 焦煤主力基差
- 焦煤现货/铁矿石现货

**功能说明**:
> 获取价差策略评估数据，包括跨区域、跨品种、期现基差、盘面利润等多种套利策略。这是核心的交易策略API，返回具体的入场点位、当前价差、策略方向和推荐星级。

**业务价值**:
- 🔴 **极高**: 包含核心套利策略
- 🔴 **极高**: 具体的入场和出场点位
- 🔴 **极高**: 三星推荐系统
- 🔴 **极高**: 实时价差监控

---

### API-3: 投机策略数据接口 ⭐核心

**端点**: `POST /newjycl/api/index/jctlIndexDatas/ts`

**完整URL**:
```
http://118.126.142.187:8089/ts-datamanager/newjcyj/api/index/jctlIndexDatas/ts
```

**请求参数**:

#### Query参数
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| token | string | 是 | 认证Token |

#### Body参数 (JSON)
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| isDisplay | string | 是 | 显示标识 (通常为"T") |
| type | string | 是 | 产品类型 (螺纹钢/热卷/铁矿石/焦炭/焦煤) |

**请求示例**:
```bash
curl -X POST "http://118.126.142.187:8089/ts-datamanager/newjcyj/api/index/jctlIndexDatas/ts?token=chinatsi123" \
  -H "Content-Type: application/json" \
  -d '{"isDisplay":"T","type":"螺纹钢"}'
```

**返回示例**:
```json
{
  "code": "0",
  "message": "获取成功",
  "data": [
    {
      "guid": {
        "countArbitrage": 0,
        "rsi": 1,
        "gz": 0,
        "c": 1,
        "larg": 0
      },
      "name": "上海-北京螺纹钢",
      "dataId": "spotsprerbbmshbmbj",
      "baseDatas": null,
      "splitName": ["上海", "北京螺纹钢"],
      "category": "跨区域",
      "dataIds": null,
      "sortNum": 1,
      "menuPath": "./index_kpz.html?dataId=xxx...",
      "cl": null
    }
  ],
  "totalCount": 14
}
```

**返回字段说明**:

#### 顶层字段
| 字段 | 类型 | 说明 |
|------|------|------|
| guid | object | 技术指标对象 (详细说明见下) |
| name | string | 策略名称 |
| dataId | string | 数据ID (内部标识) |
| baseDatas | object/null | 基础数据 |
| splitName | array[string] | 分拆名称 (如["上海", "北京螺纹钢"]) |
| category | string | 策略类别 |
| dataIds | object/null | 关联数据ID |
| sortNum | int | 排序号 |
| menuPath | string | 详情页面路径 |
| cl | object/null | 策略方向 |

#### guid对象说明 (技术指标)
| 字段 | 类型 | 说明 |
|------|------|------|
| countArbitrage | int | 跨期套利信号: -1=做空, 0=中性, 1=做多 |
| rsi | int | RSI指标: -1=超卖, 0=中性, 1=超买 |
| gz | int | 趋势指标: -1=下跌, 0=震荡, 1=上涨 |
| c | int | 策略信号: -1=做空, 0=观望, 1=做多 |
| larg | int | 大单信号: -1=大单做空, 0=无, 1=大单做多 |

**策略类别 (category)**:

| 类别 | 说明 | 示例 |
|------|------|------|
| 跨区域 | 不同地区价差 | 上海-北京螺纹钢 |
| 跨品种 | 不同品种价差 | 螺纹-热卷_唐山 |
| 期现基差 | 期货现货价差 | 螺纹钢主力基差 |
| 盘面利润 | 利润计算 | 螺纹钢主力盘面利润 |

**技术指标解读**:

#### RSI指标 (rsi)
```
-1: 超卖区 (可能反弹)
 0: 中性区
 1: 超买区 (可能回调)
```

#### 趋势指标 (gz)
```
-1: 下跌趋势
 0: 震荡趋势
 1: 上涨趋势
```

#### 策略信号 (c)
```
-1: 做空信号
 0: 观望信号
 1: 做多信号
```

#### 跨期套利 (countArbitrage)
```
-1: 跨期做空套利
 0: 无跨期套利机会
 1: 跨期做多套利
```

#### 大单信号 (larg)
```
-1: 大单做空
 0: 无明显大单
 1: 大单做多
```

**功能说明**:
> 获取投机策略的详细技术指标数据，包括RSI、趋势、策略信号、跨期套利和大单信号等多个维度的技术分析。这是比价差策略评估更详细的API，提供了完整的技术分析框架。

**业务价值**:
- 🔴 **极高**: 完整的技术指标体系
- 🔴 **极高**: 多维度策略信号
- 🔴 **极高**: 跨期套利机会
- 🔴 **极高**: 大单资金流向

**与API-2的区别**:

| 维度 | API-2 (jctlIndexDatasAssess) | API-3 (jctlIndexDatas/ts) |
|------|------------------------------|---------------------------|
| 数据深度 | 基础策略评估 | 详细技术指标 |
| 技术指标 | 无 | guid对象 (5个指标) |
| 策略方向 | cl字段 | 综合多个指标 |
| 推荐星级 | ccl (三星) | 无 |
| 使用场景 | 快速查看策略 | 深度技术分析 |

---

### API-4: 基础策略评估接口

**端点**: `POST /newjycl/api/index/jctlIndexDatas/v3`

**完整URL**:
```
http://118.126.142.187:8089/ts-datamanager/newjcyj/api/index/jctlIndexDatas/v3
```

**请求参数**:

#### Query参数
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| token | string | 是 | 认证Token |

#### Body参数 (JSON)
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| isDisplay | string | 是 | 显示标识 (通常为"T") |

**请求示例**:
```bash
curl -X POST "http://118.126.142.187:8089/ts-datamanager/newjcyj/api/index/jctlIndexDatas/v3?token=chinatsi123" \
  -H "Content-Type: application/json" \
  -d '{"isDisplay":"T"}'
```

**返回示例**:
```json
{
  "code": "0",
  "message": "获取成功",
  "data": [],
  "totalCount": 0
}
```

**功能说明**:
> 获取基础策略评估数据。当前返回空数据，可能需要额外的用户权限或参数。

---

## 历史数据类API

### API-5: 历史数据均值接口

**端点**: `GET /api_v3/iron/hcsj/type/8/mean`

**完整URL**:
```
https://service.chinatsi.net/api_v3/iron/hcsj/type/8/mean
```

**请求参数**:

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| n_code | string | 是 | 产品代码 (rb=螺纹钢, hc=热卷) |
| sdate | string | 是 | 开始日期 (YYYY-MM-DD) |
| edate | string | 是 | 结束日期 (YYYY-MM-DD) |
| cl_id | int | 否 | 策略ID (默认为2) |

**请求示例**:
```bash
curl "https://service.chinatsi.net/api_v3/iron/hcsj/type/8/mean?n_code=rb&sdate=2024-01-01&edate=2026-01-08&cl_id=2"
```

**返回示例**:
```json
{
  "code": "ok",
  "data": [],
  "message": "Success"
}
```

**功能说明**:
> 获取指定时间段内的历史数据均值。当前返回空数据，可能需要有效的产品代码和正确的日期范围。

---

### API-6: 率值数据接口

**端点**: `GET /api_v3/iron/hcsj/type/glv`

**完整URL**:
```
https://service.chinatsi.net/api_v3/iron/hcsj/type/glv
```

**请求参数**:

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| n_code | string | 是 | 产品代码 |
| sdate | string | 是 | 开始日期 |
| edate | string | 是 | 结束日期 |

**请求示例**:
```bash
curl "https://service.chinatsi.net/api_v3/iron/hcsj/type/glv?n_code=rb&sdate=2025-01-01&edate=2026-01-08"
```

**返回示例**:
```json
{
  "sr": "list index out of range",
  "code": "on",
  "message": "on"
}
```

**功能说明**:
> 获取率值数据（可能是各种技术指标的比率值）。当前返回错误，参数可能不正确。

---

### API-7: 前复权数据接口

**端点**: `GET /api_v3/iron/hcsj/fq/dheizi/aiengine`

**完整URL**:
```
https://service.chinatsi.net/api_v3/iron/hcsj/fq/dheizi/aiengine
```

**请求参数**:

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| n_code | string | 是 | 产品代码 |
| cl_id | int | 是 | 策略ID (如6=前复权长周期) |

**请求示例**:
```bash
curl "https://service.chinatsi.net/api_v3/iron/hcsj/fq/dheizi/aiengine?n_code=rb&cl_id=6"
```

**返回示例**:
```json
{
  "code": "no",
  "data": "list index out of range",
  "message": "no"
}
```

**功能说明**:
> 获取前复权数据的AI引擎分析。用于期货合约的前复权价格分析，当前返回错误。

---

### API-8: 期货历史数据获取

**端点**: `GET /api_v3/v4/ceshi/celuejianyi/getdata`

**完整URL**:
```
https://service.chinatsi.net/api_v3/v4/ceshi/celuejianyi/getdata
```

**请求参数**:

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| n_code | string | 是 | 产品代码 |
| sdate | string | 是 | 开始日期 |
| edate | string | 是 | 结束日期 |

**请求示例**:
```bash
curl "https://service.chinatsi.net/api_v3/v4/ceshi/celuejianyi/getdata?n_code=rb&sdate=2025-01-01&edate=2026-01-08"
```

**返回示例**:
```json
[]
```

**功能说明**:
> 获取期货历史数据。当前返回空数组，可能需要有效的用户认证。

---

## 价格预测类API

### API-9: 月度价格预测接口

**端点**: `GET /monthPriceForecast/index`

**完整URL**:
```
http://118.126.142.187:8089/ts-datamanager/monthPriceForecast/index
```

**请求参数**:

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| token | string | 是 | 认证Token |
| type | string | 是 | 产品代码 (rb=螺纹钢期货, hc=热卷期货) |

**请求示例**:
```bash
curl "http://118.126.142.187:8089/ts-datamanager/monthPriceForecast/index?token=chinatsi123&type=rb"
```

**返回示例**:
```json
{
  "code": "0",
  "message": "请求成功",
  "data": {},
  "totalCount": 0
}
```

**预期返回结构** (当有数据时):
```json
{
  "code": "0",
  "message": "请求成功",
  "data": {
    "base": [
      {"rq": "2025-12-01", "data": 3500},
      {"rq": "2026-01-01", "data": 3550}
    ],
    "forecast": [
      {"rq": "2026-02-01", "data": 3580},
      {"rq": "2026-03-01", "data": 3620}
    ]
  }
}
```

**字段说明**:

| 字段 | 类型 | 说明 |
|------|------|------|
| base | array | 历史基准价格数据 |
| forecast | array | 未来预测价格数据 |
| rq | string | 日期 (YYYY-MM-DD) |
| data | float | 价格数据 |

**功能说明**:
> 获取月度价格预测数据，包括历史价格和AI预测的未来价格。使用线性拟合等方法进行价格预测。当前返回空数据，可能需要配置预测模型。

---

## AI引擎类API

### API-10: AI引擎建议接口

**端点**: `GET /api_v3/v4/ceshi/celuejianyi/aiengine`

**完整URL**:
```
https://service.chinatsi.net/api_v3/v4/ceshi/celuejianyi/aiengine
```

**请求参数**:

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| n_code | string | 是 | 产品代码 |

**请求示例**:
```bash
curl "https://service.chinatsi.net/api_v3/v4/ceshi/celuejianyi/aiengine?n_code=rb"
```

**返回示例**:
```json
{
  "data": "'NoneType' object is not subscriptable",
  "message": "no",
  "code": "no"
}
```

**预期返回结构** (根据前端代码):
```json
[{
  "pos": "位置",
  "alert": "预警信息",
  "mean_price": "平均价格",
  "mean_profit": "平均盈亏",
  "price_day": "当日价格",
  "rule": [
    {
      "sort": 1,
      "rq": "2026-01-08",
      "price": "3500",
      "gl": "75%",
      "per": "30%",
      "profit": "150"
    }
  ],
  "policy": "做多",
  "sum": 1,
  "port_bt": "75%"
}]
```

**功能说明**:
> 获取AI引擎的交易建议，包括趋势判断、位置判断、分批入场建议、平均成本和盈亏计算。这是核心的AI决策引擎。

---

### API-11: AI引擎短周期建议

**端点**: `GET /api_v3/v4/ceshi/celuejianyi/aiengine/g`

**完整URL**:
```
https://service.chinatsi.net/api_v3/v4/ceshi/celuejianyi/aiengine/g
```

**请求参数**:

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| n_code | string | 是 | 产品代码 + "g" 后缀 |

**请求示例**:
```bash
curl "https://service.chinatsi.net/api_v3/v4/ceshi/celuejianyi/aiengine/g?n_code=rbg"
```

**功能说明**:
> 获取短周期的AI引擎建议，用于短期交易决策。

---

### API-12: AI引擎授权接口

**端点**: `GET /api_v3/v4/celuejianyi/tsi/authorize`

**完整URL**:
```
https://service.chinatsi.net/api_v3/v4/celuejianyi/tsi/authorize
```

**请求参数**:

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | string | 是 | 授权ID |

**请求示例**:
```bash
curl "https://service.chinatsi.net/api_v3/v4/celuejianyi/tsi/authorize?id=test123"
```

**返回示例**:
```json
{
  "data": [],
  "message": "Success",
  "code": "no"
}
```

**功能说明**:
> 验证用户是否有权限访问AI引擎功能。

---

## 图表服务API

### 图表端点列表

系统使用iframe嵌入图表服务，图表服务位于 `https://vote.chinatsi.net/dsystem/`

| 图表类型 | URL路径 | 说明 |
|----------|---------|------|
| 趋势图表 | `chart5.html` | 主要趋势图表 |
| K线图表 | `chart_d4.html` | K线图 |
| 前复权长周期 | `qianfuquanchangzhouqi.html` | 前复权长周期图 |
| 前复权短周期 | `qianfuquanduanzhouqi.html` | 前复权短周期图 |
| 迷你趋势图 | `chartmini5.html` | 迷你趋势图 |
| 迷你K线图 | `chart_d4_mini.html` | 迷你K线图 |
| 迷你前复权长周期 | `qianfuquanchangzhouqimini.html` | 迷你前复权长周期图 |
| 迷你前复权短周期 | `qianfuquanduanzhouqimini.html` | 迷你前复权短周期图 |

**使用示例**:
```html
<iframe src="https://vote.chinatsi.net/dsystem/chart5.html?dataName=rb"></iframe>
```

---

## 系统一API (在线监测预警系统)

### API-13: 用户登录接口

**端点**: `POST /online/user/login`

**完整URL**:
```
http://118.126.142.187:8088/online/user/login
```

**请求参数** (Body JSON):
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| mobile | string | 是 | 手机号 |
| password | string | 是 | 密码 |
| code | string | 是 | 验证码 |

**请求示例**:
```bash
curl -X POST "http://118.126.142.187:8088/online/user/login" \
  -H "Content-Type: application/json" \
  -d '{"mobile":"test","password":"test","code":"1234"}'
```

**返回示例**:
```json
{
  "code": "1",
  "message": "用户名或者密码失败，请重试",
  "data": null,
  "totalCount": 0
}
```

**功能说明**:
> 用户登录接口，需要正确的手机号和密码。

---

### API-14: 菜单获取接口

**端点**: `GET /menu/findMenuByUserFormat`

**完整URL**:
```
http://118.126.142.187:8088/online/menu/findMenuByUserFormat
```

**请求参数**:
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| userId | string | 是 | 用户ID |
| type | int | 是 | 菜单类型 (1=左侧菜单, 7=顶部菜单) |

**请求示例**:
```bash
curl "http://118.126.142.187:8088/online/menu/findMenuByUserFormat?userId=test&type=1"
```

**返回示例**:
```json
{
  "code": "1",
  "message": "查询失败",
  "data": null
}
```

**功能说明**:
> 获取用户的菜单权限配置。需要有效的用户ID。

---

### API-15: 微信绑定接口

**端点**: `PUT /onlineUserCustom/bindingWeChatCode`

**完整URL**:
```
http://118.126.142.187:8088/online/onlineUserCustom/bindingWeChatCode
```

**请求参数** (Body JSON):
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| code | string | 是 | 微信授权码 |
| userId | string | 是 | 用户ID |

**功能说明**:
> 绑定微信账号到系统用户。

---

## 数据字典

### 产品代码 (n_code)

| 代码 | 产品 | 说明 |
|------|------|------|
| rb | 螺纹钢期货 | Rebar Futures |
| hc | 热卷期货 | Hot Rolled Coil Futures |
| i | 铁矿石期货 | Iron Ore Futures |
| j | 焦炭期货 | Coke Futures |
| jm | 焦煤期货 | Coking Coal Futures |
| rb现货 | 螺纹钢现货 | Rebar Spot |
| hc现货 | 热卷现货 | HRC Spot |

### 产品类型 (type)

| 类型 | 说明 | API支持 |
|------|------|---------|
| 螺纹钢 | 螺纹钢相关策略 | ✅ |
| 热卷 | 热轧卷板相关策略 | ✅ |
| 铁矿石 | 铁矿石相关策略 | ✅ |
| 焦炭 | 焦炭相关策略 | ✅ |
| 焦煤 | 焦煤相关策略 | ✅ |
| 铁合金 | 铁合金相关策略 | ⚠️ 返回空 |

### 策略方向 (cl)

| 值 | 方向 | 说明 |
|----|------|------|
| -1 | 做空 | Short |
| 0 | 观望 | Neutral |
| 1 | 做多 | Long |

### 推荐星级 (ccl)

| 星级组合 | 说明 |
|----------|------|
| [1, 1, 1] | 三星做多 (强烈推荐) |
| [1, 1, 0] | 二星做多 |
| [1, 0, 0] | 一星做多 |
| [0, 0, 0] | 观望 |
| [-1, 0, 0] | 一星做空 |
| [-1, -1, 0] | 二星做空 |
| [-1, -1, -1] | 三星做空 (强烈推荐) |

### 技术指标值

| 指标 | -1 | 0 | 1 |
|------|----|----|---|
| countArbitrage | 跨期做空 | 无跨期 | 跨期做多 |
| rsi | 超卖 | 中性 | 超买 |
| gz | 下跌 | 震荡 | 上涨 |
| c | 做空 | 观望 | 做多 |
| larg | 大单做空 | 无 | 大单做多 |

---

## 错误码说明

### 通用错误码

| code | message | 说明 |
|------|---------|------|
| 0 | 获取成功/请求成功 | 操作成功 |
| 1 | 失败 | 操作失败 |
| no | no | 无数据或权限不足 |
| ok | Success | 成功 |

### HTTP状态码

| 状态码 | 说明 |
|--------|------|
| 200 | 请求成功 |
| 400 | 请求参数错误 |
| 401 | 未授权 |
| 403 | 禁止访问 |
| 404 | 资源不存在 |
| 500 | 服务器内部错误 |

### 特定错误信息

| 错误信息 | 原因 | 解决方案 |
|----------|------|----------|
| "list index out of range" | 数据索引越界 | 检查参数是否正确 |
| "'NoneType' object is not subscriptable" | 空对象访问 | 检查数据是否存在 |
| "用户名或者密码失败" | 登录失败 | 检查用户名密码 |
| "查询失败" | 数据库查询失败 | 检查用户权限 |

---

## API使用示例

### 完整的价差策略获取流程

```bash
# 1. 验证Token
curl "http://118.126.142.187:8089/ts-datamanager/newjcyj/api/simInterception/checkToken?token=chinatsi123"

# 2. 获取螺纹钢价差策略
curl -X POST "http://118.126.142.187:8089/ts-datamanager/newjcyj/api/index/jctlIndexDatasAssess?token=chinatsi123" \
  -H "Content-Type: application/json" \
  -d '{"isDisplay":"T","type":"螺纹钢"}'

# 3. 获取螺纹钢投机策略
curl -X POST "http://118.126.142.187:8089/ts-datamanager/newjcyj/api/index/jctlIndexDatas/ts?token=chinatsi123" \
  -H "Content-Type: application/json" \
  -d '{"isDisplay":"T","type":"螺纹钢"}'
```

### 获取所有产品类型的策略

```bash
# 螺纹钢
curl -X POST "http://118.126.142.187:8089/ts-datamanager/newjcyj/api/index/jctlIndexDatasAssess?token=chinatsi123" \
  -H "Content-Type: application/json" \
  -d '{"isDisplay":"T","type":"螺纹钢"}'

# 热卷
curl -X POST "http://118.126.142.187:8089/ts-datamanager/newjcyj/api/index/jctlIndexDatasAssess?token=chinatsi123" \
  -H "Content-Type: application/json" \
  -d '{"isDisplay":"T","type":"热卷"}'

# 铁矿石
curl -X POST "http://118.126.142.187:8089/ts-datamanager/newjcyj/api/index/jctlIndexDatasAssess?token=chinatsi123" \
  -H "Content-Type: application/json" \
  -d '{"isDisplay":"T","type":"铁矿石"}'

# 焦炭
curl -X POST "http://118.126.142.187:8089/ts-datamanager/newjcyj/api/index/jctlIndexDatasAssess?token=chinatsi123" \
  -H "Content-Type: application/json" \
  -d '{"isDisplay":"T","type":"焦炭"}'

# 焦煤
curl -X POST "http://118.126.142.187:8089/ts-datamanager/newjcyj/api/index/jctlIndexDatasAssess?token=chinatsi123" \
  -H "Content-Type: application/json" \
  -d '{"isDisplay":"T","type":"焦煤"}'
```

---

## 安全警告

### 🔴 严重安全漏洞

**硬编码Token暴露**: 系统在JavaScript代码中硬编码了Token `chinatsi123`，这导致：

1. 任何人都可以访问所有API接口
2. 核心交易策略数据完全暴露
3. 无用户权限控制
4. 无访问频率限制

### 潜在损失

1. **商业机密泄露**: AI交易策略、定价算法
2. **竞争优势丧失**: 客户可直接复制策略
3. **经济损失**: 客户可能不再付费订阅
4. **市场风险**: 策略被滥用降低市场效率

### 建议修复

```javascript
// ❌ 错误做法
url: ".../api/xxx?token=chinatsi123"

// ✅ 正确做法
url: ".../api/xxx?token=" + getUserToken()
```

---

## 附录

### 支持的交易所/市场

根据dataId和策略名称分析，系统支持以下市场：

**现货市场**:
- 上海、北京、沈阳、唐山、太原、广州、成都、西安、杭州、乐从、武汉、天津、日照港、曹妃甸港、吕梁、天津港

**期货市场**:
- 螺纹钢主力、热卷主力、铁矿石主力、焦炭主力、焦煤主力
- 螺纹钢01/05、热卷01/05、铁矿石01、焦炭01/05

### 数据更新频率

根据enterDate字段分析，策略数据每日更新。

### 技术架构推测

**前端**:
- Vue.js 2.x
- Element UI
- ECharts
- jQuery + Ajax

**后端**:
- Java (Spring框架推测)
- MySQL/Oracle数据库
- Nginx反向代理

**第三方服务**:
- service.chinatsi.net - 主API服务
- vote.chinatsi.net - 图表服务
- tl.chinatsi.com - 投机策略服务

---

*文档版本: v1.0*
*最后更新: 2026-01-08*
*数据来源: API实际测试*
*测试Token: chinatsi123 (硬编码漏洞)*
