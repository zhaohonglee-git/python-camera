### 设备：
CompressedAirStationEnv_01
MQTT连接参数如下：
clientId:
gwu1DfBasYk.CompressedAirStationEnv_01|securemode=2,signmethod=hmacsha256,timestamp=1678516170771|
username:
CompressedAirStationEnv_01&gwu1DfBasYk
passwd:
a3a209185ca42355eab0e43d1333f2957de64988a6cc18f4de8074c0baa990b0
mqttHostUrl:
iot-06z00isnjub2omb.mqtt.iothub.aliyuncs.com
port:1883



### 设备属性上报的Topic+Payload：
/sys/gwu1DfBasYk/CompressedAirStationEnv_01/thing/event/property/post
{"id":1678239049931,"params":{"DOAS_RunningState":1,"CurrentTemperature":34.45,"EnvHumidity":67,"DOAS_OperationControl":0},"version":"1.0","method":"thing.event.property.post"}



### 设备事件上报的Topic+Payload：
/sys/gwu1DfBasYk/CompressedAirStationEnv_01/thing/event/HighEnvironmentTempWarning/post,
{"id":1678239352331,"version":"1.0","params":{"Error":1},"method":"thing.event.HighEnvironmentTempWarning.post"}


### IOT云平台的逻辑为：温度大于等于40℃时候，平台设置物模型属性，即新风机组控制码为0（启动）
{
	"DOAS_OperationControl": 0
}


PS:新风机组控制码定义如下：
0-启动 1-暂停 2-停止


received a message "{"deviceType":"CustomCategory","iotId":"6Q1FM9Dz6HhLtkd2rxz8gwu100","requestId":"1678239049931","checkFailedData":{},"productKey":"gwu1DfBasYk","gmtCreate":1678433529695,"deviceName":"CompressedAirStationEnv_01","items":{"EnvHumidity":{"value":27,"time":1678433529688},"DOAS_RunningState":{"value":1,"time":1678433529688},"CurrentTemperature":{"value":24.45,"time":1678433529688},"DOAS_OperationControl":{"value":0,"time":1678433529688}}}"     


received a message "{"deviceType":"CustomCategory","iotId":"6Q1FM9Dz6HhLtkd2rxz8gwu100","requestId":"1678239049931","checkFailedData":{},"productKey":"gwu1DfBasYk","gmtCreate":1678433537067,"deviceName":"CompressedAirStationEnv_01","items":{"EnvHumidity":{"value":27,"time":1678433537064},"DOAS_RunningState":{"value":1,"time":1678433537064},"CurrentTemperature":{"value":14.45,"time":1678433537064},"DOAS_OperationControl":{"value":0,"time":1678433537064}}}"  


