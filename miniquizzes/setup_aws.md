##Setting Up Amazon Web Services (AWS)

This week we will be needing a lot of AWS. Following the instructions below to set up your account
and claim the free credit that is available to you.

<br>

##Part 1: Create an AWS account

Go to [http://aws.amazon.com/](http://aws.amazon.com/) and sign up: 

- You may sign in using your existing Amazon account or you can create a new account by selecting
  **Create a free account** using the button at the right, then selecting **I am a new user**.
  
- Enter your contact information and confirm your acceptance of the AWS Customer Agreement.

- Once you have created an Amazon Web Services Account, you may need to accept a telephone call to
  verify your identity. Some people have used Google Voice successfully if you don't have or don't
  want to give a mobile number.
  
- Once you have an account, go to [http://aws.amazon.com/](http://aws.amazon.com/) and sign in. You
  will work primarily from the Amazon Management Console.

- Create Security Credentials.  Go to the 
  [AWS security credentials page](https://console.aws.amazon.com/iam/home?#security_credential).
  If you are asked about IAM users, close the message.  Expand **Access Keys** and click **Create New
  Access Key**.  You will see a message **Your access key (access key ID and secret access key) has been
  created successfully**. Click **Download Key File** and save it to your home directory. 
  
  Remember where this file is. It contains the **Access Key ID** and **Secret Access Key**. 
  
<br>

##Part 2: Setting up an EC2 key pair

To connect to an Amazon EC2 instances, you need to create an **SSH key pair**. 

- After setting up your account, go to the [EC2 console](https://console.aws.amazon.com/ec2)

- Select the region to be **N.Virgina**. Please do not work with another region.

  ![image](img/region.png)

- On the left click **Key Pair** and then **Create Key Pair**
  
  <img height="400px" src="img/keypair.png">
    
- Download and save the `.pem` private key file to a new folder `.ssh` in your home directory. Any folder
  that starts with a `.` will hide the folder. In this case, you want to hide the sensitive information.
  Change the permissions of the file using this command:

  ```$ chmod 400 </path/to/saved/keypair/file.pem>```

<br>

##Part 3: Activate your AWS free credit

As a Galvanize member, you are entitled to some free credits. Follow the steps below to activate your credits.
They will come in around 2 weeks time.

Go to [http://aws.amazon.com/activate/portfolio-signup/](http://aws.amazon.com/activate/portfolio-signup/)
and fill in your details. Make sure the email you fill in is the one you have provided in the 
[spreadsheet](https://docs.google.com/spreadsheets/d/1NL-TZNnKoetI_ute_4lipfv_hldJAvOaIw7VUO5dzgw/edit#gid=0)
earlier. 

**The Org ID is 15UPn. If you cannnot sign up please let one of the instructors know.**

Apply for AWS Activate, using the following information.

    First Name:
    Last Name:
    Email:
    AWS Account Number: (Find in My Account > Account Settings)
    Company Name: Galvanize
    Company URL: http://galvanize.com
    Phone Number: 415-805-1888 
    Industry: Education
    Address: 44 Tehama St, San Francisco, CA 94105
    Country: United States
    State: California
    Postal Code: 94105
    Software Stack: Python
    Level of AWS Usage: Run dev/test workloads
    Organization ID: 15UPn

