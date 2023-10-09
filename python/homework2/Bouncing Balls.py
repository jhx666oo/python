def bouncing_ball(h, bounce, window):
    if h>0.0 and 0.0<bounce<1.0 and h>window:
        flag=1
        while h*bounce>window:
            h*=bounce
            flag+=2
        return flag
    return -1
