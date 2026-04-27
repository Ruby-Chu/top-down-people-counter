# top-down-people-counter

## Data Collection

![image](https://github.com/Ruby-Chu/top-down-people-counter/blob/master/img/000.jpg)

| dataset | images |
| :---: | :---: |
| Training Set | 946 |
| Validation Set | 120 |
| Test Set | 120 |

## Train

### Download weight

download [YOLO26n.pt](https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26n.pt)

### Dataset Directory Structure

```text
top-down-head/
├── data.yaml
├── images/
│   ├── train/
│   └── val/
└── labels/
    ├── train/
    └── val/
```

#### data.yaml

```text
path: top-down-head
train: images/train
val: images/val
names:
  0: head
```

### training

**training_main.py**
