grant_csv_titles = [
    "Identifier",
    "Title",
    "Description",
    "Currency",
    "Amount Awarded",
    "Award Date",
    "URL",
    "Planned Dates:Duration (months)",
    "Recipient Org:Identifier",
    "Recipient Org:Name",
    "Recipient Org:Charity Number",
    "Recipient Org:Company Number",
    "Recipient Org:Location:0:Geographic Code Type",
    "Recipient Org:Location:0:Geographic Code",
    "Recipient Org:Location:0:Name",
    "Recipient Org:Location:1:Geographic Code Type",
    "Recipient Org:Location:1:Geographic Code",
    "Recipient Org:Location:1:Name",
    "Recipient Org:Location:2:Geographic Code Type",
    "Recipient Org:Location:2:Geographic Code",
    "Recipient Org:Location:2:Name",
    "Funding Org:Identifier",
    "Funding Org:Name",
    "Grant Programme:Code",
    "Grant Programme:Title",
    "Grant Programme:URL",
    "Beneficiary Location:0:Name",
    "Beneficiary Location:0:Country Code",
    "Beneficiary Location:0:Geographic Code",
    "Beneficiary Location:0:Geographic Code Type",
    "Beneficiary Location:1:Name",
    "Beneficiary Location:1:Country Code",
    "Beneficiary Location:1:Geographic Code",
    "Beneficiary Location:1:Geographic Code Type",
    "Beneficiary Location:2:Name",
    "Beneficiary Location:2:Country Code",
    "Beneficiary Location:2:Geographic Code",
    "Beneficiary Location:2:Geographic Code Type",
    "Beneficiary Location:3:Name",
    "Beneficiary Location:3:Country Code",
    "Beneficiary Location:3:Geographic Code",
    "Beneficiary Location:3:Geographic Code Type",
    "Beneficiary Location:4:Name",
    "Beneficiary Location:4:Country Code",
    "Beneficiary Location:4:Geographic Code",
    "Beneficiary Location:4:Geographic Code Type",
    "Beneficiary Location:5:Name",
    "Beneficiary Location:5:Country Code",
    "Beneficiary Location:5:Geographic Code",
    "Beneficiary Location:5:Geographic Code Type",
    "Beneficiary Location:6:Name",
    "Beneficiary Location:6:Country Code",
    "Beneficiary Location:6:Geographic Code",
    "Beneficiary Location:6:Geographic Code Type",
    "Beneficiary Location:7:Name",
    "Beneficiary Location:7:Country Code",
    "Beneficiary Location:7:Geographic Code",
    "Beneficiary Location:7:Geographic Code Type",
    "The following fields are not in the 360 Giving Standard and are added by grantnav.",
    "Data Source",
    "Publisher:Name",
    "Recipient Region",
    "Recipient District",
    "Recipient Ward",
    "Retrieved for use in GrantNav",
    "License (see note)",
    "Note: this file also contains OS data © Crown copyright and database right 2016, Royal Mail data © Royal Mail copyright and Database right 2016, National Statistics data © Crown copyright and database right 2015 & 2016, see http://grantnav.threesixtygiving.org/datasets/ for more information.",
]

grant_csv_paths = [
    "result.id",
    "result.title",
    "result.description",
    "result.currency",
    "result.amountAwarded",
    "result.awardDate",
    "result.recipientOrganization.0.url",
    "result.plannedDate.duration",
    "result.recipientOrganization.0.id",
    "result.recipientOrganization.0.name",
    "result.recipientOrganization.0.charityNumber",
    "result.recipientOrganization.0.companyNumber",
    "result.recipientOrganization.0.location.0.geoCodeType",
    "result.recipientOrganization.0.location.0.geoCode",
    "result.recipientOrganization.0.location.0.name",
    "result.recipientOrganization.0.location.1.geoCodeType",
    "result.recipientOrganization.0.location.1.geoCode",
    "result.recipientOrganization.0.location.1.name",
    "result.recipientOrganization.0.location.2.geoCodeType",
    "result.recipientOrganization.0.location.2.geoCode",
    "result.recipientOrganization.0.location.2.name",
    "result.fundingOrganization.0.id",
    "result.fundingOrganization.0.name",
    "result.grantProgramme.0.code",
    "result.grantProgramme.0.title",
    "result.grantProgramme.0.url",
    "result.beneficiaryLocation.0.name",
    "result.beneficiaryLocation.0.countryCode",
    "result.beneficiaryLocation.0.geoCode",
    "result.beneficiaryLocation.0.geoCodeType",
    "result.beneficiaryLocation.1.name",
    "result.beneficiaryLocation.1.countryCode",
    "result.beneficiaryLocation.1.geoCode",
    "result.beneficiaryLocation.1.geoCodeType",
    "result.beneficiaryLocation.2.name",
    "result.beneficiaryLocation.2.countryCode",
    "result.beneficiaryLocation.2.geoCode",
    "result.beneficiaryLocation.2.geoCodeType",
    "result.beneficiaryLocation.3.name",
    "result.beneficiaryLocation.3.countryCode",
    "result.beneficiaryLocation.3.geoCode",
    "result.beneficiaryLocation.3.geoCodeType",
    "result.beneficiaryLocation.4.name",
    "result.beneficiaryLocation.4.countryCode",
    "result.beneficiaryLocation.4.geoCode",
    "result.beneficiaryLocation.4.geoCodeType",
    "result.beneficiaryLocation.5.name",
    "result.beneficiaryLocation.5.countryCode",
    "result.beneficiaryLocation.5.geoCode",
    "result.beneficiaryLocation.5.geoCodeType",
    "result.beneficiaryLocation.6.name",
    "result.beneficiaryLocation.6.countryCode",
    "result.beneficiaryLocation.6.geoCode",
    "result.beneficiaryLocation.6.geoCodeType",
    "result.beneficiaryLocation.7.name",
    "result.beneficiaryLocation.7.countryCode",
    "result.beneficiaryLocation.7.geoCode",
    "result.beneficiaryLocation.7.geoCodeType",
    "",
    "dataset.distribution.0.downloadURL",
    "dataset.publisher.name",
    "result.recipientRegionName",
    "result.recipientDistrictName",
    "result.recipientWardName",
    "dataset.datagetter_metadata.datetime_downloaded",
    "dataset.license"
]

org_csv_titles = [
    "Grants",
    "Total",
    "Average",
    "Largest",
    "Smallest"
]

recipient_csv_titles = ["Recipient Name", "Recipient ID"] + org_csv_titles
funder_csv_titles = ["Funder Name", "Funder ID"] + org_csv_titles

org_csv_paths = [
    "org_name",
    "org_id",
    "count",
    "sum",
    "avg",
    "max",
    "min"
]
