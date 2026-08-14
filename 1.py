import subprocess
import random
import sys
print("game ")
d = "eve1b.pdf"
e = "eve100.pdf"
subprocess.run([r".\collide.exe", d, e], check=True)
pat1 = f".\\out-{d}"
pat2 = f".\\out-{e}"
r = "win"
c = int(input("1,2,3"))
t = [pat1,pat2]
v = []
for i in range(100):
    h = random.randint(0,1)
    v.append(h)
q = v[random.randint(0,99)]
g = t[q]
t.remove(g)
f = t[0]
subprocess.run([r".\7-Zip\7z.exe","a", r".\my.wim",  f"{g}", "-y"], check=True)
subprocess.run([r".\7-Zip\7z.exe","a", r".\my.wim",  f"{f}", "-y"], check=True)
seven_zip_path = r".\7-Zip\7z.exe"
wim_file_path  = r".\my.wim"
output_dir     = r".\wim_out"
subprocess.run([seven_zip_path,"x",wim_file_path,f"-o{output_dir}","-y"], check=True)
def get_hash(file_path, algorithm="SHA256"):
    result = subprocess.run(
        ["certutil", "-hashfile", file_path, algorithm],
        capture_output=True,
        text=True,
        encoding="gbk",
        errors="ignore"
    )
    first_line = result.stdout.strip().splitlines()[1]
    return first_line.replace(" ", "").lower()
path1 = f".\\wim_out\\out-{d}"
path2 = f".\\wim_out\\out-{e}"
h1 = get_hash(path1)
h2 = get_hash(path2)
h3 = get_hash(pat1)
h4 = get_hash(pat2)
print(h1)
print(h2)
if h1 == h3 and c == 1 and h1 == h2:
    print(r)
elif h1 == h4 and c == 2 and h1 == h2:
    print(r)
elif h1 != h2 and c == 3:
    print(r)
else:
    print("lose")

