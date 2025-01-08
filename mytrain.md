```bash
yolo train data=coco8.yaml model=yolo11n.pt epochs=10 lr0=0.01
```


```bash
yolo detect train data=ultralytics/cfg/datasets/gx-VOC-v5.yaml model=yolo11s.pt epochs=100 imgsz=640
```

# 导出 onnx
```shell
yolo export model=./runs/detect/train/weights/best.pt format=onnx
```

```shell
python 
```
 
