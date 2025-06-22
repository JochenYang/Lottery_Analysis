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

def update_readme_recommendations(recommendations, timestamp, latest_draw=None, total_draws=0):
    """更新README.md文件中的推荐号码和最新开奖信息"""
    print("🔄 开始更新README.md中的推荐号码...")

    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"📖 成功读取README.md文件，大小: {len(content)} 字符")

        # 构建最新开奖信息
        latest_info = ""
        if latest_draw:
            red_balls = " ".join([f"{x:02d}" for x in latest_draw['red_balls']])
            latest_info = f"""
### 📊 最新开奖信息

| 期号 | 开奖日期 | 红球号码 | 蓝球 |
|------|----------|----------|------|
| {latest_draw['period']} | {latest_draw['date']} | `{red_balls}` | `{latest_draw['blue_ball']:02d}` |

**📈 数据统计**: 已收录 {total_draws} 期开奖数据 | 最后更新: {timestamp}

---
"""

        # 构建推荐号码表格
        recommendation_text = f"""### 🎯 智能推荐号码

**⚠️ 以下推荐基于历史统计分析，仅供参考，不保证中奖！**

| 序号 | 推荐类型 | 红球号码 | 蓝球 | 特征分析 |
|------|----------|----------|------|----------|"""

        for i, rec in enumerate(recommendations, 1):
            # 适配不同的推荐数据格式
            if 'red_balls' in rec:
                # lottery_analyzer.py格式
                red_str = " ".join([f"{x:02d}" for x in rec['red_balls']])
                blue_ball = f"{rec['blue_ball']:02d}"
                rec_type = rec.get('strategy', '智能推荐')
                description = rec.get('description', '基于统计分析')
                odds_evens = rec.get('odd_even', '')
                sum_val = rec.get('sum', 0)
                span_val = rec.get('span', 0)
            else:
                # main.py原格式
                red_str = rec.get('numbers', '')
                blue_ball = rec.get('blue', '01')
                rec_type = rec.get('type', '智能推荐')
                description = rec.get('description', '基于统计分析')
                odds_evens = rec.get('odds_evens', '')
                sum_val = rec.get('sum_val', 0)
                span_val = rec.get('span', 0)

            feature_text = f"{odds_evens} \\| 和值:{sum_val} \\| 跨度:{span_val}"
            recommendation_text += f"\n| {i} | {rec_type} | `{red_str}` | `{blue_ball}` | {description}<br/>{feature_text} |"

        # 添加说明信息
        recommendation_text += f"""

**🎲 温馨提示**:
- 📊 推荐基于 {total_draws} 期历史数据统计分析
- 🎯 采用多种策略组合，提高号码覆盖面
- ⚠️ 彩票具有随机性，请理性购彩，适度娱乐"""

        # 组合完整内容
        full_content = latest_info + recommendation_text

        start_marker = '<!-- RECOMMENDATIONS_START -->'
        end_marker = '<!-- RECOMMENDATIONS_END -->'

        start_index = content.find(start_marker)
        end_index = content.find(end_marker)

        if start_index != -1 and end_index != -1:
            print(f"📍 找到推荐号码标记: 开始位置 {start_index}, 结束位置 {end_index}")
            new_content = (
                content[:start_index + len(start_marker)] +
                '\n' + full_content.strip() + '\n' +
                content[end_index:]
            )

            with open('README.md', 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("✅ README.md 中的推荐号码和开奖信息已更新")
            print(f"📝 更新内容长度: {len(full_content)} 字符")
        else:
            print("⚠️  在 README.md 中未找到推荐号码标记")
            print(f"🔍 查找标记: '{start_marker}' 和 '{end_marker}'")

    except Exception as e:
        print(f"❌ 更新README.md失败: {e}")
        import traceback
        print(f"📋 详细错误信息: {traceback.format_exc()}")

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
            return None

        print(f"📊 成功获取 {len(analyzer.lottery_data)} 期开奖数据")

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
        return analyzer  # 返回analyzer实例而不是布尔值

    except Exception as e:
        print(f"❌ 双色球分析出错: {e}")
        import traceback
        print(f"📋 详细错误信息: {traceback.format_exc()}")
        return None



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
    analyzer = run_lottery_analyzer(unified_timestamp)

    # 更新README
    if analyzer is not None:
        print("\n🔄 正在更新 README.md 中的推荐号码...")
        try:
            # 使用已经成功的analyzer实例，避免重新加载数据
            print(f"📊 使用已加载的 {len(analyzer.lottery_data)} 期数据")

            # 生成推荐号码
            recommendations = analyzer.generate_recommendations(num_sets=5)
            print(f"🎯 成功生成 {len(recommendations)} 组推荐号码")

            # 获取最新开奖信息
            latest_draw = analyzer.lottery_data[0] if analyzer.lottery_data else None
            total_draws = len(analyzer.lottery_data)

            # 更新README
            update_readme_recommendations(
                recommendations,
                unified_timestamp,
                latest_draw=latest_draw,
                total_draws=total_draws
            )
            print("✅ README.md 更新成功！")
        except Exception as e:
            print(f"❌ 更新 README.md 失败: {e}")
            import traceback
            print(f"📋 详细错误信息: {traceback.format_exc()}")
    
    # 总结结果
    end_time = time.time()
    duration = end_time - start_time
    current_time = get_current_time_utc8()
    
    print("\n" + "=" * 80)
    print("📊 分析结果总结")
    print("=" * 80)
    lottery_success = analyzer is not None
    print(f"🔴 双色球分析: {'✅ 成功' if lottery_success else '❌ 失败'}")
    if lottery_success:
        print(f"📊 数据期数: {len(analyzer.lottery_data)} 期")
        print(f"📅 最新期号: {analyzer.lottery_data[0]['period'] if analyzer.lottery_data else '无'}")
    print(f"⏱️  总耗时: {duration:.1f} 秒")
    print(f"🕐 完成时间: {current_time} (UTC+8)")

    if lottery_success:
        print("\n📁 生成的文件:")
        print("• data/lottery_data.json - 双色球开奖数据")
        print("• data/lottery_aggregated_data.hjson - 双色球聚合分析数据")
        print("• reports/analysis_report.md - 双色球分析报告")
        print("• pics/lottery_frequency_analysis.png - 双色球频率图表")
        print("• README.md - 项目首页推荐号码（已更新）")

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