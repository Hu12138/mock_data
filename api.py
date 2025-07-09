from flask import Blueprint, request, jsonify
from app import db
from models import (
    TaxRegistration, TaxCredit, TaxPenalty, 
    TaxChange, TaxDeclaration, SmallBusinessBalance,
    SmallBusinessProfit, SmallBusinessCashflow
)
from datetime import datetime

api_bp = Blueprint('api', __name__)

def validate_request(required_fields, data):
    """验证请求参数"""
    missing = [field for field in required_fields if field not in data]
    if missing:
        return False, f"缺少必要参数: {', '.join(missing)}"
    return True, ""

@api_bp.route('/TaxOld', methods=['POST'])
def tax_interface():
    """统一税务接口"""
    data = request.get_json()
    
    # 验证请求头
    if 'header' not in data or 'body' not in data:
        return jsonify({
            "status": "error",
            "code": 400,
            "message": "请求格式错误"
        }), 400
        
    header = data['header']
    body = data['body']
    
    # 验证接口标识符
    if 'interface_no' not in header or 'cxName' not in body:
        return jsonify({
            "status": "error",
            "code": 400,
            "message": "缺少接口标识符"
        }), 400
        
    if header['interface_no'] != body['cxName']:
        return jsonify({
            "status": "error",
            "code": 400,
            "message": "接口标识符不匹配"
        }), 400
    
    # 根据接口类型路由到不同处理函数
    interface_no = header['interface_no']
    
    if interface_no == 'api_007_swdjxx':
        return handle_tax_registration(header, body)
    elif interface_no == 'api_007_nsxyxx':
        return handle_tax_credit(header, body)
    elif interface_no == 'api_007_xzcfxx':
        return handle_tax_penalty(header, body)
    elif interface_no == 'api_007_bgdjxx':
        return handle_tax_change(header, body)
    elif interface_no == 'api_007_nssbxx':
        return handle_tax_declaration(header, body)
    elif interface_no in ('api_007_xqyzcfz', 'api_007_xqylr', 'api_007_xqyxjl'):
        return handle_small_business_finance(header, body)
    else:
        return jsonify({
            "status": "error",
            "code": 404,
            "message": "接口不存在"
        }), 404

def handle_tax_registration(header, body):
    """处理税务登记信息查询"""
    # 验证必要参数
    valid, msg = validate_request(['certName', 'certId'], body)
    if not valid:
        return jsonify({
            "status": "error",
            "code": 400,
            "message": msg
        }), 400
    
    # 查询数据库
    records = TaxRegistration.query.filter_by(nsrsbh=body['certId']).all()
    
    if not records:
        return jsonify({
            "header": {
                **header,
                "orgId": "124",
                "unique": "1234567890"
            },
            "body": [],
            "status": "success",
            "code": 404,
            "message": "无数据"
        }), 404
    
    # 格式化响应数据
    response_data = [{
        "nsrmc": record.nsrmc,
        "nsrsbh": record.nsrsbh,
        "djlx": record.djlx,
        "djrq": record.djrq.strftime('%Y-%m-%d') if record.djrq else None,
        "hy": record.hy,
        "zcdz": record.zcdz,
        "scjydz": record.scjydz,
        "swjg": record.swjg,
        "fddbr": record.fddbr,
        "zcrq": record.zcrq.strftime('%Y-%m-%d') if record.zcrq else None,
        "zczb": record.zczb,
        "yyqx": record.yyqx,
        "zzjgdm": record.zzjgdm,
        "swdjzh": record.swdjzh
    } for record in records]
    
    return jsonify({
        "header": {
            **header,
            "orgId": "124",
            "unique": "1234567890"
        },
        "body": response_data,
        "status": "success",
        "code": 200,
        "message": "查询成功"
    })

def handle_tax_credit(header, body):
    """处理纳税信用信息查询"""
    # 验证必要参数
    valid, msg = validate_request(['certName', 'certId', 'nd'], body)
    if not valid:
        return jsonify({
            "status": "error",
            "code": 400,
            "message": msg
        }), 400
    
    # 查询数据库
    records = TaxCredit.query.filter_by(
        nsrsbh=body['certId'],
        pjnd=body['nd']
    ).all()
    
    if not records:
        return jsonify({
            "header": {
                **header,
                "orgId": "124",
                "unique": "1234567890"
            },
            "body": [],
            "status": "success",
            "code": 404,
            "message": "无数据"
        }), 404
    
    # 格式化响应数据
    response_data = [{
        "nsrmc": record.nsrmc,
        "nsrsbh": record.nsrsbh,
        "pjjg": record.pjjg,
        "pjnd": record.pjnd,
        "xyjb": record.xyjb,
        "xyjbmc": record.xyjbmc,
        "xyjf": record.xyjf,
        "xyjbdj": record.xyjbdj,
        "bzyy": record.bzyy,
        "pjsj": record.pjsj.strftime('%Y-%m-%d') if record.pjsj else None,
        "sftb": record.sftb,
        "fpsm": record.fpsm
    } for record in records]
    
    return jsonify({
        "header": {
            **header,
            "orgId": "124",
            "unique": "1234567890"
        },
        "body": response_data,
        "status": "success",
        "code": 200,
        "message": "查询成功"
    })

def handle_tax_penalty(header, body):
    """处理行政处罚信息查询"""
    # 验证必要参数
    valid, msg = validate_request(['certName', 'certId', 'clcfjdrq'], body)
    if not valid:
        return jsonify({
            "status": "error",
            "code": 400,
            "message": msg
        }), 400
    
    # 解析日期范围
    try:
        start_date, end_date = body['clcfjdrq'].split('-')
        start_date = datetime.strptime(start_date.strip(), '%Y/%m/%d').date()
        end_date = datetime.strptime(end_date.strip(), '%Y/%m/%d').date()
    except:
        return jsonify({
            "status": "error",
            "code": 400,
            "message": "日期格式错误，应为yyyy/MM/dd-yyyy/MM/dd"
        }), 400
    
    # 查询数据库
    records = TaxPenalty.query.filter(
        TaxPenalty.nsrsbh == body['certId'],
        TaxPenalty.cfjdrq.between(start_date, end_date)
    ).all()
    
    if not records:
        return jsonify({
            "header": {
                **header,
                "orgId": "124",
                "unique": "1234567890"
            },
            "body": [],
            "status": "success",
            "code": 404,
            "message": "无数据"
        }), 404
    
    # 格式化响应数据
    response_data = [{
        "wfxwmc": record.wfxwmc,
        "cfjdrq": record.cfjdrq.strftime('%Y-%m-%d') if record.cfjdrq else None,
        "cfjds": record.cfjds,
        "cfyj": record.cfyj,
        "cfnr": record.cfnr,
        "cfjg": record.cfjg,
        "wfxwlx": record.wfxwlx,
        "cfje": record.cfje,
        "frdb": record.frdb,
        "nsrsbh": record.nsrsbh,
        "wfssrq": record.wfssrq.strftime('%Y-%m-%d') if record.wfssrq else None,
        "cfzt": record.cfzt
    } for record in records]
    
    return jsonify({
        "header": {
            **header,
            "orgId": "124",
            "unique": "1234567890"
        },
        "body": response_data,
        "status": "success",
        "code": 200,
        "message": "查询成功"
    })

def handle_tax_change(header, body):
    """处理变更登记信息查询"""
    # 验证必要参数
    valid, msg = validate_request(['certName', 'certId', 'bgrq'], body)
    if not valid:
        return jsonify({
            "status": "error",
            "code": 400,
            "message": msg
        }), 400
    
    # 解析日期范围
    try:
        start_date, end_date = body['bgrq'].split('-')
        start_date = datetime.strptime(start_date.strip(), '%Y/%m/%d').date()
        end_date = datetime.strptime(end_date.strip(), '%Y/%m/%d').date()
    except:
        return jsonify({
            "status": "error",
            "code": 400,
            "message": "日期格式错误，应为yyyy/MM/dd-yyyy/MM/dd"
        }), 400
    
    # 查询数据库
    records = TaxChange.query.filter(
        TaxChange.nsrsbh == body['certId'],
        TaxChange.bgrq.between(start_date, end_date)
    ).all()
    
    if not records:
        return jsonify({
            "header": {
                **header,
                "orgId": "124",
                "unique": "1234567890"
            },
            "body": [],
            "status": "success",
            "code": 404,
            "message": "无数据"
        }), 404
    
    # 格式化响应数据
    response_data = [{
        "bgxm": record.bgxm,
        "bgrq": record.bgrq.strftime('%Y-%m-%d') if record.bgrq else None,
        "bgqnr": record.bgqnr,
        "bghnr": record.bghnr,
        "bgyy": record.bgyy,
        "nsrsbh": record.nsrsbh,
        "nsrmc": record.nsrmc,
        "swjg": record.swjg,
        "bgr": record.bgr,
        "bglx": record.bglx,
        "djbh": record.djbh
    } for record in records]
    
    return jsonify({
        "header": {
            **header,
            "orgId": "124",
            "unique": "1234567890"
        },
        "body": response_data,
        "status": "success",
        "code": 200,
        "message": "查询成功"
    })

def handle_tax_declaration(header, body):
    """处理纳税申报信息查询"""
    # 验证必要参数
    valid, msg = validate_request(['certName', 'certId', 'sssqq', 'sssqz'], body)
    if not valid:
        return jsonify({
            "status": "error",
            "code": 400,
            "message": msg
        }), 400
    
    # 解析日期
    try:
        start_date = datetime.strptime(body['sssqq'], '%Y/%m/%d').date()
        end_date = datetime.strptime(body['sssqz'], '%Y/%m/%d').date()
    except:
        return jsonify({
            "status": "error",
            "code": 400,
            "message": "日期格式错误，应为yyyy/MM/dd"
        }), 400
    
    # 查询数据库
    records = TaxDeclaration.query.filter(
        TaxDeclaration.nsrsbh == body['certId'],
        TaxDeclaration.skssqq >= start_date,
        TaxDeclaration.skssqz <= end_date
    ).all()
    
    if not records:
        return jsonify({
            "header": {
                **header,
                "orgId": "124",
                "unique": "1234567890"
            },
            "body": [],
            "status": "success",
            "code": 404,
            "message": "无数据"
        }), 404
    
    # 格式化响应数据
    response_data = [{
        "sbrq": record.sbrq.strftime('%Y-%m-%d') if record.sbrq else None,
        "ssq": record.ssq,
        "szmc": record.szmc,
        "sbje": record.sbje,
        "ynse": record.ynse,
        "yjnse": record.yjnse,
        "sjse": record.sjse,
        "sbzt": record.sbzt,
        "nsrsbh": record.nsrsbh,
        "nsrmc": record.nsrmc,
        "skssqq": record.skssqq.strftime('%Y-%m-%d') if record.skssqq else None,
        "skssqz": record.skssqz.strftime('%Y-%m-%d') if record.skssqz else None,
        "sbzl": record.sbzl
    } for record in records]
    
    return jsonify({
        "header": {
            **header,
            "orgId": "124",
            "unique": "1234567890"
        },
        "body": response_data,
        "status": "success",
        "code": 200,
        "message": "查询成功"
    })

def handle_small_business_finance(header, body):
    """处理小企业财务报表查询"""
    # 验证必要参数
    valid, msg = validate_request(['certName', 'certId', 'sssqq', 'sssqz'], body)
    if not valid:
        return jsonify({
            "status": "error",
            "code": 400,
            "message": msg
        }), 400
    
    # 解析日期
    try:
        start_date = datetime.strptime(body['sssqq'], '%Y/%m/%d').date()
        end_date = datetime.strptime(body['sssqz'], '%Y/%m/%d').date()
    except:
        return jsonify({
            "status": "error",
            "code": 400,
            "message": "日期格式错误，应为yyyy/MM/dd"
        }), 400
    
    # 根据接口类型确定报表类型
    report_type = header['interface_no'].split('_')[-1]  # xqyzcfz/xqylr/xqyxjl
    
    # 查询数据库
    # 根据报表类型选择对应的模型
    if report_type == 'xqyzcfz':
        model = SmallBusinessBalance
    elif report_type == 'xqylr':
        model = SmallBusinessProfit
    elif report_type == 'xqyxjl':
        model = SmallBusinessCashflow
    else:
        return jsonify({
            "header": {
                **header,
                "orgId": "124",
                "unique": "1234567890"
            },
            "body": [],
            "status": "success",
            "code": 404,
            "message": "无数据"
        }), 404

    records = model.query.filter(
        model.nsrsbh == body['certId'],
        model.bbq.between(
            start_date.strftime('%Y-%m'),
            end_date.strftime('%Y-%m')
        )
    ).all()
    
    if not records:
        return jsonify({
            "header": {
                **header,
                "orgId": "124",
                "unique": "1234567890"
            },
            "body": [],
            "status": "success",
            "code": 404,
            "message": "无数据"
        }), 404
    
    # 格式化响应数据
    response_data = []
    for record in records:
        data = {
            "bbq": record.bbq,
            "nsrsbh": record.nsrsbh
        }
        
        if report_type == 'xqyzcfz':
            # 资产负债表字段
            data.update({
                "zzcje": record.zzcje,
                "fzcze": record.fzcze,
                "syzqy": record.syzqy,
                "ldzchj": record.ldzchj,
                "ldfzhj": record.ldfzhj,
                "gdzcje": record.gdzcje,
                "ch": record.ch,
                "yszk": record.yszk,
                "yfzk": record.yfzk,
                "hbzc": record.hbzc,
                "yspj": record.yspj,
                "qtysk": record.qtysk,
                "gdzcyz": record.gdzcyz,
                "ljzj": record.ljzj
            })
        elif report_type == 'xqylr':
            # 利润表字段
            data.update({
                "yysr": record.yysr,
                "yycb": record.yycb,
                "yylr": record.yylr,
                "lrze": record.lrze,
                "jlr": record.jlr,
                "xssr": record.xssr,
                "yysjjfj": record.yysjjfj,
                "glfy": record.glfy,
                "xsjlr": record.xsjlr,
                "yyfy": record.yyfy,
                "cbfy": record.cbfy,
                "tzzs": record.tzzs,
                "yysrzk": record.yysrzk,
                "yywzc": record.yywzc
            })
        elif report_type == 'xqyxjl':
            # 现金流量表字段
            data.update({
                "jyhdxjje": record.jyhdxjje,
                "tzhdxjje": record.tzhdxjje,
                "czhdxjje": record.czhdxjje,
                "xjxjje": record.xjxjje,
                "jyhdxjlr": record.jyhdxjlr,
                "jyhdxjlc": record.jyhdxjlc,
                "qmxjyye": record.qmxjyye,
                "cqqmye": record.cqqmye,
                "tzhdxjlr": record.tzhdxjlr,
                "tzhdxjlc": record.tzhdxjlc,
                "czhdxjlr": record.czhdxjlr,
                "czhdxjlc": record.czhdxjlc,
                "xjdyxj": record.xjdyxj
            })
        else:
            continue
            
        response_data.append(data)
    
    return jsonify({
        "header": {
            **header,
            "orgId": "124",
            "unique": "1234567890"
        },
        "body": response_data,
        "status": "success",
        "code": 200,
        "message": "查询成功"
    })
