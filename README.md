# Heatwave Plugin

**Author:** qiaofei  
**Version:** 0.0.2  
**Type:** tool

## Description
Heatwave is a powerful trending topics aggregator plugin for Dify that collects and displays real-time hot topics from major Chinese social media and content platforms. Currently supports Weibo, Zhihu, WeChat, Douyin, and Baidu.

## Features
- Real-time trending topics aggregation
- Multi-platform support (Weibo, Zhihu, WeChat, Douyin, Baidu)
- Structured data output in markdown format
- Customizable platform selection
- Clean and user-friendly display format

## Installation
```bash
# Install required dependencies
pip install -r requirements.txt
```

## Usage
```python
from plugins.dify.heatwave.tools.heatwave import HeatwaveTool

# Initialize the tool
tool = HeatwaveTool()

# Get trending topics from all supported platforms
results = tool._invoke({})

# Get trending topics from specific platforms
results = tool._invoke({
    'platforms': ['微博', '知乎']
})
```

## Configuration
No additional configuration required. The plugin works out of the box with default settings.

## API Rate Limits
- Recommended to maintain reasonable request intervals
- Follow each platform's API usage guidelines
- Default cache time: 5 minutes

## Output Format
The plugin returns data in markdown format:
```markdown
# Today's Trending Topics

## Platform Name
1. [Topic Title](Topic URL)
2. [Topic Title](Topic URL)
...
```

## Dependencies
- Python 3.12+
- requests
- beautifulsoup4

## Privacy & Security
- Only collects publicly available data
- No user data collection or storage
- Complies with platform terms of service
- For detailed privacy information, see [PRIVACY.md](PRIVACY.md)

## Contributing
Please read [DEVELOPER_GUIDELINES.md](DEVELOPER_GUIDELINES.md) for details on our code of conduct and the process for submitting pull requests.

## License
MIT License

## Contact
- Email: qiaofei9@foxmail.com
- Issues: Please submit via GitHub Issues



