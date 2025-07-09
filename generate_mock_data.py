import random
from datetime import datetime, timedelta
from faker import Faker
from tqdm import tqdm
from models import (
    db, TaxRegistration, TaxCredit, TaxPenalty,
    TaxChange, TaxDeclaration, SmallBusinessBalance,
    SmallBusinessProfit, SmallBusinessCashflow
)

fake = Faker('zh_CN')

industries = [
    "制造业", "批发和零售业", "建筑业", "交通运输业", 
    "住宿和餐饮业", "信息传输业", "金融业", "房地产业",
    "租赁和商务服务业", "科学研究和技术服务业"
]

tax_authorities = [
    "国家税务总局北京市税务局",
    "国家税务总局上海市税务局",
    "国家税务总局广州市税务局",
    "国家税务总局深圳市税务局",
    "国家税务总局杭州市税务局"
]

tax_types = [
    "增值税", "企业所得税", "个人所得税", 
    "消费税", "城市维护建设税", "房产税",
    "印花税", "土地增值税", "车船税"
]

credit_levels = ["A", "B", "C", "D", "M"]
credit_level_names = ["优秀", "良好", "一般", "较差", "未评价"]

def generate_tax_id():
    return str(random.randint(91000000, 91999999))

def random_date(start_date, end_date):
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

def generate_tax_registration():
    reg_date = random_date(datetime(2010, 1, 1), datetime(2023, 12, 31))
    return TaxRegistration(
        nsrmc=fake.company(),
        nsrsbh=generate_tax_id(),
        djlx=random.choice([1, 2]),
        djrq=reg_date,
        hy=random.choice(industries),
        zcdz=fake.address(),
        scjydz=fake.address(),
        swjg=random.choice(tax_authorities),
        fddbr=fake.name(),
        zcrq=reg_date - timedelta(days=random.randint(1, 365)),
        zczb=round(random.uniform(10, 10000), 2),
        yyqx=f"{reg_date.year + random.randint(1, 20)}年",
        zzjgdm=str(random.randint(10000000, 99999999)),
        swdjzh=f"SW{random.randint(10000000, 99999999)}"
    )

def generate_tax_credit(nsrmc, nsrsbh):
    year = random.randint(2018, 2023)
    xyjb = random.choice(credit_levels)
    sftb = random.choice([0, 1])
    return TaxCredit(
        nsrmc=nsrmc,
        nsrsbh=nsrsbh,
        pjjg=random.choice(tax_authorities),
        pjnd=str(year),
        xyjb=xyjb,
        xyjbmc=credit_level_names[credit_levels.index(xyjb)],
        xyjf=random.randint(60, 100) if xyjb in ["A", "B", "C"] else None,
        xyjbdj=f"{xyjb}级",
        bzyy=None if xyjb != "M" else random.choice(["新设立企业", "评价年度内无生产经营业务收入", "其他原因"]),
        pjsj=datetime(year, 12, 31),
        sftb=sftb,
        fpsm=None if sftb == 0 else random.choice(["纳税人申请复评", "税务机关发起复评"])
    )

def generate_tax_penalty(nsrsbh):
    penalty_date = random_date(datetime(2018, 1, 1), datetime(2023, 12, 31))
    return TaxPenalty(
        wfxwmc=random.choice([
            "未按规定期限办理纳税申报",
            "虚假纳税申报",
            "逃避缴纳税款",
            "发票违法",
            "其他税收违法行为"
        ]),
        cfjdrq=penalty_date,
        cfjds=f"税罚〔{penalty_date.year}〕{random.randint(100, 999)}号",
        cfyj="《中华人民共和国税收征收管理法》第六十二条",
        cfnr=f"罚款人民币{random.randint(1000, 50000)}元",
        cfjg=random.choice(tax_authorities),
        wfxwlx=random.choice(["申报违法", "发票违法", "其他"]),
        cfje=round(random.uniform(1000, 50000), 2),
        frdb=fake.name(),
        nsrsbh=nsrsbh,
        wfssrq=penalty_date - timedelta(days=random.randint(30, 365)),
        cfzt=random.choice([0, 1])
    )

def generate_tax_change(nsrmc, nsrsbh):
    change_date = random_date(datetime(2018, 1, 1), datetime(2023, 12, 31))
    change_item = random.choice([
        "法定代表人变更", "注册资本变更",
        "经营范围变更", "注册地址变更", "企业名称变更"
    ])
    if change_item == "法定代表人变更":
        old = fake.name()
        new = fake.name()
    elif change_item == "注册资本变更":
        old = f"{random.randint(10, 1000)}万元"
        new = f"{random.randint(10, 1000)}万元"
    else:
        old = fake.address() if "地址" in change_item else fake.company()
        new = fake.address() if "地址" in change_item else fake.company()
    return TaxChange(
        bgxm=change_item,
        bgrq=change_date,
        bgqnr=old,
        bghnr=new,
        bgyy=random.choice(["经营需要", "股东变更", "其他原因"]),
        nsrsbh=nsrsbh,
        nsrmc=nsrmc,
        swjg=random.choice(tax_authorities),
        bgr=fake.name(),
        bglx=1 if change_item in ["法定代表人变更", "企业名称变更"] else 2,
        djbh=f"BG{random.randint(100000, 999999)}"
    )

def generate_tax_declaration(nsrmc, nsrsbh):
    year = random.randint(2018, 2023)
    month = random.randint(1, 12)
    declare_date = datetime(year, month, random.randint(1, 28))
    tax_type = random.choice(tax_types)
    sbje = round(random.uniform(1000, 100000), 2)
    return TaxDeclaration(
        sbrq=declare_date,
        ssq=f"{year}-{month:02d}",
        szmc=tax_type,
        sbje=sbje,
        ynse=round(sbje * random.uniform(0.8, 1.2), 2),
        yjnse=round(sbje * random.uniform(0.9, 1.1), 2),
        sjse=round(sbje * random.uniform(0.95, 1.0), 2),
        sbzt=1,
        nsrsbh=nsrsbh,
        nsrmc=nsrmc,
        skssqq=datetime(year, month, 1),
        skssqz=datetime(year, month, 28),
        sbzl=random.choice(["月度申报", "季度申报", "年度申报"])
    )

def generate_small_business_finance(nsrsbh):
    year = random.randint(2018, 2023)
    month = random.randint(1, 12)
    report_date = f"{year}-{month:02d}"

    # 资产负债表数据
    hbzc = round(random.uniform(10000, 500000), 2)
    yspj = round(random.uniform(5000, 200000), 2)
    qtysk = round(random.uniform(5000, 100000), 2)
    ch = round(random.uniform(10000, 300000), 2)
    gdzcyz = round(random.uniform(50000, 500000), 2)
    ljzj = round(random.uniform(10000, 100000), 2)
    yszk = round(random.uniform(10000, 200000), 2)
    yfzk = round(random.uniform(10000, 200000), 2)

    ldzchj = round(hbzc + yspj + qtysk + ch + yszk, 2)
    ldfzhj = round(yfzk + random.uniform(5000, 100000), 2)
    gdzcje = round(gdzcyz - ljzj, 2)
    zzcje = round(ldzchj + gdzcje, 2)
    fzcze = round(ldfzhj + random.uniform(5000, 100000), 2)
    syzqy = round(zzcje - fzcze, 2)

    balance = SmallBusinessBalance(
        bbq=report_date,
        nsrsbh=nsrsbh,
        hbzc=hbzc, yspj=yspj, qtysk=qtysk, ch=ch, gdzcyz=gdzcyz,
        ljzj=ljzj, yszk=yszk, yfzk=yfzk,
        ldzchj=ldzchj, ldfzhj=ldfzhj,
        gdzcje=gdzcje, zzcje=zzcje, fzcze=fzcze, syzqy=syzqy
    )

    # 利润表数据
    xssr = round(random.uniform(100000, 1000000), 2)
    yysr = round(xssr * random.uniform(0.9, 1.1), 2)
    yycb = round(yysr * random.uniform(0.4, 0.7), 2)
    yysjjfj = round(yysr * random.uniform(0.05, 0.1), 2)
    glfy = round(yysr * random.uniform(0.05, 0.1), 2)
    yyfy = round(yysr * random.uniform(0.03, 0.08), 2)
    cbfy = round(yysr * random.uniform(0.01, 0.05), 2)
    yylr = round(yysr - yycb - yysjjfj - glfy - yyfy - cbfy, 2)
    yysrzk = round(random.uniform(0, 50000), 2)
    yywzc = round(random.uniform(0, 30000), 2)
    tzzs = round(random.uniform(0, 20000), 2)
    lrze = round(yylr + yysrzk - yywzc - tzzs, 2)
    jlr = round(lrze * 0.75, 2)
    xsjlr = round(xssr - yycb, 2)

    profit = SmallBusinessProfit(
        bbq=report_date,
        nsrsbh=nsrsbh,
        xssr=xssr, yysr=yysr, yycb=yycb, yysjjfj=yysjjfj,
        glfy=glfy, yyfy=yyfy, cbfy=cbfy, yylr=yylr,
        yysrzk=yysrzk, yywzc=yywzc, tzzs=tzzs,
        lrze=lrze, jlr=jlr, xsjlr=xsjlr
    )

    # 现金流量表数据
    jyhdxjlr = round(yysr * random.uniform(0.8, 1.2), 2)
    jyhdxjlc = round(jyhdxjlr * random.uniform(0.7, 0.9), 2)
    jyhdxjje = round(jyhdxjlr - jyhdxjlc, 2)
    tzhdxjlr = round(random.uniform(0, 100000), 2)
    tzhdxjlc = round(random.uniform(0, 150000), 2)
    tzhdxjje = round(tzhdxjlr - tzhdxjlc, 2)
    czhdxjlr = round(random.uniform(0, 200000), 2)
    czhdxjlc = round(random.uniform(0, 100000), 2)
    czhdxjje = round(czhdxjlr - czhdxjlc, 2)
    cqqmye = round(random.uniform(10000, 50000), 2)
    xjxjje = round(jyhdxjje + tzhdxjje + czhdxjje, 2)
    qmxjyye = round(cqqmye + xjxjje, 2)
    xjdyxj = round(xjxjje * random.uniform(0.9, 1.1), 2)

    cashflow = SmallBusinessCashflow(
        bbq=report_date,
        nsrsbh=nsrsbh,
        jyhdxjlr=jyhdxjlr, jyhdxjlc=jyhdxjlc, jyhdxjje=jyhdxjje,
        tzhdxjlr=tzhdxjlr, tzhdxjlc=tzhdxjlc, tzhdxjje=tzhdxjje,
        czhdxjlr=czhdxjlr, czhdxjlc=czhdxjlc, czhdxjje=czhdxjje,
        cqqmye=cqqmye, xjxjje=xjxjje, qmxjyye=qmxjyye, xjdyxj=xjdyxj
    )

    return balance, profit, cashflow

def generate_all_data():
    print("开始生成模拟数据...\n")

    registrations = []
    for _ in tqdm(range(100), desc="生成税务登记信息"):
        reg = generate_tax_registration()
        registrations.append(reg)
        db.session.add(reg)

    db.session.commit()

    for reg in tqdm(registrations, desc="生成纳税人数据"):
        for _ in range(random.randint(1, 3)):
            db.session.add(generate_tax_credit(reg.nsrmc, reg.nsrsbh))
        if random.random() < 0.7:
            for _ in range(random.randint(0, 2)):
                db.session.add(generate_tax_penalty(reg.nsrsbh))
        for _ in range(random.randint(0, 3)):
            db.session.add(generate_tax_change(reg.nsrmc, reg.nsrsbh))
        for _ in range(random.randint(12, 36)):
            db.session.add(generate_tax_declaration(reg.nsrmc, reg.nsrsbh))
        for _ in range(random.randint(12, 36)):
            balance, profit, cashflow = generate_small_business_finance(reg.nsrsbh)
            db.session.add(balance)
            db.session.add(profit)
            db.session.add(cashflow)
        db.session.commit()

    print("\n模拟数据生成完成!")

if __name__ == '__main__':
    from app import create_app
    app = create_app()
    with app.app_context():
        generate_all_data()