## PDF page 1/191
Lecture Notes in Civil Engineering
Andrius Jurelionis
Paris A. FokaidesLivio MazzarellaTimo Hartmann    Editors
Building 
Digital Twins
Proceedings of BDTIC 2025
Jurelionis · Fokaides · Mazzarella · 
Hartmann   Eds. Building Digital Twins

## PDF page 2/191
Lecture Notes in Civil Engineering 775 
Series Editors 
Marco di Prisco, Politecnico di Milano, Milano, Italy 
Sheng-Hong Chen, School of Water Resources and Hydropower Engineering, Wuhan 
University, Wuhan, China 
Ioannis Vayas, Institute of Steel Structures, National Technical University of Athens, 
Athens, Greece 
Sanjay Kumar Shukla, School of Engineering, Edith Cowan University, Joondalup, 
Australia 
Anuj Sharma, Iowa State University, Ames, USA 
Nagesh Kumar, Department of Civil Engineering, Indian Institute of Science 
Bangalore, Bengaluru, India 
Chien Ming Wang, School of Civil Engineering, The University of Queensland, 
Brisbane, Australia 
Zhen-Dong Cui, China University of Mining and Technology, Xuzhou, China 
Xinzheng Lu, Department of Civil Engineering, Tsinghua University, Beijing, China

## PDF page 3/191
Lecture Notes in Civil Engineering (LNCE) publishes the latest developments in Civil 
Engineering—quickly, informally and in top quality. Though original research reported 
in proceedings and post-proceedings represents the core of LNCE, edited volumes of 
exceptionally high quality and interest may also be considered for publication. V olumes published in LNCE embrace all aspects and subﬁelds of, as well as new challenges in, 
Civil Engineering. Topics in the series include:
Construction and 
Structural Mechanics
Building Materials
Concrete, Steel and Timber Structures
Geotechnical Engineering
Earthquake Engineering
Coastal Engineering
Ocean and Offshore Engineering; Ships and Floating Structures
Hydraulics, Hydrology and Water Resources Engineering
Environmental Engineering and Sustainability
Structural Health and Monitoring
Surveying and Geographical Information Systems
Indoor Environments
Transportation and Trafﬁc
Risk Analysis
Safety and Security 
To 
submit a proposal or request further information, please contact the appropriate 
Springer Editor: 
– Pierpaolo 
Riva at pierpaolo.riv
a@springer.com (Europe and 
Americas); 
– Swati 
Meherishi at swati.meherishi@springer
.com (Asia—except 
China, Australia, 
and Ne w 
Zealand); 
– Wayne Hu at wayne.hu@springer
.com (China). 
All books 
in the series now indexed by Scopus and EI Compendex database!

## PDF page 4/191
Andrius Jurelionis · Paris A. Fokaides · 
Livio Mazzarella · Timo Hartmann 
Editors 
Building Digital Twins 
Proceedings of BDTSC 2025

## PDF page 5/191
Editors 
Andrius Jurelionis 
Faculty of Civil Engineering and Architecture Kaunas University of Technology Kaunas, Lithuania 
Livio Mazzarella Dipartimento di Energia Politecnico di Milano Milan, Italy Paris A. Fokaides School of Engineering Frederick University Nicosia, Cyprus 
Timo Hartmann Contecht GmbH Berlin, Germany 
ISSN 2366-2557 ISSN 2366-2565 (electronic) 
Lecture Notes in Civil Engineering 
ISBN 978-3-032-09039-3 ISBN 978-3-032-09040-9 (eBook) 
https://doi.org/10.1007/978-3-032-09040-9 
© The Editor(s) (if applicable) and The Author(s) 2026. This book is an open access publication. 
Open Access This book is licensed under the terms of the Creative Commons Attribution 4.0 International 
License ( http://creativecommons.org/licenses/by/4.0/ ), which permits use, sharing, adaptation, distribution 
and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and 
the source, provide a link to the Creative Commons license and indicate if changes were made. 
The images or other third party material in this book are included in the book’s Creative Commons license, 
unless indicated otherwise in a credit line to the material. If material is not included in the book’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, 
you will need to obtain permission directly from the copyright holder. 
The use of general descriptive names, registered names, trademarks, service marks, etc. in this publication 
does not imply, even in the absence of a speciﬁc statement, that such names are exempt from the relevant 
protective laws and regulations and therefore free for general use. 
The publisher, the authors and the editors are safe to assume that the advice and information in this book 
are believed to be true and accurate at the date of publication. Neither the publisher nor the authors or the editors give a warranty, expressed or implied, with respect to the material contained herein or for any errors 
or omissions that may have been made. The publisher remains neutral with regard to jurisdictional claims in 
published maps and institutional afﬁliations. 
This Springer imprint is published by the registered company Springer Nature Switzerland AG 
The registered company address is: Gewerbestrasse 11, 6330 Cham, Switzerland 
If disposing of this product, please recycle the paper.

## PDF page 6/191
Preface 
It is with great pleasure that I present the proceedings of the 1st International Con-
ference on Building Digital Twin and Smart Cities (BDTSC), hosted at Kaunas Uni-
versity of Technology (KTU) in 2025. As Chairman of this inaugural edition, I am honoured to introduce this collection of peer-reviewed contributions that reﬂect the lat-
est advancements and emerging research directions in the ﬁeld of digital twins for the 
built environment. 
The BDTSC conference was established to respond to the accelerating digital trans-
formation of our buildings, cities, and infrastructure. As society grapples with the chal-lenges of climate change, urbanisation, energy efﬁciency, and citizen wellbeing, digital 
twins are becoming key enablers of smarter, more sustainable, and data-driven decision-
making. BDTSC was conceived as a multidisciplinary platform to convene researchers, practitioners, and policymakers around the shared objective of advancing digital twin 
methodologies, tools, and implementations for buildings and cities. 
This conference was organised under the framework of the SmartWins project, a 
Horizon Europe Twinning initiative (Grant Agreement No. 101078997) coordinated by Kaunas University of Technology, which aims to enhance KTU’s research excellence in 
the domain of digital twins for the built environment. 
The contributions presented in this volume are the result of a highly competitive 
selection process and reﬂect the diversity of topics and approaches discussed during the event. A total of 15 papers are included, representing academic institutions, applied research centres, and innovation ecosystems from across Europe. Together, they offer a 
snapshot of current thinking and a springboard for further collaboration and exploration. 
Several papers focus on frameworks and methodological innovations. The DWELT 
framework (Deﬁne, Wire, Engineer, Leverage, Transfer) proposes a structured path towards scalable and interoperable digital twin solutions through a System-of-Systems 
lens. Another study evaluates the compatibility of TEASER and AixLib libraries in 
the Modelon Impact environment, offering insights into functional interoperability of 
physics-based models. Meanwhile, a paper exploring IFC-based open BIM models on web platforms demonstrates the importance of openness and long-term data reliability 
for sustainable digital workﬂows. 
Urban-scale applications of digital twins were also strongly represented. Two papers 
provide com

## PDF page 7/191
vi Preface
Several papers offer tangible case studies. A study from the HYCOOL-IT project 
presents a digital twin for a data centre integrating waste heat recovery and predictive 
control strategies. Another case from the HPC4AI data centre in Turin documents the 
implementation of experimental server cooling systems and management platforms, reinforcing the research-to-application link. 
Innovation in 3D data acquisition is also featured. One contribution introduces a 
dynamic method for automated planning and re-planning of terrestrial laser scanning (TLS) using discretised key-points and next-best-view algorithms. In parallel, a study 
focusing on a building’s heat storage system illustrates how numerical models integrated 
into a digital twin can optimise heating performance and reduce energy loss. 
Digitalisation in heritage conservation is addressed through a paper on sustainable 
renovation of a cultural heritage building in Kaunas, combining HBIM, environmental monitoring, and low-carbon material selection. This intersection of technology, history, and sustainability reﬂects an increasingly important research direction. 
Training and user engagement are also critical components of the digital twin ecosys-
tem. A study on XR technologies in high-risk industrial training offers a methodological framework for evaluating training effectiveness and instructor adoption. In a different 
domain, the DCU Campus Explorer illustrates how a digital twin can enhance citizen 
engagement and inclusion across a university campus, supporting access to wellness services, quiet spaces, and real-time navigation. 
Finally, a study on a knowledge-based conﬁguration expert system offers a solution 
for empowering non-expert users – such as apartment managers – in early-stage reno-
vation planning. The proposed system, tested in the Estonian context, bridges the gap 
between technical complexity and user-friendly decision support. 
On behalf of the organising committee, I would like to extend my sincere thanks to 
all authors, reviewers, session chairs, and participants who contributed to the success of the conference. Special recognition is due to Kaunas University of Technology for its vision and support in hosting this ﬁrst edition and to the SmartWins consortium for 
fostering the collaborative environment that made this gathering possible. 
It is my hope that this volume will serve as a valuable reference and inspiration for 
future research and innovation in digita

## PDF page 8/191
Organization 
Committees 
Paris A. Fokaides Kaunas University of Technology, Lithuania; 
Frederick Uni
versity, Cyprus 
Andrius Jurelionis Kaunas University of Technology, Lithuania 
Livio Mazzarella Politecnico di Milano, Italy 
Timo Hartmann Technical University of Berlin, Germany 
Scientiﬁc Committee 
Paris A. Fokaides (Chair of 
Committee) Kaunas University of Technology, Lithuania; 
Frederick Uni
versity, Cyprus 
Ali Intizar Dublin City University, Ireland 
Andrius Jurelionis Kaunas University of Technology, Lithuania 
Angelo Ciribini Università degli Studi di Brescia, Italy 
Darius Pupeikis Kaunas University of Technology, Lithuania 
Dimosthenis Ioannidis Centre for Research and Technology-Hellas, 
Greece 
Edmond Saliklis California Polytechnic State University, USA 
Farzad Pour Rahimian Teesside University, UK 
Ioannis Brilakis University of Cambridge, UK 
Kjeld Svidt Aalborg University, Denmark 
Lavinia Chiara Tagliabue University of Turin, Italy 
Livio Mazzarella Politecnico di Milano, Italy 
Qian Wang KTH Royal Institute of Technology, Sweden 
Rossano Scoccia Politecnico di Milano, Italy 
Sanju Tiwari Sharda University, Greater Noida, India 
Targo Kalamees Tallinn University, Estonia 
Timo Hartmann Technical University of Berlin, Germany 
Vangelis Angelakis Linköping University, Sweden 
Vishal Singh Indian Institute of Science, India 
Pieter Pauwels Eindhoven University of Technology, Netherlands 
Pedro Meda Magalhães University of Porto, Portugal

## PDF page 9/191
viii Organization
Organizing Committee 
Lina Morkūnaitė Kaunas University of Technology, Lithuania 
Gintarė Stankevičiūtė Kaunas University of Technology, Lithuania 
Paulius Spūdys Kaunas University of Technology, Lithuania 
Iryna Osadcha Kaunas University of Technology, Lithuania 
Viktoras Jasaitis Kaunas University of Technology, Lithuania 
Aušra Andriukaitienė Kaunas University of Technology, Lithuania 
Aušra Mlinkauskienė Kaunas University of Technology, Lithuania 
Building Digital Twin Scientiﬁc Conference (BDTSC) 2025 ( https://bdtsc.ktu.edu/ 
bdtsc-2025/ )

## PDF page 10/191
Contents 
Design Wire Engineer Leverage and Transfer (DWELT) Framework 
for Building-Level Digital Twins ........................................ 1 
Karim Farghaly, Pedro Mêda, Conor Shaw, James O’Donnell, 
Fulvio Re Cecconi, and Nicola Moretti 
Evaluating the Interoperability of TEASER and AixLib for Building Digital Twins Within Modelon Impact Environment: A Case Study ........... 13 
Laura Zabala Urrutia, Sergiu Crisan, Estíbaliz Pérez Iribarren, Iker González Pino, and Jesús Febres Pascual 
A Digital Twins Model Based on IFC Open BIM Models Managed on Web Platforms ............................................................. 26 
Costantino Carlo Mastino, Juozas Vai čiūnas, Raffaello Possidente, 
Andrea Frattolillo, Mohsen Zavari, and Valerio Da Pos 
Overview of the Use of AI in Buildings Sustainability Assessment ............ 40 
Turkay Ersener and Paris A. Fokaides 
Urban Digital Twin Data Requirements and Reference Architecture for Green Spaces and Ecosystems ........................................ 50 
Lina Morkunaite, Darius Pupeikis, Vytautas Bocullo, Egle Klumbyte, 
Andrea Conserva, Chiara Farinea, Alice Bazzica, Peter Barmann, 
and Fruzsina Csala 
Towards True Networked Urban Digital Twins – A Development Agenda ...... 63 
Juho-Pekka Virtanen, Laura Mrosla, and Tapani Heino 
Automated Planning, Execution, and Re-planning of Terrestrial Laser Scanning in the Built Environment ....................................... 74 
Thivageran Duraimany and Frédéric Bosché 
Digital Twins for Data Centre Cooling Optimisation and Waste Heat 
Recovery ............................................................. 86 
Sara Giordani, Rossano Scoccia, and Marcello Aprile 
Digital Twin for Datacenter: HPC4AI UniTO Case Study ................... 99 
Viviana Vaccaro, Robert Birke, Silvia Meschini, 
Lavinia Chiara Tagliabue, Sergio Rabellino, Pablo Vicente Legazpi, 
and Marco Andinucci

## PDF page 21/191
10 K. Farghaly et al.
at the top—allowing new applications to emerge – and at the bottom – enabling ﬂexi-
ble integration of diverse functional components – thereby fulﬁlling SoSE criteria for 
openness, emergent behavior, and dynamic scalability within complex DTw ecosystems. 
5 Conclusions 
The DWELT framework presents a scalable, interoperable, and decentralized approach to DTw implementation in the built environment, addressing data fragmentation, poor 
interoperability, and limited accessibility. By adopting SoS architecture, DWELT enables seamless integration between existing digital tools and new analytical solutions, ensuring 
that DT ecosystems are modular, adaptable, and aligned with evolving industry require-
ments. The ﬁve-layered architecture forms the foundation of this approach, beginning with the Data Requirements and Speciﬁcations Layer (Deﬁne – D), which establishes a 
federated data model through a top-down and bottom-up approach to requirement iden-
tiﬁcation. The Data Validation and System Alignment Layer (Wire – W) ensures that data is structured, validated, and interoperable, enabling seamless integration between 
heterogeneous sources. The Integrated Data Ecosystem Layer (Engineer – E) provides a 
secure and federated database solution, facilitating real-time data exchange through APIs and publish/subscribe mechanisms. The Advanced Analytics and Automation Building 
Layer (Leverage – L) enhances decision-making and operational efﬁciency by leveraging 
machine learning, scenario analysis, and predictive modeling, ensuring that DT solu-tions evolve with data-driven automation. Finally, the User Interaction and Insight Deliv-
ery Layer (Transfer – T) ensures stakeholder engagement through intuitive dashboards 
and 3D visualizations, bridging technical insights with end-user needs. By embedding 
plug-and-play approach and semantic enrichment, DWELT provides a comprehensive 
framework for implementing DTw across the entire building lifecycle. Whilst prelimi-nary comparisons with existing frameworks are discussed, a more extensive comparative 
analysis remains a limitation and will be addressed in future research directions. Com-
pared to other architectures, the embedded continuous co-creation cycle ensures that the system remains aligned with industry regulations, sustainability goals, and real-world 
requirements, fostering widespread adoption and long-term impact. In addition to this, 
as the AECO industry continues its digital transf

## PDF page 41/191
30 C. C. Mastino et al.
sensors, BIM models, and advanced algorithms, digital twins allow monitoring, predic-
tive analysis, and optimized maintenance of buildings and facilities. Integration through 
the use of Open BIM models and digital twins revolutionizes the construction sector, 
offering advantages that can be summarized in the following points:
Interoperability between different software and platforms.
Real-time monitoring of building performance.
Predictive simulations to optimize consumption and maintenance.  Intelligent building 
management throughout its lifecycle.
Use and integration of artiﬁcial intelligence in the management of building systems and f
acilities. 
In the context of systems (HV AC, electrical, hydraulic), the digital twin allows the 
detection of anomalies, prevention of failures, and improvement of energy efﬁciency. Open BIM ensures that information is accessible to all involved professionals, reducing 
errors and operational costs. This synergy between open digital models and real-time 
data represents the future of smart building automation, improving sustainability from various perspectives (energy, environmental, economic, etc.) and the multi-objective 
comfort of built environments. 
1.1 The HV AC Simulation Laboratory 
In this work, the design of a prototype plant developed at the University of Cagliari in 
the Faculty of Engineering and Architecture is presented, which will allow the simu-lation of systems plant behavior in various internal climate conﬁgurations. Everything 
will be managed and monitored through a digital twin created using the systems OPEN 
BIM model with the use of a WEB OPEN BIM platform capable of operating on BIM models in open IFC format [
48–50]. The prototype plant will be developed in the Lab-
oratory of Technical Physics and Energy at the university and will have the capability to manage, always through the Digital Twin, on a BIM Web platform, as many as 14 different plant conﬁgurations. Figure 
1 shows the different plant conﬁgurations planned 
for the prototype. As can be seen, various generation systems are provided that allow the simultaneous production of thermal and refrigeration energy. There are also thermal and photovoltaic solar panels that will enable a more accurate simulation of the plant size 
related to the climatic location and their producibility. The systems based on renewable 
energy production can be studied for different types of envelope. In fact, the labora-
tory wi