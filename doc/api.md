### 税务登记信息接口文档  
**接口地址**: `/api/v7/TaxOld`  
**请求体**:  
```json
{
  "header": {
    "interface_no": "api_007_swdjxx",
    "loginName": "test",
    "department": "测试",
    "orgId": "123"
  },
  "body": {
    "cxName": "api_007_swdjxx",
    "certName": "企业全称",
    "certId": "统一社会信用代码"
  }
}
```

**返回体**:  
```json
{
  "header": {
    "interface_no": "api_007_swdjxx",
    "loginName": "test",
    "department": "测试",
    "orgId": "124",
    "unique": "1234567890"
  },
  "body": [{
    "nsrmc": "纳税人名称",
    "nsrsbh": "纳税人识别号",
    "djlx": "登记类型(1:单位纳税人 2:个体纳税人)",
    "djrq": "登记日期(yyyy-MM-dd)",
    "hy": "行业",
    "zcdz": "注册地址",
    "scjydz": "生产经营地址",
    "swjg": "主管税务机关",
    "fddbr": "法定代表人",
    "zcrq": "注册日期(yyyy-MM-dd)",
    "zczb": "注册资本(万元)",
    "yyqx": "营业期限",
    "zzjgdm": "组织机构代码",
    "swdjzh": "税务登记证号"
  }],
  "status": "success",
  "code": 200,
  "message": "查询成功"
}
```

---

### 纳税信用信息接口文档  
**接口地址**: `/api/v7/TaxOld`  
**请求体**:  
```json
{
  "header": {
    "interface_no": "api_007_nsxyxx",
    "loginName": "test",
    "department": "测试",
    "orgId": "123"
  },
  "body": {
    "cxName": "api_007_nsxyxx",
    "certName": "企业全称",
    "certId": "统一社会信用代码",
    "nd": "2019"
  }
}
```

**返回体**:  
```json
{
  "header": {
    "interface_no": "api_007_nsxyxx",
    "loginName": "test",
    "department": "测试",
    "orgId": "124",
    "unique": "1234567890"
  },
  "body": [{
    "nsrmc": "纳税人名称",
    "nsrsbh": "纳税人识别号",
    "pjjg": "评价机关",
    "pjnd": "评价年度",
    "xyjb": "信用级别(A/B/C/D/M)",
    "xyjbmc": "信用级别名称",
    "xyjf": "信用积分",
    "xyjbdj": "信用等级",
    "bzyy": "不评价原因",
    "pjsj": "评价时间(yyyy-MM-dd)",
    "sftb": "是否复评(0:否 1:是)",
    "fpsm": "复评说明"
  }],
  "status": "success",
  "code": 200,
  "message": "查询成功"
}
```

---

### 行政处罚信息接口文档  
**接口地址**: `/api/v7/TaxOld`  
**请求体**:  
```json
{
  "header": {
    "interface_no": "api_007_xzcfxx",
    "loginName": "test",
    "department": "测试",
    "orgId": "123"
  },
  "body": {
    "cxName": "api_007_xzcfxx",
    "certName": "企业全称",
    "certId": "统一社会信用代码",
    "clcfjdrq": "2019/01/01-2019/12/09"
  }
}
```

**返回体**:  
```json
{
  "header": {
    "interface_no": "api_007_xzcfxx",
    "loginName": "test",
    "department": "测试",
    "orgId": "124",
    "unique": "1234567890"
  },
  "body": [{
    "wfxwmc": "违法行为名称",
    "cfjdrq": "处罚决定日期(yyyy-MM-dd)",
    "cfjds": "处罚决定书文号",
    "cfyj": "处罚依据",
    "cfnr": "处罚内容",
    "cfjg": "处罚机关",
    "wfxwlx": "违法行为类型",
    "cfje": "处罚金额(元)",
    "frdb": "法人代表",
    "nsrsbh": "纳税人识别号",
    "wfssrq": "违法事实日期(yyyy-MM-dd)",
    "cfzt": "处罚状态(0:未执行 1:已执行)"
  }],
  "status": "success",
  "code": 200,
  "message": "查询成功"
}
```

---

### 变更登记信息接口文档  
**接口地址**: `/api/v7/TaxOld`  
**请求体**:  
```json
{
  "header": {
    "interface_no": "api_007_bgdjxx",
    "loginName": "test",
    "department": "测试",
    "orgId": "123"
  },
  "body": {
    "cxName": "api_007_bgdjxx",
    "certName": "企业全称",
    "certId": "统一社会信用代码",
    "bgrq": "2019/01/01-2019/12/09"
  }
}
```

**返回体**:  
```json
{
  "header": {
    "interface_no": "api_007_bgdjxx",
    "loginName": "test",
    "department": "测试",
    "orgId": "124",
    "unique": "1234567890"
  },
  "body": [{
    "bgxm": "变更项目",
    "bgrq": "变更日期(yyyy-MM-dd)",
    "bgqnr": "变更前内容",
    "bghnr": "变更后内容",
    "bgyy": "变更原因",
    "nsrsbh": "纳税人识别号",
    "nsrmc": "纳税人名称",
    "swjg": "税务机关",
    "bgr": "变更人",
    "bglx": "变更类型(1:关键信息 2:非关键信息)",
    "djbh": "登记编号"
  }],
  "status": "success",
  "code": 200,
  "message": "查询成功"
}
```

---

### 纳税申报信息接口文档  
**接口地址**: `/api/v7/TaxOld`  
**请求体**:  
```json
{
  "header": {
    "interface_no": "api_007_nssbxx",
    "loginName": "test",
    "department": "测试",
    "orgId": "123"
  },
  "body": {
    "cxName": "api_007_nssbxx",
    "certName": "企业全称",
    "certId": "统一社会信用代码",
    "sssqq": "2016/01/01",
    "sssqz": "2016/01/01"
  }
}
```

**返回体**:  
```json
{
  "header": {
    "interface_no": "api_007_nssbxx",
    "loginName": "test",
    "department": "测试",
    "orgId": "124",
    "unique": "1234567890"
  },
  "body": [{
    "sbrq": "申报日期(yyyy-MM-dd)",
    "ssq": "所属期(yyyy-MM)",
    "szmc": "税种名称",
    "sbje": "申报金额(元)",
    "ynse": "应纳税额(元)",
    "yjnse": "应缴纳税额(元)",
    "sjse": "实缴税额(元)",
    "sbzt": "申报状态(0:未申报 1:已申报)",
    "nsrsbh": "纳税人识别号",
    "nsrmc": "纳税人名称",
    "skssqq": "税款所属期起(yyyy-MM-dd)",
    "skssqz": "税款所属期止(yyyy-MM-dd)",
    "sbzl": "申报种类"
  }],
  "status": "success",
  "code": 200,
  "message": "查询成功"
}
```

---

### 小企业财务报表接口文档  
#### 1. 资产负债  
**请求体**:  
```json
{
  "header": {
    "interface_no": "api_007_xqyzcfz",
    "loginName": "test",
    "department": "测试",
    "orgId": "123"
  },
  "body": {
    "cxName": "api_007_xqyzcfz",
    "certName": "企业全称",
    "certId": "统一社会信用代码",
    "sssqq": "2016/01/01",
    "sssqz": "2016/01/01"
  }
}
```

**返回体**:  
```json
{
  "header": {
    "interface_no": "api_007_xqyzcfz",
    "loginName": "test",
    "department": "测试",
    "orgId": "124",
    "unique": "1234567890"
  },
  "body": [{
    "bbq": "报表期间(yyyy-MM)",
    "zzcje": "资产总计(元)",
    "fzcze": "负债总计(元)",
    "syzqy": "所有者权益(元)",
    "ldzchj": "流动资产合计(元)",
    "ldfzhj": "流动负债合计(元)",
    "gdzcje": "固定资产净值(元)",
    "ch": "存货(元)",
    "yszk": "应收账款(元)",
    "yfzk": "应付账款(元)",
    "nsrsbh": "纳税人识别号",
    "hbzc": "货币资金(元)",
    "yspj": "应收票据(元)",
    "qtysk": "其他应收款(元)",
    "gdzcyz": "固定资产原值(元)",
    "ljzj": "累计折旧(元)"
  }],
  "status": "success",
  "code": 200,
  "message": "查询成功"
}
```

#### 2. 利润表  
**请求体**:  
```json
{
  "header": {
    "interface_no": "api_007_xqylr",
    "loginName": "test",
    "department": "测试",
    "orgId": "123"
  },
  "body": {
    "cxName": "api_007_xqylr",
    "certName": "企业全称",
    "certId": "统一社会信用代码",
    "sssqq": "2016/01/01",
    "sssqz": "2016/01/01"
  }
}
```

**返回体**:  
```json
{
  "header": {
    "interface_no": "api_007_xqylr",
    "loginName": "test",
    "department": "测试",
    "orgId": "124",
    "unique": "1234567890"
  },
  "body": [{
    "bbq": "报表期间(yyyy-MM)",
    "yysr": "营业收入(元)",
    "yycb": "营业成本(元)",
    "yylr": "营业利润(元)",
    "lrze": "利润总额(元)",
    "jlr": "净利润(元)",
    "xssr": "销售收入(元)",
    "yysjjfj": "营业税金及附加(元)",
    "glfy": "管理费用(元)",
    "xsjlr": "销售利润(元)",
    "nsrsbh": "纳税人识别号",
    "yyfy": "营业费用(元)",
    "cbfy": "财务费用(元)",
    "tzzs": "投资损失(元)",
    "yysrzk": "营业外收入(元)",
    "yywzc": "营业外支出(元)"
  }],
  "status": "success",
  "code": 200,
  "message": "查询成功"
}
```

#### 3. 现金流量表  
**请求体**:  
```json
{
  "header": {
    "interface_no": "api_007_xqyxjl",
    "loginName": "test",
    "department": "测试",
    "orgId": "123"
  },
  "body": {
    "cxName": "api_007_xqyxjl",
    "certName": "企业全称",
    "certId": "统一社会信用代码",
    "sssqq": "2016/01/01",
    "sssqz": "2016/01/01"
  }
}
```

**返回体**:  
```json
{
  "header": {
    "interface_no": "api_007_xqyxjl",
    "loginName": "test",
    "department": "测试",
    "orgId": "124",
    "unique": "1234567890"
  },
  "body": [{
    "bbq": "报表期间(yyyy-MM)",
    "jyhdxjje": "经营活动现金净额(元)",
    "tzhdxjje": "投资活动现金净额(元)",
    "czhdxjje": "筹资活动现金净额(元)",
    "xjxjje": "现金净增加额(元)",
    "jyhdxjlr": "经营活动现金流入(元)",
    "jyhdxjlc": "经营活动现金流出(元)",
    "qmxjyye": "期末现金余额(元)",
    "cqqmye": "期初余额(元)",
    "nsrsbh": "纳税人识别号",
    "tzhdxjlr": "投资活动现金流入(元)",
    "tzhdxjlc": "投资活动现金流出(元)",
    "czhdxjlr": "筹资活动现金流入(元)",
    "czhdxjlc": "筹资活动现金流出(元)",
    "xjdyxj": "现金等价物净增加额(元)"
  }],
  "status": "success",
  "code": 200,
  "message": "查询成功"
}
```

---

### 接口规范说明  
1. **通用字段**:
   - `header.interface_no`: 接口唯一标识符
   - `body.cxName`: 必须与interface_no值一致
   - `header.unique`: 请求唯一标识（响应时回传）

2. **时间格式**:
   - 年度: `yyyy`
   - 日期范围: `yyyy/MM/dd-yyyy/MM/dd`
   - 单日/日期字段: `yyyy/MM/dd`
   - 月份字段: `yyyy-MM`

3. **金额单位**:
   - 所有金额字段单位为元，保留两位小数

4. **状态码说明**:
   - `200`: 成功
   - `400`: 参数错误
   - `404`: 无数据
   - `500`: 服务器内部错误
   - `601`: 权限不足

5. **分页机制**:
   - 当返回数据量过大时，body自动分页
   - 分页信息包含在header中：
     ```json
     "header": {
       ...,
       "pageNo": 1,
       "pageSize": 100,
       "totalCount": 350
     }
     ```