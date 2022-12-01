## NetLabX  **1.0.0**  
![
](https://camo.githubusercontent.com/56f040121ad5740119e34f278f43bbfcf7abaab9/687474703a2f2f69636f6e73686f772e6d652f6d656469612f696d616765732f53797374656d2f706c65782d69636f6e732f706e672f4f746865722f3235362f707974686f6e2e706e67)  
  
  **NetLabX Project**
  With the growth of the world-wide computer network and its use, it becomes necessary studiesand abstractions of concepts used in the area. In this way a great demand arises for applicationsrelated to security, expansion and its maintenance. The definition of computer networks is givenby the set of interconnected equipment in order to exchange information and share resources,such as files, printers, modems, software, among others. With this, in order to obtain and studythe behavior of a network, a large amount of equipment and technical capacity for configurationis  necessary,  in  the  academic  environment  this  necessity  makes  the  study  costly.  Thus,  analternative to obtain a complete network environment is the simulation, where the equipmentis not allocated physically, but in virtual form within a computer application, every necessaryequipment or resource is created within that capable software to simulate a real machine. Thesimulation process brings several benefits, due to its low investment and better understanding. Asimulated environment requires a reduced amount of physical equipment, and its configurationcan be automated. In the activities carried out in the technology course in internet systems,at the Guarapuava campus of the Federal Technological University of Paran ́a, the lack of avisually intuitive and simple configuration environment was observed, where any academic or tea-cher can perform their simulations and tests, without lost most time in creating this environment.
  
**Article Project Link**
[article.pdf](https://tcc.tsi.gp.utfpr.edu.br/attachments/approvals/157/GP_COINT_2019_1_PROPOSTA_PATRICK_FERRO_RIBEIRO.pdf?1559303561)
    
**Python 2.7**:
- Desktop application using TkInter.

**Run**  

  To run the project on your equipment, type this in the netlabx folder.  

    python netlabx.py

**Virtualenv save requirements**  
pip freeze > requirements.txt  

**Virtualenv load requirements**  
Required virtualenv and run:  
$ virtualenv <env_name>  
$ source <env_name>/bin/activate  
(<env_name>)$ pip install -r path/to/requirements.txt  


**Compile Project**  
    pyinstaller netlabxnew.py --hidden-import='PIL._tkinter_finder' --onefile  
