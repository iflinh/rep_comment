print('Chuong trinh tinh giai thua cua mot so:')
n = int(input('Nhap vao so tu nhien n: '))

def gt__f(n): #nhan tu nho den lon
    gt = 1
    if n == 0 or n == 1:
        return 1
    else :
        for i in range(1, n + 1):
            gt = gt * i
        return gt



def gt2__f(n): #nhan tu lon den nho
    gt2 = n
    k = n
    if n > 2:
        for i in range(n):
            gt2 = gt2 * (n - 1)
            if n < 3: break
            n = n - 1
        return gt2
    elif n == 0 or n == 1:
        return 1



def fact(n): #ham truy hoi, copy cua nguoi ta
    if n == 0:
        return 1
    return n * fact(n - 1)

print('Giai thua cua',n, 'theo fact la: ', fact(n))
print('Giai thua cua',n, 'theo gt1 la : ', gt__f(n))
print('Giai thua cua',n, 'theo gt2 la : ', gt2__f(n))
print('fact la ham truy hoi, gt1 la 1*2*3*4..., gt2 la 9*8*7*6*5...')

#Còn 2 cách nữa mà hay ở đây: https://gist.github.com/phamkhactuy/4197065
#Cách khác tự viết theo mảng

print('Chuong trinh tinh giai thua: ')
n = int(input('Nhap: n = '))
tn = type(n)
def gt4__f(n):
    if n < 0:
        print('Ban da nhap n sai.')
        quit()
    else:
        if n == 0:
            return [1]
        else:
            stn__l = []
            for i in range(1, n+1):
                stn__l.append(i)
            gt__l = [1]
            for i in range(1, n):
                gt__l.append(gt__l[i-1] * (i +1) )
            return gt__l

# print('Mang giai thua cua ', n, 'la: ', gt4__f(n))
manggt__l = gt4__f(n)
socuoi = str(manggt__l[-1])
dodaisocuoi = len(socuoi)
print(dodaisocuoi) #cách này tính được độ dài số 50k! mà không tính được 100k! (60k! có 260635 chữ số)

