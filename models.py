from app import db
from datetime import datetime

class TaxRegistration(db.Model):
    """税务登记信息模型"""
    __tablename__ = 'tax_registration'
    
    id = db.Column(db.Integer, primary_key=True)
    nsrmc = db.Column(db.String(100), nullable=False)  # 纳税人名称
    nsrsbh = db.Column(db.String(20), nullable=False)  # 纳税人识别号
    djlx = db.Column(db.Integer)  # 登记类型(1:单位纳税人 2:个体纳税人)
    djrq = db.Column(db.Date)  # 登记日期
    hy = db.Column(db.String(50))  # 行业
    zcdz = db.Column(db.String(200))  # 注册地址
    scjydz = db.Column(db.String(200))  # 生产经营地址
    swjg = db.Column(db.String(100))  # 主管税务机关
    fddbr = db.Column(db.String(50))  # 法定代表人
    zcrq = db.Column(db.Date)  # 注册日期
    zczb = db.Column(db.Float)  # 注册资本(万元)
    yyqx = db.Column(db.String(50))  # 营业期限
    zzjgdm = db.Column(db.String(20))  # 组织机构代码
    swdjzh = db.Column(db.String(50))  # 税务登记证号

class TaxCredit(db.Model):
    """纳税信用信息模型"""
    __tablename__ = 'tax_credit'
    
    id = db.Column(db.Integer, primary_key=True)
    nsrmc = db.Column(db.String(100), nullable=False)  # 纳税人名称
    nsrsbh = db.Column(db.String(20), nullable=False)  # 纳税人识别号
    pjjg = db.Column(db.String(100))  # 评价机关
    pjnd = db.Column(db.String(4))  # 评价年度
    xyjb = db.Column(db.String(1))  # 信用级别(A/B/C/D/M)
    xyjbmc = db.Column(db.String(20))  # 信用级别名称
    xyjf = db.Column(db.Integer)  # 信用积分
    xyjbdj = db.Column(db.String(20))  # 信用等级
    bzyy = db.Column(db.String(200))  # 不评价原因
    pjsj = db.Column(db.Date)  # 评价时间
    sftb = db.Column(db.Integer)  # 是否复评(0:否 1:是)
    fpsm = db.Column(db.String(200))  # 复评说明

class TaxPenalty(db.Model):
    """行政处罚信息模型"""
    __tablename__ = 'tax_penalty'
    
    id = db.Column(db.Integer, primary_key=True)
    wfxwmc = db.Column(db.String(200))  # 违法行为名称
    cfjdrq = db.Column(db.Date)  # 处罚决定日期
    cfjds = db.Column(db.String(50))  # 处罚决定书文号
    cfyj = db.Column(db.String(200))  # 处罚依据
    cfnr = db.Column(db.String(500))  # 处罚内容
    cfjg = db.Column(db.String(100))  # 处罚机关
    wfxwlx = db.Column(db.String(50))  # 违法行为类型
    cfje = db.Column(db.Float)  # 处罚金额(元)
    frdb = db.Column(db.String(50))  # 法人代表
    nsrsbh = db.Column(db.String(20))  # 纳税人识别号
    wfssrq = db.Column(db.Date)  # 违法事实日期
    cfzt = db.Column(db.Integer)  # 处罚状态(0:未执行 1:已执行)

class TaxChange(db.Model):
    """变更登记信息模型"""
    __tablename__ = 'tax_change'
    
    id = db.Column(db.Integer, primary_key=True)
    bgxm = db.Column(db.String(100))  # 变更项目
    bgrq = db.Column(db.Date)  # 变更日期
    bgqnr = db.Column(db.String(500))  # 变更前内容
    bghnr = db.Column(db.String(500))  # 变更后内容
    bgyy = db.Column(db.String(200))  # 变更原因
    nsrsbh = db.Column(db.String(20))  # 纳税人识别号
    nsrmc = db.Column(db.String(100))  # 纳税人名称
    swjg = db.Column(db.String(100))  # 税务机关
    bgr = db.Column(db.String(50))  # 变更人
    bglx = db.Column(db.Integer)  # 变更类型(1:关键信息 2:非关键信息)
    djbh = db.Column(db.String(50))  # 登记编号

class TaxDeclaration(db.Model):
    """纳税申报信息模型"""
    __tablename__ = 'tax_declaration'
    
    id = db.Column(db.Integer, primary_key=True)
    sbrq = db.Column(db.Date)  # 申报日期
    ssq = db.Column(db.String(7))  # 所属期(yyyy-MM)
    szmc = db.Column(db.String(50))  # 税种名称
    sbje = db.Column(db.Float)  # 申报金额(元)
    ynse = db.Column(db.Float)  # 应纳税额(元)
    yjnse = db.Column(db.Float)  # 应缴纳税额(元)
    sjse = db.Column(db.Float)  # 实缴税额(元)
    sbzt = db.Column(db.Integer)  # 申报状态(0:未申报 1:已申报)
    nsrsbh = db.Column(db.String(20))  # 纳税人识别号
    nsrmc = db.Column(db.String(100))  # 纳税人名称
    skssqq = db.Column(db.Date)  # 税款所属期起
    skssqz = db.Column(db.Date)  # 税款所属期止
    sbzl = db.Column(db.String(50))  # 申报种类

class SmallBusinessBalance(db.Model):
    """小企业资产负债表模型"""
    __tablename__ = 'small_business_balance'
    
    id = db.Column(db.Integer, primary_key=True)
    bbq = db.Column(db.String(7))  # 报表期间(yyyy-MM)
    nsrsbh = db.Column(db.String(20))  # 纳税人识别号
    zzcje = db.Column(db.Float)  # 资产总计(元)
    fzcze = db.Column(db.Float)  # 负债总计(元)
    syzqy = db.Column(db.Float)  # 所有者权益(元)
    ldzchj = db.Column(db.Float)  # 流动资产合计(元)
    ldfzhj = db.Column(db.Float)  # 流动负债合计(元)
    gdzcje = db.Column(db.Float)  # 固定资产净值(元)
    ch = db.Column(db.Float)  # 存货(元)
    yszk = db.Column(db.Float)  # 应收账款(元)
    yfzk = db.Column(db.Float)  # 应付账款(元)
    hbzc = db.Column(db.Float)  # 货币资金(元)
    yspj = db.Column(db.Float)  # 应收票据(元)
    qtysk = db.Column(db.Float)  # 其他应收款(元)
    gdzcyz = db.Column(db.Float)  # 固定资产原值(元)
    ljzj = db.Column(db.Float)  # 累计折旧(元)

class SmallBusinessProfit(db.Model):
    """小企业利润表模型"""
    __tablename__ = 'small_business_profit'
    
    id = db.Column(db.Integer, primary_key=True)
    bbq = db.Column(db.String(7))  # 报表期间(yyyy-MM)
    nsrsbh = db.Column(db.String(20))  # 纳税人识别号
    yysr = db.Column(db.Float)  # 营业收入(元)
    yycb = db.Column(db.Float)  # 营业成本(元)
    yylr = db.Column(db.Float)  # 营业利润(元)
    lrze = db.Column(db.Float)  # 利润总额(元)
    jlr = db.Column(db.Float)  # 净利润(元)
    xssr = db.Column(db.Float)  # 销售收入(元)
    yysjjfj = db.Column(db.Float)  # 营业税金及附加(元)
    glfy = db.Column(db.Float)  # 管理费用(元)
    xsjlr = db.Column(db.Float)  # 销售利润(元)
    yyfy = db.Column(db.Float)  # 营业费用(元)
    cbfy = db.Column(db.Float)  # 财务费用(元)
    tzzs = db.Column(db.Float)  # 投资损失(元)
    yysrzk = db.Column(db.Float)  # 营业外收入(元)
    yywzc = db.Column(db.Float)  # 营业外支出(元)

class SmallBusinessCashflow(db.Model):
    """小企业现金流量表模型"""
    __tablename__ = 'small_business_cashflow'
    
    id = db.Column(db.Integer, primary_key=True)
    bbq = db.Column(db.String(7))  # 报表期间(yyyy-MM)
    nsrsbh = db.Column(db.String(20))  # 纳税人识别号
    jyhdxjje = db.Column(db.Float)  # 经营活动现金净额(元)
    tzhdxjje = db.Column(db.Float)  # 投资活动现金净额(元)
    czhdxjje = db.Column(db.Float)  # 筹资活动现金净额(元)
    xjxjje = db.Column(db.Float)  # 现金净增加额(元)
    jyhdxjlr = db.Column(db.Float)  # 经营活动现金流入(元)
    jyhdxjlc = db.Column(db.Float)  # 经营活动现金流出(元)
    qmxjyye = db.Column(db.Float)  # 期末现金余额(元)
    cqqmye = db.Column(db.Float)  # 期初余额(元)
    tzhdxjlr = db.Column(db.Float)  # 投资活动现金流入(元)
    tzhdxjlc = db.Column(db.Float)  # 投资活动现金流出(元)
    czhdxjlr = db.Column(db.Float)  # 筹资活动现金流入(元)
    czhdxjlc = db.Column(db.Float)  # 筹资活动现金流出(元)
    xjdyxj = db.Column(db.Float)  # 现金等价物净增加额(元)
