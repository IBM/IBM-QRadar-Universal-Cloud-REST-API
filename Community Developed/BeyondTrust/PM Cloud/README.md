# BeyondTrust PM Cloud + IBM QRadar Integration

***Written and maintained by:** BeyondTrust Corporation*

These workflows facilitate the integration between BeyondTrust Privilege Management Cloud and IBM QRadar.  They are intended to be used in conjuction with the [BeyondTrust Privilege Management Cloud extension](https://apps.xforce.ibmcloud.com/extension/6826dcbb3d0255c0545903d26cb969e6) available in the [IBM Security App Exchange](https://apps.xforce.ibmcloud.com/).

The integration consists of:
- a pair of workflow definitions that are leveraged by IBM's Universal Cloud REST API Protocol (located alongside this README)
- corresponding workflow parameters files (also located alongside this README)
- an extension package which provides Log Source Categories, Log Source Extensions, Event Mappings, QID Records, and other components 

---

# Documentation

Please refer to the published documentation available on the BeyondTrust site for the latest information on this integration as well as BeyondTrust Privilege Management.

- [Integration Install Guide](https://docs.beyondtrust.com/epm-wm/docs/qradar)
- [Endpoint Privilege Management for Windows and Mac](https://docs.beyondtrust.com/epm-wm/docs/welcome-to-endpoint-privilege-management-for-windows-and-mac)
- [Endpoint Privilege Management for Linx](https://docs.beyondtrust.com/epm-l/docs/index)

---

# Troubleshooting and Support

Should you encounter issues with event ingestion, the application does write to the standard QRadar log and error log.  Review these logs first to determine if an issue has occurred.

You can find more information on QRadar logs, including how to access them, here:  [https://www.ibm.com/docs/en/qsip/7.5?topic=problems-qradar-log-files](https://www.ibm.com/docs/en/qsip/7.5?topic=problems-qradar-log-files)

For any issues which require additional assistance, please contact BeyondTrust Support at [mysupport@beyondtrust.com](mailto:mysupport@beyondtrust.com) or through the Customer Support Portal.