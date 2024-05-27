from inference_sdk import InferenceHTTPClient
import PIL

# res_dict_test = {'time': 0.040622095999424346, 
#             'image': {'width': 3000, 'height': 4000}, 
#             'predictions': 
#             [
#             {'x': 1097.65625, 'y': 763.671875, 'width': 250.0, 'height': 277.34375, 'confidence': 0.874109148979187, 'class': 'LED', 'class_id': 1, 'detection_id': '2709e1e1-0692-45bf-afee-1628c94d6c7d'}, 
#             {'x': 828.125, 'y': 1123.046875, 'width': 320.3125, 'height': 261.71875, 'confidence': 0.8585530519485474, 'class': 'LED', 'class_id': 1, 'detection_id': 'c119a12e-6108-4249-9056-521d62027c2e'}, 
#             {'x': 992.1875, 'y': 412.109375, 'width': 148.4375, 'height': 292.96875, 'confidence': 0.8228565454483032, 'class': 'LED', 'class_id': 1, 'detection_id': '4ddd1885-38f0-410e-b880-564985f547d2'}, 
#             {'x': 1888.671875, 'y': 642.578125, 'width': 238.28125, 'height': 324.21875, 'confidence': 0.8221799731254578, 'class': 'CAPACITOR', 'class_id': 0, 'detection_id': 'a679762b-de69-4cb8-a97f-4fe86194d3d1'}, 
#             {'x': 300.78125, 'y': 1291.015625, 'width': 210.9375, 'height': 339.84375, 'confidence': 0.8217990398406982, 'class': 'LED', 'class_id': 1, 'detection_id': '9bfdb046-2702-4909-808c-17cb8acb0fd4'}, 
#             {'x': 933.59375, 'y': 1603.515625, 'width': 195.3125, 'height': 332.03125, 'confidence': 0.8181244134902954, 'class': 'RESISTOR', 'class_id': 2, 'detection_id': '6a91c79c-1c46-4e3f-aabc-70c7a9f20d6a'}, 
#             {'x': 427.734375, 'y': 1925.78125, 'width': 167.96875, 'height': 437.5, 'confidence': 0.787625789642334, 'class': 'CAPACITOR', 'class_id': 0, 'detection_id': 'a24191f8-f015-4079-bf14-5d1fabfe2356'}, 
#             {'x': 2068.359375, 'y': 976.5625, 'width': 136.71875, 'height': 343.75, 'confidence': 0.786731481552124, 'class': 'LED', 'class_id': 1, 'detection_id': '88e986f9-9975-4232-b8e9-7a532fa55da0'}, 
#             {'x': 1585.9375, 'y': 1076.171875, 'width': 132.8125, 'height': 363.28125, 'confidence': 0.779346227645874, 'class': 'RESISTOR', 'class_id': 2, 'detection_id': 'ba47232d-7ca4-4785-b790-78d4b7fc49c5'}, 
#             {'x': 2130.859375, 'y': 1804.6875, 'width': 355.46875, 'height': 179.6875, 'confidence': 0.7692291736602783, 'class': 'LED', 'class_id': 1, 'detection_id': '51923886-2682-4e2b-bed5-11637e87e6ce'}, 
#             {'x': 394.53125, 'y': 2607.421875, 'width': 148.4375, 'height': 480.46875, 'confidence': 0.7329177260398865, 'class': 'RESISTOR', 'class_id': 2, 'detection_id': '91654de6-f181-4576-9a2d-76027b650504'}, 
#             {'x': 1505.859375, 'y': 2457.03125, 'width': 128.90625, 'height': 484.375, 'confidence': 0.7136199474334717, 'class': 'RESISTOR', 'class_id': 2, 'detection_id': 'f9946dc6-8e3f-4ed5-91c0-e99a2f88d1f1'}, 
#             {'x': 2080.078125, 'y': 2421.875, 'width': 183.59375, 'height': 359.375, 'confidence': 0.7092617750167847, 'class': 'RESISTOR', 'class_id': 2, 'detection_id': 'd50c1f60-f4af-4761-aef4-08c0035e0f4e'}, 
#             {'x': 1046.875, 'y': 2580.078125, 'width': 242.1875, 'height': 339.84375, 'confidence': 0.6810650825500488, 'class': 'RESISTOR', 'class_id': 2, 'detection_id': 'e7825b8f-c612-4602-8f25-97fa3788ac2b'}, 
#             {'x': 1326.171875, 'y': 1931.640625, 'width': 378.90625, 'height': 128.90625, 'confidence': 0.6602399349212646, 'class': 'RESISTOR', 'class_id': 2, 'detection_id': '9823faec-b4fb-4f30-8e51-5bb408360a7f'}, 
#             {'x': 2933.59375, 'y': 1736.328125, 'width': 132.8125, 'height': 339.84375, 'confidence': 0.47802382707595825, 'class': 'CAPACITOR', 'class_id': 0, 'detection_id': '236cbb59-dfc2-481a-8437-a1161ccf1c5e'}
#             ]
#            }

res_dict_test = {'time': 0.03687704300000405, 'image': {'width': 4000, 'height': 3000}, 'predictions': [{'x': 1531.25, 'y': 1917.96875, 'width': 515.625, 'height': 328.125, 'confidence': 0.7944501042366028, 'class': 'CAPACITOR', 'class_id': 0, 'detection_id': 'bdfeaaf4-cd9d-4036-aaec-adf6a05d7399'}, {'x': 2984.375, 'y': 400.390625, 'width': 515.625, 'height': 269.53125, 'confidence': 0.7825040221214294, 'class': 'CAPACITOR', 'class_id': 0, 'detection_id': 'd54a2269-5077-41f1-8fed-c19dd00eb4c0'}, {'x': 708.984375, 'y': 1781.25, 'width': 269.53125, 'height': 343.75, 'confidence': 0.7706283330917358, 'class': 'CAPACITOR', 'class_id': 0, 'detection_id': '45bf7074-1475-4edb-b038-f7583f7662e8'}, {'x': 2986.328125, 'y': 400.390625, 'width': 503.90625, 'height': 253.90625, 'confidence': 0.7632450461387634, 'class': 'LED', 'class_id': 1, 'detection_id': '7faaecd1-271b-4d1f-8451-d0e23f8655f2'}, {'x': 324.21875, 'y': 357.421875, 'width': 492.1875, 'height': 378.90625, 'confidence': 0.7066272497177124, 'class': 'TRANSISTOR', 'class_id': 3, 'detection_id': '886be934-0c14-431d-9551-0d265e49f133'}, {'x': 2011.71875, 'y': 1197.265625, 'width': 437.5, 'height': 214.84375, 'confidence': 0.6960435509681702, 'class': 'CAPACITOR', 'class_id': 0, 'detection_id': '248eeff7-8da7-4755-b01c-5fd11f56430c'}, {'x': 2609.375, 'y': 937.5, 'width': 125.0, 'height': 390.625, 'confidence': 0.6377803087234497, 'class': 'RESISTOR', 'class_id': 2, 'detection_id': '2c72764f-a346-44e3-b872-5a9c84491559'}, {'x': 1601.5625, 'y': 947.265625, 'width': 273.4375, 'height': 175.78125, 'confidence': 0.6368553638458252, 'class': 'RESISTOR', 'class_id': 2, 'detection_id': 'ef0d65ad-42cd-4f48-8d85-7f98b33f760d'}]}

def proc_func(test = 0, path = "./assets/original.jpg"):
    
    # print(res_dict)
    if test:
        res_dict = res_dict_test
    else:
        CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key="P0d4OwuZDmHRjacqXJtf"
        )
        res_dict = CLIENT.infer(path, model_id="component_recognition_v2/2")
    print(res_dict)
    user_input = input("""These are the components type to be selected:
    LED
    RESISTOR
    CAPACITOR
    Please Choose: """)

    for prediction_list in res_dict['predictions']:
        if prediction_list['class'] == user_input:
            print(prediction_list['x'] + (prediction_list['width']/2), prediction_list['y'] + (prediction_list['height']/2))
            x = prediction_list['x'] + (prediction_list['width']/2)
            y = prediction_list['y'] + (prediction_list['height']/2)
            return x,y

if __name__ == "__main__":
    proc_func(1)