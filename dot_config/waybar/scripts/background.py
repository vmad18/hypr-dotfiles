#!/usr/bin/env python3

import os


def main():
    
    script = "~/.config/waybar/scripts/randbg.sh"
    bgs = (
            "~/.config/Backgrounds/citycotton.jpeg",
            "~/.config/Backgrounds/flowers.png",
            "~/.config/Backgrounds/powerline.png",
            "~/.config/Backgrounds/cityscape.jpg",
            "~/.config/Backgrounds/saturn.png",
            "~/.config/Backgrounds/summerbeach.jpg",
            ".config/Backgrounds/awawaaaaa.jpg")
    
    f = open("/home/v18/.config/waybar/scripts/next_idx.txt", "r+")
    idx = str(f.read())
    f = open("/home/v18/.config/waybar/scripts/next_idx.txt", "w")
    f.write(str((int(idx)+1) % len(bgs)))
    f.close()
    
    background = bgs[int(idx)%len(bgs)]
    os.system(f"sh {script} {background}")
    

if __name__ == "__main__":
    main()