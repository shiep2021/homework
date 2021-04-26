#### [Home Assistant](https://github.com/home-assistant)

 是一款基于 Python 的智能家居开源系统，支持众多品牌的智能家居设备，可以轻松实现设备的语音控制、自动化等。

#### virtualenv

在开发Python应用程序的时候，系统安装的Python3只有一个版本：3.7。所有第三方的包都会被`pip`安装到Python3的`site-packages`目录下。

如果我们要同时开发多个应用程序，那这些应用程序都会共用一个Python，就是安装在系统的Python 3。如果应用A需要jinja 2.7，而应用B需要jinja 2.6怎么办？

这种情况下，每个应用可能需要各自拥有一套“独立”的Python运行环境。virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境。

##### 安装



```
pip install virtualenv
```

##### 创建

```
#创建目录
mkdir myproject
cd myproject
#创建一个独立的Python运行环境，命名为venv
virtualenv venv1
#进入acetive所在目录
cd venv\Scripts
#启动
active
#关闭
deactivate.bat
```

#### 安装Home Assistant

##### 可能遇到的问题![](.\sources\缺失.png)

[解决方式](https://blog.csdn.net/keeppractice/article/details/115712094)

1、[下载](https://visualstudio.microsoft.com/zh-hans/visual-cpp-build-tools/)

2、安装![](.\sources\安装插件.png)

```
#python 版本<3.7
pip install homeassistant==0.86.2

#正常使用
pip install homeassistant
```

确认

![z](.\sources\确认.png)

##### 启动Home Assitant

```
Desktop\work\myproject\venv\Scripts\activate
hass --open-ui
```

##### 创建用户

![](.\sources\创建用户.png)

##### 时区

![](.\sources\时区.png)



##### 密码遗忘

##### ![](.\sources\遗忘.png)

解决方式——删除.storage 文件夹(C:\Users\SK0509\AppData\Roaming\.homeassistant)

![](.\sources\密码遗忘.png)

#### YAML文件

##### 配置目录（P7）

##### 语法规则（P8）

```
HomeAssistant的配置文件配置规则	：
1、在“#”右边的文字用于注释，不起实际作用。
2、冒号（:）左边的字符串代表配置项的名称，冒号右边是配置项的值。
3、如果冒号右边是空的，那么下一行开始所有比这行缩进（左边多两个空格）的都是这个配置项的值。
4、如果配置项的值以减号（-）开始，代表这个配置项有若干个并列的值（也可能仅并列一个），每个都是以相同缩进的减号开始。
```

##### [修改经纬度](http://map.jiqrxx.com/jingweidu/)

中心点经纬度：30.899483, 121.890045 北纬N：30°53′58.14″ 东经E：121°53′24.16

```
homeassistant:
  latitude: 30.899483
  longitude: 121.890045
  elevation: 0
  unit_system: metric
  time_zone: Asia/Shanghai
  name: EIS
```

![](.\sources\经纬度.png)

修改后重启![](.\sources\重启.png)

![](.\sources\经纬度修改.png)

#### [配置天气](https://www.hachina.io/docs/6743.html)——接入自定义组件

[WinPcap](https://www.winpcap.org/install/default.htm)

[Npcap](https://nmap.org/download.html)

[注册和风天气](https://dev.qweather.com/)

[登陆](https://id.qweather.com/?#/homepage)

[创建应用和key](https://dev.qweather.com/docs/start/get-key/)

参考

```
和风天气官网
https://www.heweather.com/

和风天气组件程序
https://github.com/morestart/HeWeather

注：从HomeAssistant 0.88版本开始，自定义组件需放置在自身名称的子目录中。

在其中放置组件程序、__init__.py(可能是一个空的文件)、manifest.json文件
```

```
sensor:
  - platform: HeWeather 
    city: 上海 
    appkey: 43e15439494a4a26b99fb831fd388ecf 
    options: 
      - tmp 
      - hum
      - wind_spd
      - wind_sc
      - qlty    
      - cond_txt 
      - tmp_max 
      - tmp_min 
      - pop
```

#### 短信通知

##### [注册](https://www.twilio.com/)

https://signup.sendgrid.com/

[参考链接](https://blog.csdn.net/ddjhpxs/article/details/107692185)

```
pip install twilio
```

```
twilio:
  account_sid: AC39ee1471e977a8b5f1cb1f5749dc90aa
  auth_token: 92e061cfcb565764042f4dadf853cdfc
 
notify:
  - name: my_twilio_sms
    platform: twilio_sms
    from_number: "+13238317203" 
```



#### 家电控制

##### 小米网关

参考链接

https://www.home-assistant.io/integrations/xiaomi_aqara/

https://blog.csdn.net/weixin_42635922/article/details/106140343