#task4: Fibonacci Sequence


def fibonacci():
    num= int(input("Enter number of terms: "))
    a=0
    b=1
    count=0
    print("The Fibonacci sequence up to", num, "terms:", a, end=" ")
    print(b,end=" ")

    while(num-2>count):
        result=a+b
        print(result,end=" ")
        a=b
        b=result
        count=count+1
fibonacci()
