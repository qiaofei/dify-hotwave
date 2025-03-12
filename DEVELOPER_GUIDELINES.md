# Heatwave Plugin Developer Guidelines

## Feature Description
Heatwave is a tool-type plugin designed to aggregate trending topics from major platforms. Currently, it supports real-time hot topic retrieval from Weibo, Zhihu, WeChat, Douyin, and Baidu.

## Plugin Value
1. Provides one-stop trending information aggregation service
2. Supports unified access to multiple platform data sources
3. Delivers structured data output
4. Enables real-time updates and customized display

## Privacy and Security
1. This plugin only retrieves publicly accessible trending data
2. Does not collect any user personal information
3. All data comes from public API interfaces
4. Complies with usage terms and API limitations of each platform

## Usage Guidelines
1. Recommended to maintain reasonable API request frequency
2. Comply with relevant platform terms of service
3. Must not be used for illegal or inappropriate purposes
4. Recommend citing data sources in usage instructions

## Technical Requirements
1. Python 3.12 or above
2. Dependencies: requests and beautifulsoup4 libraries
3. Ensure network access to relevant platforms

## Contribution Guidelines
1. Welcome submissions for new platform support
2. Code submissions must pass testing
3. Maintain consistent code style
4. Provide complete documentation 