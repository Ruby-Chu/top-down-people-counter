import os, random, shutil

if __name__ == "__main__":
    p = "images"
    s = "image/val"
    files = os.listdir(p)
    train_rate = 0.5
    picknumber = int(len(files)*train_rate)
    samples = random.sample(files, picknumber)
    for n in samples:
        readfile = os.path.join(p, n)
        movefile = os.path.join(s, n)
        shutil.move(readfile, movefile)