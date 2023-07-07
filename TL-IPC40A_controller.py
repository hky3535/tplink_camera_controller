import requests


class TL_IPC40A:
    def __init__(self):
        # 初始化云台控制
        self.camera_control_url = "http://192.168.10.77:80/"
        self.stok = self.init_stok()
        # 云台控制指令
        self.control_key_dict = {
            "left": "{\"method\":\"do\",\"motor\":{\"move\":{\"x_coord\":\"-45\",\"y_coord\":\"0\"}}}",
            "right": "{\"method\":\"do\",\"motor\":{\"move\":{\"x_coord\":\"45\",\"y_coord\":\"0\"}}}",
            "up": "{\"method\":\"do\",\"motor\":{\"move\":{\"x_coord\":\"0\",\"y_coord\":\"45\"}}}",
            "down": "{\"method\":\"do\",\"motor\":{\"move\":{\"x_coord\":\"0\",\"y_coord\":\"-45\"}}}",
            "stop": "{\"method\":\"do\",\"motor\":{\"stop\":\"null\"}}"
        }

    def init_stok(self):
        headers = {"Content-Type": "application/json; charset=UTF-8"}
        login_data = "{\"method\": \"do\", \"login\": {\"username\": \"admin\", \"password\": \"admin\"}}"
        login_res = requests.post(url=self.camera_control_url, data=login_data, headers=headers).text
        print(login_res)
        return eval(login_res)["stok"]

    def control_once(self, key):
        control_camera_url = f"{self.camera_control_url}/stok={self.stok}/ds"
        control_camera_res = requests.post(url=control_camera_url, data=self.control_key_dict[key]).text
        print(control_camera_res)

    def main(self):
        self.control_once("left")
        self.control_once("right")
        self.control_once("up")
        self.control_once("down")


if __name__ == '__main__':
    tl_ipc40a = TL_IPC40A()
    tl_ipc40a.main()

# 其他参数:
# PTZ to preset position      {"method":"do","preset":{"goto_preset": {"id": "1"}}}
# PTZ by coord                {"method":"do","motor":{"move":{"x_coord":"10","y_coord":"0"}}}
# PTZ horizontal by step      {"method":"do","motor":{"movestep":{"direction":"0"}}}
# PTZ vertical by step        {"method":"do","motor":{"movestep":{"direction":"90"}}}
# stop PTZ                    {"method":"do","motor":{"stop":"null"}}
# add PTZ preset position     {"method":"do","preset":{"set_preset":{"name":"name","save_ptz":"1"}}}
# lens mask                   {"method":"set","lens_mask":{"lens_mask_info":{"enabled":"on"}}}

# {"method":"do","motor":{"move":{"x_coord":"10","y_coord":"10"}}}
# x范围有360度 y范围有180度