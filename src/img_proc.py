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

# res_dict_test = {'time': 0.03687704300000405, 'image': {'width': 4000, 'height': 3000}, 'predictions': [{'x': 1531.25, 'y': 1917.96875, 'width': 515.625, 'height': 328.125, 'confidence': 0.7944501042366028, 'class': 'CAPACITOR', 'class_id': 0, 'detection_id': 'bdfeaaf4-cd9d-4036-aaec-adf6a05d7399'}, {'x': 2984.375, 'y': 400.390625, 'width': 515.625, 'height': 269.53125, 'confidence': 0.7825040221214294, 'class': 'CAPACITOR', 'class_id': 0, 'detection_id': 'd54a2269-5077-41f1-8fed-c19dd00eb4c0'}, {'x': 708.984375, 'y': 1781.25, 'width': 269.53125, 'height': 343.75, 'confidence': 0.7706283330917358, 'class': 'CAPACITOR', 'class_id': 0, 'detection_id': '45bf7074-1475-4edb-b038-f7583f7662e8'}, {'x': 2986.328125, 'y': 400.390625, 'width': 503.90625, 'height': 253.90625, 'confidence': 0.7632450461387634, 'class': 'LED', 'class_id': 1, 'detection_id': '7faaecd1-271b-4d1f-8451-d0e23f8655f2'}, {'x': 324.21875, 'y': 357.421875, 'width': 492.1875, 'height': 378.90625, 'confidence': 0.7066272497177124, 'class': 'TRANSISTOR', 'class_id': 3, 'detection_id': '886be934-0c14-431d-9551-0d265e49f133'}, {'x': 2011.71875, 'y': 1197.265625, 'width': 437.5, 'height': 214.84375, 'confidence': 0.6960435509681702, 'class': 'CAPACITOR', 'class_id': 0, 'detection_id': '248eeff7-8da7-4755-b01c-5fd11f56430c'}, {'x': 2609.375, 'y': 937.5, 'width': 125.0, 'height': 390.625, 'confidence': 0.6377803087234497, 'class': 'RESISTOR', 'class_id': 2, 'detection_id': '2c72764f-a346-44e3-b872-5a9c84491559'}, {'x': 1601.5625, 'y': 947.265625, 'width': 273.4375, 'height': 175.78125, 'confidence': 0.6368553638458252, 'class': 'RESISTOR', 'class_id': 2, 'detection_id': 'ef0d65ad-42cd-4f48-8d85-7f98b33f760d'}]}

# res_dict_test = {'time': 0.0351845919999505, 'image': {'width': 4000, 'height': 3000}, 'predictions': [{'x': 1531.25, 'y': 1917.96875, 'width': 515.625, 'height': 328.125, 'confidence': 0.7944501042366028, 'class': 'CAPACITOR', 'class_id': 0, 'detection_id': '3781528d-e00a-4a8c-8bf9-c30fe38630a1'}, {'x': 2984.375, 'y': 400.390625, 'width': 515.625, 'height': 269.53125, 'confidence': 0.7825040221214294, 'class': 'CAPACITOR', 'class_id': 0, 'detection_id': 'a0c0b28d-db9f-4ae0-966e-60a775a4c2ed'}, {'x': 708.984375, 'y': 1781.25, 'width': 269.53125, 'height': 343.75, 'confidence': 0.7706283330917358, 'class': 'CAPACITOR', 'class_id': 0, 'detection_id': '539f5b51-6398-41b7-aac1-acaf4f0d21e7'}, {'x': 2986.328125, 'y': 400.390625, 'width': 503.90625, 'height': 253.90625, 'confidence': 0.7632450461387634, 'class': 'LED', 'class_id': 1, 'detection_id': '9044ed4d-3385-44d6-a7ac-62f1915dc069'}, {'x': 324.21875, 'y': 357.421875, 'width': 492.1875, 'height': 378.90625, 'confidence': 0.7066272497177124, 'class': 'TRANSISTOR', 'class_id': 3, 'detection_id': '3ef9f348-4302-4fe1-a24b-b7e11e0d4fd5'}, {'x': 2011.71875, 'y': 1197.265625, 'width': 437.5, 'height': 214.84375, 'confidence': 0.6960435509681702, 'class': 'CAPACITOR', 'class_id': 0, 'detection_id': '1d9c01c7-90f1-40f8-b0f4-29133a5e2a96'}, {'x': 2609.375, 'y': 937.5, 'width': 125.0, 'height': 390.625, 'confidence': 0.6377803087234497, 'class': 'RESISTOR', 'class_id': 2, 'detection_id': '51197468-ec53-4504-92e3-fac03bef51ec'}, {'x': 1601.5625, 'y': 947.265625, 'width': 273.4375, 'height': 175.78125, 'confidence': 0.6368553638458252, 'class': 'RESISTOR', 'class_id': 2, 'detection_id': 'c2260359-bfe8-4b62-9c17-850909a326d6'}]}

# res_dict_test = {'time': 0.05463164399998277, 'image': {'width': 4000, 'height': 3000}, 'predictions': [{'x': 2216.796875, 'y': 2794.921875, 'width': 300.78125, 'height': 222.65625, 'confidence': 0.7194410562515259, 'class': 'RESISTOR', 'class_id': 2, 'detection_id': '18d08eff-3c39-41a8-ab23-54b10579b3b1'}, {'x': 1607.421875, 'y': 2203.125, 'width': 472.65625, 'height': 156.25, 'confidence': 0.6967458724975586, 'class': 'CAPACITOR', 'class_id': 0, 'detection_id': '04f6a592-6659-4bb1-bc04-f3470c41c32d'}, {'x': 3539.0625, 'y': 166.015625, 'width': 921.875, 'height': 308.59375, 'confidence': 0.6932172775268555, 'class': 'CAPACITOR', 'class_id': 0, 'detection_id': '1f9aeca1-aee0-40db-912a-e89d75aaf1f1'}, {'x': 1597.65625, 'y': 2199.21875, 'width': 445.3125, 'height': 148.4375, 'confidence': 0.6768060922622681, 'class': 'LED', 'class_id': 1, 'detection_id': '1bb35cc7-2512-4707-9aa2-30aba525d887'}, {'x': 2875.0, 'y': 2273.4375, 'width': 257.8125, 'height': 218.75, 'confidence': 0.6692739725112915, 'class': 'LED', 'class_id': 1, 'detection_id': '844988ec-e6ba-4761-b2ef-bd0cdcec5b2d'}, {'x': 3718.75, 'y': 632.8125, 'width': 523.4375, 'height': 273.4375, 'confidence': 0.6645803451538086, 'class': 'LED', 'class_id': 1, 'detection_id': '75e58f71-c4b8-4a16-8bd7-5b65b1040b8f'}, {'x': 3101.5625, 'y': 1791.015625, 'width': 250.0, 'height': 207.03125, 'confidence': 0.6606467962265015, 'class': 'RESISTOR', 'class_id': 2, 'detection_id': 'b3fa1808-f0c9-42af-a777-31602bcfb03f'}, {'x': 3197.265625, 'y': 1240.234375, 'width': 496.09375, 'height': 230.46875, 'confidence': 0.6580352783203125, 'class': 'LED', 'class_id': 1, 'detection_id': 'e4c6b71e-9557-4096-ad5d-dba933ed4950'}, {'x': 1947.265625, 'y': 1302.734375, 'width': 246.09375, 'height': 199.21875, 'confidence': 0.6487857103347778, 'class': 'RESISTOR', 'class_id': 2, 'detection_id': 'baa3fdf4-8a6c-48ce-8acf-aaebccfc6dc4'}, {'x': 2322.265625, 'y': 1480.46875, 'width': 402.34375, 'height': 234.375, 'confidence': 0.6156385540962219, 'class': 'CAPACITOR', 'class_id': 0, 'detection_id': '3e2c2bf0-bf77-4f21-8ab1-4018f61e4030'}, {'x': 875.0, 'y': 2113.28125, 'width': 140.625, 'height': 273.4375, 'confidence': 0.6112461090087891, 'class': 'RESISTOR', 'class_id': 2, 'detection_id': '508391df-fbb6-4252-8367-9341c57480c1'}, {'x': 359.375, 'y': 136.71875, 'width': 562.5, 'height': 273.4375, 'confidence': 0.603914737701416, 'class': 'CAPACITOR', 'class_id': 0, 'detection_id': 'b1df0a05-5cfe-4446-9784-75c469a44bee'}, {'x': 2322.265625, 'y': 1476.5625, 'width': 394.53125, 'height': 250.0, 'confidence': 0.49223533272743225, 'class': 'LED', 'class_id': 1, 'detection_id': '750b34e1-e7ac-4b1e-9e08-3e6e360fc0c2'}, {'x': 1220.703125, 'y': 2751.953125, 'width': 519.53125, 'height': 214.84375, 'confidence': 0.4530971348285675, 'class': 'LED', 'class_id': 1, 'detection_id': 'c8629b81-54b6-4bee-866d-37b4b4aeca2c'}]}

res_dict_test = {'time': 0.035279596000009406, 'image': {'width': 4000, 'height': 3000}, 'predictions': [{'x': 236.328125, 'y': 417.96875, 'width': 464.84375, 'height': 554.6875, 'confidence': 0.5773434638977051, 'class': 'CAPACITOR', 'class_id': 0, 'detection_id': 'b2ea39f9-4980-42d2-b31a-43009d1d6b05'}, {'x': 3199.21875, 'y': 697.265625, 'width': 421.875, 'height': 105.46875, 'confidence': 0.5764647126197815, 'class': 'RESISTOR', 'class_id': 2, 'detection_id': '5d65004a-51a7-4920-828f-64d6d04873d3'}, {'x': 1160.15625, 'y': 2041.015625, 'width': 179.6875, 'height': 355.46875, 'confidence': 0.5531340837478638, 'class': 'RESISTOR', 'class_id': 2, 'detection_id': '248bc746-acc1-4576-819a-0d817fab8b22'}, {'x': 1630.859375, 'y': 759.765625, 'width': 207.03125, 'height': 246.09375, 'confidence': 0.4855283200740814, 'class': 'RESISTOR', 'class_id': 2, 'detection_id': 'e0515c66-e012-478b-9677-41a5f5b8c994'}]}

def proc_func(test = 0, path = "../assets/original.jpg", user_input = "RESISTOR"):
    
    pixels_per_cm = 127

    if test:
        res_dict = res_dict_test
    else:
        CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key="P0d4OwuZDmHRjacqXJtf"
        )
        res_dict = CLIENT.infer(path, model_id="component_recognition_v2/2")
    # print(res_dict)

    for prediction_list in res_dict['predictions']:
        if prediction_list['class'] == user_input:
            # print(prediction_list['x'] + (prediction_list['width']/2), prediction_list['y'] + (prediction_list['height']/2))
            x = prediction_list['x'] + (prediction_list['width']/2)
            y = prediction_list['y'] + (prediction_list['height']/2)
            break        
    
    x = pixels_per_cm * x/res_dict["image"]["width"]
    y = pixels_per_cm * y/res_dict["image"]["height"]
    return x,y

if __name__ == "__main__":
    print(proc_func(1))