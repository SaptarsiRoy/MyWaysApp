[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

---

## 📝 Table of Contents

- [Problem Statement](#prstatement)
- [Website Frontend Designing](#webdesign) 
- [Deployment](#deploy)
- [How to deploy](#howdeploy)
- [Built Using](#built_using)
- [Working Prototype](#work-pics)
- [Destroy the environment](#destroy)
- [Author](#author)

---

## 🧐 [Problem Statement](#prstatement)

To create a simple web application for <strong>Candidate Portal</strong> which has some basic functionalities of - 
    - Add the details of a new candidate
    - Delete the details of an existing Candidate
    - Search for the details of a candidate from the database

The portal has the provision to upload a unique candidate ID, their name and a short profile description. 

The infrastructure has been deployed using relevant AWS services for frontend-backend integration and tweaked with an implemented CI/CD using proper automation tool.

<br>

## 🚀 [Website Frontend Designing](#webdesign) 

The frontend comprises of the wesite pages coded exclusively in HTML, CSS and Javascript. 

1. <u>Home page</u><br>
The <strong>main or home page</strong>, framed as <i>index.html</i>, provides the user a list of choices of action. For the functionality of searching a candidate's details, a search bar has been implemented styled with CSS. Simultaneously, adding or deleting of candidate details occurs via hyperlinked buttons, that redirects to the corresponding webpages.

2. <u>Page for adding details of a new candidate</u><br>
The <strong>add page</strong>, framed as <i>add/add.html</i>, is a simple form that has the fields to input <i>Candidate Unique ID</i>, <i>Name</i>, and <i>Candidate description</i>. Candidate Unique ID and Name are simple text inputs whereas Candidate Description is a text area of 5 rows and 162 columns. The form is concluded with a responsive <i>Add button</i> that forwards the add functionality.

3. <u>Page for deleting details of an existing candidate</u><br>
The <strong>delete page</strong>, framed as <i>del/del.html</i>, is again a form that inputs only the Unique ID of the candidate whose details needs to be deleted. The <i>Delete</i> button next to the ID input provides the delete functionality to the page.

<br>

## 🎈 [Deployment Strategy](#deploy)
Since the website has been made responsive, there exists a backend tier to the frontend site. The backend tier has been deployed with the help of AWS service, <strong>AWS Lambda</strong>.  The Lambda contains respective functions that are invoked by respective API calls. The backend also contains a <strong>DynamoDB</strong> table as the database.

The launched EC2 instance has a configured <strong>Apache HTTPD webserver</strong> using Ansible and contains the webpages and the <strong>CGI scripts<strong> that integrate with the API and acts as a bridge between the frontend and the backend.

❗ <strong>NOTE:</strong> ❗ <br>
In order to deploy the frontend webpages, there is a much safer and higher availability option of using the object storage S3 service. But for a greater cause, EC2 is a better option here. This is so because -
<br>
    1. Since here's an integration of CGI scripts with the API for bridging the frontend and backend, this  approach would not have been implementable in case S3 was used, because S3 is a simple object storage service and does not allow CGI integration.
<br>
    2. Using EC2 instead allows the developers to implement an internal loadbalancing service, in order to reduce any data loss or latency.

<br>

## ❓ [How to deploy with CI/CD](#howdeploy)
### <strong><u>Pre Requisites</u></strong>
1. AWS account
2. IAM user in the AWS account with the following accesse:-
   - IAMFullAccess
   - IAMUserChangePassword
   - PowerUserAccess
3. Git CLI, Terraform and Ansible installed in system
4. Preferred OS - Linux

<br>

The following steps to be followed to view the website in own machine:-

- Clone the repository using git cli.
```
git clone https://github.com/SaptarsiRoy/MyWaysApp.git
```

- Change the profile name and region (your preferred region) in <i>provider.tf</i> file.
```
provider "aws" {
    region="YOUR PREFERRED REGION"
    profile="YOUR PROFILE"
}
```
- Initialise the terraform providers.
```
terraform init
```
<img src="https://raw.githubusercontent.com/SaptarsiRoy/MyWaysApp/main/.media/init.png" height="300" width="500">

- Apply the terraform code to setup the infrastructure (when propmted for approval, enter 'yes').
```
terraform apply
```
<img src="https://raw.githubusercontent.com/SaptarsiRoy/MyWaysApp/main/.media/apply.png" height="300" width="500">

<br>

After successful deployment of the terraform code, three API's for three different functions need to be created. In order to create the API's and add the API endpoints into proper file for further use, please go through the following [video](https://drive.google.com/file/d/1bumCk0zzsXJneRx8IuqmlJuucjFVSWFJ/view?usp=sharing).

<br>

Finally, its the turn of running the ansible playbook!
```
ansible-playbook play.yml
```
<img src="https://raw.githubusercontent.com/SaptarsiRoy/MyWaysApp/main/.media/ansible.png" height="300" width="500">

<br>

## ⛏️ [Built Using](#toc)

- [RHEL-8](https://www.redhat.com/en/enterprise-linux-8) - Base OS
- [AWS](https://aws.amazon.com/) - Cloud Service Provider
- [Terraform](https://www.terraform.io/) - Infrastructure as a Code
- [Ansible](https://www.ansible.com/) - Configuration Management

<br>

## 📊 [Working Prototype](#work-pics)
A video exhibiting the working prototype of the website is available [here](https://drive.google.com/file/d/1g2q85NUYLOu_B3z8-uoh0t6BgBQfAKVp/view?usp=sharing)! Please have a look...

<br>

## ❌ [Destroy the environment](#destroy)
After testing of all the setup, in order to destroy the whole architecture, use the command -
```
terraform destry -auto-approve
```
<br>

Also, reach out to the API Gateway Portal in AWS console to delete the created API.

<br>

---
## ✍️ [Author](#author)
 [Saptarsi Roy](https://www.linkedin.com/in/saptarsiroy/)
