<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="css/homePage.css">
    <script src="https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>
    <script src="js/HomePage.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript" src=" https://cdn.staticfile.org/echarts/4.3.0/echarts.min.js"></script>
    <title>HomePage</title>
<body>
<div id="container">

    <div id="d1">
        <div class="tab">
            <ul class="title">
                <span>self service</span>
                <ul>
                    <li class="active"><a href="#">Account Mgmt</a></li>
                    <li><a href="#">Password</a></li>
                </ul>
                <span>Report</span>
                <ul>
                    <li><a href="#">Auto</a></li>
                    <li><a href="#">Manual</a></li>
                    <li><a href="#">Chart</a></li>
                </ul>
                </li>
            </ul>
        </div>

    </div>

    <div id="d2">
        <div id="content">
            <div class="mod">
                <div id="d3">
                    <div style="margin: 0.625rem;">
                        <span style="font-size: large;" >UserName:</span>
                        <input style="width:25rem;height:1.875rem;" placeholder="请输入搜索内容" type="text" name="search" id="search">
                        <button style="width:5rem;height:2.2rem ;"><span style="font-size: large;">search</span></button>
                    </div>
                </div>
                <table id="table" style="margin-left: 2rem;" border="1px" width="760px" >
                    <tr>
                        <td>ID</td>
                        <td>name</td>
                        <td>total</td>
                        <td>Automation</td>
                        <td>manaul</td>
                        <td>Admin</td>
                    </tr>
                </table>
            </div>
            <div class="mod" style="display: none">
                <h1>修改密码</h1>
                <form style="margin-top: 10%;margin-left: 15%;">
                    <table>
                        <tr>
                            <td style="text-align: right">原密码：</td>
                            <td><input type="password"></td>
                            <td></td>
                        </tr>
                        <tr>
                            <td style="text-align: right;">新密码：</td>
                            <td><input type="password"></td>
                            <td></td>
                        </tr>
                        <tr>
                            <td style="text-align: right;">确认新密码：</td>
                            <td><input type="password"></td>
                            <td></td>
                        </tr>
                        <tr>
                            <td></td>
                            <td>
                                <button type="submit">确认修改</button>
                                <button type="reset" style="width: 50%;" >重置</button>
                            </td>
                        </tr>
                    </table>
                </form>

            </div>
            <div class="mod" style="display: none">
                <span>关于automation 的report</span>
            </div>
            <div class="mod" style="display: none">
                <span>关于manual的report</span>
            </div>
            <div class="mod" style="display: none">
                <div>
                    <div id="chart_div"></div>
                </div>
                <div id="main" style="width: 600px;height:400px;"></div>
                <div id="main1" style="width: 600px;height:400px;"></div>
                <script type="text/javascript">
                    // 基于准备好的dom，初始化echarts实例
                    var myChart = echarts.init(document.getElementById('main'));

                    // 指定图表的配置项和数据
                    var option = {
                        title: {
                            text: 'ECharts 入门示例'
                        },
                        tooltip: {},
                        legend: {
                            data:['销量']
                        },
                        xAxis: {
                            data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
                        },
                        yAxis: {},
                        series: [{
                            name: '销量',
                            type: 'bar',
                            data: [5, 20, 36, 10, 10, 20]
                        }]
                    };

                    // 使用刚指定的配置项和数据显示图表。
                    myChart.setOption(option);

                    echarts.init(document.getElementById('main1')).setOption({
                        series: {
                            type: 'pie',
                            data: [
                                {name: 'testA', value: 1212},
                                {name: 'testB', value: 2323},
                                {name: 'testC', value: 1919}
                            ]
                        }
                    });
                </script>
                <!-- <div id="chart_div1" style="float: left;"></div> -->
            </div>
        </div>


    </div>
</div>
</body>
</html>