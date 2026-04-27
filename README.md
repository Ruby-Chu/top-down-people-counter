# top-down-people-counter

---
## Data Collection

<img src="https://github.com/Ruby-Chu/top-down-people-counter/blob/master/img/000.jpg" width="50%">

| dataset | images |
| :---: | :---: |
| Training Set | 946 |
| Validation Set | 120 |
| Test Set | 120 |

---
## Train

### Download weight

download [YOLO26n.pt](https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26n.pt)

### dataset directory structure

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

**data.yaml**

```text
path: top-down-head
train: images/train
val: images/val
names:
  0: head
```

### training

💻 Environment & Hardware<br>
Platform: kaggle<br>
GPU: NVIDIA T4<br>
Runtime: 24m 29s<br>

**training_main.py**

- Precision: 0.9934
- Recall: 0.9481
- mAP@50: 0.9835

<img src="https://github.com/Ruby-Chu/top-down-people-counter/blob/master/img/results.png" width="50%">

---
## Predict

<img src="https://github.com/Ruby-Chu/top-down-people-counter/blob/master/img/003.png" height="250"> <img src="https://github.com/Ruby-Chu/top-down-people-counter/blob/master/img/004.png" height="250"> <img src="https://github.com/Ruby-Chu/top-down-people-counter/blob/master/img/005.png" height="250">

---
## tracking and counting

[top-down-head.pt](https://www.kaggle.com/models/chuchuying/top-down-head)



