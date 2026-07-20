## p7
vi
Series Editor for this Volume
Olav Lysne, Simula Metropolitan Center for Digital Engineering, Oslo, NorwaySeries Foreword

## p8
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

## p9
viii Preface
In the last part, we present a wide application of DT as an enabling technology for
6G networks, Aerial-Ground Networks, and Unmanned Aerial Vehicles (UAVs). Wealso identify the future direction of DT in Reconﬁgurable Intelligent Surface (RIS)and Internet of Vehicles.
The primary audience includes senior undergraduates, postgraduates, educators,
scientists, researchers, engineers, innovators and research strategists. This book ismainly designed for academics and researchers from both academia and industrywho are working in the ﬁeld of telecommunications, computer science and engi-neering, and digitalization. Students majoring in computer science, electronics, and
communications will also beneﬁt from this book.
October, 2023 Yan Zhang

## p10
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
twin as well as make this book possible.

## p11
x Acknowledgements
to IEEE Fellow have been carried out at Simula Research Laboratory. As an ad-
junct chief research scientist, I still receive strong support from Simula ResearchLaboratory, for which I am always much appreciated.
I am very grateful for the staﬀs at Springer for their support, patience and pro-
fessionalism since the beginning until the ﬁnal stage. All of them are extremelyprofessional and cooperative. Last but not least, I want to give my deep thanks to myfamilies and friends for their constant encouragement, patience and understandingthroughout this project.
Yan Zhang 17.05.2022

## p12
Contents
1 Introduction ................................................... 1
1.1 Overview of Digital Twin .................................... 1
1.2 Digital Twin Concepts, Features, and Visions ................... 3
1.3 Book Organization ......................................... 8
2 Digital T win Models and Networks ............................... 1 1
2.1 Digital Twin Models . . . ..................................... 1 1
2.1.1 DT Modelling Methods . . . ............................ 1 2
2.1.2 DT Modelling Challenges . ............................ 1 5
2.2 DT Networks (DTNs) . . ..................................... 1 6
2.2.1 DTN Concepts . ..................................... 1 7
2.2.2 DTN Communications ................................ 1 8
2.2.3 DTN Applications . . . ................................ 1 9
2.2.4 Open DTN Research Issues ............................ 2 0
3 Artiﬁcial Intelligence for Digital T win ............................ 2 3
3.1 Artiﬁcial Intelligence in Digital Twin . . . ....................... 2 3
3.2 DRL-Empowered DT . . ..................................... 2 6
3.2.1 Introduction to DRL . . ................................ 2 6
3.2.2 Incorporation of DT and DRL . . ....................... 2 7
3.2.3 Open Research Issues. ................................ 3 0
3.3 Federated Learning (FL) for DT . . ............................ 3 1
3.3.1 Introduction to FL . . . ................................ 3 1
3.3.2 Incorporation of DT and FL ........................... 3 2
3.3.3 Open Research Issues. ................................ 3 5
3.4 Transfer Learning (TL) for DT . . . ............................ 3 5
3.4.1 Introduction to TL . . . ................................ 3 5
3.4.2 Incorporation of DT and TL ........................... 3 7
3.4.3 Open Research Issues. ................................ 3 8
xi

## p13
xii Contents
4 Edge Computing for Digital T win ................................ 4 1
4.1 Digital Twin Edge Networks . ................................ 4 1
4.1.1 Digital Twin Edge Network Architecture . . . .............. 4 1
4.1.2 Computation Oﬄoading in Digital Twin Edge Networks .... 4 5
4.2 AI for Digital Twin Edge Networks ............................ 4 7
4.2.1 System Model . . ..................................... 4 7
4.2.2 Communication and Computation Model . . .............. 4 9
4.2.3 Latency Model . ..................................... 5 0
4.3 Edge Association for Digital Twin Edge Networks . .............. 5 1
4.3.1 System Model . . ..................................... 5 1
4.3.2 Edge Association: Deﬁnition and Problem Formulation .... 5 3
4.3.3 Multi-Agent DRL for Edge Association .................. 5 7
5 Blockchain for Digital T win ..................................... 6 1
5.1 Blockchain-Empowered Digital Twin . . . ....................... 6 1
5.2 Block Generation and Consensus for Digital Twin . .............. 6 4
5.2.1 Blockchain Model . . . ................................ 6 5
5.2.2 Relay-Assisted Transaction Relaying Scheme ............. 6 7
5.2.3 DPoS-Based Lightweight Block Veriﬁcation Scheme . ..... 6 8
5.2.4 Conclusion ......................................... 6 9
6 Digital T win for 6G Networks ................................... 7 1
6.1 Integration of Digital Twin and Sixth-Generation (6G) Networks . . . 71
6.2 Potential Use Cases ......................................... 7 2
6.3 Digital Twin for RIS . . . ..................................... 7 4
6.3.1 System Model . . ..................................... 7 4
6.3.2 Computation Oﬄoading in Digital Twin–Aided RIS . ..... 7 5
6.4 Stochastic Computation Oﬄoading ............................ 7 8
6.4.1 System Model . . ..................................... 7 8
6.4.2 Stochastic Computation Oﬄoading: Deﬁnition and
Problem Formulation . ................................ 7 9
6.4.3 Lyapunov Optimization for Stochastic Computation
Oﬄoading .......................................... 8 3
7 Digital T win for Aerial-Ground Networks ......................... 8 7
7.1 Introduction . .............................................. 8 7
7.2 Key Techniques . . .......................................... 8 9
7.2.1 Cross-Domain Resource Management ................... 8 9
7.2.2 Cross-Device Intelligent Cooperation ................... 9 2
7.3 DT for Task Oﬄoading in Aerial-Ground Networks .............. 9 4
7.3.1 System Model . . ..................................... 9 4
7.3.2 Utility Function ..................................... 9 4
7.3.3 Distributed Incentives for Satisfaction and Energy
Eﬃciency Maximization . . ............................ 9 5
7.3.4 Illustration of the Results . . ............................ 9 7

## p14
Contents xiii
7.4 DT and Federated Learning for Aerial-Ground Networks ......... 9 8
7.4.1 A DT Drone-Assisted Ground Network Model . . . ......... 9 8
7.4.2 Contribution Measurement and Reputation Value Model . . . 99
7.4.3 Incentive for Federated Learning Utility Maximization .....1 0 0
7.4.4 Illustration of the Results . . ............................1 0 1
8 Digital T win for the Internet of Vehicles ..........................1 0 5
8.1 Introduction . ..............................................1 0 5
8.2 DT for Vehicular Edge Computing ............................1 0 8
8.2.1 System Model . . .....................................1 0 9
8.2.2 DT and Multi-Agent Deep Reinforcement Learning for VEC 1118.2.3 Illustrative Results . . . ................................1 1 3
8.3 DT for Vehicular Edge Caching . . . ............................1 1 4
8.3.1 System Model . . .....................................1 1 6
8.3.2 DT-Empowered Content Caching .......................1 1 7
8.3.3 Illustrative Results . . . ................................1 1 9
References .........................................................1 2 1

## p15
Acronyms
6G Sixth generation mobile networks
AI Artiﬁcial intelligenceAR Augmented realityBS Base stationsD2D Device to deviceDDPG Deep deterministic policy gradientDITEN Digital twin edge networksDPoS Delegated proof of stakeDRL Deep reinforcement learningDT Digital twinDTN Digital twin networksEOS Enterprise Operation SystemIIoT Industrial Internet of thingsIoT Internet of thingsIoV Internet of vehiclesITS Intelligent transportation systemLSTM Long short-term memoryMBS Macro base stationMIMO Massive multiple-input-multiple-outputNFV Network function virtualizationPoW Proof-of-workPLM Product life-cycle managementRIS Reconﬁgurable intelligence surfaceRSU Roadside unitSDN Software deﬁned networkingTDMA Time division medium accessUAV Unmanned aerial vehicles
V2I Vehicle-to-infrastructure
V2P Vehicle-to-pedestrianV2R Vehicle-to-RSUV2S Vehicle-to-sensor
xv