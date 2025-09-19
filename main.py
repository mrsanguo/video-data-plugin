#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
抖音视频数据获取插件
用于获取抖音视频的详细统计数据
"""

import requests
import json
import sys
from typing import Dict, List, Any

class DouyinVideoPlugin:
    """抖音视频数据获取插件类"""
    
    def __init__(self, api_key: str, client_secret: str):
        """
        初始化插件
        
        Args:
            api_key: 抖音开放平台的API密钥
            client_secret: 抖音开放平台的客户端密钥
        """
        self.api_key = api_key
        self.client_secret = client_secret
        self.base_url = "https://open.douyin.com/api/apps/v1/video_bc/query/"
        
    def get_access_token(self, open_id: str) -> str:
        """
        获取访问令牌
        
        Args:
            open_id: 用户的唯一标识符
            
        Returns:
            访问令牌字符串
        """
        # 注意：这里需要根据实际的token获取流程来实现
        # 通常需要通过OAuth流程获取
        return f"bus_act.{self.api_key}"
    
    def query_video_data(self, open_id: str, video_ids: List[str]) -> Dict[str, Any]:
        """
        查询视频数据
        
        Args:
            open_id: 用户的唯一标识符
            video_ids: 视频ID列表
            
        Returns:
            包含视频数据的字典
        """
        try:
            # 获取访问令牌
            access_token = self.get_access_token(open_id)
            
            # 构建请求头
            headers = {
                "access-token": access_token,
                "content-type": "application/json"
            }
            
            # 构建请求参数
            params = {
                "open_id": open_id
            }
            
            # 构建请求体
            data = {
                "item_ids": video_ids
            }
            
            # 发送POST请求
            response = requests.post(
                self.base_url,
                headers=headers,
                params=params,
                json=data,
                timeout=30
            )
            
            # 检查响应状态
            response.raise_for_status()
            
            # 解析响应数据
            result = response.json()
            
            # 检查API响应是否成功
            if result.get("err_no") != 0:
                raise Exception(f"API错误: {result.get('err_msg', '未知错误')}")
            
            return self.format_response(result)
            
        except requests.exceptions.RequestException as e:
            return {
                "success": False,
                "error": f"网络请求错误: {str(e)}",
                "data": None
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"处理错误: {str(e)}",
                "data": None
            }
    
    def format_response(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        格式化响应数据
        
        Args:
            raw_data: 原始API响应数据
            
        Returns:
            格式化后的数据
        """
        try:
            video_list = raw_data.get("data", {}).get("data", {}).get("list", [])
            
            formatted_videos = []
            for video in video_list:
                formatted_video = {
                    "video_id": video.get("item_id", ""),
                    "title": video.get("title", ""),
                    "create_time": video.get("create_time", 0),
                    "video_status": video.get("video_status", 0),
                    "share_url": video.get("share_url", ""),
                    "cover": video.get("cover", ""),
                    "is_top": video.get("is_top", False),
                    "is_reviewed": video.get("is_reviewed", False),
                    "media_type": video.get("media_type", 0),
                    "statistics": {
                        "点赞数": video.get("statistics", {}).get("digg_count", 0),
                        "下载数": video.get("statistics", {}).get("download_count", 0),
                        "播放数": video.get("statistics", {}).get("play_count", 0),
                        "分享数": video.get("statistics", {}).get("share_count", 0),
                        "转发数": video.get("statistics", {}).get("forward_count", 0),
                        "评论数": video.get("statistics", {}).get("comment_count", 0)
                    }
                }
                formatted_videos.append(formatted_video)
            
            return {
                "success": True,
                "error": None,
                "data": {
                    "total_videos": len(formatted_videos),
                    "videos": formatted_videos,
                    "log_id": raw_data.get("log_id", "")
                }
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"数据格式化错误: {str(e)}",
                "data": None
            }

def main():
    """
    插件主函数
    从命令行参数或标准输入获取参数并执行
    """
    try:
        # 从标准输入读取参数（Coze IDE会通过这种方式传递参数）
        input_data = sys.stdin.read()
        params = json.loads(input_data)
        
        # 获取必需参数
        api_key = params.get("api_key")
        client_secret = params.get("client_secret")
        open_id = params.get("open_id")
        video_ids = params.get("video_ids", [])
        
        # 验证参数
        if not api_key:
            raise ValueError("缺少必需参数: api_key")
        if not client_secret:
            raise ValueError("缺少必需参数: client_secret")
        if not open_id:
            raise ValueError("缺少必需参数: open_id")
        if not video_ids:
            raise ValueError("缺少必需参数: video_ids")
        
        # 创建插件实例
        plugin = DouyinVideoPlugin(api_key, client_secret)
        
        # 查询视频数据
        result = plugin.query_video_data(open_id, video_ids)
        
        # 输出结果
        print(json.dumps(result, ensure_ascii=False, indent=2))
        
    except json.JSONDecodeError as e:
        error_result = {
            "success": False,
            "error": f"JSON解析错误: {str(e)}",
            "data": None
        }
        print(json.dumps(error_result, ensure_ascii=False, indent=2))
        
    except Exception as e:
        error_result = {
            "success": False,
            "error": f"执行错误: {str(e)}",
            "data": None
        }
        print(json.dumps(error_result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()