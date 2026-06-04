import mysql.connector as m
con=m.connect(host='localhost',user='root',passwd='your_passwd', database='inventory_management_system')
cur=con.cursor()

role=input("Are you an employee or an admin? ").lower()
password=input("Enter password: ")

if role=='admin':
    if password=='admin123':
        print('Successful login')
        while True:
            print('''Welcome! 
                  Choose the command which you want to perform from the below listed command
                  1. Add product
                  2. View inventory
                  3. Update product
                  4. Delete product
                  5. Search product
                  6. Sort product
                  7. Sell Product
                  8. Total Sales amount
                  9. Exit''')
        
            choice=int(input('Enter choice(1-9):  '))

            if choice==1:
                a=int(input('How many products do you want to enter?:  '))
                for i in range(a):
                    pd=int(input("Enter Product ID: "))
                    pname=input('Enter Product Name: ')
                    cat=input("Enter category of the product: ")
                    quan=int(input("Enter quantity: "))
                    price=int(input("Enter price per unit: "))
                    query1=f"insert into inventory (product_id, product_name, category, quantity, price) values ({pd}, '{pname}', '{cat}', {quan}, {price})"
                    cur.execute(query1)
                con.commit()
                print('Record(s) added succesfully')

            elif choice==2:
                query2="select * from inventory"
                cur.execute(query2)
                data=cur.fetchall()
                for i in data:
                    print(i)
                print("Here's the inventory!")   
            
            elif choice==3:
                prod_id=int(input("Enter product ID that you want to update: "))
                print(''' Select from the following:
              1. Update product name
              2. Update category
              3. Update quantity
              4. Update price''')
                ch=int(input('Enter choice (1-4):  '))
                if ch==1:
                    prod_name=input("Enter new product name")
                    query3_1=f"update inventory set product_name='{prod_name}' where product_id={prod_id}"
                    cur.execute(query3_1)
                    con.commit()
                    print('Successfull!')

                elif ch==2:
                    categ=input('Enter category')
                    query3_2=f"update inventory set category='{categ}' where product_id={prod_id}"
                    cur.execute(query3_2)
                    con.commit()
                    print('Successfull!')
                
                elif ch==3:
                    q=int(input("Enter quantity: "))
                    query3_3=f"update inventory set quantity={q} where product_id={prod_id}"
                    cur.execute(query3_3)
                    con.commit()
                    print('Successfull!')
                    
                elif ch==4:
                    pr=int(input('Enter Price: '))
                    query3_4=f"update inventory set price={pr} where product_id={prod_id}"
                    cur.execute(query3_4)
                    con.commit()
                    print("Successfull!")
            
            elif choice==4:
                d_id=int(input("Enter product ID:  "))
                query4=f"delete from inventory where product_id={d_id}"
                cur.execute(query4)
                con.commit()
                print("Successfully deleted")

            elif choice==5:
                s_id=int(input("Enter product ID: "))
                query5=f"select * from inventory where product_id={s_id}"
                cur.execute(query5)
                data=cur.fetchall()
                for i in data:
                    print(i)

            elif choice==6:
                sor=input('''Do you want to sort the products in ascending order or descending order?
                          Type asc for ascending and desc for descending''').lower()
                sor_cat=input('''Enter the category by which you want to sort your products
                              1. Price
                              2. ProductID
                              3. Quantity''').lower()
                if sor_cat=='price':
                    if sor=='asc':
                        query6_1="select * from inventory order by price"
                        cur.execute(query6_1)
                        data=cur.fetchall()
                        for i in data:
                            print(i)
                    else:
                        query6_2="select * from inventory order by price desc"
                        cur.execute(query6_2)
                        data=cur.fetchall()
                        for i in data:
                            print(i)
                
                if sor_cat=='productid':
                    if sor=='asc':
                        query6_3="select * from inventory order by product_id"
                        cur.execute(query6_3)
                        data=cur.fetchall()
                        for i in data:
                            print(i)
                    if sor=='desc':
                        query6_4="select * from inventory order by product_id desc"
                        cur.execute(query6_4)
                        data=cur.fetchall()
                        for i in data:
                            print(i)
                            
                if sor_cat=='quantity':
                    if sor=='asc':
                        query6_5="select * from inventory order by quantity"
                        cur.execute(query6_5)
                        data=cur.fetchall()
                        for i in data:
                            print(i)
                    if sor=='desc':
                        query6_6="select * from inventory order by quantity desc"
                        cur.execute(query6_6)
                        data=cur.fetchall()
                        for i in data:
                            print(i)

            elif choice==7:
                p_id=int(input("Enter product ID of the product to be sold"))
                quan_sell=int(input("Enter no. of quantities to be sold"))
                query7=f"update inventory set quantity=quantity - {quan_sell} where product_id={p_id}"
                cur.execute(query7)
                con.commit()
                query_check=f"select quantity from inventory where product_id={p_id}"
                cur.execute(query_check)
                data=cur.fetchone()
                if data:
                    qty=data[0]
                    if qty<10:
                        print("Product is low in stock!!")
                    else:
                        print("Sufficient stock")

            elif choice==8:
                query8="select sum(price) from inventory"
                cur.execute(query8)
                data=cur.fetchall()
                for i in data:
                    print(i)

            else:
                print("Thank-you!")
                break
    
    else:
        print("Wrong input")

if role=='employee':
    if password=='emp123':
        print("Successfull login")
        while True:
             print('''Welcome! 
                  Choose the command which you want to perform from the below listed command
                  1. View inventory
                  2. Search product
                  3. Sort product
                  4. Sell Product
                  5. Total Sales amount
                  6. Exit''')
             
             choice=int(input('Enter choice(1-6):  ')) 

             if choice==1:
                query="select * from inventory"
                cur.execute(query)
                data=cur.fetchall()
                for i in data:
                    print(i)
                print("Here's the inventory!")   

             elif choice==2:
                s_id=int(input("Enter product ID: "))
                query2=f"select * from inventory where product_id={s_id}"
                cur.execute(query2)
                data=cur.fetchall()
                for i in data:
                    print(i)
                
             elif choice==3:
                 sor=input('''Do you want to sort the products in ascending order or descending order?
                          Type asc for ascending and desc for descending''').lower()
                 sor_cat=input('''Enter the category by which you want to sort your products
                              1. Price
                              2. ProductID
                              3. Quantity''').lower()
                 if sor_cat=='price':
                    if sor=='asc':
                        query3_1="select * from inventory order by price"
                        cur.execute(query3_1)
                        data=cur.fetchall()
                        for i in data:
                            print(i)
                    else:
                        query3_2="select * from inventory order by price desc"
                        cur.execute(query3_2)
                        data=cur.fetchall()
                        for i in data:
                            print(i)
                
                 if sor_cat=='productid':
                    if sor=='asc':
                        query3_3="select * from inventory order by product_id"
                        cur.execute(query3_3)
                        data=cur.fetchall()
                        for i in data:
                            print(i)
                    if sor=='desc':
                        query3_4="select * from inventory order by product_id desc"
                        cur.execute(query3_4)
                        data=cur.fetchall()
                        for i in data:
                            print(i)

                 if sor_cat=='quantity':
                    if sor=='asc':
                        query3_5="select * from inventory order by quantity"
                        cur.execute(query3_5)
                        data=cur.fetchall()
                        for i in data:
                            print(i)
                    if sor=='desc':
                        query3_6="select * from inventory order by quantity desc"
                        cur.execute(query3_6)
                        data=cur.fetchall()
                        for i in data:
                            print(i)

             elif choice==4:
                p_id=int(input("Enter product ID of the product to be sold"))
                quan_sell=int(input("Enter no. of quantities to be sold"))
                query4=f"update inventory set quantity=quantity - {quan_sell} where product_id={p_id}"
                cur.execute(query4)
                con.commit()
                query_check=f"select quantity from inventory where product_id={p_id}"
                cur.execute(query_check)
                data=cur.fetchone()
                if data:
                    qty=data[0]
                    if qty<10:
                        print("Product is low in stock!!")
                    else:
                        print("Sufficient stock")    

             elif choice==5:
                query5="select sum(price) from inventory"
                cur.execute(query5)
                data=cur.fetchall()
                for i in data:
                    print(i)

             else:
                print("Thank-you!")
                break    

    else:
        print("Unsuccessful login")        

                

                

                
        
            
    
    



    




    

