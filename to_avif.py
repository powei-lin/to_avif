from argparse import ArgumentParser
from PIL import Image
from pillow_avif import AvifImagePlugin
import cv2

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-i', '--imgs', nargs='+', type=str)
    parser.add_argument('-v', '--video', type=str)
    parser.add_argument('-o', '--output', type=str)
    args = parser.parse_args()
    
    imgs = []
    if args.imgs:
        imgs = [Image.open(img) for img in args.imgs]
    else:
        video = cv2.VideoCapture(args.video)
        while True:
            ret, frame = video.read()
            if not ret:
                break
            cv2.imshow("img", frame)
            cv2.waitKey(1)
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            im_pil = Image.fromarray(img)
            imgs.append(im_pil)
            # if len(imgs) > 00:
            #     break
    print("start converting")
    skip = 3
    imgs[0].save(
            args.output,
            save_all=True,
            append_images=imgs[skip::skip],
            duration=1,
            loop=0
        )
