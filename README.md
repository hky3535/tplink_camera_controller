# tplink_camera_controller
TL-IPC40A云台摄像头云台控制http接口

## 通过局域网post请求控制tplink云台
* 云台控制参数:
* 云台预置点位“1”
> {"method":"do","preset":{"goto_preset": {"id": "1"}}}
* 云台相对移动角度
> {"method":"do","motor":{"move":{"x_coord":"10","y_coord":"0"}}}
* 云台水平移动角度      
> {"method":"do","motor":{"movestep":{"direction":"0"}}}
* 云台垂直移动角度      
> {"method":"do","motor":{"movestep":{"direction":"90"}}}
* 云台停止              
> {"method":"do","motor":{"stop":"null"}}
* 添加云台预置点位“1”   
> {"method":"do","preset":{"set_preset":{"name":"name","save_ptz":"1"}}}
* 镜头遮罩              
> {"method":"set","lens_mask":{"lens_mask_info":{"enabled":"on"}}}
* 注：x范围有360度 y范围有180度