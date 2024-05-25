from inference_sdk import InferenceHTTPClient
import PIL

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="P0d4OwuZDmHRjacqXJtf"
)

result = CLIENT.infer("C:\\Users\\Bhargav\\Desktop\\Robotics\\proj_comp_det\\src\\original.jpg", model_id="component_recognition_v2/2")
print(result)