from app import create_app, db
from models import TaxRegistration, TaxCredit
from datetime import datetime

def init_test_data():
    """初始化测试数据"""
    # 税务登记信息
    reg1 = TaxRegistration(
        nsrmc="测试企业1",
        nsrsbh="91310101MA1FPX1234",
        djlx=1,
        djrq=datetime.strptime("2020-01-15", "%Y-%m-%d"),
        hy="信息技术服务",
        zcdz="上海市浦东新区张江高科技园区",
        scjydz="上海市浦东新区张江高科技园区",
        swjg="上海市浦东新区税务局",
        fddbr="张三",
        zcrq=datetime.strptime("2019-12-01", "%Y-%m-%d"),
        zczb=500.0,
        yyqx="2020-01-01至2030-12-31",
        zzjgdm="12345678",
        swdjzh="沪税浦字123456"
    )
    
    reg2 = TaxRegistration(
        nsrmc="测试企业2",
        nsrsbh="91310101MA1FPX5678",
        djlx=1,
        djrq=datetime.strptime("2021-03-20", "%Y-%m-%d"),
        hy="电子商务",
        zcdz="上海市徐汇区漕河泾开发区",
        scjydz="上海市徐汇区漕河泾开发区",
        swjg="上海市徐汇区税务局",
        fddbr="李四",
        zcrq=datetime.strptime("2020-11-15", "%Y-%m-%d"),
        zczb=200.0,
        yyqx="2021-01-01至2031-12-31",
        zzjgdm="87654321",
        swdjzh="沪税徐字654321"
    )
    
    # 纳税信用信息
    credit1 = TaxCredit(
        nsrmc="测试企业1",
        nsrsbh="91310101MA1FPX1234",
        pjjg="上海市税务局",
        pjnd="2020",
        xyjb="A",
        xyjbmc="A级",
        xyjf=95,
        xyjbdj="优秀",
        pjsj=datetime.strptime("2021-04-15", "%Y-%m-%d"),
        sftb=0
    )
    
    credit2 = TaxCredit(
        nsrmc="测试企业2",
        nsrsbh="91310101MA1FPX5678",
        pjjg="上海市税务局",
        pjnd="2020",
        xyjb="B",
        xyjbmc="B级",
        xyjf=85,
        xyjbdj="良好",
        pjsj=datetime.strptime("2021-04-15", "%Y-%m-%d"),
        sftb=0
    )
    
    db.session.add_all([reg1, reg2, credit1, credit2])
    db.session.commit()

if __name__ == '__main__':
    app = create_app('development')
    with app.app_context():
        # 创建所有表
        db.create_all()
        # 初始化测试数据
        init_test_data()
    print("数据库初始化完成!")
