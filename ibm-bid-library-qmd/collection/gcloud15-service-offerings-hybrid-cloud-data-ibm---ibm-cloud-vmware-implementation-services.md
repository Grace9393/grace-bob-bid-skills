---
document_id: "gcloud15-service-offerings-hybrid-cloud-data-ibm---ibm-cloud-vmware-implementation-services"
entry_id: "gcloud15-service-offerings-hybrid-cloud-data-ibm---ibm-cloud-vmware-implementation-services"
title: "IBM Cloud VMware Implementation Services"
source_path: "source.docx"
category: "G-Cloud 15 Service Offerings"
tags:
  - g-cloud-15
  - service-offering
  - gcloud15-service-offerings
---

Email: ukcat@uk.ibm.comContact: Anne-Marie WheelerIBM ConsultingG-Cloud 15IBM – IBM Cloud VMWare Implementation ServicesService Definition DocumentEmail: ukcat@uk.ibm.comContact: Anne-Marie WheelerIBM ConsultingG-Cloud 15IBM – IBM Cloud VMWare Implementation ServicesService Definition Document

Email: ukcat@uk.ibm.com

Contact: Anne-Marie Wheeler

IBM Consulting

G-Cloud 15

IBM – IBM Cloud VMWare Implementation Services

Service Definition Document

Email: ukcat@uk.ibm.com

Contact: Anne-Marie Wheeler

IBM Consulting

G-Cloud 15

IBM – IBM Cloud VMWare Implementation Services

Service Definition Document

Contents

Solution Description of VMware Cloud Foundation on IBM Cloud3

Scope of Works – Vmware Cloud Foundation on IBM Cloud5

About IBM - Supporting Government14

About IBM – This is IBM in the UK15

IBM Cloud VMware Implementation Services

Solution Description of VMware Cloud Foundation on IBM Cloud

VMware Cloud Foundation is the Software Defined Data Center (SDDC) Platform of virtualized compute, storage and networking.

Clients can onboard with VMware Cloud Foundation and start small, with a single base deployment, and then seamlessly expand and retract additional workload capacity as needed.

IBM Cloud provides the enhanced security of a single tenant, with air gap architecture throughout the environment, including bare metal servers, network and storage.

VMware Cloud Foundation provides you full, native access to the entire VMware stack, including vSphere Enterprise Plus, NSX, and Virtual SAN, allowing you to move your workloads to and from the cloud without changing your workloads, tooling, scripts or investing in new skills.

This is the true definition of hybrid cloud. VMware Cloud Foundation is available for purchase via a predictable OPEX monthly subscription that includes all infrastructure and software licenses.

Cloud Foundation Configuration:

4 X IBM IBM Cloud Bare Metal Servers

VMware Licenses included:

VMware vSphere Enterprise Plus (compute virtualization),

VMware vCenter Server (virtualization management)

VMware NSX (network virtualization)

VMware Virtual SAN™ (storage virtualization)

VMware SDDC Manager

IBM CloudDriver Lifecycle Management

Backup of the SDDC management system included.

Options include:

Zerto Disaster Recovery

Trusted Security & Compliance with Intel TXT & Hytrust

Veeam Data Backup

vRealize Management and Orchestration

However, these options are not included in this Services SoW.

The minimum allowed configuration of four servers, this is expandable in increments of 1 server.

Through advanced provisioning automation, IBM Cloud provides you your own dedicated, supported Cloud Foundation environment in just days instead of weeks.

IBM Cloud VMware Implementation Services

Scope of Works – Vmware Cloud Foundation on IBM Cloud

IBM will provide an implementation service for a VMware Cloud Foundation on IBM Cloud

The Cloud design is based on the VMware SDDC on IBM Cloud Standard Architecture.

At the chosen IBM Cloud Global DataCentre, IBM will provision:

4 Bare Metal Servers for a VMware Cloud Foundation for the following Workloads:

Management

Edge

Compute

and a Private Virtual Server for Jump Server.

The Customer DataCentre will be linked to the IBM Cloud Datacentre by IPSeC VPN.

All post implementation activities including:

Creation of VM’s

Migrating Workloads

Installation of Operating Systems and Applications

Security Hardening

Backup of Applications

Infrastructure and Application Monitoring and Management

will be provided by Customer using their own products, processes, staff & facilities.

Activity 1 - Project Initiation

The purpose of this activity is to facilitate a kick-off meeting for a mutually agreed number of Customer and IBM participants, for up to two hours, at an agreed date and time, via a conference call.

IBM Responsibilities:

IBM will:

Introduce the IBM project participants

Discuss project team roles and responsibilities

Review and document the project objectives

Provide a “Build Requirements” sheet

Discuss the steps required to complete the sheet

Provide the IBM Build Team’s User IDs to enable the Customer team to create the necessary administration users within the IBM Cloud Portal

Customer Responsibilities:

Customer will:

Attend the kick off call with relevant Technical and Management resources who will work on the project

Provide IBM a list of Customer team members participating in the project and their associated roles

Provide details on which IBM Cloud Datacenter location will be used for deployment

Ensure a IBM Cloud account has been created

Provide the IBM Build Team adequate access and authorization to the IBM Cloud account

Complete build requirement sheet no more than two weeks after received

Deliverable Materials:

Provide to the Customer a list of current IBM Build Team members and their associated roles within the project.

Provide to the Customer a Build Requirements sheet to enable Customer to provide detailed information for the deployment.

Provide to the Customer the IBM Build Team’s User IDs to enable the Customer team to create the necessary administration users within the IBM Cloud Portal.

Completion Criteria:

This activity completes at the conclusion of the project.

Activity 2 - Develop Design

The purpose of this activity is to analyse the proposed solution as defined in the Build Requirements document, and then to update the design to include the connectivity requirements.

To review and validate the proposed solution A technical workshop may be requested by either party, for a mutually agreed number of Customer and IBM participants, for up to two hours, at an agreed date and time; via a conference call, or at the Customers location.

IBM Responsibilities:

IBM will:

Review the Customer supplied Build and Connectivity requirements

Attend a technical workshop (if required)

Validate connectivity requirements between Customer and IBM Cloud DataCentres (IPSeC VPN, NSX VxLAN’s)

Produce the Build document

Customer Responsibilities:

Customer will:

Provide at the commencement of this activity, the Build Requirements document for incorporation to the Build document

Provide Fully Qualified Domain Names (FQDN) to all IBM Cloud Infrastructure components including both Cloud Central and Cloud Region

Provide at the commencement of this activity, details of the proposed connectivity between the Customer datacentre and the IBM Cloud DataCentre

Confirm availability of IP’s for NSX UnderLay Network (for VPN)

Provide Bring Your Own IP (BYOIP) addresses for NSX OverLay Networks

Provide relevantly trained and experienced personnel to participate in any technical workshop to finalise the VPN and/or NSX configurations to facilitate Customer Network connectivity to IBM Cloud DataCentre

Review and provide comments within 3 working days of the Build Document being supplied

Sign off the Build document prior to commencement of the Build phase

Create and deliver proposed test plan

Deliverable Materials:

Provide to the Customer a Build Document

Provide to IBM a proposed test plan

Completion Criteria:

This activity will be complete when IBM has successfully demonstrated the build

Activity 3 – Build Infrastructure to Design

The purpose of this activity is to build the environment based on the agreed proposed Detailed Design

IBM Responsibilities:

IBM will:

Provision and configure all the hardware and software components as defined in the Build Document; including:

4x Bare Metal Servers, forming the VMware Cloud Foundation cluster

VMware vSphere Enterprise Plus (compute virtualization),

VMware vCenter Server (virtualization management)

VMware NSX (network virtualization)

VMware Virtual SAN™ (storage virtualization)

VMware SDDC Manager

IBM CloudDriver Lifecycle Management

Windows Jump Sever for Out of Band (OOB) Management

Provide any VMWare Licences purchased for Servers, as part of VMware Cloud Foundation; vSphere, vCenter, NSX and VSAN.

Configure as defined in the Build document, at the IBM Cloud DataCentre:

IPSeC VPN tunnel between Customer DataCentre and IBM Cloud Datacentre

NSX UnderLay and OverLay Networks

Utilize temporary use of local administration accounts for authentication

Utilize temporary hosts file or temporary DNS service for infrastructure hostname lookup

Perform functional testing to ensure readiness for acceptance testing by Customer

Customer Responsibilities:

Customer will:

Designate the Master User for the IBM Cloud account

Create IBM Cloud portal users for the IBM build team to implement solution

Deploy a Customer vCenter

If Bring Your Own License (BYOL), provide licencing for these VMware components

Provide Bring Your Own IP (BYOIP) addresses for NSX overlay networks

Install and configure the Customer Network and Internet Connection to facilitate Customer Network connectivity to IBM Cloud DataCentres

Configure as defined in the Detailed Design document, at the Customer DataCentre:

NSX UnderLay and OverLay Networks

IPSeC VPN tunnel between Customer DataCentre and IBM IBM Cloud Datacentre

Deliverable Materials:

IBM to provide functional test results to Customer

Completion Criteria:

This activity will be complete when IBM has demonstrated the build.

Activity 4 - User Demonstration

The purpose of this activity is to analyse the proposed architecture to determine how to tailor the proposed cloud solution and then update the deployment automation to accommodate the customization requirements.

IBM Responsibilities:

IBM will provide:

Skills Transfer

Accessing the IBM Cloud Portal and vCentre of VMware Cloud Foundation

using the IBM Cloud Portal to Monitor, Manage and Modify IBM Cloud infrastructure and Networks

Povide a Hands-on Skills Transfer session of 4 hours (for up to 5 client personnel) on:

Post Implementation Support

Provide 8 hours remote Post Implementation Assistance and Support.

Customer Responsibilities:

Customer will:

Review and accept the servers as built to the design

Designate up to 5 relevantly trained and experienced personnel to attend skills transfer session

Ensure adequate facilities are made available for conducting the skills transfer session

Deliverable Materials

• None

Completion Criteria:

• This activity will be complete when IBM has completed the skills transfer

Activity 5 - Customers Post Implementation Tasks

After IBM have concluded the implementation and handed over the VMware Cloud Foundation to the Customer; the following are activities that may be required by the Customer to enable VMware Cloud Foundation to be integrated to their existing VMware environments.

Post Implementation activities:

Configure Active Directory (AD) integration with Customer AD Services

Configure DNS integration with Customer DNS services

Integration with Products and Processes for:

Service Desk

Service Monitoring and Management

Event Management

Patch Management

Planning, Design, Implementation and Testing of any vSphere or 3rd party:

Backup and Restore of Applications

High Availability

Disaster Recovery

Creation of VM’s

Installation of Operating Systems and Applications

Security Hardening

Handover to Day 2 Steady State support

Migration of existing workloads from source platforms:

Physical to Cloud (P2C)

Virtual to Cloud (V2C)

Cloud to Cloud (C2C)

IBM Cloud VMWare Implementation Services

About IBM - Supporting Government

We help government organisations in the UK and worldwide deliver and transform essential public services – our teams are passionate and proud about helping you to make a real difference to people’s lives.

Government Services Supported by IBMDefence and IntelligencePublic Safety and PolicingHealthcareLife SciencesTax and Revenue ManagementNational Infrastructure Social CareEducationWork and Pensions Government Services Supported by IBMDefence and IntelligencePublic Safety and PolicingHealthcareLife SciencesTax and Revenue ManagementNational Infrastructure Social CareEducationWork and Pensions The problems we solve for clients are complex and cannot be satisfied with technology alone. They require a partner that can also offer deep industry expertise and a relationship of trust.

Government Services Supported by IBM

Defence and Intelligence

Public Safety and Policing

Healthcare

Life Sciences

Tax and Revenue Management

National Infrastructure

Social Care

Education

Work and Pensions

Government Services Supported by IBM

Defence and Intelligence

Public Safety and Policing

Healthcare

Life Sciences

Tax and Revenue Management

National Infrastructure

Social Care

Education

Work and Pensions

IBM combines the portfolio, people and sense of purpose necessary to meet today’s enterprise demands. Every day, we support and manage complex delivery for government clients where the impact of delivery has wide-reaching impact on citizens and national services.

We bring access to the industry experience, insight and technology capability to deliver and operate secure, scalable, optimised and available services for government.

We support you by bringing:

Industry expertise – Professionals who understand and are passionate about delivering quality public services and can bring industry insights and apply innovation to your business processes

Trust and security capabilities – Protecting valuable data and insights and deploying new innovations responsibly

Innovative technology – Expertise in areas such as AI, blockchain, 5G, Automation, IoT, cybersecurity and quantum, delivered in a Hybrid Cloud environment

Experienced Services professionals to support strategy, innovation and deliver transformation and change to processes, applications, and cloud infrastructure

Global alliances – valuable partnerships with the world’s leading vendors.

IBM Cloud VMWare Implementation Services

About IBM – This is IBM in the UK

We have worked together with organisations in the UK for over 100 years, with a rish history of joint innovation and achievements, built on trusted relationships.

Case Studies

AI Governance Industry Leader

IBM named a Leader in The Forrester Wave™: AI Governance Solutions, Q3 2025 with watsonx.governance:

Forrester recognized IBM for our ability to manage the complexity of AI governance across many roles and responsibilities. Our strategy reflects years of collaboration with customers in complex and highly regulated industries — and that experience is built into watsonx.governance.

Sport

The Official AI, Cloud and Digital Transformation Partner for The All England Lawn Tennis Club:

IBM is the long-standing technology partner for The All England Lawn Tennis Club. From the launch of the Wimbledon website in 1995 and the mobile application in 2009, to the first integration of enhanced AI-powered solutions in 2017, IBM and the All England Club have collaborated for 36 years to deepen global fan engagement across Wimbledon’s world-class digital platforms.

Education

IBM and Pearson collaborate to build new AI-powered learning tools for organisations and individuals worldwide:

IBM and Pearson, the world’s lifelong learning company, have a global partnership to build new personalised learning products powered by AI for businesses, public organisations and educational institutions.

Quantum

IBMQ, the world’s most advanced quantum computing intitiative for commerical use, is being used by CERN.

For more information, visit the IBM UK websiteFor more information, visit the IBM UK website

For more information,

visit the IBM UK website

For more information,

visit the IBM UK website

Environment

IBM’s focus on sustainability began in 1971 with our first environmental policy.

Services & Solutions

IBM in the UK provides various services and solutions, including:

Cloud Computing: IBM offers cloud computing services, including infrastructure, platform, and software as a service, to help businesses in the UK to innovate and grow.

Artificial Intelligence: IBM provides artificial intelligence (AI) solutions, including Watson, to help businesses in the UK to make better decisions and improve their operations.

Cybersecurity: IBM offers cybersecurity solutions to help businesses in the UK to protect themselves from cyber threats and ensure the security of their data.

Internet of Things (IoT): IBM provides IoT solutions to help businesses in the UK to connect and manage their devices, and to analyze and act on the data generated by those devices.

Blockchain: IBM offers blockchain solutions to help businesses in the UK to create secure, transparent, and efficient supply chains.

Consulting: IBM provides consulting services to help businesses in the UK to improve their operations, reduce costs, and increase efficiency.

Research and Development: IBM has a strong research and development presence in the UK, with a focus on emerging technologies such as AI, blockchain, and quantum computing.

For more information, visit the IBM UK websiteFor more information, visit the IBM UK website

For more information,

visit the IBM UK website

For more information,

visit the IBM UK website

## Image Descriptions

- Image 1: This image visually represents cloud computing, featuring a glowing cube with two stylized clouds hovering above, set amidst a complex network of circuit board-like elements, symbolizing data storage and accessibility. The overall design emphasizes a technologically advanced and interconnected approach to cloud services and digital infrastructure.
- Image 2: The image displays a technical diagram depicting a data flow process, likely related to a network or software system. It includes labeled boxes representing different stages or components of the flow, along with arrows indicating the direction of data transmission, suggesting a complex system architecture.
- Image 3: This document outlines various government services supported by IBM, specifically listing categories such as Defence, Healthcare, and Tax Revenue Management. The list is presented in a simple, bulleted format, showcasing the different areas of government support provided.
- Image 4: The image shows a text message encouraging the reader to visit the IBM UK website for more information. The text is highlighted in blue, adding emphasis to the website address.
- Image 5: Here’s a description of the image based on its content:

The image is a simple text-based graphic, directing the viewer to visit the IBM UK website for additional information.  It features a bold call to action with the text "visit the IBM UK website" emphasized in blue and underlined.
- Image 6: This image depicts the IBM logo, which consists of a stylized representation of the Chinese characters for "data," indicated by horizontal blue rectangles stacked to form lines.  The iconic design immediately identifies the company and its core focus on data and technology services.
