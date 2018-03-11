import orionsdk

swis = orionsdk.SwisClient("solarwinds-server", "username", "password")

# This query was made to select the model numbers and IP addresses of every Cisco and Juniper device in the network
devices = swis.query("Select n.IPAddress, j.JnxContentsSerialNo, c.Model FROM Orion.Nodes n INNER JOIN NCM.Nodes AS x ON n.NodeID = x.CoreNodeID RIGHT JOIN NCM.EntityPhysicalJuniper AS j ON x.NodeID =  j.NodeID RIGHT JOIN NCM.EntityPhysical AS c ON x.NodeID =  c.NodeID")

print(devices)
