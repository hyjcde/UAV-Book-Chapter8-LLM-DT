## PDF page 1/136
Simula SpringerBriefs on Computing 16
Yan Zhang
Digital Twin
Architectures, Networks, 
and Applications

## PDF page 2/136
Simula SpringerBriefs on Computing
V olume 16
Editor-in-Chief
Joakim Sundnes, Simula Research Laboratory, Oslo, Norway
Series Editors
Shaukat Ali, Simula Research Laboratory, Oslo, Norway
Evrim Acar Ataman, Simula Metropolitan Center for Digital Engineering, Oslo, Norway
Are Magnus Bruaset, Simula Research Laboratory, Oslo, Norway
Xing Cai, Simula Research Laboratory and University, Oslo, Norway
Kimberly Claffy, University of California, San Diego, CA, USA
Andrew Edwards, Simula Research Laboratory, Oslo, Norway
Arnaud Gotlieb, Simula Research Laboratory, Oslo, Norway
Magne Jørgensen, Simula Metropolitan Center for Digital Engineering, Oslo, Norway
Olav Lysne, Simula Metropolitan Center for Digital Engineering, Oslo, Norway
Kent-Andre Mardal, Simula Research Laboratory, University of Oslo, Oslo, Norway
Kimberly McCabe, Simula Research Laboratory, Oslo, Norway
Andrew McCulloch, University of California San Diego, San Diego, CA, USA
Leon Moonen, Simula Research Laboratory, Oslo, Norway
Michael Riegler, Simula Metropolitan Center for Digital Engineering, Oslo Metropolitan
University, Oslo, Norway; UiT The Arctic University of Norway, Tromsø, Norway
Marie Rognes, Simula Research Laboratory, Oslo, Norway
Fabian Theis, Helmholtz Munich, Munich, Germany
Aslak Tveito, Simula Research Laboratory, Oslo, Norway
Karen Willcox, The University of Texas at Austin, Austin, USA
Tao Yue, Beihang University, Beijing, China
Andreas Zeller, Saarland University, Saarbrücken, Germany
Yan Zhang, University of Oslo, Oslo, Norway

## PDF page 3/136
About this series
In 2016, Springer and Simula launched the book series Simula SpringerBriefs on
Computing , which aims to provide introductions to selected research topics in
computing. The series provides compact introductions for students and researchers
entering a new ﬁeld, brief disciplinary overviews of the state-of-the-art of select
ﬁelds, and raises essential critical questions and open challenges in the ﬁeld of
computing. Published by SpringerOpen, all Simula SpringerBriefs on Computing
are open access, allowing for faster sharing and wider dissemination of knowledge.
Simula Research Laboratory is a leading Norwegian research organization which
specializes in computing. Going forward, the book series will provide introductory
volumes on the main topics within Simula’s expertise, including communications
technology, software engineering and scientiﬁc computing.
By publishing the Simula SpringerBriefs on Computing , Simula Research Labo-
ratory acts on its mandate of emphasizing research education. Books in this series are
published by invitation from one of the series editors. Authors interested in publishing
in the series are encouraged to contact any member of the editorial board.

## PDF page 4/136
Y an Zhang
Digital Twin
Architectures, Networks, and Applications

## PDF page 5/136
Yan Zhang
University of Oslo
Oslo, Norway
ISSN 2512-1677 ISSN 2512-1685 (electronic)
Simula SpringerBriefs on Computing
ISBN 978-3-031-51818-8 ISBN 978-3-031-51819-5 (eBook)
https://doi.org/10.1007/978-3-031-51819-5
© The Author(s) 2024. This book is an open access publication.
Open Access This book is licensed under the terms of the Creative Commons Attribution 4.0 International
License ( http://creativecommons.org/licenses/by/4.0/ ), which permits use, sharing, adaptation, distribu-
tion and reproduction in any medium or format, as long as you give appropriate credit to the original
author(s) and the source, provide a link to the Creative Commons license and indicate if changes were
made.
The images or other third party material in this book are included in the book’s Creative Commons license,
unless indicated otherwise in a credit line to the material. If material is not included in the book’s Creative
Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright holder.
The use of general descriptive names, registered names, trademarks, service marks, etc. in this publication
does not imply, even in the absence of a speciﬁc statement, that such names are exempt from the relevant
protective laws and regulations and therefore free for general use.
The publisher, the authors, and the editors are safe to assume that the advice and information in this book
are believed to be true and accurate at the date of publication. Neither the publisher nor the authors or
the editors give a warranty, expressed or implied, with respect to the material contained herein or for any
errors or omissions that may have been made. The publisher remains neutral with regard to jurisdictional
claims in published maps and institutional afﬁliations.
This Springer imprint is published by the registered company Springer Nature Switzerland AG
The registered company address is: Gewerbestrasse 11, 6330 Cham, Switzerland
Paper in this product is recyclable.

## PDF page 6/136
Series Foreword
Dear reader,
Scientiﬁc research is increasingly interdisciplinary, and both students and expe-
rienced researchers often face the need to learn the foundations, tools, and methods
of a new research ﬁeld. This process can be quite demanding, and typically involves
extensive literature searches and reading dozens of scientiﬁc papers in which the
notation and style of presentation varies considerably. Since the establishment ofthis series in 2016 by founding editor-in-chief Aslak Tveito, the briefs in this serieshave aimed to ease the process by introducing and explaining important conceptsand theories in a relatively narrow ﬁeld, and to outline open research challenges andpose critical questions on the fundamentals of that ﬁeld. The goal is to provide the
necessary understanding and background knowledge and to motivate further studies
of the relevant scientiﬁc literature. A typical brief in this series should be around 100pages and should be well suited as material for a research seminar in a well-deﬁnedand limited area of computing.
We publish all items in this series under the SpringerOpen framework, as this
allows authors to use the series to publish an initial version of their manuscript that
could subsequently evolve into a full-scale book on a broader theme. Since the briefsare freely available online, the authors do not receive any direct income from the
sales; however, remuneration is provided for every completed manuscript. Briefs arewritten on the basis of an invitation from a member of the editorial board. Suggestionsfor possible topics are most welcome and can be sent to sundnes@simula.no.
March 2023 Dr. Joakim Sundnes
Editor-in-Chief
Simula Research Laboratory
sundnes@simula.no
Dr. Martin Peters
Executive Editor Mathematics
Springer Heidelberg, Germany
martin.peters@springer.com
v

## PDF page 7/136
vi
Series Editor for this Volume
Olav Lysne, Simula Metropolitan Center for Digital Engineering, Oslo, NorwaySeries Foreword

## PDF page 8/136
Preface
Digital Twin: Architectures, Networks, and Applications oﬀers comprehensive, self-
contained knowledge on Digital Twin (DT), which is a highly promising technology
for achieving digital intelligence and digitally transformed society. DT is a key tech-
nology to connect physical systems and digital spaces. A digital twin is deﬁned as
the real-time digital replica of a real-world physical object. Digital twin in the digital
space is able to monitor, design, analyze, optimize and predict physical systems. The
advantages, including low maintenance cost, reduced security risk, and substantially
increased Quality-of-Service. Digital twin can also create unprecedented applica-
tions and services, ranging from Extended Reality (XR), immersive multimedia to
remote medical care, autonomous driving, Web 3.0 and Metaverse.
The objectives of this book are to provide the basic concepts of DT, to explore
the promising applications of DT integrated with emerging technologies, and to give
insights into the possible future directions of DT. For easy understanding, this book
also presents several use cases for DT models and applications in diﬀerent scenarios.
This book has the following salient features:
•Provides a comprehensive reference on state-of-the-art technologies for digital
twin
•Covers basic concepts, techniques, research topics and future directions
•Contains illustrative ﬁgures that enable easy understanding of digital twin
•Allows complete cross-referencing owing to the broad coverage on digital twin
•Identiﬁes the unique challenges for eﬃciently improving the performance of
digital twin networks
This book allows an easy cross-reference owing to the broad coverage on both the
principle and applications of DT. It provides a comprehensive technical guide cover-
ing basic concepts, innovative techniques, fundamental research challenges, recent
advances and future directions on DT. The book starts with the basic concepts, mod-
els, and network architectures of DT. Then, we present the new opportunities when
DT meets edge computing, Blockchain and Artiﬁcial Intelligence, and distributed
machine learning (e.g., federated learning, multi-agent deep reinforcement learning).
viibi-directional interaction between physical spaces and digital spaces brings many

## PDF page 9/136
viii Preface
In the last part, we present a wide application of DT as an enabling technology for
6G networks, Aerial-Ground Networks, and Unmanned Aerial Vehicles (UAVs). Wealso identify the future direction of DT in Reconﬁgurable Intelligent Surface (RIS)and Internet of Vehicles.
The primary audience includes senior undergraduates, postgraduates, educators,
scientists, researchers, engineers, innovators and research strategists. This book ismainly designed for academics and researchers from both academia and industrywho are working in the ﬁeld of telecommunications, computer science and engi-neering, and digitalization. Students majoring in computer science, electronics, and
communications will also beneﬁt from this book.
October, 2023 Yan Zhang

## PDF page 10/136
Acknowledgements
This early morning when I am about to write the preface and acknowledgement, I
came to realize that today is a very special day in Norway, ”Grunnlovsdagen” means
National day in Norwegian. Many people near Oslo travel to the city center and
celebrate the important day with happiness, mostly importantly without using mask.
In February 2022, Norway decided to lift all COVID-related restrictions. I would
like to take this opportunity to wish you all healthy, safe, and joyful every day.
I started to think of the research challenges related to Digital Twin from April
2020 when we had to stay at home due to COVID-19. After fruitful discussions with
collaborators and students, we came to understand the potential as well as the unique
challenges of DT. I am very proud that we are now leading this research ﬁeld of Digital
Twin, demonstrated by several landmark ”Hot Papers” and ”Highly Cited Papers”
in this ﬁeld. We invented new terms including Digital Twin Networks, Digital Twin
Edge Networks, and Wireless Digital Twin Networks, which are quickly recognized
and followed by the scientiﬁc community and industry. We also identiﬁed several
fundamental and unique challenges related to Digital Twin, e.g., edge association,
which reﬂects the essential physical-digital interaction. My gratefulness should go to
Special thanks go to Department of Informatics (IFI) at University of Oslo (UiO)
where I work full-time from 2016, which is one of the most important periods of
my career development. As a world-leading university over the world, UiO oﬀers
the chances to collaborate with the established professors, and the smart and hard-
working students in IFI. UiO strongly encourages an open, collaborative and student-
oriented environment. I am so lucky to have freedom to vision the future research
direction and then establish our research reputation in the ﬁeld of edge intelligence,
blockchain, energy informatics and recently digital twin.
Special thanks go to Simula Research Laboratory and Simula Metropolitan Cen-
ter for Digital Engineering where I worked full-time during 2006-2016 and part-time
after 2016 until now. The most important scientiﬁc contributions for elevating me
ixall of the excellent students and research collaborators Yulong Lu, Yueyue Dai, Wen
Sun, Sabita Maharjan, Li Jiang, and Ke Zhang and many others. I appreciate all their
contributions of time, discussions and ideas to study this exciting research ﬁeld digital
twin as well as make this bo

## PDF page 21/136
1.2 Digital Twin Concepts, Features, and Visions 5
Fig. 1.4 Digital twin: data–model–software
The digital twin provides precise mapping from the physical world to digital
space, with real-time interactions. Digital twin mitigates the huge gap between
physical space and digital space through continuous synchronization and updates.The features of digital twins can be summarized as follows.
•Precise mapping: Digital twin establishes the mapping between physical objects
and digital space. The historical data and current running status of physical objectsare synchronized to the digital space for further processing and analysis. Basedon the transmitted data, digital twins can completely reﬂect the status of physical
objects and establish full mapping between the physical space and digital space.
The mapping should completely reﬂect the full state of physical objects, with lowmapping error.
•Real time: Diﬀerent from conventional simulation and modelling technologies,digital twins keep synchronizing with physical objects in real time. The collecteddata are computed on the digital twin side to extract the corresponding status andbuild the model of physical objects. Communication is also executed continuouslyto update the digital twin models. Thus, real-time edge computing should beimplemented to ensure the timeliness of digital twins.
•Distributed : The physical objects of digital twins can be sensors, IoT devices, and
physical systems. In digital twin–assisted wireless networks, multiple physicalentities are distributed across the network. The digital twins of these entitiesare also distributed among diﬀerent edge servers. In such cases, distributed AItechniques are required to model digital twins from distributed physical objects.
•Intelligent : In addition to reﬂecting the running status of physical objects through
real-time data, digital twins also incorporate running models of physical objects.Intelligent techniques, especially AI algorithms, can be used to build digital
twin models by processing and analysing the large amounts of running data.With the help of the constructed models, digital twins can provide physical
systems with optimization, decisions, and predictions. For example, in intelligenttransportation, the digital twin of road traﬃc can help drivers decide on the optimal

## PDF page 41/136
3.2 DRL-Empowered DT 27
Agent
State Environment
Parameter 
TDeep Neural Network
(,)saTSPolicyAction ta State
1ts Observe New State Reward tr
ts
Fig. 3.2 DRL framework
Essentially, DRL is applied to sequential decision making, which can be mathe-
matically formulated as a Markov decision process (MDP). The DRL framework is
shown in Fig. 3.2. In each time slot 𝑡, the agent observes the current environment
state 𝑠𝑡and uses its policy to select an action 𝑎𝑡. A policy can be considered a map-
ping from any state to an action. After the action 𝑎𝑡is performed, the environment
moves to state 𝑠𝑡+1in the next time slot with transition probability 𝑃(𝑠𝑡+1|𝑠𝑡,𝑎𝑡).I n
addition, a corresponding reward 𝑟𝑡=𝑅(𝑠𝑡,𝑎𝑡)is obtained via the immediate reward
function, which is the evaluative feedback of the action taken. Given a stationaryand Markovian policy 𝜋, the next state of the environment, 𝑠
𝑡+1, is completely de-
termined by the current state, 𝑠𝑡. In this context, the current policy together with the
transition probability function determines the long-term cumulative reward. Assum-
ing𝜏=(𝑠𝑡,𝑎𝑡,𝑠𝑡+1,𝑎𝑡+1,···,𝑠𝑇,𝑎𝑇)is a trajectory from an MDP, the long-term
cumulative reward can be deﬁned as
𝐺(𝜏)=𝑇−𝑡/summationdisplay.1
𝑖=0𝛾𝑖𝑅(𝑠𝑡+𝑖,𝑎𝑡+𝑖), (3.1)
where 𝛾∈(0,1]is the discount factor that measures the importance of the future
reward and 𝑇is the length of an episode. For a continuous MDP, we have 𝑇−→ ∞ .
In an MDP, the key issue is to ﬁnd the optimal policy that maximizes the long-term
cumulative reward.
3.2.2 Incorporation of DT and DRL
As a promising AI technology, DRL provides a feasible method for solving complexproblems in unknown environments. However, there are still challenges to be resolved
in the process of DRL learning and implementation, which are discussed below.