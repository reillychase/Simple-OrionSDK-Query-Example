# Python OrionSDK Simple Query Example
***Quickstart***

Main.py is a simple example of a Solarwinds SQL query.

It uses Python OrionSDK library: https://github.com/solarwinds/orionsdk-python

Reading the DB schema documentation was very helpful in building this query https://solarwinds.github.io/OrionSDK/schema/index.html

Understanding how SQL works in general will also be very helpful in knowing how to build your query https://www.w3schools.com/sql

**Troubleshooting**

One of the difficult parts I had was an error message of "cannot convert GUID to data type Int32". After looking at the DB schema, I found that trying to join NodeID of the table I was on with NodeID of Orion.Nodes wasn't going to work because one was type Int32 and the other was type GUID. What I found out was I had to first join that table back to NCM.Nodes and then join NCM.CoreNodeID to Orion.Nodes.

Another difficulty I had was when I was looking at Cirrus table, and I found out later that the Cirrus module has been discontinued in place of Network Configuration Manager module. So I used the NCM tables instead.
