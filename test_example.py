#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
抖音视频数据获取插件测试示例
用于测试插件功能是否正常
"""

import json
import sys
import os

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import DouyinVideoPlugin

def test_plugin():
    """测试插件功能"""
    
    # 测试参数（请替换为您的实际参数）
    test_params = {
        "api_key": "your_client_key_here",  # 替换为您的Client Key
        "client_secret": "your_client_secret_here",  # 替换为您的Client Secret
        "open_id": "your_open_id_here",  # 替换为用户的open_id
        "video_ids": ["your_video_id_here"]  # 替换为实际的视频ID
    }
    
    print("=== 抖音视频数据获取插件测试 ===\n")
    
    # 检查参数是否已配置
    if any(value.startswith("your_") for value in test_params.values() if isinstance(value, str)):
        print("⚠️  请先在test_example.py中配置您的实际参数：")
        print("   - api_key: 抖音开放平台的Client Key")
        print("   - client_secret: 抖音开放平台的Client Secret") 
        print("   - open_id: 用户的唯一标识符")
        print("   - video_ids: 要查询的视频ID列表")
        print("\n配置完成后再运行此测试脚本。")
        return
    
    try:
        # 创建插件实例
        plugin = DouyinVideoPlugin(
            test_params["api_key"], 
            test_params["client_secret"]
        )
        
        print("✅ 插件实例创建成功")
        
        # 查询视频数据
        print("🔍 正在查询视频数据...")
        result = plugin.query_video_data(
            test_params["open_id"], 
            test_params["video_ids"]
        )
        
        # 输出结果
        print("\n📊 查询结果：")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        
        # 分析结果
        if result["success"]:
            video_count = result["data"]["total_videos"]
            print(f"\n✅ 查询成功！共获取到 {video_count} 个视频的数据")
            
            for i, video in enumerate(result["data"]["videos"], 1):
                print(f"\n📹 视频 {i}:")
                print(f"   标题: {video['title']}")
                print(f"   播放数: {video['statistics']['播放数']}")
                print(f"   点赞数: {video['statistics']['点赞数']}")
                print(f"   评论数: {video['statistics']['评论数']}")
        else:
            print(f"\n❌ 查询失败: {result['error']}")
            
    except Exception as e:
        print(f"\n❌ 测试过程中发生错误: {str(e)}")

def test_input_format():
    """测试标准输入格式（模拟Coze IDE调用方式）"""
    
    print("\n=== 测试标准输入格式 ===\n")
    
    # 模拟Coze IDE传入的JSON数据
    test_input = {
        "api_key": "your_client_key_here",
        "client_secret": "your_client_secret_here",
        "open_id": "your_open_id_here", 
        "video_ids": ["your_video_id_here"]
    }
    
    print("📝 模拟输入数据:")
    print(json.dumps(test_input, ensure_ascii=False, indent=2))
    
    print("\n💡 在Coze IDE中，您需要提供以上格式的JSON数据作为插件输入。")

if __name__ == "__main__":
    # 运行测试
    test_plugin()
    test_input_format()
    
    print("\n" + "="*50)
    print("📚 使用说明:")
    print("1. 请先配置test_example.py中的测试参数")
    print("2. 运行 python3 test_example.py 进行测试")
    print("3. 在Coze IDE中上传插件并配置相应参数")
    print("4. 详细使用方法请参考 README.md 文档")
    print("="*50)