# 抖音视频数据获取插件

这是一个用于Coze IDE的插件，可以获取抖音视频的详细统计数据，包括点赞数、播放数、评论数等信息。

## 功能特性

- 获取抖音视频的基本信息（标题、创建时间、封面等）
- 获取视频统计数据（点赞数、播放数、评论数、分享数等）
- 支持批量查询多个视频
- 返回格式化的JSON数据

## 安装步骤

### 1. 准备工作

在开始之前，您需要：

1. **获取抖音开放平台账号**
   - 访问 [抖音开放平台](https://developer.open-douyin.com/)
   - 注册并创建应用
   - 获取 `Client Key` 和 `Client Secret`

2. **完成授权配置**
   - 在抖音开放平台配置应用权限
   - 获取用户的 `open_id`
   - 完成经营关系授权

### 2. 安装依赖

在插件目录下运行以下命令安装Python依赖：

```bash
pip3 install -r requirements.txt
```

或者单独安装每个依赖：

```bash
pip3 install requests>=2.28.0
pip3 install urllib3>=1.26.0
pip3 install json5>=0.9.0
```

### 3. 在Coze IDE中配置插件

1. **打开Coze IDE**
   - 访问 [Coze IDE](https://www.coze.cn/open/docs/guides/ide)
   - 登录您的账号

2. **创建新插件**
   - 在IDE中选择"创建插件"
   - 选择"API插件"类型

3. **上传插件文件**
   - 将整个 `douyin-video-plugin` 文件夹上传到Coze IDE
   - 确保包含以下文件：
     - `plugin.json` (插件配置文件)
     - `main.py` (主程序文件)
     - `requirements.txt` (依赖文件)
     - `README.md` (说明文档)

4. **配置插件参数**
   - 在插件配置界面设置以下参数：
     - `api_key`: 您的抖音开放平台Client Key
     - `client_secret`: 您的抖音开放平台Client Secret
     - `open_id`: 目标用户的唯一标识符
     - `video_ids`: 要查询的视频ID列表

## 使用方法

### 参数说明

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `api_key` | string | 是 | 抖音开放平台的Client Key |
| `client_secret` | string | 是 | 抖音开放平台的Client Secret |
| `open_id` | string | 是 | 用户的唯一标识符 |
| `video_ids` | array | 是 | 要查询的视频ID列表 |

### 输入示例

```json
{
  "api_key": "your_client_key_here",
  "client_secret": "your_client_secret_here", 
  "open_id": "ba253642-0590-40bc-9bdf-9a1334b94059",
  "video_ids": ["@9VwFxf*****", "@8hxdhauTCMppanGnM4ltGM780mDqPP+KPpR0qQOmLVAXb/T060zdRmYqig357zEBq6CZRp4NVe6qLIJW/V/x1w=="]
}
```

### 输出示例

```json
{
  "success": true,
  "error": null,
  "data": {
    "total_videos": 1,
    "videos": [
      {
        "video_id": "@8hxdhauTCMppanGnM4ltGM780mDqPP+KPpR0qQOmLVAXb/T060zdRmYqig357zEBq6CZRp4NVe6qLIJW/V/x1w==",
        "title": "测试视频 #测试话题 @抖音小助手",
        "create_time": 1571075129,
        "video_status": 5,
        "share_url": "https://www.iesdouyin.com/share/video/...",
        "cover": "https://p3-dy.byteimg.com/img/tos-cn-p-0015/...",
        "is_top": false,
        "is_reviewed": true,
        "media_type": 2,
        "statistics": {
          "点赞数": 200,
          "下载数": 10,
          "播放数": 300,
          "分享数": 10,
          "转发数": 10,
          "评论数": 100
        }
      }
    ],
    "log_id": "20230213140437EEEDFAB3025AEA105C06"
  }
}
```

## 错误处理

插件会返回详细的错误信息，常见错误包括：

- **参数错误**: 缺少必需参数或参数格式不正确
- **认证错误**: API密钥无效或权限不足
- **网络错误**: 请求超时或网络连接问题
- **API错误**: 抖音API返回的业务错误

错误响应格式：

```json
{
  "success": false,
  "error": "错误描述信息",
  "data": null
}
```

## 注意事项

1. **权限要求**
   - 需要完成抖音开放平台的应用审核
   - 需要获取"视频数据查询"权限
   - 需要完成用户的经营关系授权

2. **API限制**
   - 遵守抖音开放平台的API调用频率限制
   - 只能查询公开视频的数据
   - 隐私视频会返回创建时间为0的记录

3. **数据时效性**
   - 返回的数据是实时的
   - 统计数据可能存在延迟

## 技术支持

如果您在使用过程中遇到问题，请：

1. 检查参数配置是否正确
2. 确认抖音开放平台权限是否完整
3. 查看错误日志获取详细信息
4. 参考抖音开放平台官方文档

## 版本信息

- 版本: 1.0.0
- Python版本要求: Python 3.6+
- 依赖库: requests, urllib3, json5

## 许可证

本插件仅供学习和研究使用，请遵守抖音开放平台的使用条款。