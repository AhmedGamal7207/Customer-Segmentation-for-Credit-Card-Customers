<h1 align="center">💳 Customer Segmentation for Credit Card Customers</h1>

<p align="center">
  <b>Unsupervised Machine Learning Project</b><br>
  Information Technology Institute (ITI)
</p>

---

<p align="center">
  <img src="https://img.shields.io/badge/Track-AI-blueviolet?style=for-the-badge">
  <img src="https://img.shields.io/badge/Intake-46-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/Branch-Alexandria-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Subject-Unsupervised%20Machine%20Learning-red?style=for-the-badge">
</p>

---

## 👨‍💻 Author Information

- **Name:** Ahmed Gamal Ahmed  
- **Track:** AI – Intake 46 – Alexandria Branch  
- **Subject:** Unsupervised Machine Learning Final Project  

---

## 📌 Project Overview

This repository contains the full implementation of the **Customer Segmentation for Credit Card Customers** project.  
The goal of this project is to apply **unsupervised machine learning techniques** to segment customers based on their financial behavior and credit usage patterns.

---

<details open>
<summary><h1><b>📊 Credit Card Dataset — Data Dictionary (Business + Examples)</b></h1></summary>
<br>
<table>
  <thead>
    <tr>
      <th align="center">Feature Name</th>
      <th align="center">Short Description</th>
      <th align="center">Long Description</th>
      <th align="center">Effects (Insights)</th>
      <th align="center">Todo</th>
      <th align="center">Responsible Value</th>
      <th align="center">Responsible Interpretation</th>
      <th align="center">Irresponsible Value</th>
      <th align="center">Irresponsible Interpreation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>CUST_ID</b></td>
      <td>Identification of Credit Card holder (Categorical)</td>
      <td>Unique ID for each customer.</td>
      <td>No effect</td>
      <td>Check for repetition<br>Drop - Not Useful</td>
      <td align="center"><code>C10001</code></td>
      <td>-</td>
      <td align="center"><code>C10002</code></td>
      <td>-</td>
    </tr>
    <tr>
      <td><b>BALANCE</b></td>
      <td>Balance amount left in their account to make purchases (</td>
      <td>Remaining unpaid amount on the credit card<br>(This is how much the customer still owes the bank)</td>
      <td>High BALANCE → customer carries debt<br>Low BALANCE → customer pays quickly</td>
      <td>-</td>
      <td align="center"><code>300</code></td>
      <td>He spent $2500 this month but paid $2200 already.<br>Business meaning: He doesn’t carry debt. Very controlled.</td>
      <td align="center"><code>6000</code></td>
      <td>She owes $6000 She’s almost maxing her limit</td>
    </tr>
    <tr>
      <td><b>BALANCE_FREQUENCY</b></td>
      <td>How frequently the Balance is updated, score between 0 and 1 (1 = frequently updated, 0 = not frequently updated)</td>
      <td>How often balance is updated. (Shows activity consistency)</td>
      <td>1 → Updated every month (active user)<br>0 → Rarely updated (inactive card)</td>
      <td>-</td>
      <td align="center"><code>0.95</code></td>
      <td>Balance updates almost every month. He uses the card regularly. Active consistent user.</td>
      <td align="center"><code>0.8</code></td>
      <td>Balance changes often. Active but debt heavy.</td>
    </tr>
    <tr>
      <td><b>PURCHASES</b></td>
      <td>Amount of purchases made from account</td>
      <td>Total amount spent using card.</td>
      <td>Measures spending power and consumption level</td>
      <td>-</td>
      <td align="center"><code>2500</code></td>
      <td>Total yearly spending</td>
      <td align="center"><code>1500</code></td>
      <td>Spending is moderate. But balance is high → not paying.</td>
    </tr>
    <tr>
      <td><b>ONEOFF_PURCHASES</b></td>
      <td>Maximum purchase amount done in one-go</td>
      <td>Largest amount spent in a single transaction</td>
      <td>High value → customer makes big purchases (travel,exp)<br>Low value → everyday spending</td>
      <td>-</td>
      <td align="center"><code>1200</code></td>
      <td>Largest single purchase = $1200. Comfortable making large purchases.</td>
      <td align="center"><code>400</code></td>
      <td>No huge purchases. Mostly medium-sized shopping.</td>
    </tr>
    <tr>
      <td><b>INSTALLMENTS_PURCHASES</b></td>
      <td>Amount of purchase done in installment</td>
      <td>Total amount bought using installment plans.</td>
      <td>Shows how much customer prefer to pay in installments</td>
      <td>-</td>
      <td align="center"><code>800</code></td>
      <td>Phone for $800 paid over 8 months.</td>
      <td align="center"><code>1000</code></td>
      <td>Most of purchases in installments.</td>
    </tr>
    <tr>
      <td><b>CASH_ADVANCE</b></td>
      <td>Cash in advance given by the user</td>
      <td>Money withdrawn as cash using credit card. (RISKY)</td>
      <td>High cash advance → financially stressed customer<br>Bank charges high interest here</td>
      <td>-</td>
      <td align="center"><code>0</code></td>
      <td>Very good sign. He never uses expensive emergency borrowing.</td>
      <td align="center"><code>2000</code></td>
      <td>She withdrew $2000 cash Dangerous behavior.</td>
    </tr>
    <tr>
      <td><b>PURCHASES_FREQUENCY</b></td>
      <td>How frequently the Purchases are being made, score between 0 and 1 (1 = frequently purchased, 0 = not frequently purchased)</td>
      <td>How often purchases are made.</td>
      <td>1 → Frequent shopping<br>0 → Rare usage</td>
      <td>Check corr with BALANCE_FREQUENCY</td>
      <td align="center"><code>0.85</code></td>
      <td>He purchases almost every month.</td>
      <td align="center"><code>0.4</code></td>
      <td>Not shopping frequently.</td>
    </tr>
    <tr>
      <td><b>ONEOFFPURCHASESFREQUENCY</b></td>
      <td>How frequently Purchases are happening in one-go (1 = frequently purchased, 0 = not frequently purchased)</td>
      <td>How often large single purchases happen.</td>
      <td>If customer buys big electronics often → high score.</td>
      <td>-</td>
      <td align="center"><code>0.4</code></td>
      <td>Occasionally makes large purchases. Not every month</td>
      <td align="center"></td>
      <td></td>
    </tr>
    <tr>
      <td><b>PURCHASESINSTALLMENTSFREQUENCY</b></td>
      <td>How frequently purchases in installments are being done (1 = frequently done, 0 = not frequently done)</td>
      <td>How often installment purchases occur.</td>
      <td>High → customer regularly buys on EMI<br>Low → rarely uses installment option</td>
      <td>-</td>
      <td align="center"><code>0.3</code></td>
      <td>Sometimes uses installments. Balanced behavior.</td>
      <td align="center"></td>
      <td></td>
    </tr>
    <tr>
      <td><b>CASHADVANCEFREQUENCY</b></td>
      <td>How frequently the cash in advance being paid</td>
      <td>How often customer withdraws cash from credit card.</td>
      <td>High frequency = risky client.</td>
      <td>-</td>
      <td align="center"><code>0</code></td>
      <td>Never withdraws cash</td>
      <td align="center"><code>0.7</code></td>
      <td>Frequently withdrawing cash.</td>
    </tr>
    <tr>
      <td><b>CASHADVANCETRX</b></td>
      <td>Number of Transactions made with "Cash in Advanced"</td>
      <td>Number of cash advance transactions.</td>
      <td>EG: 3 ATM withdrawals</td>
      <td>-</td>
      <td align="center"><code>0</code></td>
      <td>Never withdraws cash</td>
      <td align="center"><code>12</code></td>
      <td>12 ATM withdrawals.</td>
    </tr>
    <tr>
      <td><b>PURCHASES_TRX</b></td>
      <td>Numbe of purchase transactions made</td>
      <td>Number of purchase transactions.</td>
      <td>Customer A: $2000 in 2 transactions (big spender)<br>Customer B: $2000 in 100 transactions (frequent shopper)</td>
      <td>Create the ratio, compare with frequencies</td>
      <td align="center"><code>45</code></td>
      <td>45 purchase transactions. Means that 500$ is made over a lot of trxs</td>
      <td align="center"><code>18</code></td>
      <td>Not many purchases</td>
    </tr>
    <tr>
      <td><b>CREDIT_LIMIT</b></td>
      <td>Limit of Credit Card for user</td>
      <td>Maximum allowed borrowing limit.</td>
      <td>High credit limit → trusted customer</td>
      <td>-</td>
      <td align="center"><code>8000</code></td>
      <td>High credit trust. Bank trusts him</td>
      <td align="center"><code>7000</code></td>
      <td>Almost fully used. Balance = 6000 Limit = 7000 Very Risky</td>
    </tr>
    <tr>
      <td><b>PAYMENTS</b></td>
      <td>Amount of Payment done by user</td>
      <td>Total amount paid by customer.</td>
      <td>If customer paid $1800 during year → PAYMENTS = 1800</td>
      <td>-</td>
      <td align="center"><code>2200</code></td>
      <td>He paid 2200</td>
      <td align="center"><code>800</code></td>
      <td>She paid only $800 total.</td>
    </tr>
    <tr>
      <td><b>MINIMUM_PAYMENTS</b></td>
      <td>Minimum amount of payments made by user</td>
      <td>Minimum required payment paid.</td>
      <td>If bill = $1000, Minimum due = $50<br>If customer pays only $50 → financially weak behavior.</td>
      <td>-</td>
      <td align="center"><code>150</code></td>
      <td>Minimum due was $150 but he paid the whole</td>
      <td align="center"><code>700</code></td>
      <td>She paid just slightly above minimum.</td>
    </tr>
    <tr>
      <td><b>PRCFULLPAYMENT</b></td>
      <td>Percent of full payment paid by user</td>
      <td>Percentage of months where full balance was paid.</td>
      <td>High PRCFULLPAYMENT → responsible<br>Low → revolver (bank earns interest)</td>
      <td>-</td>
      <td align="center"><code>0.95</code></td>
      <td>95% of months he pays full.</td>
      <td align="center"><code>0.1</code></td>
      <td>Only 10% of months she paid full.<br><br>Almost always carries debt.</td>
    </tr>
    <tr>
      <td><b>TENURE</b></td>
      <td>Tenure of credit card service for user</td>
      <td>Number of months/years customer has had the credit card.</td>
      <td>Long tenure → loyal customer<br>Short tenure → new client</td>
      <td>-</td>
      <td align="center"><code>4</code></td>
      <td>4 years customer.</td>
      <td align="center"><code>2</code></td>
      <td>2 years customer</td>
    </tr>
  </tbody>
</table>
<br>
</details>
