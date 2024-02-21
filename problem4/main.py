def muncul_sekali(angka):
    number = [int(chr) for chr in angka]
    kemunculan = {}
    for i in number:
        if i in kemunculan:
            kemunculan[i] +=1
        else:
            kemunculan[i] =1
    once = [key for key, value in kemunculan.items() if value == 1]
    return once

if __name__ == '__main__':
    print(muncul_sekali("1234123")) # [4]
    print(muncul_sekali("76523752")) # [6, 3]
    print(muncul_sekali("12345")) # [1, 2, 3, 4, 5]
    print(muncul_sekali("1122334455")) # []
    print(muncul_sekali("0872504")) # [8, 7, 2, 5, 4]