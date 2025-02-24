# AWS MySQL Instance Setup and Security Guide

## **1. Overview**
This guide provides steps to securely set up and connect to an AWS-hosted MySQL database while ensuring only authorized users have access.

## **2. Finding Your Public IP**
Before modifying security settings, find your public IP address:
```bash
curl ifconfig.me
```
Example output:
```
106.216.68.90
```
This IP will be used to allow access to MySQL.

## **3. Configuring AWS Security Groups**
### **Step 1: Access AWS Security Groups**
1. Log in to the [AWS Console](https://aws.amazon.com/console/).
2. Go to **EC2 Dashboard** > **Security Groups** (under "Network & Security").
3. Locate the Security Group associated with your MySQL instance.

### **Step 2: Modify Inbound Rules**
1. Click **Inbound rules** > **Edit inbound rules**.
2. Remove any rule that allows `0.0.0.0/0` or `::/0` on port `3306`.
3. Add a new rule:
   - **Type:** MySQL/Aurora
   - **Protocol:** TCP
   - **Port Range:** 3306
   - **Source:** My IP
   - **Value:** `106.216.68.90/32` _(Replace with your public IP)_
4. Save the changes.

## **4. Connecting to MySQL**
Use the following command to connect from your local machine:
```bash
mysql -u admin -h <AWS_INSTANCE_PUBLIC_IP> -p
```
Enter your MySQL password when prompted.

## **5. Granting Access to a Specific IP in MySQL**
If needed, explicitly grant access from your IP in MySQL:
```sql
GRANT ALL PRIVILEGES ON your_database.* TO 'admin'@'106.216.68.90' IDENTIFIED BY 'your_password';
FLUSH PRIVILEGES;
```
Replace `your_database`, `admin`, `your_password`, and `106.216.68.90` as necessary.

## **6. Best Practices**
- 🚀 **Do not use `0.0.0.0/0` for MySQL connections**; always restrict access to known IPs.
- 🔐 **Use a VPN or Bastion Host** instead of directly exposing your MySQL instance.
- 🔄 **Rotate credentials regularly** and disable remote `root` login with:
  ```sql
  UPDATE mysql.user SET Host='localhost' WHERE User='root';
  FLUSH PRIVILEGES;
  ```

## **7. Troubleshooting**
- ❌ If unable to connect:
  - Ensure **your IP matches the allowed IP** in the security group.
  - If using **AWS RDS**, verify **Public Accessibility** is enabled.
  - Check if the MySQL server is **running** and allows remote connections.

✅ **Now your MySQL instance is secure and accessible only from trusted sources!** 🚀

