# 训练
## 测试训练
```bash
yolo train data=coco8.yaml model=yolo11n.pt epochs=10 lr0=0.01
```

## 装甲车识别训练

#### 第五版本
```bash
yolo detect train data=ultralytics/cfg/datasets/gx-VOC-v5.yaml model=yolo11s.pt epochs=100 imgsz=640
```

#### 第6版本
```bash
yolo detect train data=ultralytics/cfg/datasets/gx-yolov11-v6.yaml model=yolo11s.pt epochs=100 imgsz=640
```

### 导出 onnx
```shell
yolo export model=./runs/detect/train/weights/best.pt format=onnx
```
### 转化onnx
```shell
python onnx-typecast/convert.py ./runs/detect/train/weights/best-v6.onnx ./runs/detect/train/weights/int32-best-v6.onnx
```
