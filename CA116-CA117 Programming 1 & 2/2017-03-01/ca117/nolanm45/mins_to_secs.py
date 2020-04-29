def mins_to_secs(t):
    t=t.split(":")
    minute=t[0]
    seconds=t[1]
    return(int(minute)*60 + int(seconds))


def main():
   print(mins_to_secs("6:00"))

if __name__=="__main__":
     main()
