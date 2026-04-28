import os, glob
import cv2

if __name__ == '__main__':
    path = "video"
    save_folder = "img"
    files = glob.glob(os.path.join(path, '*.mp4'))
    for index, filename in enumerate(files):
        sp = filename.split('\\')
        f1 = sp[len(sp) - 1][:-4]
        save_path = os.path.join(save_folder, f1)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        cap = cv2.VideoCapture(filename)
        length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        step = int(fps / 1.5)
        for i in range(0, length, step):
            cap.set(cv2.CAP_PROP_POS_FRAMES, i)
            _, frame = cap.read()
            if _:
                fn = "{}_{:05d}.jpg".format(f1, i)
                save_ = os.path.join(save_path, fn)
                cv2.imwrite(save_, frame)
