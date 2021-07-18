print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("                                    |||***Welcome in SHOAIB shopping App***|||")
print("                                  ==============================================")
print("\n")


def start():
    print("                                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("                                             Press - 1 - to START")
    print("                                        Press - 2 - to EXIT from Program")
    print("                                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("\n")
    while True:
        try:
            v = int(input("Enter your Choice : "))
            print("\n")
            if v == 1:
                loginpannel()
            elif v == 2:
                print("\n")
                print("          |||***Thank you for comming in SHOAIB shopping App***|||")
                print("             ==============================================")
                print("\n")
                exit()
        except Exception as e:
            print('Sorry you choose wrong option')
            print('please try again')

def loginpannel():
    while True:
        try:
            print(' Login Panel')
            print('----------------------------------------')
            print(' press 1 for admin login')
            print(' press 2 for Shopping')
            print(' press 3 to logout')
            print('---------------------------------------')
            while True:
                n = int(input('enter your choice : '))
                if n == 1:
                    adminpass()
                elif n == 2:
                    shopping()
                elif n == 3:
                    exit()
                else:
                    print('Sorry, wrong input given')
                    print('press 1 for logout')
                    print('press 2 for go to main menu')
                    v = int(input('enter your choice : '))
                    if v == 1:
                        print("Thank You for using PYTHON Application")
                        exit()

        except Exception as e:
            print('Sorry you choose wrong option')
            print('please try again')


product=[[11, 'chunni', 300.0, 3, 'very nice product', 'cloth'], [12, 'lehnga', 500.0, 2, 'nice febric', 'cloth']]
cart=[]
def adminpass():
    print('\n')
    password=input('enter password :')
    if password=='admin':
        admin()
    else:
        print('you enter wrong password')
        shopping()


def admin():


    while True:
        print('\n')
        print('\n')
        print('\n')
        print("                     *WELCOME IN ADMIN Panel*")
        print("#######################################################################")
        print("1. to Add Product :")
        print("2. to View all Product :")
        print("3. Search Product by ID :")
        print("4. Search Product by Name :")
        print("5. Search Product by Price Range :")
        print("6. for shopping panel")
        print("7. for exit")
        print("#######################################################################")
        print('\n')

        try:
            ch = int(input('enter your choice :'))

            if ch==1:
                AddProduct()
            elif ch==2:
                ViewProduct()
            elif ch==3:
                searchbyid()
            elif ch==4:
                searchbyname()
            elif ch==5:
                pricerange()
            elif ch==6:
                shopping()
            elif ch==7:
                print("\n")
                print("          |||***Thank you for comming in SHOAIB shopping App***|||")
                print("             ==============================================")
                print("\n")

                exit()
        except Exception as e:
            print('Sorry you insert wrong option')
            print('please try again')
            admin()

def shopping():
    while True:
        print("                     *WELCOME IN SHOPPING PANEL*")
        print("#######################################################################")
        print("1. to View all Product :")
        print("2. Search Product by ID :")
        print("3. Search Product by Name :")
        print("4. Search Product by Price Range :")
        print("5. to Add in Cart :")
        print("6. to View cart and Checkout")
        print("7. for main menu")
        print("8. for exit")
        print("#######################################################################")

        try:
            ch = int(input('enter your choice :'))

            if ch==1:
                ViewProduct()
            elif ch==2:
                searchbyid()
            elif ch==3:
                searchbyname()
            elif ch==4:
                pricerange()
            elif ch==5:
                addcart()
            elif ch == 6:
                viewcart()
            elif ch == 7:
                loginpannel()
            elif ch==8:
                print("\n")
                print("          |||***Thank you for comming in SHOAIB shopping App***|||")
                print("             ==============================================")
                print("\n")

                exit()
        except Exception as e:
            print('Sorry, you insert wrong option try again')
            shopping()


def AddProduct():
    try:
        pid=int(input('enter product id'))
        name=input('Enter product Name:')
        price=float(input('Enter Price:'))
        qty=int(input('Enter Stock:'))
        desc=input("Enter Product Details:")
        cat=input('enter Catogary:')
        for b in product:
            if pid==b[0]:
                print('this product id is already present please insert new id')

        product.append([pid, name, price, qty, desc, cat])
        print('product added succefully:')
    except Exception as e:
        print('you insert wrong',e)



def ViewProduct():
    for i in product:
        print('\n')
        print("----------------------------------")
        print("Product-ID : ", i[0])
        print("Product-Name : ", i[1])
        print("Product price : ", i[2])
        print("Product quantity : ", i[3])
        print("Product description : ", i[4])
        print("Product cat : ",i[5])
        print('\n')
        print("----------------------------------")


def searchbyid():
    try:
        s = int(input("Enter Emp-ID : "))
        for i in product:
            if s == i[0]:
                print('\n')
                print('\n')
                print("----------Your Search ID Product is-----------")
                print("Product-ID : ", i[0])
                print("Product-Name : ", i[1])
                print("Product price : ", i[2])
                print("Product quantity : ", i[3])
                print("Product description : ", i[4])
                print("Product cat : ", i[5])
                print('\n')
                print('\n')
                print("------------------------------------------------")
                continue
            else:
                print('this ID Product is not available ')
                print('try again')
                break
    except Exception as e:
        print('\n')
        print('you not insert number Please insert number')
        print('\n')



def searchbyname():
    try:
        s = input("Enter Product Name : ")
        for i in product:
            if s == i[1]:
                print("-----------Your Search name Product is----------------")
                print("Product-ID : ", i[0])
                print("Product-Name : ", i[1])
                print("Product price : ", i[2])
                print("Product quantity : ", i[3])
                print("Product description : ", i[4])
                print("Product cat : ", i[5])
                print("-------------------------------------------------------")
                continue
            else:
                print('you insert wrong name ')
                print('try again')
                break
    except Exception as e:
        print('\n')
        print('you not insert alpphabet Please insert alphabet')
        print('\n')



def pricerange():
    try:
        s1 = int(input("Enter 1st Salary Range : "))
        s2 = int(input("Enter 2nd Salary Range : "))
        for i in product:
            if i[2] >= s1 and i[2] <= s2:
                print("Product Details between Price Range : ", s1, " - ", s2)
                print("----------------------------------")
                print("Product-ID : ", i[0])
                print("Product-Name : ", i[1])
                print("Product price : ", i[2])
                print("Product quantity : ", i[3])
                print("Product description : ", i[4])
                print("Product cat : ", i[5])
                continue
            else:
                print('Sorry, this range product are not available')
                break
    except Exception as e:
        print('\n')
        print('you not insert number Please insert number')
        print('\n')


def addcart():
    try:
        s=int(input('enter Product ID to add cart'))
        for i in product:
            if s==i[0]:
                cart.append(i)
                print('\n')
                print('Your Product Added Successfully in your cart')
                print('\n')
                print('             name is  :',i[1])
                print('             price is :',i[2])
                print('\n')
                break
            else:
                print("you choose wrong product id")
                print("try again")
                break
    except Exception as e:
        print('\n')
        print('you not insert number Please insert number')
        print('\n')


def viewcart():
    if len(cart)==0:
        print('\n')
        print('\n')
        print('your cart is empty select something')
        print('\n')
        print('\n')
    else:
        count=0
        for i in cart:
            print('\n')
            print("----------------------------------")
            print("Product-ID : ", i[0])
            print("Product-Name : ", i[1])
            print("Product price : ", i[2])
            print("Product quantity : ", i[3])
            print("Product description : ", i[4])
            print("Product cat : ", i[5])
            print('\n')
            print("----------------------------------")
            count=count+i[2]

        print('if you want to continue to shopping press 1')
        print('press 2 for bill and exit')
        o=int(input('enter your choice: '))
        if o==1:
            start()
        elif o==2:
            for x in cart:
                print("your Product name is [",x[1],"] and item price is =",x[2])
            print("                                               Total=",count)
            print("\n")
            print("          |||***Thank you for comming in SHOAIB shopping App***|||")
            print("             ==============================================")
            print("\n")

            exit()



start()
