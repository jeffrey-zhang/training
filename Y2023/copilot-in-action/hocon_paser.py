# script to paser and mutate HOCON file: https://github.com/vesoft-inc/nebula-algorithm/blob/master/nebula-algorithm/src/main/resources/application.conf

# 使用 Pyhocon 库解析 HOCON 文件

from pyhocon import ConfigFactory

# 读取 HOCON 文件
config = ConfigFactory.parse_file("application.conf")

# 改写 HOCON 文件中的参数
config["algorithm"]["executeAlgo"] = "Jeffrey"
