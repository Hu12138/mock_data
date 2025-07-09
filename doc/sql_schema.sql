-- 税务登记信息表
CREATE TABLE tax_registration (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nsrmc VARCHAR(100) COMMENT '纳税人名称',
    nsrsbh VARCHAR(50) COMMENT '纳税人识别号',
    djlx TINYINT COMMENT '登记类型(1:单位纳税人 2:个体纳税人)',
    djrq DATE COMMENT '登记日期',
    hy VARCHAR(50) COMMENT '行业',
    zcdz VARCHAR(200) COMMENT '注册地址',
    scjydz VARCHAR(200) COMMENT '生产经营地址',
    swjg VARCHAR(100) COMMENT '主管税务机关',
    fddbr VARCHAR(50) COMMENT '法定代表人',
    zcrq DATE COMMENT '注册日期',
    zczb DECIMAL(15,2) COMMENT '注册资本(万元)',
    yyqx VARCHAR(50) COMMENT '营业期限',
    zzjgdm VARCHAR(50) COMMENT '组织机构代码',
    swdjzh VARCHAR(50) COMMENT '税务登记证号',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 纳税信用信息表
CREATE TABLE tax_credit (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nsrmc VARCHAR(100) COMMENT '纳税人名称',
    nsrsbh VARCHAR(50) COMMENT '纳税人识别号',
    pjjg VARCHAR(100) COMMENT '评价机关',
    pjnd VARCHAR(10) COMMENT '评价年度',
    xyjb CHAR(1) COMMENT '信用级别(A/B/C/D/M)',
    xyjbmc VARCHAR(20) COMMENT '信用级别名称',
    xyjf INT COMMENT '信用积分',
    xyjbdj VARCHAR(20) COMMENT '信用等级',
    bzyy VARCHAR(200) COMMENT '不评价原因',
    pjsj DATE COMMENT '评价时间',
    sftb TINYINT COMMENT '是否复评(0:否 1:是)',
    fpsm VARCHAR(200) COMMENT '复评说明',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 行政处罚信息表
CREATE TABLE tax_penalty (
    id INT AUTO_INCREMENT PRIMARY KEY,
    wfxwmc VARCHAR(200) COMMENT '违法行为名称',
    cfjdrq DATE COMMENT '处罚决定日期',
    cfjds VARCHAR(50) COMMENT '处罚决定书文号',
    cfyj VARCHAR(200) COMMENT '处罚依据',
    cfnr TEXT COMMENT '处罚内容',
    cfjg VARCHAR(100) COMMENT '处罚机关',
    wfxwlx VARCHAR(50) COMMENT '违法行为类型',
    cfje DECIMAL(15,2) COMMENT '处罚金额(元)',
    frdb VARCHAR(50) COMMENT '法人代表',
    nsrsbh VARCHAR(50) COMMENT '纳税人识别号',
    wfssrq DATE COMMENT '违法事实日期',
    cfzt TINYINT COMMENT '处罚状态(0:未执行 1:已执行)',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 变更登记信息表
CREATE TABLE tax_change (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bgxm VARCHAR(100) COMMENT '变更项目',
    bgrq DATE COMMENT '变更日期',
    bgqnr TEXT COMMENT '变更前内容',
    bghnr TEXT COMMENT '变更后内容',
    bgyy VARCHAR(200) COMMENT '变更原因',
    nsrsbh VARCHAR(50) COMMENT '纳税人识别号',
    nsrmc VARCHAR(100) COMMENT '纳税人名称',
    swjg VARCHAR(100) COMMENT '税务机关',
    bgr VARCHAR(50) COMMENT '变更人',
    bglx TINYINT COMMENT '变更类型(1:关键信息 2:非关键信息)',
    djbh VARCHAR(50) COMMENT '登记编号',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 纳税申报信息表
CREATE TABLE tax_declaration (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sbrq DATE COMMENT '申报日期',
    ssq VARCHAR(10) COMMENT '所属期(yyyy-MM)',
    szmc VARCHAR(50) COMMENT '税种名称',
    sbje DECIMAL(15,2) COMMENT '申报金额(元)',
    ynse DECIMAL(15,2) COMMENT '应纳税额(元)',
    yjnse DECIMAL(15,2) COMMENT '应缴纳税额(元)',
    sjse DECIMAL(15,2) COMMENT '实缴税额(元)',
    sbzt TINYINT COMMENT '申报状态(0:未申报 1:已申报)',
    nsrsbh VARCHAR(50) COMMENT '纳税人识别号',
    nsrmc VARCHAR(100) COMMENT '纳税人名称',
    skssqq DATE COMMENT '税款所属期起',
    skssqz DATE COMMENT '税款所属期止',
    sbzl VARCHAR(50) COMMENT '申报种类',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 小企业资产负债表
CREATE TABLE small_business_balance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bbq VARCHAR(10) COMMENT '报表期间(yyyy-MM)',
    zzcje DECIMAL(15,2) COMMENT '资产总计(元)',
    fzcze DECIMAL(15,2) COMMENT '负债总计(元)',
    syzqy DECIMAL(15,2) COMMENT '所有者权益(元)',
    ldzchj DECIMAL(15,2) COMMENT '流动资产合计(元)',
    ldfzhj DECIMAL(15,2) COMMENT '流动负债合计(元)',
    gdzcje DECIMAL(15,2) COMMENT '固定资产净值(元)',
    ch DECIMAL(15,2) COMMENT '存货(元)',
    yszk DECIMAL(15,2) COMMENT '应收账款(元)',
    yfzk DECIMAL(15,2) COMMENT '应付账款(元)',
    nsrsbh VARCHAR(50) COMMENT '纳税人识别号',
    hbzc DECIMAL(15,2) COMMENT '货币资金(元)',
    yspj DECIMAL(15,2) COMMENT '应收票据(元)',
    qtysk DECIMAL(15,2) COMMENT '其他应收款(元)',
    gdzcyz DECIMAL(15,2) COMMENT '固定资产原值(元)',
    ljzj DECIMAL(15,2) COMMENT '累计折旧(元)',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 小企业利润表
CREATE TABLE small_business_profit (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bbq VARCHAR(10) COMMENT '报表期间(yyyy-MM)',
    yysr DECIMAL(15,2) COMMENT '营业收入(元)',
    yycb DECIMAL(15,2) COMMENT '营业成本(元)',
    yylr DECIMAL(15,2) COMMENT '营业利润(元)',
    lrze DECIMAL(15,2) COMMENT '利润总额(元)',
    jlr DECIMAL(15,2) COMMENT '净利润(元)',
    xssr DECIMAL(15,2) COMMENT '销售收入(元)',
    yysjjfj DECIMAL(15,2) COMMENT '营业税金及附加(元)',
    glfy DECIMAL(15,2) COMMENT '管理费用(元)',
    xsjlr DECIMAL(15,2) COMMENT '销售利润(元)',
    nsrsbh VARCHAR(50) COMMENT '纳税人识别号',
    yyfy DECIMAL(15,2) COMMENT '营业费用(元)',
    cbfy DECIMAL(15,2) COMMENT '财务费用(元)',
    tzzs DECIMAL(15,2) COMMENT '投资损失(元)',
    yysrzk DECIMAL(15,2) COMMENT '营业外收入(元)',
    yywzc DECIMAL(15,2) COMMENT '营业外支出(元)',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 小企业现金流量表
CREATE TABLE small_business_cashflow (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bbq VARCHAR(10) COMMENT '报表期间(yyyy-MM)',
    jyhdxjje DECIMAL(15,2) COMMENT '经营活动现金净额(元)',
    tzhdxjje DECIMAL(15,2) COMMENT '投资活动现金净额(元)',
    czhdxjje DECIMAL(15,2) COMMENT '筹资活动现金净额(元)',
    xjxjje DECIMAL(15,2) COMMENT '现金净增加额(元)',
    jyhdxjlr DECIMAL(15,2) COMMENT '经营活动现金流入(元)',
    jyhdxjlc DECIMAL(15,2) COMMENT '经营活动现金流出(元)',
    qmxjyye DECIMAL(15,2) COMMENT '期末现金余额(元)',
    cqqmye DECIMAL(15,2) COMMENT '期初余额(元)',
    nsrsbh VARCHAR(50) COMMENT '纳税人识别号',
    tzhdxjlr DECIMAL(15,2) COMMENT '投资活动现金流入(元)',
    tzhdxjlc DECIMAL(15,2) COMMENT '投资活动现金流出(元)',
    czhdxjlr DECIMAL(15,2) COMMENT '筹资活动现金流入(元)',
    czhdxjlc DECIMAL(15,2) COMMENT '筹资活动现金流出(元)',
    xjdyxj DECIMAL(15,2) COMMENT '现金等价物净增加额(元)',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
