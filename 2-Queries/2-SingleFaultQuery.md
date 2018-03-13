Name:  Pull all instances of a particular Fault
Method: GET
URL:  https://{{APIC}}/api/node/class/faultInfo.json?query-target-filter=eq(faultInfo.code,"{{FAULT}}")

Description:  This recipe pulls all instances of a particular fault code "FAULT"

Sample Faults:
  F0532 - Physical Interface or Port-Channel is down, but used by an ePG.

For a list of faults, see [Cisco Documentation](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/aci/apic/sw/2-x/syslog/guide/b_ACI_System_Messages_Guide.html)