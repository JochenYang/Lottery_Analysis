#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
彩票数据分析统一入口脚本

⚠️  重要免责声明 ⚠️
1. 本脚本仅用于技术学习和数据分析研究目的
2. 彩票开奖结果完全随机，历史数据无法预测未来结果
3. 本分析结果仅供参考，不构成任何投注建议
4. 请理性购彩，量力而行，未满18周岁禁止购买彩票
5. 开发者不承担因使用本脚本产生的任何损失

功能：
1. 统一运行双色球和大乐透数据分析
2. 自动创建必要的目录结构
3. 生成完整的数据文件和分析报告
"""

import os
import sys
import time
from datetime import datetime, timezone, timedelta

sys.path.append('scripts')
from scripts.lottery_analyzer import DoubleColorBallAnalyzer

def create_directories():
    """创建必要的目录结构"""
    directories = ['data', 'reports', 'pics', 'scripts']
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"✅ 创建目录: {directory}/")
        else:
            print(f"📁 目录已存在: {directory}/")

def get_current_time_utc8():
    """获取UTC+8时区的当前时间"""
    utc8_tz = timezone(timedelta(hours=8))
    return datetime.now(utc8_tz).strftime('%Y年%m月%d日 %H:%M:%S')

def show_disclaimer():
    """显示免责声明"""
    print("=" * 80)
    print("🎯 彩票数据分析统一系统")
    print("=" * 80)
    print("⚠️  重要免责声明：")
    print("• 彩票开奖完全随机，历史数据无法预测未来")
    print("• 本分析仅供学习参考，不构成投注建议")
    print("• 请理性购彩，量力而行，未满18周岁禁止购买")
    print("• 使用本软件产生的任何后果由用户自行承担")
    print("=" * 80)

def update_readme_recommendations(recommendations, timestamp):
    """更新README.md文件中的推荐号码"""
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()

        recommendation_text = f"### 双色球推荐 (更新时间: {timestamp})\n\n"
        for i, rec in enumerate(recommendations):
            recommendation_text += f"**推荐 {i+1}** ({rec['type']}): `{rec['numbers']}` + `{rec['blue']}`  \n"
            recommendation_text += f"*{rec['description']} | {rec['odds_evens']} | 和值:{rec['sum_val']} | 跨度:{rec['span']}*\n\n"

        start_marker = '<!-- RECOMMENDATIONS_START -->'
        end_marker = '<!-- RECOMMENDATIONS_END -->'

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)

        if start_index != -1 and end_index != -1:
            new_content = (
                content[:start_index + len(start_marker)] +
                '\n' + recommendation_text.strip() + '\n' +
                content[end_index:]
            )
            
            with open('README.md', 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("✅ README.md 中的推荐号码已更新")
        else:
            print("⚠️  在 README.md 中未找到推荐号码标记")

    except Exception as e:
        print(f"❌ 更新README.md失败: {e}")

def run_lottery_analyzer(unified_timestamp=None):
    """运行双色球分析器"""
    print("\n" + "=" * 60)
    print("🔴 开始运行双色球数据分析...")
    print("=" * 60)
    
    try:
        analyzer = DoubleColorBallAnalyzer()
        
        # 获取最大页数并抓取数据
        max_pages = analyzer.get_max_pages()
        analyzer.fetch_lottery_data(max_pages=max_pages)
        analyzer.save_data()
        
        if not analyzer.lottery_data:
            print("❌ 双色球数据获取失败")
            return False
        
        # 执行分析
        analyzer.analyze_frequency()
        analyzer.analyze_patterns()
        analyzer.analyze_trends()
        analyzer.generate_recommendations(num_sets=8)
        
        # 生成图表和报告
        try:
            analyzer.visualize_frequency()
        except Exception as e:
            print(f"⚠️  双色球图表生成失败: {e}")
        
        analyzer.generate_analysis_report()
        
        # 生成聚合数据文件
        analyzer.generate_aggregated_data_hjson()
        

        
        print("✅ 双色球分析完成！")
        return True
        
    except Exception as e:
        print(f"❌ 双色球分析出错: {e}")
        return False



def main():
    """主函数"""
    start_time = time.time()
    
    # 生成统一的时间戳（UTC+8）
    unified_timestamp = get_current_time_utc8()
    
    # 显示免责声明
    show_disclaimer()
    
    print(f"\n🕐 开始时间: {unified_timestamp} (UTC+8)")
    print("🚀 正在初始化系统...")
    
    # 创建目录结构
    create_directories()
    
    # 运行分析器（传入统一时间戳）
    lottery_success = run_lottery_analyzer(unified_timestamp)
    
    # 更新README
    if lottery_success:
        print("\n🔄 正在更新 README.md 中的推荐号码...")
        try:
            # 重新实例化分析器以获取最新数据
            analyzer = DoubleColorBallAnalyzer()
            analyzer.load_data()
            recommendations = analyzer.generate_recommendations(num_sets=5)
            update_readme_recommendations(recommendations, unified_timestamp)
            print("✅ README.md 更新成功！")
        except Exception as e:
            print(f"❌ 更新 README.md 失败: {e}")
    
    # 总结结果
    end_time = time.time()
    duration = end_time - start_time
    current_time = get_current_time_utc8()
    
    print("\n" + "=" * 80)
    print("📊 分析结果总结")
    print("=" * 80)
    print(f"🔴 双色球分析: {'✅ 成功' if lottery_success else '❌ 失败'}")
    print(f"⏱️  总耗时: {duration:.1f} 秒")
    print(f"🕐 完成时间: {current_time} (UTC+8)")
    
    if lottery_success:
        print("\n📁 生成的文件:")
        print("• data/lottery_data.json - 双色球开奖数据")
        print("• data/lottery_aggregated_data.hjson - 双色球聚合分析数据")
        print("• reports/analysis_report.md - 双色球分析报告")
        print("• pics/lottery_frequency_analysis.png - 双色球频率图表")
    
    print("\n" + "=" * 80)
    print("📋 重要提醒：")
    print("• 以上分析结果基于历史统计，仅供参考")
    print("• 彩票具有偶然性，请勿过度依赖任何预测")
    print("• 理性购彩，适度娱乐，珍惜家庭和睦")
    print("• 如有赌博问题，请寻求专业帮助")
    print("=" * 80)
    
    if lottery_success:
        print("\n🎉 双色球分析任务完成！")
        return 0
    else:
        print("\n⚠️  双色球分析任务失败，请检查网络连接和依赖库")
        return 1

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\n👋 用户中断，程序退出")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 程序运行出错: {e}")
        print("请检查网络连接和依赖库安装情况")
        sys.exit(1)