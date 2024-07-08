"# CodeMonk" 
"Steps to run this project"

1. git clone :

       git clone https://github.com/TRahulT/CodeMonk.git
    
2. After succussful clone Open the project in any IDE ( vscode, pycharm or any other )
   
3. Start the Docker Desktop application
   
4. open the terminal  in IDE (VSCode) and type  docker-compose command ->

          docker-compose run web python manage.py migrate
   
5. next command ->

          docker-compose run web python manage.py makemigrations
   
6. next command ->
    
              docker-compose run web python manage.py migrate
 
7. make sure these command make images inside docker  desktop application  
                i) codemon-web  size --1.11 GB approx
   
                ii) postgres    size   450 MB approx
   
                iii) check migrate and migration command  reflect succussfully
   
8. next command ->

       docker-compose run web python manage.py createsuperuser
   
9. last step -->

         docker-compose up 
    
"Open the admin panel first "
 
     -> http://127.0.0.1:8000/admin/
---> click on CustomUser --> create a User mannual  for example  name = Ram and email = ram@gmail.com 

Note -->  Please Don't think Why you are  doing this mannually , its just because of Security purpose because we can't access the "CustomUserCreate" API without 
                  a Token
---> make sure the Custom User is Created successfully

![image](https://github.com/TRahulT/CodeMonk/assets/89895996/f5e15914-07ce-40bd-8ab7-8ea8a6339010)


"For testing the REST API'S open POSTMAN" :
     
-> I used TokenAuthentication Here: for the  API's  by creating A Middleware.py file

Steps :

1) http://127.0.0.1:8000/customuser-login/
       i) request -> POST
    
                       {
                              "name":"Ram",
                              "email":"ram@gmail.com"   # case senstive 
                            }
3) it will return the Response :

                       {
                        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE3MjA0OTg2NzIuNTg4NDA2fQ.0V-sVBC_-snXePUuJpjrX1LOmRTj3dmFhqSpuOsuzQw",
                        "message": "CustomUser logged in successfully.",
                        "is_log": true,
                        "username": "Ram"
                        }
   
4) Use this Token to access all the other API's 

"For Upload the TEXT "
            -> make a new POST https Request in POSTMAN 
            
                    i) http://127.0.0.1:8000/upload/
                    ii) Authorization --> Bearer Token -> add the token here which is generated by the customuser-login
                    iii) Body --> Form-data  
                    
 ![image](https://github.com/TRahulT/CodeMonk/assets/89895996/df1a9810-5d26-4252-bfc8-4c33f833cab4)
 
 ● A paragraph is defined by two newline characters.
<img width="653" alt="image" src="https://github.com/TRahulT/CodeMonk/assets/89895996/dcb4da82-8585-4327-8b8c-befba02fc5d1">

"For Search " 
            -> make a new GET https Request in POSTMAN 
            
                    i) http://127.0.0.1:8000/search/{key}/   key : can be anything from the TEXT
 ![image](https://github.com/TRahulT/CodeMonk/assets/89895996/2fc5781b-229d-4c13-a3b8-08a04911e069)

NOTE : If it doen't work feel free to contact me gmail : gujjarrahul716@gmail.com
