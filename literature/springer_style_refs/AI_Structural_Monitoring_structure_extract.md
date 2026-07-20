===== p1 =====
Qiang Li · Peixuan Wang · 
Bawar Iftikhar · Yan Jiang · Mingfeng Huang
A Hybrid Data-Model 
and AI-Driven Approach for Structural Monitoring in Hazardous Construction
Li · Wang · Iftikhar · Jiang · HuangA Hybrid Data-Model and AI-Driven Approach for Structural 
Monitoring in Hazardous Construction

===== p2 =====
A Hybrid Data-Model and AI-Driven Approach 
for Structural Monitoring in Hazardous 
Construction

===== p3 =====
Qiang Li · Peixuan Wang · Bawar Iftikhar · 
Yan Jiang · Mingfeng Huang 
A Hybrid Data-Model 
and AI-Driven Approach for Structural Monitoring in Hazardous Construction

===== p4 =====
Author 
See next page 
ISBN 978-981-95-8687-5 ISBN 978-981-95-8688-2 (eBook) 
https://doi.org/10.1007/978-981-95-8688-2 
This work was supported by Ningbo Y outh Science and Technology Innovation Leading Talent Program 
(2025QL050), Ningbo Public Welfare Research Program (2023S004, 2024S005, 2025S023), National 
Natural Science Foundation of China (52508586), Natural Science Foundation of Zhejiang Province 
(LY24E080012), Ningbo Key R&D Program (2023Z221, 2024Z287, 2025Z037) and Ningbo International 
Sci-tech Cooperation Project (2024H019). 
© The Editor(s) (if applicable) and The Author(s) 2026. This book is an open access publication. 
Open Access This book is licensed under the terms of the Creative Commons Attribution-
NonCommercial-NoDerivatives 4.0 International License ( http://creativecommons.org/licenses/by-nc-
nd/4.0/ ), which permits any noncommercial use, sharing, distribution and reproduction in any medium or 
format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the 
Creative Commons license and indicate if you modiﬁed the licensed material. Y ou do not have permission 
under this license to share adapted material derived from this book or parts of it. 
The images or other third party material in this book are included in the book’s Creative Commons license, 
unless indicated otherwise in a credit line to the material. If material is not included in the book’s Creative 
Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted 
use, you will need to obtain permission directly from the copyright holder. 
This work is subject to copyright. All commercial rights are reserved by the author(s), whether the whole 
or part of the material is concerned, speciﬁcally the rights of translation, reprinting, reuse of illustrations, 
recitation, broadcasting, reproduction on microﬁlms or in any other physical way, and transmission or 
information storage and retrieval, electronic adaptation, computer software, or by similar or dissimilar methodology now known or hereafter developed. Regarding these commercial rights a non-exclusive 
license has been granted to the publisher. 
The use of general descriptive names, registered names, trademarks, service marks, etc. in this publication does not imply, even in the absence of a speciﬁc statement, that such names are exempt from the relevant protective laws and regulations and therefore free for general use. 
The publisher, the authors and the editors are safe to assume that the advice and information in this book are believed to be true and accurate at the date of publication. Neither the publisher nor the authors or the editors give a warranty, expressed or implied, with respect to the material contained herein or for any errors or omissions that may have been made. The publisher remains neutral with regard to jurisdictional 
claims in published maps and institutional afﬁliations. 
This Springer imprint is published by the registered company Springer Nature Singapore Pte Ltd. 
The registered company address is: 152 Beach Road, #21-01/04 Gateway East, Singapore 189721, 
Singapore 
If disposing of this product, please recycle the paper.

===== p5 =====
Qiang Li 
School of Civil Engineering 
NingboTech University Ningbo, Zhejiang, China 
Bawar Iftikhar School of Civil Engineering 
NingboTech University Ningbo, Zhejiang, China 
College of Civil Engineering and Architecture Zhejiang University Hangzhou, China 
Mingfeng Huang 
College of Civil Engineering and Architecture Zhejiang University Hangzhou, China 
School of Civil Engineering and Architecture Guangxi University Nanning, China Peixuan Wang Ningbo Construction Engineering Safety and Quality Management Service Center Ningbo, China 
Yan Jiang School of Civil Engineering 
Chongqing Jiaotong University Chongqing, China

===== p6 =====
Acknowledgements The work described in this study was supported by the 
National Natural Science Foundation of China (52508586); Zhejiang Provincial 
Natural Science Foundation of China (LY24E080012); Ningbo Y outh Science and Technology Innovation Leading Talent Program (2025QL050); Ningbo Key 
R&D Program (2023Z221, 2024Z287, 2025Z037); Ningbo Public Welfare Research Program (2023S004, 2024S005, 2025S023); Ningbo International Sci-tech Cooper-ation Project (2024H019). 
Competing Interests The authors have no competing interests to declare that are 
relevant to the content of this manuscript.
vii

===== p7 =====
Contents 
1 Introduction ................................................... 1 
1.1 Research Background and Signiﬁcance ........................ 1 
1.2 Review of Related Work ..................................... 3 
1.2.1 Safety Monitoring Technologies for Major Hazardous 
and Complex Engineering Structures .................... 3 
1.2.2 Artiﬁcial Intelligence in Safety Management and Risk 
Prediction of Critical Engineering Systems .............. 7 
1.2.3 State of the Art of Hybrid Data-Model-Driven Methods ... 8 
1.2.4 Summary and Research Gaps .......................... 11 
1.3 Research Objectives ........................................ 11 
1.4 Research Framework and Technical Roadmap .................. 12 
2 Hybrid Data-Model-Driven Theory .............................. 17 
2.1 Fundamentals of Machine Learning Models .................... 18 
2.1.1 Convolutional Neural Networks (CNNs) ................. 18 
2.1.2 Recurrent Neural Networks (RNNs) and BiLSTM ........ 20 
2.1.3 AdaBoost Ensemble Learning Algorithm ................ 22 
2.1.4 CNN-BiLSTM-AdaBoost Hybrid Algorithm ............. 23 
2.2 Hybrid Data-Model-Driven Methodology ...................... 25 
2.3 Summary .................................................. 28 
3 Hybrid Data-Model-Driven Prediction of T ower Crane 
Dynamic Responses Under Typhoon Loading ..................... 29 
3.1 IoT-Based Real-Time Monitoring System for Tower Cranes ...... 31 
3.1.1 Monitoring Equipment ................................ 31 
3.1.2 Monitoring Cloud Platform ............................ 33 
3.1.3 Monitoring Data Analysis ............................. 34 
3.2 Finite Element Dynamic Response Analysis of Tower Cranes 
Under Extreme Typhoon Loading ............................. 37 
3.2.1 Development and Calibration of the Finite Element 
Model .............................................. 37 
3.2.2 Simulation of Extreme Typhoon Conditions .............. 40
ix

===== p8 =====
x Contents
3.2.3 Dynamic Response Analysis of the Tower Crane 
Using FEM ......................................... 41 
3.3 Machine Learning-Based Prediction of Tower Crane 
Dynamic Responses ........................................ 45 
3.3.1 Data-Driven Prediction of Tower-Top Displacement ....... 45 
3.3.2 Hybrid Data-Model-Driven Prediction of Tower-Top 
Displacement ........................................ 49 
3.4 Summary .................................................. 53 
4 Real-Time Displacement Monitoring of High Formwork 
Support Structures Based on Computer Vision .................... 55 
4.1 Principles of Computer Vision-Based Displacement 
Measurement .............................................. 56 
4.2 Inﬂuence of External Factors on Measurement Accuracy ......... 61 
4.2.1 Major External Inﬂuencing Factors ..................... 61 
4.2.2 Experimental Design and Analysis of Factor Impacts 
on Accuracy ......................................... 63 
4.3 Real-Time Monitoring System for High Formwork Support 
Structures Based on Computer Vision ......................... 74 
4.3.1 Project Overview .................................... 74 
4.3.2 Real-Time Displacement Monitoring During Concrete 
Pouring ............................................. 75 
4.3.3 Monitoring Data Analysis ............................. 80 
4.4 Summary .................................................. 80 
5 Hybrid Data-Model-Driven Updating of Monitoring Alarm 
Thresholds and Short-T erm Response Prediction for High 
Formwork Support Structures ................................... 85 
5.1 Determination and Updating of Monitoring Alarm Thresholds .... 86 
5.1.1 Initial Alarm Threshold Determination .................. 86 
5.1.2 Updating of Alarm Thresholds ......................... 91 
5.2 Machine Learning-Based Response Prediction of High 
Formwork Support Structures ................................ 93 
5.2.1 Short-Term Structural Displacement Prediction ........... 93 
5.2.2 Rapid Inversion of Upper Construction Loads ............ 97 
5.3 Summary .................................................. 103 
6 Conclusions and Future Perspectives ............................. 111 
6.1 Key Innovations and Contributions ............................ 111 
6.2 Main Conclusions .......................................... 112 
6.3 Future Research Directions .................................. 113 
References ........................................................ 115

===== p9 =====
Chapter 1 
Introduction 
Abstract The background and signiﬁcance of research on hybrid data-model-driven 
safety monitoring and early warning technologies for hazardous engineering struc-
tures are presented. A comprehensive review and summary of the current domestic 
and international research status in structural safety monitoring, safety management, 
risk prediction, and hybrid data-model-driven methods for hazardous works are 
provided. The research content and chapter organization of this study are introduced. 
Keywords Structural safety monitoring ·Artiﬁcial intelligence ·Risk prediction ·
Hybrid data-model-driven methods 
1.1 Research Background and Signiﬁcance 
In recent years, with the in-depth implementation of national strategies such as 
“New-Type Urbanization” and “Strengthening the Nation through Transportation,” 
China has continuously increased investment in and construction of municipal infras-
tructure, leading to the emergence of a large number of major municipal projects, 
including large-scale bridges, interchanges, and elevated road systems. These large 
municipal projects are generally characterized by high clearance, large spans, long 
continuous sections, and irregular structural forms, which have resulted in the increas-
ingly widespread use of hazardous sub-item engineering works (hereinafter referred to as major hazardous works) during the construction stage. 
According to Order No. 37 of the Ministry of Housing and Urban–Rural Develop-
ment of the People’s Republic of China, Regulations on the Safety Management of Hazardous Sub-item Engineering Works, major hazardous works refer to sub-item 
construction works in building and municipal infrastructure projects that are prone to causing mass casualties or signiﬁcant economic losses during construction. Typical examples include tower cranes, high formwork support systems, and deep founda-
tion pits. Furthermore, the document Notice of the General Ofﬁce of the Ministry of Housing and Urban–Rural Development on Issues Related to the Implementation 
of the Regulations on the Safety Management of Hazardous Sub-item Engineering
© The Author(s) 2026 
Q. Li et al., A Hybrid Data-Model and AI-Driven Approach for Structural Monitoring in 
Hazardous Construction, https://doi.org/10.1007/978-981-95-8688-2_1 1

===== p10 =====
2 1 Introduction
Works (Jianban Zhi [2018] No. 31) speciﬁes that major hazardous works include, 
but are not limited to: concrete formwork support systems with a erection height of 
5 m or more, a span of 10 m or more, a total construction load of 10 kN/m2 or more, 
a concentrated line load of 15 kN/m or more, or structures whose height exceeds 
the horizontal projection width of the support and consist of relatively independent 
members without effective connections; as well as hoisting operations involving the installation and dismantling of lifting machinery, the use of unconventional lifting 
equipment or methods, and single lifting weights of 10 kN or more. 
Inﬂuenced by multiple factors, major hazardous engineering structures often 
exhibit low lateral stiffness and poor overall stability during construction, making 
instability and collapse accidents relatively frequent. As indispensable heavy equip-
ment on construction sites, tower cranes, owing to their tall and ﬂexible structural characteristics, face particularly high collapse risks under extreme weather condi-
tions. In recent years, frequent “gray swan” typhoon events along China’s south-eastern coastal regions have brought strong winds and heavy rainfall, posing severe threats to tower crane safety at coastal construction sites, as illustrated in Fig. 1. 
According to incomplete statistics, in September 2016, Typhoon Meranti made land-fall in Xiang’an District, Xiamen, causing the collapse of 79 tower cranes and damage 
to 30 tower cranes at construction sites across the city. In August 2017, Typhoon Hato struck Jinwan District, Zhuhai, resulting in varying degrees of damage to 137 tower cranes. In July 2021, Typhoon In-fa made landfall in Zhejiang Province with 
maximum wind speeds reaching Level 13 near its center, posing a signiﬁcant threat to the stability of tower cranes in coastal areas. In 2024, during the passage of the super typhoon Yagi across Haikou, Guangdong, and surrounding regions, numerous tower 
cranes were broken by strong winds and collapsed onto nearby residential build-ings, causing wall cracking and plaster detachment to varying degrees and seriously endangering public safety. 
In practical engineering projects, as construction height increases, the self-weight 
of support systems grows, deformation intensiﬁes, and structural stability decreases. Once a high formwork support system experiences sudden load variations during 
concrete pouring, ensuring its safety becomes increasingly difﬁcult. As temporary structures, high formwork systems are often subject to less stringent standards in erec-tion, dismantling, and full-process management compared with permanent structural 
construction, which has led to frequent collapse accidents, as shown in Fig. 2. For example, in 2017, improper concrete pouring procedures at the Xianshan Peony Expo Park Water Amusement Project in Macheng, Hubei Province, resulted in 9 fatalities 
and 8 injuries. In 2019, the collapse of a formwork support system due to non-compliant structural parameters at the Garden Home Furnishing Market construction 
project in Nanma Town, Dongyang City, caused 5 deaths and 5 injuries. In 2020, a high formwork collapse occurred at a tourism development project in Wuhan due to improper erection and concentrated loading, resulting in 6 deaths and 5 injuries. 
In 2023, a high formwork support structure in a railway logistics project in Shanxi Province collapsed because of excessive spacing between vertical members and axial compression overload, leading to 7 fatalities.

===== p11 =====
1.2 Review of Related Work 3
The above accident cases repeatedly demonstrate that once major hazardous engi-
neering structures lose stiffness and stability, they often progress to overall collapse 
within minutes or even seconds, leaving an extremely limited escape window for on-site personnel. Therefore, real-time and effective safety monitoring and intelli-
gent early warning for major hazardous works are critical means to achieve predic-tive maintenance and ensure long-term structural safety. However, traditional moni-toring methods largely rely on manual inspections and simple sensing technologies, 
which suffer from limitations such as restricted monitoring coverage, insufﬁcient data processing capability, and delayed warning responses. The rapid development of technologies such as the Internet of Things (IoT) and artiﬁcial intelligence has 
provided new technical approaches for safety monitoring and early warning of major hazardous engineering structures. By integrating data analysis with physical model simulation-namely, hybrid data-model-driven techniques-the structural safety state 
can be assessed more comprehensively and accurately, enabling early warning and intelligent decision-making. 
In summary, to ensure the safety and reliable operation of major hazardous engi-
neering structures during construction, it is necessary to leverage advanced sensing technologies and artiﬁcial intelligence algorithms to establish a hybrid data-model-
driven safety monitoring and early warning system for major hazardous works, thereby improving the overall technical level of structural safety monitoring and early warning. The successful implementation of this research can provide robust 
technical support for safety monitoring and early warning of major hazardous engi-neering structures and is of great signiﬁcance for enhancing safety management prac-tices, improving the accuracy and reliability of early warning systems, preventing 
and reducing safety accidents, and ultimately safeguarding human life. 
1.2 Review of Related Work 
1.2.1 Safety Monitoring Technologies for Major Hazardous 
and Complex Engineering Structures 
Structural safety monitoring technology has long been a research focus in the ﬁeld 
of civil engineering. In recent years, with the rapid development of sensors, the 
Internet of Things (IoT), and computer technologies, research on structural safety monitoring has exhibited a trend toward multi-technology integration, intelligence, 
and systematization, with the core objective of preventing potential safety accidents through real-time monitoring and data analysis. 
In the area of safety monitoring for major hazardous engineering structures, 
numerous scholars have developed advanced IoT-based sensing and monitoring technologies [1–4]. These technologies deploy various sensors on structures-such 
as accelerometers, load sensors, distance sensors, tilt sensors, and displacement sensors-to collect structural parameters in real time, including acceleration, lifting

===== p12 =====
4 1 Introduction
load, working radius, inclination, and displacement. For tower crane structures, 
Wu et al. [5] developed a blockchain-based framework in which an IoT system 
(including load sensors, distance sensors, tilt sensors, and unmanned aerial vehi-cles) was employed to semi-automatically collect relevant data, enabling real-time 
monitoring of crane group safety risks and identiﬁcation of potential on-site hazards. Zhong et al. [6] proposed an IoT-based safety management system for tower crane clusters, which acquires real-time crane status through sensors measuring trolley 
horizontal and vertical positions, jib and load angles, as well as tower inclination and wind speed, aiming to enhance safety and reduce collision risks during construc-tion activities. Cheng and Teizer [7] installed an ultra-wideband (UWB) sensing 
infrastructure to track the positions of ground workers and crane hooks, thereby improving operators’ ability to identify potentially unsafe crane behaviors. Luo et al. [8] proposed an autonomous construction site safety monitoring system that utilizes 
various sensors (radio-frequency identiﬁcation, positioning sensors, accelerome-ters, and load measurement units) to collect information and monitor crane oper-ating conditions and worker locations in real time. This system can promptly detect 
unsafe distances between workers and crane loads and issue corresponding warn-ings, thereby reducing accident occurrence. For high formwork structures, Y uan 
et al. [9] developed a cyber-physical system (CPS)-based temporary structure moni-toring system, which uses different types of sensors (load sensors, switch sensors, accelerometers, and displacement sensors) to collect performance data of scaffolding 
structures and transmit them in real time to a cloud database for storage and anal-ysis, enabling immediate alarms when potential hazards are detected; Chen et al. [10] developed an intelligent monitoring system for high formwork structures, which 
improves construction safety by conducting real-time and high-frequency monitoring of structural settlement, inclination, and displacement; Moon et al. [11] established a local ubiquitous sensor network (USN) for real-time data acquisition to monitor the 
inclination, deﬂection, and strain of formwork support systems and compare them with limit values to determine whether the systems remain stable within allowable ranges, and subsequently proposed an integrated environment that combines multiple 
communication technologies to achieve real-time data acquisition, wireless trans-mission, visualization, and remote monitoring via mobile devices [12, 13], gradually advancing technological development and application depth and improving the efﬁ-
ciency and effectiveness of construction safety monitoring. In summary, monitoring systems based on IoT and sensor technologies can effectively improve construc-tion site safety and productivity by collecting and analyzing structural parameters 
in real time, thereby reducing accident risks. However, these contact-based sensors require manual climbing during installation, inspection, maintenance, and disman-
tling, which poses signiﬁcant operational safety risks. In addition, extensive cable deployment increases potential safety hazards. Therefore, it is necessary to develop a remote, non-contact monitoring and early warning system suitable for complex 
construction site environments. 
In recent years, computer vision technology, as a typical non-contact monitoring 
method, has been widely applied in the ﬁeld of structural monitoring [14–17]. A 
typical computer vision-based measurement method mainly consists of three parts:

===== p13 =====
1.2 Review of Related Work 5
camera calibration, target tracking, and three-dimensional reconstruction [18, 19]. 
This technology is primarily used in studies on structural surface damage identi-
ﬁcation [20, 21], vibration response monitoring [22], strain monitoring [23], and risk target tracking [24, 25]. In structural monitoring, measurement accuracy has 
become a major concern. Factors affecting the accuracy of computer vision-based structural vibration measurements can be divided into internal and external factors. Internal factors include image quality, image motion blur, camera calibration algo-
rithms, and target tracking algorithms, while external factors include camera vibra-tion, camera tilt angle, target size, changes in ambient lighting, fog, temperature, and heat haze [26–28]. Most studies focus on verifying whether newly proposed computer 
vision-based monitoring systems are effective and accurate, while also considering the inﬂuence of certain external factors on measurement results. Some researchers have experimentally investigated how external factors affect computer vision moni-
toring systems and attempted to identify corresponding solutions. For example, Ye et al. [29] studied the effects of illumination, camera elevation angle, and fog on template matching methods and proposed using adaptive algorithms and predic-
tive algorithms to address measurement accuracy issues caused by lighting condi-tions and vapor-induced target occlusion; Zhou et al. [30] investigated the impact 
of long-term environmental temperature variations on visual monitoring systems and proposed that temperature-induced measurement errors could be removed from displacement measurements by exploiting the relationship between measurement 
error and temperature change or by using time–frequency analysis methods. 
In the ﬁeld of monitoring major hazardous engineering structures, computer 
vision-based methods have received a certain degree of attention [31–33]. In applica-
tions to tower crane structures, some researchers installed top-view cameras on crane 
jibs with the optical axis pointing toward the ground to perform image recognition of hazardous areas, workers, or crane hooks. For example, Yang et al. [34] proposed 
a novel safety distance monitoring method that collects video data using pan-tilt-zoom (PTZ) cameras and applies Mask R-CNN to identify potential hazards, hooks, and workers, helping crane operators work more effectively and reducing collision 
accidents; however, such PTZ cameras can only capture the working plane and are highly sensitive to lighting conditions. Wang et al. [35] proposed a real-time three-dimensional spatial map reconstruction method based on images from PTZ cameras 
mounted on crane tops, which displays workspace boundary lines during crane oper-ations to improve safety and efﬁciency; Price et al. [36] developed a real-time tower crane monitoring system integrating vision systems and laser scanning technology, 
in which a monocular camera mounted at the jib tip is used for load tracking and detection of nearby workers, thereby improving safety and efﬁciency in blind lifting 
operations. However, the use of top-view cameras mounted on ﬁxtures introduces additional installation complexity, interference, and limited ﬁelds of view. To address these issues, some scholars have utilized existing monocular long-range surveillance 
PTZ cameras for remote monitoring. For example, Wang et al. [37] proposed a framework for real-time recognition and localization of tower cranes and hooks using monocular long-range cameras, which integrates multiple advanced computer 
vision methods to achieve real-time three-dimensional positioning of tower cranes,

===== p14 =====
6 1 Introduction
including precise monitoring of jib orientation and hook position, thereby supporting 
safety supervision for construction sites and crane operators and reducing collision 
accidents; Yang et al. [38] installed PTZ cameras on the rooftops of buildings near construction sites and automatically identiﬁed the operational states of tower cranes 
during construction, such as concrete pouring and non-concrete material transporta-tion, by tracking jib rotation angles and combining site layout information, thereby improving construction efﬁciency and safety. In applications to high-formwork struc-
tures, an intelligent real-time construction monitoring method based on computer vision and ﬁnite element analysis was established [39], enabling remote, real-time, and multi-point monitoring of support structures; Feng et al. [40] compared the 
performance of three algorithms-population-based intelligent digital image corre-lation (DIC), David Lowe’s scale-invariant feature transform (SIFT), and Hessian matrix-based speeded-up robust features (SURF)-in feature detection and matching, 
and proposed a vision-based monitoring method capable of accurately monitoring displacement and strain of support structures in real time, thereby ensuring construc-tion safety; Jung et al. [41] proposed using image processing techniques to auto-
matically detect deformation of support systems and identify minor changes through small-scale experiments; Luo et al. [42] achieved three-dimensional deformation 
monitoring of support systems using laser point cloud data by establishing and comparing scaled pipe-axis models at different time points. However, during concrete pouring operations, frequent occlusion of optical paths by workers and machinery 
often leads to target tracking failure and centroid drift, resulting in distorted moni-toring results. To address this issue, a real-time monitoring method for high formwork support systems based on online cameras was proposed to resolve target occlusion 
challenges in complex environments, and this method has been successfully applied in practical formwork engineering projects [43]. 
Some innovative technologies have also been preliminarily applied to major 
hazardous engineering structures. For example, Zhang and Pan [44] proposed the use of virtual reality (VR) technology to allow workers to immersively experience various safety risks that may be encountered during construction; He et al. [45] suggested that 
augmented reality (AR) technology could overlay real-time data or instructions onto crane control devices, helping operators understand data and interact with equip-ment, thereby enabling informed and precise decision-making during maintenance 
and production tasks. However, VR and AR systems involve high costs in hardware, software development, and operator training, and may not be suitable for smaller projects with limited resources. In addition, some researchers have applied unmanned 
aerial vehicles (UA Vs) to structural monitoring [46]; however, due to limited battery life and safety concerns, UA Vs cannot remain airborne for long durations. 
Although signiﬁcant progress has been made in real-time monitoring of major 
hazardous engineering structures, there are still some deﬁciencies in prediction and early warning. Most existing monitoring systems are limited to data collection and 
recording and lack reliable early warning capabilities, making it difﬁcult to accurately predict structural response trends. When structures face potential risks, insufﬁcient emergency response time is provided for construction sites, thereby increasing safety 
risks. Moreover, for high formwork structures, the setting of alarm thresholds in

===== p15 =====
1.2 Review of Related Work 7
existing monitoring systems is usually based on general safety standards and manu-
facturers’ recommendations. Since each project has unique design characteristics, 
construction conditions, and service environments, these standards may not be appli-cable to speciﬁc projects. Therefore, the development of scientiﬁc and reasonable 
methods for determining early warning thresholds is of great importance. 
1.2.2 Artiﬁcial Intelligence in Safety Management and Risk 
Prediction of Critical Engineering Systems 
Machine learning (ML) and deep learning, as core technologies of artiﬁcial intelli-
gence, have broad application prospects in the engineering ﬁeld [47, 48]. Owing to 
their strong data pattern recognition capabilities and powerful nonlinear modeling abilities, they demonstrate clear advantages in handling complex engineering prob-
lems. As a result, a large number of studies have been conducted on safety management and risk prediction for major hazardous engineering structures. 
In the area of safety management for major hazardous engineering works, existing 
studies mainly focus on three aspects: real-time structural monitoring and state assessment, unsafe behavior identiﬁcation, and operation optimization and path plan-
ning [49–54]. For example, in real-time structural monitoring and state assessment, Sakhakarmi et al. [55] used support vector machines (SVMs) to analyze real-time strain data to ensure scaffold safety, achieving prediction accuracy exceeding 98% 
with limited datasets and demonstrating the potential of ML for real-time scaffold assessment. By leveraging the strong random search capability and global optimiza-tion tendency of genetic algorithms, an improved genetic algorithm was developed 
and integrated with a BP neural network using the inverse of the sum of squared errors as the ﬁtness function [56]. This approach effectively predicted and identiﬁed the operational states of tower cranes for fault diagnosis, demonstrating the effectiveness 
of combining optimization algorithms with neural networks for state assessment. In terms of unsafe behavior identiﬁcation, Ding et al. [54] developed an unsupervised learning model based on generative adversarial networks (GANs), incorporating ﬁve 
pseudo-anomaly synthesizers to detect unsafe behaviors of construction workers; Jiang et al. [57] proposed a transfer learning-based recognition framework to identify 
unsafe tower crane hoisting behaviors, particularly inclined lifting, sudden braking, and sudden unloading, with results showing that the transfer learning model achieved a recognition accuracy of 76.74%, outperforming other methods. Current studies 
mostly focus on identifying single behaviors or individual components; however, in real construction environments, multiple unsafe behaviors are often interrelated. In the area of operation optimization and path planning, Yin et al. [58] proposed a coop-
erative co-evolutionary genetic algorithm (CCGA) to optimize the service scheduling problem of overlapping tower cranes and compared its performance with traditional genetic algorithms (TGA) and nearest neighbor algorithms (NNA), showing that 
CCGA outperformed the others in terms of optimal completion time and required

===== p16 =====
8 1 Introduction
CPU time; Kim et al. [59] adopted a deep learning-based deep global registration 
(DGR) algorithm to determine relative transformations between consecutive point 
clouds in scaffold structures. 
In terms of risk prediction, research has mainly focused on structural dynamic 
response prediction, stability prediction, fault prediction, and collision avoidance prediction [60–67]. For example, Li et al. [64] established a real-time tower crane monitoring system based on IoT technology to achieve long-term monitoring of 
crane dynamic responses under extreme weather conditions such as typhoons, and, based on on-site measured wind speed data, used BP and RBF ML models to predict the maximum displacement of tower cranes in advance under the strong typhoon 
“In-fa”; Zhang and Ge [65] applied a trajectory prediction model based on the trans-former algorithm to predict the future trajectories of monitored objects within the next 10 s using historical data, helping workers avoid potential collision accidents 
and improving tower crane construction safety; Wei [66] developed an LSTM neural network-based warning system to predict and prevent scaffold failures under extreme wind conditions, integrating wind speed prediction models, wind force analysis, 
and scaffold collapse assessment to address safety issues in typhoon-prone regions. Moreover, tower crane safety prediction was predicted by constructing ML models 
[67] that use load, working radius, rotation angle, wind speed, and height as inputs to predict crane moment variations, and employed a cuckoo algorithm to optimize neural networks to avoid local optima during training, thereby improving prediction 
accuracy. 
In summary, data-driven methods based on artiﬁcial intelligence have achieved 
signiﬁcant breakthroughs and widespread application in engineering management 
and monitoring; however, many challenges remain. For instance, although tradi-
tional data-driven approaches can achieve good predictive accuracy within the range of available datasets, they heavily depend on the completeness of historical data. 
When data are incomplete, difﬁcult to obtain, or when samples of extreme events are insufﬁcient, these methods exhibit notable limitations [68]. Therefore, to overcome these shortcomings, it is necessary to improve traditional data-driven approaches 
in order to enhance the accuracy of structural response prediction under extreme conditions. 
1.2.3 State of the Art of Hybrid Data-Model-Driven Methods 
In recent years, hybrid data-model-driven methods have become one of the key tech-
nologies for ensuring structural safety and improving project management efﬁciency. 
In the ﬁeld of civil engineering, the applications of such methods can generally be classiﬁed into two categories. The ﬁrst category involves using on-site monitoring 
data to perform real-time calibration, error compensation, and parameter updating of digital models, governing equations, or physical models, thereby enabling model-based representations to better reﬂect actual operating conditions. The second cate-
gory focuses on generating a large number of extreme-condition or missing-condition

===== p17 =====
1.2 Review of Related Work 9
samples through ﬁnite element simulations to compensate for insufﬁcient historical 
data, thereby enabling early warning and prediction of structural responses. 
Within hybrid data-model-driven applications, the establishment of digital twin 
models plays a critical role in structural safety management. Numerous studies have demonstrated that integrating Building Information Modeling (BIM) with IoT 
technologies can signiﬁcantly improve efﬁciency by enabling real-time feedback 
and visualized management, thereby enhancing project collaboration efﬁciency and 
decision-making quality [69–74]. For example, Cheng [72] employed Revit software 
to construct three-dimensional models and connected physical entities with virtual models via IoT technology to enable real-time updating and prediction of building 
states and performance; Pan and Zhang [73] proposed a digital twin framework based on IoT, BIM, and data mining to promote intelligent construction management; simi-larly, Zhang et al. [74] developed a digital twin analysis framework integrating BIM, 
IoT, and data storage and analysis, which was shown to improve construction quality, efﬁciency, and safety. However, BIM models primarily describe geometric conﬁgu-rations, spatial locations, and material properties, and are unable to directly simulate 
structural mechanical behavior or predict structural responses under varying loading conditions. 
To address these limitations, some researchers have integrated monitoring data 
with mechanism-based governing equations, thereby improving simulation accu-racy and numerical stability. For example, Gao et al. [75] proposed a mechanism-
data hybrid-driven method for predicting drilling energy consumption by estab-lishing power and energy models combined with an LSSVM-based data compensa-tion model and an improved whale optimization algorithm, achieving high-accuracy 
energy consumption prediction and validating the effectiveness of the hybrid-driven approach through multi-perspective visualization. A hybrid-driven urban drainage ﬂow simulation model was developed in which neural networks were employed as 
error correctors to calibrate numerical solutions of the one-dimensional Saint–V enant equations, demonstrating that the integration of deep learning not only improves simulation accuracy and numerical stability but also reveals intrinsic relationships 
between modeling errors and input conditions, thereby overcoming key limitations of traditional mechanism-based models [76]. In another study, a mechanism-data hybrid-driven dynamic model for hunting dampers was established by coupling 
damper mechanism models with neural network techniques, resulting in enhanced model stability and accelerated convergence speed [77]. Furthermore, a mechanism-data hybrid-driven short-process power model was proposed for steel production 
enterprises, in which a mechanism-based model was used to capture the coupling characteristics of material and energy ﬂows between successive processes, while 
data-driven models were applied to construct mappings between non-electrical process variables and power function parameters [78]. Case studies based on measured data from a domestic steel enterprise veriﬁed the effectiveness and accu-
racy of the proposed model. Overall, the integration of mechanism-based models and data-driven methods demonstrates strong potential by providing deeper physical insight and compensating for the shortcomings of traditional mechanism models. 
However, once structural geometry, damage states, or loading conditions change,

===== p18 =====
10 1 Introduction
mechanism-based models often require re-derivation or substantial modiﬁcation of 
governing equations and cannot be updated as efﬁciently as ﬁnite element models 
through mesh modiﬁcation and parameter adjustment. 
With the advancement of computer technology, ﬁnite element models (FEMs), as 
powerful numerical analysis tools, can provide more accurate descriptions of struc-tural mechanical behavior; however, FEMs are highly dependent on precise material parameters and boundary conditions and are often difﬁcult to adapt to uncertainties 
in real engineering applications. To overcome these limitations, researchers have increasingly combined monitoring technologies with FEMs to achieve more compre-hensive structural analysis and prediction [79–88]. For example, Ghahari et al. [84] 
updated beam FEM using measured data and trained Gaussian process regression models based on residuals between predicted and measured responses to estimate seismic responses of building ﬂoors without installed sensors. A three-dimensional 
milling ﬁnite element model was constructed using ABAQUS, and a Python subrou-tine based on the Fick wear rate model was developed to accurately simulate the evolution of tool wear, with ﬁnal wear prediction achieved through a MA TLAB-based 
graphical user interface module [85]. In the domain of lifting machinery and special equipment, a comprehensive strategy combining measured samples, ﬁnite element 
simulation, and cyclic sample iteration was proposed to address challenges related to large-scale load spectrum testing and fatigue life simulation errors, thereby enabling reliable evaluation of the remaining fatigue life of crane metal structures [86]. In the 
ﬁeld of formwork support systems, Wang et al. [87] developed a reliability-based limit state design method using advanced ﬁnite element techniques and updated statistical data on scaffold resistance and construction loads; Cho et al. [88] developed wireless 
strain sensing modules for real-time data acquisition, constructed FEM models to characterize scaffold behavior under speciﬁc loading conditions, and applied support vector machine (SVM) algorithms for decision-making, achieving an average predic-
tion accuracy of 97.66%. Furthermore, some studies have integrated monitoring tech-nologies, BIM, and FEM to establish digital twin frameworks, enabling prediction and analysis of structural mechanical responses under different loading conditions 
and signiﬁcantly improving the efﬁciency and accuracy of engineering manage-ment and safety control. For example, Sun et al. [88, 89] established a digital twin framework integrating FEM, BIM, and IoT technologies to achieve efﬁcient data 
management and four-dimensional visualization of bridge structures; Jiang et al. [90] combined BIM and FEM to develop virtual models and dynamic analyses, and proposed a digital twin-based framework for human–machine interaction in tower 
crane construction activities to evaluate the effects of unsafe lifting behaviors on crane stability; Liu et al. [91, 92] investigated digital twin-based safety assessment 
methods for prestressed steel structures by integrating BIM, FEM, monitoring data, and SVM-based predictive models to estimate structural safety risk levels. 
In summary, hybrid data-model-driven methods play a crucial role in the digital 
transformation of the construction industry. By integrating the complementary strengths of data-driven and model-driven approaches, these methods have been

===== p123 =====
References 117
44. Zhang, Z., Pan, W.: Virtual reality supported interactive tower crane layout planning for 
high-rise modular integrated construction. Autom. Constr. 130 (2021) 
45. He, F., Ong, S.K., Nee, A.Y .C.: An integrated mobile augmented reality digital twin monitoring system. Computers 10(8) (2021) 
46. Shanti, M.Z., et al.: Real-time monitoring of work-at-height safety hazards in construction sites using drones and deep learning. J. Safety Res. 83, 364–370 (2022) 
47. Baduge, S.K., et al.: Artiﬁcial intelligence and smart vision for building and construction 4.0: machine and deep learning methods and applications. Autom. Constr. 141 (2022) 
48. Mohtasham Moein, M., et al.: Predictive models for concrete properties using machine learning and deep learning approaches: A review. J. Build. Eng. 63 (2023) 
49. Zhang, C., Hammad, A.: Improving lifting motion planning and re-planning of cranes with consideration for safety and efﬁciency. Adv. Eng. Inform. 26(2), 396–410 (2012) 
50. Hyun, H., et al.: Tower crane location optimization for heavy unit lifting in high-rise modular construction. Buildings 11(3) (2021) 
51. Khodabandelu, A., Park, J., Arteaga, C.: Improving multitower crane layout planning by leveraging operational ﬂexibility related to motion paths. J. Manag. Eng. 39(5) (2023) 
52. Lu, Y ., et al.: Automated detection of dangerous work zone for crawler crane guided by UA V 
images via Swin transformer. Autom. Constr. 147 (2023) 
53. Wang, Z., et al.: Integrated reinforcement and imitation learning for tower crane lift path 
planning. Autom. Constr. 165 (2024) 
54. Ding, C., et al.: Identifying unsafe behaviors of construction workers through an unsupervised multi-anomaly GAN approach. Autom. Constr. 165 (2024) 
55. Sakhakarmi, S., et al.: Automated scaffolding safety analysis: strain feature investigation using support vector machines 47(8), 921–928 (2020) 
56. Jingqiang, S., Sicong, Y ., Dongdong, W., et al.: Application of genetic algorithm-optimized BP neural networks in fault diagnosis of tower cranes. Hoisting Conveying Mach. 04, 61–64 (2012). (In Chinese) 
57. Jiang, W., Ding, L.: Unsafe hoisting behavior recognition for tower crane based on transfer learning. Autom. Constr. 160 (2024) 
58. Yin, J., et al.: Optimization of service scheduling problem for overlapping tower cranes with cooperative coevolutionary genetic algorithm. Eng. Constr. Archit. Manag. 31(3), 1348–1369 
(2022) 
59. Kim, J., et al.: Point cloud registration considering safety nets during scaffold installation using sensor fusion and deep learning. Autom. Constr. 159 (2024) 
60. Shen, T., Nagai, Y ., Gao, C.: Design of building construction safety prediction model based on optimized BP neural network algorithm. Soft. Comput. 24(11), 7839–7850 (2019) 
61. Smoczek, J., Szpytko, J.: Evolutionary algorithm-based design of a fuzzy TBF predictive model and TSK fuzzy anti-sway crane control system. Eng. Appl. Artif. Intell. 28, 190–200 
(2014) 
62. Jianrong, Z., Wei, Z., Nannan, X., et al.: Safety accident prediction and cause analysis of tower cranes based on random forest algorithm. Saf. Environ. Eng. 28(05), 36–42 (2021). (In 
Chinese) 
63. Yanbin, X., et al.: Research on optimization of crane fault predictive control system based on data mining. Nonlinear Eng. 12(1) (2023) 
64. Li, Q., et al.: Machine learning-based prediction of dynamic responses of a tower crane under strong coastal winds. J. Mar. Sci. Eng. 11(4) (2023) 
65. Zhang, M., Ge, S.: Vision and trajectory-based dynamic collision prewarning mechanism for tower cranes 148(7), 04022057 (2022) 
66. Wei, C.-C.: Collapse warning system using LSTM neural networks for construction disaster prevention in extreme wind weather. J. Civ. Eng. Manag. 27(4), 230–245 (2021) 
67. Han, J., Bixiong, Z., Yicheng, L., et al.: Safety analysis of tower cranes based on BP neural networks optimized by the cuckoo search algorithm. Ind. Constr. 53(S2), 790–793 (2023). 
(In Chinese)

===== p124 =====
118 References
68. Tamascelli, N., et al.: Learning from major accidents: a machine learning approach. Comput. 
Chem. Eng. 162 (2022) 
69. Tang, S., et al.: A review of building information modeling (BIM) and the internet of things (IoT) devices integration: present status and future trends. Autom. Constr. 101, 127–139 
(2019) 
70. Hu, X., Assaad, R.H.: A BIM-enabled digital twin framework for real-time indoor environment monitoring and visualization by integrating autonomous robotics, LiDAR-based 3D mobile mapping, IoT sensing, and indoor positioning technologies. J. Build. Eng. 86 (2024) 
71. Tak, A.N., et al.: BIM-based 4D mobile crane simulation and onsite operation management. Autom. Constr. 128 (2021) 
72. Cheng, J.C.P., et al.: Data-driven predictive maintenance planning framework for MEP components based on BIM and IoT using machine learning algorithms. Autom. Constr. 112 
(2020) 
73. Pan, Y ., Zhang, L.: A BIM-data mining integrated digital twin framework for advanced project management. Autom. Constr. 124 (2021) 
74. Zhang, J., et al.: Digital twins for construction sites: concepts, LoD deﬁnition, and applications. J. Manag. Eng. 38(2) (2022) 
75. Gao, K., Xu, X., Jiao, S.: Prediction and visualization analysis of drilling energy consumption based on mechanism and data hybrid drive. Energy 261 (2022) 
76. Zhenyu, H., Yiming, W., Dazhen, Z., et al.: Hybrid mechanism-data-driven modeling method for urban drainage pipe networks. Water Wastewater Eng. 60(11), 149–159 (2024). (In Chinese) 
77. Changxin, C., Kewei, W., Liqian, W., et al.: Dynamic modeling of hunting dampers based on a mechanism-data hybrid-driven approach. Modern Urban Transit 01, 72–80 (2025). (In 
Chinese) 
78. Yi, Z., Shouquan, S., Siyang, L., et al.: Mechanism-data hybrid-driven short-process power model for steel production enterprises. Proc. Chin. Soc. Electr. Eng. 45(18), 7098–7110 (2025). (In Chinese) 
79. Johns, B., Abdi, E., Arashpour, M.: Dynamical modelling of boom tower crane rigging systems: model selection for construction. Arch. Civ. Mech. Eng. 23(3) (2023) 
80. Ebrahimian, H., et al.: Estimation of soil-structure model parameters for the millikan library building using a sequential Bayesian ﬁnite element model updating technique. Buildings 13(1) 
(2022) 
81. Roohi, M., Hernandez, E.M., Rosowsky, D.: Nonlinear seismic response reconstruction and performance assessment of instrumented wood-frame buildings-Validation using NEESWood Capstone full-scale tests. Struct. Control. Health Monit. 26(9) (2019) 
82. Chen, W., et al.: Wind-induced tower crane vibration and safety evaluation. J. Low Freq. Noise, Vib. Act. Control. 39(2), 297–312 (2019) 
83. Ereiz, S., Duvnjak, I., Fernando Jiménez-Alonso, J.: Review of ﬁnite element model updating 
methods for structural applications. Structures 41, 684–723 (2022) 
84. Ghahari, F., et al.: A hybrid model-data method for seismic response reconstruction of 
instrumented buildings. Earthq. Spectra 40(2), 1235–1268 (2024) 
85. Wang, Y .: Simulation study on ball-end milling tool wear during TC4 milling processes. Harbin University of Science and Technology (2020) (In Chinese) 
86. Xiaogang, Q., Xiaokang, Z., Songyan, J., et al.: Numerical simulation of remaining service life of bridge cranes based on fracture mechanics. J . S a f . E n v i r o n . 22(03), 1284–1290 (2022).
(In Chinese)
87. Wang, C., et al.: System reliability-based limit state design of support scaffolding systems. Eng. Struct. 216 (2020) 
88. Cho, C., et al.: Data-driven monitoring system for preventing the collapse of scaffolding structures. J. Constr. Eng. Manag. 144(8) (2018) 
89. Sun, L., et al.: Hybrid monitoring methodology: A model-data integrated digital twin frame-work for structural health monitoring and full-ﬁeld virtual sensing. Adv. Eng. Inform. 60 (2024)

===== p125 =====
References 119
90. Jiang, W., Ding, L., Zhou, C.: Digital twin: Stability analysis for tower crane hoisting safety 
with a scale model. Autom. Constr. 138 (2022) 
91. Liu, Z., et al.: Digital twin-based safety evaluation of prestressed steel structure. Adv. Civ. Eng. 2020(1) (2020) 
92. Liu, Z., et al.: Intelligent prediction method for operation and maintenance safety of prestressed steel structure based on digital twin technology. Adv. Civ. Eng. 2021(1) (2021) 
93. Shan, L., et al.: CNN-BiLSTM hybrid neural networks with attention mechanism for well log prediction. J. Pet. Sci. Eng. 205 (2021) 
94. Ma, T., et al.: Horizontal in situ stresses prediction using a CNN-BiLSTM-attention hybrid neural network. Geomech. Geophys. Geo-Energy Geo-Resour. 8(5) (2022) 
95. Wei, Z., et al.: A method for sound speed proﬁle prediction based on CNN-BiLSTM-attention network. J. Mar. Sci. Eng. 12(3) (2024) 
96. Xu, J., et al.: A novel and robust data anomaly detection framework using LAL-AdaBoost for structural health monitoring. J. Civ. Struct. Heal. Monit. 12(2), 305–321 (2022) 
97. Huang, M., et al.: Typhoon wind hazard estimation by full-track simulation with various wind intensity models. J. Wind. Eng. Ind. Aerodyn. 218 (2021) 
98. Vickery, P.J., Wadhera, D.: Statistical models of Holland pressure proﬁle parameter and 
radius to maximum winds of hurricanes from ﬂight-level pressure and h*wind data. J. Appl. 
Meteorol. Climatol. 47(10), 2497–2517 (2008) 
99. Li, Q., et al.: Typhoon-induced fragility analysis of transmission tower in ningbo area considering the effect of long-term corrosion. Appl. Sci. 12(9) (2022) 
100. Li, Q., et al.: Typhoon loss assessment in rural housing in Ningbo based on township-level resolution. Appl. Sci. 12(7) (2022) 
101. Busca, G., et al.: Vibration monitoring of multiple bridge points by means of a unique vision-based measuring system. Exp. Mech. 54(2), 255–271 (2013) 
102. Liu, X., et al.: Videogrammetric technique for three-dimensional structural progressive collapse measurement. Measurement 63, 87–99 (2015) 
103. Huang, M., et al.: A deep learning augmented vision-based method for measuring dynamic displacements of structures in harsh environments. J. Wind. Eng. Ind. Aerodyn. 217 (2021) 
104. Redmon, J., et al.: You only look once: uniﬁed, real-time object detection. In: 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR) (2016) 
105. Huang, M., Zhang, B., Lou, W.: A computer vision-based vibration measurement method for wind tunnel tests of high-rise buildings. J. Wind Eng. Ind. Aerodyn. 182, 222–234 (2018) 
106. Li, Q., et al.: M-DA VIM-based vibration monitoring and factor analysis for tower crane structures under complex construction environments. Structures 82 (2025)