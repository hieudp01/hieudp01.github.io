serial = b"CTF{efghijklmnopqrstuvwxyz{|}"
wtf = []

def swap(arr, a, b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

for i in range(0x8):
    x = 0
    mem = list(range(0x100))
    tmp = [0] * 3
    for j in range(128):
        x = (x + serial[2*i]) & 0xff
        swap(mem, 2*j, x)
        x = (x + mem[2*j+1]) & 0xff

        x = (x + serial[2*i+1]) & 0xff
        swap(mem, 2*j+1, x)
        x = (x + mem[(2*j+2) & 0xff]) & 0xff

    x = 0
    for j in range(3):
        x = (x + mem[j]) & 0xff
        swap(mem, j, x)
        tmp[j] += mem[(mem[j] + mem[x]) & 0xff]
    
    wtf += tmp

mults = [
    [155, 190, 208, 123, 214, 146, 211, 85, 87, 251, 122, 60, 237, 27, 63, 207, 33, 138, 51, 103, 58, 68, 120, 111],
    [254, 21, 157, 204, 56, 134, 79, 115, 9, 91, 46, 12, 34, 45, 200, 131, 184, 180, 5, 100, 61, 59, 52, 249],
    [163, 170, 112, 210, 157, 233, 53, 51, 235, 1, 160, 42, 207, 196, 66, 16, 138, 152, 227, 7, 142, 97, 102, 23],
    [125, 180, 152, 26, 204, 69, 4, 121, 211, 4, 126, 99, 147, 212, 55, 69, 65, 182, 229, 193, 130, 102, 4, 160],
    [170, 43, 11, 21, 253, 86, 3, 83, 224, 114, 160, 189, 160, 237, 130, 114, 82, 136, 7, 125, 88, 189, 143, 219],
    [23, 26, 212, 235, 21, 38, 97, 230, 7, 143, 200, 31, 101, 67, 150, 19, 55, 137, 75, 211, 30, 208, 182, 38],
    [10, 217, 231, 199, 229, 252, 108, 178, 189, 172, 80, 66, 5, 170, 112, 25, 228, 218, 135, 235, 196, 240, 223, 112],
    [131, 189, 196, 65, 214, 175, 83, 185, 77, 83, 232, 195, 76, 59, 121, 124, 91, 222, 77, 244, 74, 137, 175, 90],
    [140, 227, 161, 82, 108, 53, 217, 219, 130, 110, 181, 52, 123, 144, 172, 91, 6, 66, 253, 43, 227, 12, 211, 232],
    [194, 44, 61, 224, 6, 31, 90, 171, 56, 37, 251, 129, 24, 134, 136, 203, 146, 167, 178, 6, 26, 31, 178, 200],
    [152, 110, 68, 91, 143, 137, 86, 105, 190, 119, 103, 193, 56, 0, 197, 252, 1, 240, 130, 52, 88, 179, 176, 175],
    [169, 21, 204, 246, 237, 171, 236, 121, 213, 26, 236, 246, 227, 108, 138, 165, 119, 7, 45, 196, 1, 232, 76, 187],
    [60, 115, 207, 3, 83, 252, 112, 52, 250, 39, 5, 75, 227, 168, 3, 115, 124, 166, 164, 127, 72, 43, 57, 5],
    [26, 18, 119, 193, 45, 207, 28, 31, 165, 163, 230, 65, 244, 13, 205, 63, 0, 219, 74, 223, 220, 235, 151, 165],
    [207, 123, 9, 70, 51, 144, 96, 54, 239, 71, 221, 50, 193, 173, 238, 103, 158, 194, 184, 181, 157, 74, 242, 49],
    [66, 177, 147, 17, 135, 94, 32, 173, 86, 155, 2, 111, 207, 52, 173, 15, 235, 210, 54, 138, 62, 90, 175, 117],
    [228, 40, 69, 141, 187, 243, 41, 151, 49, 244, 228, 166, 45, 49, 61, 219, 64, 2, 235, 161, 128, 87, 86, 12],
    [100, 212, 151, 172, 90, 96, 172, 96, 212, 235, 253, 198, 220, 245, 167, 66, 92, 247, 55, 173, 43, 71, 235, 194],
    [26, 25, 171, 223, 176, 200, 159, 47, 112, 136, 129, 172, 210, 217, 6, 73, 34, 235, 0, 201, 61, 192, 212, 201],
    [102, 160, 104, 1, 226, 252, 226, 61, 245, 167, 252, 63, 233, 204, 247, 239, 186, 208, 241, 198, 221, 195, 246, 184],
    [207, 27, 39, 42, 41, 116, 121, 243, 167, 228, 203, 169, 13, 227, 62, 113, 185, 1, 120, 35, 112, 96, 190, 155],
    [88, 254, 96, 231, 86, 29, 112, 167, 232, 200, 1, 109, 31, 205, 179, 125, 236, 148, 37, 62, 32, 75, 33, 227],
    [75, 134, 77, 120, 229, 252, 78, 102, 205, 89, 62, 118, 207, 250, 55, 53, 111, 47, 12, 101, 233, 156, 100, 120],
    [58, 101, 2, 202, 6, 250, 222, 87, 212, 151, 179, 72, 235, 228, 61, 240, 179, 164, 175, 192, 41, 62, 50, 58]
]

consts = [0xfffffffffffa00b1, 0xfffffffffffa608a, 0xfffffffffffa0a1e, 0xfffffffffffa7510, 0xfffffffffff9b125, 0xfffffffffff9e59c, 0xfffffffffff85543, 0xfffffffffff99fda, 0xfffffffffff967ac, 0xfffffffffffa22b9, 0xfffffffffffa49e3, 0xfffffffffff86f81, 0xfffffffffffb7d48, 0xfffffffffff8a759, 0xfffffffffff88a1d, 0xfffffffffff9f131, 0xfffffffffffa59be, 0xfffffffffff78985, 0xfffffffffff9924c, 0xfffffffffff70587, 0xfffffffffff9ac6e, 0xfffffffffff92853, 0xfffffffffffa0636, 0xfffffffffff8dda8]
sum = 0

for i in range(24):
    x = consts[i]
    for j in range(24):
        x = (x + wtf[j] * mults[i][j]) & 0xffffffffffffffff
    sum = sum + (x & 0xffffff)

print(hex(sum))

print(wtf)