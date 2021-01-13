
"""
day 1
"""
# print
#print("hello world")

"""
温度转换

"""
def turnTemp():
    h = float(input("请输入华氏温度"))
    s = (h-32)/1.8
    print("华氏温度%1.f，摄氏温度%1.f" % (h,s))

#turnTemp();

"""
输入半径计算圆的面积和周长

"""
def calCircle():
    r = float(input("请输入半径:"))
    long = 2*3.1415*r
    big = 3.1415 *r *r
    print("圆的周长：%.2f, 面积： %.2f" % (long, big))

calCircle();
