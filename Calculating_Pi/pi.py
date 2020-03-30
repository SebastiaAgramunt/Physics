from random import uniform, seed

def In(x: int, y: int):
    return pow(x,2.0)+pow(y,2.0)<1.0

if __name__ == '__main__':

    seed(1)
    max_iter = 9999999
    i=0
    in_points = 0

    while i<max_iter:
        i+=1

        x = uniform(0,1)
        y = uniform(0,1)

        if In(x, y):
            in_points+=1


    print(4.0*in_points/max_iter)






