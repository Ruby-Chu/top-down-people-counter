from ultralytics import YOLO
import yaml
import os, random
from PIL import Image
import matplotlib.pyplot as plt

if __name__ == "__main__":
    ### kaggle
    original_yaml = "/kaggle/input/datasets/chuchuying/top-down-head/data.yaml"
    new_yaml_path = "/kaggle/working/data.yaml"

    with open(original_yaml, 'r') as f:
        config = yaml.safe_load(f)

    config['path'] = '/kaggle/input/datasets/chuchuying/top-down-head'
    config['train'] = 'images/train'
    config['val'] = 'images/val'

    with open(new_yaml_path, 'w') as f:
        yaml.dump(config, f)

    print(f"generate new config file：{new_yaml_path}")

    ### Load a pretrained model
    model = YOLO("yolo26n.pt")
    ### yaml path
    yaml_path = "top-down-head/data.yaml"
    # yaml_path = "/kaggle/working/data.yaml"
    ### Train the model
    train_results = model.train(
        data=yaml_path,
        epochs=100,
        imgsz=640,
        device='cpu', # GPU=0, CPU='cpu'
        cache=False,
        verbose=False
    )


    ### Evaluate the model's performance on the validation set
    metrics = model.val()
    print(f"Precision: {metrics.results_dict['metrics/precision(B)']:.4f}")
    print(f"Recall: {metrics.results_dict['metrics/recall(B)']:.4f}")
    print(f"mAP@50: {metrics.results_dict['metrics/mAP50(B)']:.4f}")

    ### Predict
    test_path = "top-down-head/images/test"
    # test_path = "/kaggle/input/datasets/chuchuying/top-down-head/images/test"

    files = os.listdir(test_path)
    number = 5
    samples = random.sample(files, number)

    for img_name in samples:
        p = os.path.join(test_path, img_name)
        results = model.predict(source=p, conf=0.80, verbose=False, save=False)
        im_array = results[0].plot()
        im = Image.fromarray(im_array[..., ::-1])
        plt.figure(figsize=(10, 6))
        plt.imshow(im)
        plt.title(f"filename: {img_name.split('/')[-1].replace('.jpg', '')}")
        plt.axis('off')
        plt.show()