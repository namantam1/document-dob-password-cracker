import pikepdf
from tqdm import tqdm

found = None


def get(num, digits=2):
    num = str(num)
    return '0'*(digits-len(num)) + num

def check_password(password, file="sample.pdf"):
    # print(threading.current_thread().name)
    global found
    try:
        pikepdf.open(file, password=password)
        found = password
        print("found = ", password)
        return password
    except:
        pass

def get_passwords(ini="52254", days=(1,32), months=(1,13), years=(1995,2005)):
    for year in range(*years):
        for month in range(*months):
            for day in range(*days):
                yield  (ini + get(day) + get(month) + get(year)[-2:],
                 {"day": day, "month": month, "year": year})  

def sample(r=20000):
    for i in range(r):
        yield get(i, 4)

for i in tqdm(get_passwords(years=(1995, 2006)), "passwords"):
# for i in tqdm(sample(), "passwords"):
    print(i[0])
    if check_password(i[0], "naman.pdf"):
        print(i[1])
        break
    
