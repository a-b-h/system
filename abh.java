#steps to genrate app pass of google account 
go to google account 
security 
2step veri. :on
app pass
select app : email
select device: window computer


#steps to configure app password with jenkins
manage jenkins
configure system
email notification
smtp serve: smtp.gmail.com
select use smtp authentica
username : jain931838@gmail.com
pass : copy-paste google app

select use ssl

smtp port : 465
reply to address: jain931838@gmail.com

select test config...
test email reciepient : jain931838@gail.com
apply and save

Role based authorization 

manage jenkins 
manage plugin 
available plugin
role-based-autho
install wihtout restart

configure global setting 
authorization-Role based-startegy
appy& save 

manage & assign roles
manage roles 
roles to add
developer1 : add(assign developer perms)
developer2 : add(assign developer perms)
QA1: add(assign qa perms)
QA2: add(assign qa perms)
Devops1 : add(same)
admin

give permission all overall read&job,job discover to view configure vire c&r
apply save 

manage jenkins 
manage users
create user (username & pwd)
username-dev1

dashboard -manage jenkins-manage and assign 
search developer1(add)-developer role
qa1-qa role ,devops-devops role
apply and save 

now open the brwser
localhost:8080
now open developer 1 & you not see manage option 
 

