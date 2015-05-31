============================================================================
**Software Project: Configuring and deploying Data Visualization Dashboard**
============================================================================

**Course ID:**   BUEX-V594

**Name:** Rahul Bindra

**Link to reStructuredText format:** http://rst.ninjs.org/?n=27a12d178a2209f7880cc5136d945494&theme=nature

================
**Introduction**
================

Data Visualization is an important concept that gains prominence more so in today's world because of huge variety, velocity and volume of data that is gathered through a multitude of systems around us. In order to make meaningful interpretations off this huge chunk of data, we need the right approaches that condense the endless alphanumeric text into graphs that can be interacted with to generate meaningful insights. 

Such a data visualization approach involves many steps such as:

1. Identification of data set to be analyzed
2. Creating a Virtual Machine for solution deployment
3. Software pre-requisite configuration on Virtual Machine (VM)
4. Database installation and configuration on VM
5. Solution development (code base for dashboard, database link etc.)
6. Solution deployment on VM
7. Running the solution from VM to view dashboard on browser

======================================
**Scope of this Project and Tutorial**
======================================

The aim of this particular project is to build upon the code base already developed and available online that develops a data visualization dashboard. This project uses the existing code base and develops a DevOps wrapper around it using ansible. The objective is not to demonstrate how to develop a data visualization dashboard but on **DevOps functionality using Ansible** and how teams can use the same for effective software provisioning and deployment on customer systems/cloud.

==================
**Pre-requisites**
==================
The following conditions around accesses need to be satisfied before the steps provided in this tutorial can be executed:

1. Login access to `FutureSystems Portal <https://portal.futuresystems.org/>`_
2. `Putty <http://www.putty.org/>`_ installed and configured for FutureSystems access with virtual environment set up
3. Access to Openstack and corresponding configuration settings in FutureSystems
4. Login access to `Openstack Horizon <https://openstack-j.india.futuresystems.org/horizon/>`_

====================
**Technology Stack**
====================

Python
------------------
 Python is used as the primary programming language to accomplish a variety of activities ranging from environment set-up to creation of final file that creates the visualization and connects to the Mongo DB

Mongo DB
------------------
 Mongo DB is used as the data base to store the 700,000+ strong data in the form of a collection within the project database and downloaded from an externally hosted site

D3.js
------------------
 D3.js (Data-Driven Documents) is a library in JavaScript that is used for producing dynamic and interactive visualizations for the dashboard using the Mongo DB data

DC.js
------------------
 Leverages D3.js to render charts from large data charts in a friendly format

Flask
------------------
 `Flask <http://en.wikipedia.org/wiki/Flask_%28web_framework%29>`_ is a micro-framework based on Python that provides the tools to build the web application

Ansible
------------------
 Used to deploy the solution using the DevOps framework

==============
**Resources**
==============

- All the resources for this project can be found at the following GitHub repository `GitHub Link <https://github.com/futuresystems/465-rahulbindra/tree/master/VisualizationProject>`_
- Background information on the actual development of the code base (not part of this project/tutorial) can be found at the following link `Code Base <http://adilmoujahid.com/posts/2015/01/interactive-data-visualization-d3-dc-python-mongodb/>`_

======================================
**Configuration and Deployment Steps**
======================================

1. Create a new VM instance (ubuntu 14.04) by logging into `Horizon <https://openstack-j.india.futuresystems.org/horizon/>`_
    Note the internal IP of the VM (IP_Internal). Execute the following commands to link an external IP (IP_External) to the VM 

    nova floating-ip-create ext-net 

    nova floating-ip-associate <VMName>

2. Log in to FutureSystems Portal via Putty

3. Use the following commands to load appropriate modules for GitHub and Openstack
    module load git

    module load openstack

    source ~/.cloudmesh/clouds/india/juno/openrc.sh
4. Copy the resources from project repository using the following command
    git clone https://github.com/futuresystems/465-rahulbindra
5. Navigate to /465-rahulbindra/VisualizationProject/FuturesystemsArtifacts

6. Edit inventory.txt to add the actual internal IP instead of IP_Internal (in the file)

7. Log in to virtual env using source command

8. Install ansible and upgrade pip using the following commands
    pip install ansible

    pip install --upgrade pip

9. Execute following commands to add identity for ssh access
    eval $(ssh-agent -s)

    ssh-add ~/.ssh/id_rsa

10. Set up the environment on VM by installing software pre-requisites using the following command
        ansible-playbook -i inventory.txt -c ssh VMSetup.yaml

11. Install Mongo DB on VM and load data using the following command 
        ansible-playbook -i inventory.txt -c ssh mongo.yaml

12. Login to virtual machine using the following command 
        ssh ubuntu@IP_Internal

13. Log in to virtual environment already set up using the following command
        source ~/ENV/bin/activate

14. Navigate to /465-rahulbindra/VisualizationProject/

15. Edit app.py to add the actual internal IP instead of IP_Internal (in the file)

16. Execute the following command to run the application
        sudo python app.py

17. Go to browser and type the following url <IP_External>:5000
        Note: Use the IP_External from point 1 above

18. After VM use type exit to go back to FutureSystems (Putty)

19. Execute the following command to delete the VM
        nova delete <VMName>
