# GoogleDorkScan
一款自动化进行googledork的工具，帮助测试人员迅速进行敏感信息收集

## Features
![](https://qiniu.xxf.world/pic/2024/04/06/3a679188-f4a4-4058-9136-6c2e4ba5e32b.png)
---
- [x] 参数检查
- [x] 日志记录
- [x] 自定义dork语法
- [x] 自定义全局代理
- [ ] 结果写入文件

## usage
```
 Example:
    python3 googledorkscan.py --target example.com run
    python3 googledorkscan.py --target example.com --proxy http://127.0.0.1:7890 run

Note:
    --target        target domain, dork is site:target(required)
    --delay         every query delay, default is 10 seconds
    --pagesize      the number of URLs in each query result, default is 5
    --proxy         http proxy, not support socks, default is none

```

## Thanks
感谢以下开源项目

https://github.com/MarioVilas/googlesearch

https://github.com/IvanGlinkin/Fast-Google-Dorks-Scan