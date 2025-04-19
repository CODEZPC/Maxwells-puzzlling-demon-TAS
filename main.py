import keyboard, time, os

dict = {
    "0-1": "./world/w0/1",
    "1-1": "./world/w0/w1/1",
    "1-2": "./world/w0/w1/2",
    "1-3": "./world/w0/w1/3",
    "1-4": "./world/w0/w1/4",
    "1-5": "./world/w0/w1/5",
    "1-6": "./world/w0/w1/6",
    "1-7": "./world/w0/w1/7",
    "1-13": "./world/w0/w1/13",
    "5-1": "./world/w0/w5/1",
    "7-1": "./world/w0/w7/1",
    "7-2": "./world/w0/w7/2",
    "9-5": "./world/w0/w9/5",
    "9-6": "./world/w0/w9/6",
    "9-R7": "./world/w0/w9/R7",
    "9-R8": "./world/w0/w9/R8",
    "9-R13": "./world/w0/w9/R13",
    "9-9": "./world/w0/w9/9",
    "9-10": "./world/w0/w9/10",
    "9-12": "./world/w0/w9/12",
    "A-42": "./world/w0/wA/42",
    "A-45": "./world/w0/wA/45",
    "A-46": "./world/w0/wA/46",
    "A-49": "./world/w0/wA/49",
    "A-63": "./world/w0/wA/63",
    "A-73": "./world/w0/wA/73",
    "A-75": "./world/w0/wA/75",
    "B-1": "./world/w0/wB/1",
    "B-2": "./world/w0/wB/2",
    "B-A": "./world/w0/wB/A",
    "alpha": "./world/w0/α/alpha",
    "kappa2": "./world/w0/κ/kappa2",
}

opt = {
    "w": "UP",
    "a": "LEFT",
    "s": "DOWN",
    "d": "RIGHT",
    "x": "ENTER LEVEL",
    "q": "QUIT LEVEL",
    "r": "RESET LEVEL",
    "l": "WAIT",
    "h": "ENTER HINT",
}


def ctrl(inp):
    j = 0
    l = str(len(inp)).zfill(3)
    for i in inp.lower():
        j += 1
        print(f"[{str(j).zfill(3)}/{l}]:{opt[i]}")
        wait = 0.6 if i == "x" or i == "q" or i == "h" else 0.15
        if i == "l":
            time.sleep(1)
            continue
        keyboard.press(i)
        time.sleep(0.05)
        keyboard.release(i)
        time.sleep(wait)


def main():
    while True:
        os.system("cls")
        path = dict[input("输入关卡：")]
        f = open(path, "r").readlines()
        pre = f[0]
        os.system("cls")
        if input(f"请检查依赖项:\n{pre}输入Y继续：") == "Y":
            start = f[1]
            os.system("cls")
            input(f"到达此位置后按Enter开始：{start}")
            print("3秒后开始……")
            time.sleep(3)
            os.system("cls")
            ctrl(f[2])
            os.system("cls")
            print("Completed!")
            time.sleep(3)


if __name__ == "__main__":
    main()
