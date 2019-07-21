# dancing-commits

dancing-commits 只是用来玩儿的!!! 它能以一些简单的文字或随机生成git的提交记录

如下所示

## 示例
### 生成随机提交记录
```Bash
dancing --repo ./example-repo
```

### 生成文字样式的提交记录
```Bash
dancing --repo ./example-repo --mode=text --text='abcdefg'
```


## 参数说明
```Bash
--repo  # 指定git仓库目录, 如果没有会自动创建, 如果有会在其基础上生成新的提交记录
--mode  # 默认为random, 随机生成, 还可以为text, 指定文字
--text  # 如果--mode为text, 则--text必须指定
--year  # 指定提交的年份, 如果不指定, 指最近一整年, 例如, 当时日期为2019.07.21, 则起始日期为2018.07.22
        # 与github中的 x contributions in the last year中的起始日期和结束日期保持一致
--font  # 字体, 如果非ascii字符(如中文), 必须要指定, 但由于像素限制, 复杂字符显示会失真
```
