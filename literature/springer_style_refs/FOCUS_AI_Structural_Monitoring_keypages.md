## p6
Acknowledgements The work described in this study was supported by the 
National Natural Science Foundation of China (52508586); Zhejiang Provincial 
Natural Science Foundation of China (LY24E080012); Ningbo Y outh Science and Technology Innovation Leading Talent Program (2025QL050); Ningbo Key 
R&D Program (2023Z221, 2024Z287, 2025Z037); Ningbo Public Welfare Research Program (2023S004, 2024S005, 2025S023); Ningbo International Sci-tech Cooper-ation Project (2024H019). 
Competing Interests The authors have no competing interests to declare that are 
relevant to the content of this manuscript.
vii

## p7
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

## p8
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

## p9
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

## p10
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

## p11
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

## p24
Chapter 2 
Hybrid Data-Model-Driven Theory 
Abstract The fundamental principles of three representative machine learning 
models-Convolutional Neural Networks (CNN), Bidirectional Long Short-Term 
Memory networks (BiLSTM), and the ensemble learning algorithm AdaBoost-are 
systematically analyzed. Based on the respective advantages and limitations of indi-
vidual models, a CNN-BiLSTM-AdaBoost hybrid prediction model is developed. 
Furthermore, an overall framework and implementation pathway for hybrid data-
model-driven monitoring of major hazardous engineering structures are proposed, 
providing methodological and theoretical support for subsequent prediction of 
tower crane dynamic responses under typhoon loading, dynamic determination and 
updating of monitoring and warning thresholds for high formwork support structures, 
and short-term structural response prediction. In this framework, multi-source moni-
toring data are acquired in real time by various sensing devices and synchronously 
transmitted to an early warning platform for integration, visualization, and analysis, 
while simultaneously driving the dynamic updating of ﬁnite element models. Based 
on measured data and simulation results from the updated models, safety evalua-
tion and response prediction are conducted, and the assessment results and warning 
information are fed back to the construction site, thereby realizing a closed-loop inter-
action among the physical structure, the ﬁnite element model, and the monitoring 
and early warning platform. 
Keywords Hybrid data-model-driven theory ·CNN ·BiLSTM ·AdaBoost 
To address the deﬁciencies of existing monitoring systems for tower cranes and 
high formwork support structures in terms of safety monitoring and response, early warning prediction, and to ensure construction safety and reduce accident occur-
rence, this chapter proposes a hybrid data-model-driven approach for structural moni-toring and early warning. This approach integrates the complementary advantages of physical modeling and artiﬁcial intelligence algorithms. It not only overcomes the
© The Author(s) 2026 
Q. Li et al., A Hybrid Data-Model and AI-Driven Approach for Structural Monitoring in 
Hazardous Construction, https://doi.org/10.1007/978-981-95-8688-2_2 17

## p25
18 2 Hybrid Data-Model-Driven Theory
limitations of traditional physical models, which struggle to adapt to changing real-
world operating conditions, but also mitigates the shortcomings of conventional data-
driven methods, such as insufﬁcient extreme-event samples and weak generalization capability under extreme conditions. 
This chapter discusses both the construction of traditional data-driven models 
and the principles of hybrid data-model-driven approaches. First, commonly used ML models in the ﬁeld of safety monitoring and early warning for major hazardous 
engineering structures-namely Convolutional Neural Networks (CNN) and Bidirec-tional Long Short-Term Memory networks (BiLSTM)-are reviewed, and their respec-tive advantages and limitations are analyzed. On this basis, the Adaptive Boosting 
ensemble learning algorithm (AdaBoost) is further introduced to improve the CNN-BiLSTM model, resulting in the development of a CNN-BiLSTM-AdaBoost hybrid model framework. This framework is designed to enhance prediction accuracy 
under extreme operating conditions and to provide theoretical support for subse-quent studies on response monitoring and early warning for tower cranes and high-formwork structures. Subsequently, the overall framework and implementa-
tion pathway of the hybrid data-model-driven approach are established, dynamically linking the physical structure, FEM, and monitoring and early warning platform. This 
integration enables structural monitoring and predictive early warning and provides a systematic research approach for subsequent studies on safety monitoring and early warning of major hazardous engineering structures. 
2.1 Fundamentals of Machine Learning Models 
Data-driven approaches mainly rely on measured data obtained from practice 
(including data from sensors, monitoring systems, and historical records) to extract 
useful information through data analysis. In such approaches, data serve as the core, and ML techniques are used to learn the mapping relationships between inputs and 
outputs from historical samples. In the ﬁeld of structural safety monitoring, these methods are commonly applied to state identiﬁcation, structural monitoring and detection, and short-term prediction. 
2.1.1 Convolutional Neural Networks (CNNs) 
A convolutional neural network (CNN) is a type of feedforward neural network that employs local connectivity and shared weights to perform high-dimensional mapping of raw data, thereby effectively extracting data features. Its basic architecture consists 
of an input layer, convolutional layers, pooling layers, fully connected layers, and an output layer, as illustrated in Fig. 
2.1.
The convolutional layer is the core component of a CNN and also the layer with 
relatively high computational cost during model training. It captures local features

## p36
Chapter 3 
Hybrid Data-Model-Driven Prediction 
of T ower Crane Dynamic Responses 
Under Typhoon Loading 
Abstract A hybrid data-model-driven method is proposed for predicting tower crane 
displacement responses under extreme typhoon conditions. Using a tower crane 
from an actual engineering project as a case study, an IoT-based real-time moni-
toring system is established to obtain displacement response data throughout the 
construction period. In parallel, a ﬁnite element model is developed to simulate 
the structural displacement of the tower crane under extreme wind loads, compen-
sating for the scarcity of extreme-condition samples in the monitoring data. Based 
on the CNN-BiLSTM-AdaBoost algorithm, both purely data-driven and hybrid data-
model-driven displacement predictions are conducted for normal wind conditions and 
extreme typhoon conditions. The results indicate that purely data-driven methods 
exhibit limited predictive capability under extreme conditions and tend to under-
estimate structural responses. In contrast, the hybrid data-model-driven approach 
effectively integrates measured data with ﬁnite element simulation results, signif-
icantly improving the accuracy and reliability of displacement predictions under 
extreme typhoon loading. 
Keywords Tower crane ·Response prediction ·CNN-BiLSTM-AdaBoost ·
Extreme typhoon 
With global climate change, the frequency of “gray swan” typhoon events (i.e., low-
probability but high-impact events) in the southeastern coastal regions of China has continued to increase, posing a serious risk of collapse to tower cranes at coastal 
construction sites. Real-time monitoring and response prediction of tower cranes can enable timely identiﬁcation of structural displacement trends, provide sufﬁcient time for on-site emergency response, and reduce accident risks. However, tradi-
tional data-driven methods, which mainly rely on historical measured data, exhibit 
inherent limitations when confronted with extreme operating conditions. In prac-
tice, historical datasets often lack samples corresponding to extreme conditions. As 
a result, prediction models may underestimate structural responses due to insufﬁ-
cient learning of extreme scenarios, making it difﬁcult to provide accurate response 
predictions. For example, in “gray swan” typhoon events that may occur only once
© The Author(s) 2026 
Q. Li et al., A Hybrid Data-Model and AI-Driven Approach for Structural Monitoring in Hazardous Construction, 
https://doi.org/10.1007/978-981-95-8688-2_3 29

## p37
30 3 Hybrid Data-Model-Driven Prediction of Tower Crane Dynamic …
IoT monitoring 
system Extreme typhoon 
simulation Wind speed 
Wind load 
FEM dynamic 
response analysis 
Wind speed Displacement Input 
Current time CNN-BiLSTM-
AdaBoost Output 
Subsequent time 
Displacement Dynamic response analysis of FEM under typhoon 
Data-model hybrid driven 
prediction under typhoon 
Tower top displacement prediction Data-driven prediction 
under constant wind Data feedback 
to correct the 
model 
Fig. 3.1 Data model hybrid driven framework for tower top displacement response prediction 
in a century or even once in a millennium, prediction approaches based solely on 
typical benign wind conditions struggle to accurately estimate structural responses 
and tend to produce underestimations. Therefore, it is necessary to improve conven-
tional data-driven methods to enhance the accuracy of structural response prediction 
under such extreme conditions. 
To address these challenges, this chapter proposes a hybrid data-model-driven 
framework for predicting tower-top displacement responses of tower cranes under 
extreme typhoon loading, as illustrated in Fig. 3.1. The framework consists of 
three core modules. The ﬁrst module is an IoT-based monitoring system, which 
monitors on-site wind speed and tower crane displacement. The collected data are 
used to optimize and calibrate the parameters of the FEM in the second module and can also be applied to displacement prediction under benign wind conditions. 
The second module is a ﬁnite element dynamic response analysis module under typhoon loading, in which full-path typhoon simulation and wind ﬁeld simula-tion methods are employed to compute the mean wind speed and ﬂuctuating wind 
speed at the site. Subsequently, a FEM of the tower crane is established and cali-
brated using measured data. By applying wind load time histories to the calibrated 
model and performing multiple dynamic response analyses, a large typhoon wind 
speed-displacement dataset is generated. These datasets serve as a supplement to 
measured data and provide sufﬁcient extreme-condition training samples for the third 
module. The third module focuses on tower-top displacement prediction, where the 
typhoon wind speed-displacement dataset is used for model training. The model 
takes the current wind speed and displacement as input variables and applies the 
CNN-BiLSTM-AdaBoost algorithm to predict the displacement at the next time 
step.

## p62
Chapter 4 
Real-Time Displacement Monitoring 
of High Formwork Support Structures 
Based on Computer Vision 
Abstract The inﬂuence of various external factors on the proposed M-DA VIM 
visual measurement method is systematically investigated through laboratory tests 
and ﬁeld monitoring. After identifying common environmental and operational 
inﬂuencing factors, a series of periodic vibration experiments is conducted under 
controlled conditions to analyze the effects of illumination intensity, fog concentra-
tion, camera elevation angle, target size, and camera vibration. A laser displacement 
sensor is employed as a reference to quantitatively evaluate measurement errors 
induced by these factors. Furthermore, the visual monitoring system is deployed at a 
high formwork construction site in Ningbo, enabling real-time tracking and displace-
ment monitoring of critical structural nodes. The results demonstrate that under 
optimal lighting conditions (200–400 lx) and with target marker sizes exceeding 18 
pixels, the M-DA VIM method achieves sub-millimeter measurement accuracy and 
maintains high precision and strong robustness under adverse conditions such as fog 
and vibration. Field monitoring results from May 27, 2023, show that all monitored 
indicators remain below the code-speciﬁed alarm thresholds, indicating structural 
safety. Nevertheless, due to continuous changes in structural conditions caused by 
factors such as component aging and load variation, there remains a need for scientiﬁc 
and adaptive methods to determine and dynamically update monitoring and warning 
thresholds. 
Keywords High-formwork support system ·Computer vision ·M-DA VIM ·
External inﬂuencing factors 
With the rapid development of the construction industry in China, building struc-
tures are becoming increasingly complex, taller, and characterized by larger spans. 
High formwork support structures are therefore widely used in engineering practice. 
Owing to their large height and small cross-sectional dimensions, the vertical posts 
of high formwork systems have large slenderness ratios. During concrete pouring or 
for a period after pouring, the applied loads may increase suddenly, which can easily 
lead to settlement and lateral deformation. As a result, the structure may lose overall 
stability and pose a threat to the safety of the entire construction project. To prevent
© The Author(s) 2026 
Q. Li et al., A Hybrid Data-Model and AI-Driven Approach for Structural Monitoring in 
Hazardous Construction, https://doi.org/10.1007/978-981-95-8688-2_4 55

## p63
56 4 Real-Time Displacement Monitoring of High Formwork Support …
accidents, it is necessary to monitor the settlement and deformation of the support 
system. Traditional displacement monitoring methods generally use instruments such 
as levels, theodolites, and total stations to measure structural displacement. These measurements require manual operation and can only be performed at one point at 
a time, resulting in disadvantages such as inconvenient operation, low efﬁciency, and the inability to conduct long-term continuous monitoring. In addition, although traditional displacement sensors can be installed near the support system for auto-
matic measurement, their close proximity to the structure makes them susceptible to construction-induced vibrations, which adversely affect measurement accuracy. 
Taking a high formwork support structure from a construction project in Ningbo as 
the case study, this chapter proposes a computer vision-based displacement measure-ment method to improve measurement accuracy and to achieve real-time construc-tion monitoring and safety early warning. First, indoor experiments are conducted 
to investigate the inﬂuence of different external factors-such as illumination, target size, camera pose, and camera vibration-on the measurement accuracy of computer vision-based displacement monitoring. Subsequently, a real-time monitoring system 
for high formwork support structures based on computer vision is established at the construction site. By acquiring video data of the target structure during construction 
and combining it with a self-developed multi-point real-time displacement moni-toring system, the structural displacement is obtained, enabling real-time monitoring and early warning of the structure. 
4.1 Principles of Computer Vision-Based Displacement 
Measurement 
Computer vision has been widely applied in the ﬁeld of civil engineering. Its basic principle is to simulate biological vision using computers and related electronic 
devices, whereby speciﬁc information required by users can be extracted from images or videos through dedicated algorithms. Based on practical engineering requirements, this study adopts a self-developed displacement measurement algorithm to accom-
plish target tracking and displacement monitoring. The theoretical implementation of this method consists of three main steps: camera calibration, target tracking, and 
three-dimensional reconstruction. 
(1) Camera calibration 
The purpose of camera calibration is to establish a one-to-one correspondence 
between image coordinates and real-world coordinates. For planar displacement 
measurement using a monocular camera, planar calibration methods can be employed. Common approaches include Zhang’s calibration method and the scale 
factor method. In this chapter, the scale factor method is adopted, as it is a simpler and more efﬁcient calibration approach. The principle of this method is to deter-mine the ratio between a known actual length in the spatial coordinate system and 
the corresponding pixel length in the image coordinate system, and then convert

## p91
Chapter 5 
Hybrid Data-Model-Driven Updating 
of Monitoring Alarm Thresholds 
and Short-T erm Response Prediction 
for High Formwork Support Structures 
Abstract A hybrid data-model-driven framework for monitoring threshold deter-
mination and dynamic updating is proposed, enabling short-term structural response 
prediction and construction load inversion (back-calculation). The framework 
consists of three core modules. The ﬁrst module comprises a visual displacement 
monitoring system responsible for data acquisition, real-time warning, and contin-
uous information transmission to the second module. The second module deter-
mines and updates monitoring thresholds using hybrid data-model-driven methods 
and provides extensive training samples for the third module. The third module 
employs the CNN-BiLSTM-AdaBoost algorithm to perform short-term prediction 
of structural displacement responses and inversion of construction loads, allowing 
displacement trends to be predicted up to one hour in advance and enabling early 
warning. The results demonstrate that the proposed monitoring threshold determina-
tion and updating method can be continuously reﬁned in engineering practice. The 
buckling failure displacement predicted by the updated model exceeds the initial 
alarm threshold, indicating that the initial threshold is conservative and appropriately 
deﬁned. Moreover, the CNN-BiLSTM-AdaBoost-based approach exhibits strong 
robustness and high prediction accuracy, enabling real-time response prediction and 
load inversion, and shows considerable potential for practical engineering monitoring 
applications. 
Keywords High-formwork support system ·Monitoring threshold update ·
Response prediction ·CNN-BiLSTM-AdaBoost 
For high formwork support structures, existing applications and studies lack scien-
tiﬁc methods for determining and updating monitoring alarm thresholds. Moreover, 
current response alarm systems are triggered only when displacement exceeds preset 
limits and are unable to accurately predict response trends. To address these shortcom-
ings, this study proposes a hybrid data-model-driven approach for determining and 
updating monitoring thresholds. Taking the actual high formwork project introduced 
in Chap. 4 as a case study, a closed-loop framework is established to achieve real-time
© The Author(s) 2026 
Q. Li et al., A Hybrid Data-Model and AI-Driven Approach for Structural Monitoring in 
Hazardous Construction, https://doi.org/10.1007/978-981-95-8688-2_5 85

## p92
86 5 Hybrid Data-Model-Driven Updating of Monitoring Alarm Thresholds …
perception of structural displacement and feedback-based updating, enabling contin-
uous iterative updating of alarm thresholds. In addition, hybrid deep learning models 
and ensemble learning algorithms are employed to perform short-term prediction of structural displacement and rapid inversion of construction loads, thereby providing 
early warning for structural safety. 
The analytical framework for updating monitoring alarm thresholds and short-
term response prediction of high formwork support structures is shown in Figure 5.1, 
which mainly consists of three modules. The ﬁrst module is the computer vision-based multi-point displacement monitoring system described in Chap. 
4, which is 
used to perceive structural response data in real time, issue over-limit alarm signals, 
and provide continuous feedback to the second module. The second module adopts a 
hybrid data-model-driven approach to determine and update monitoring thresholds. The virtual-physical interaction process is as follows: ﬁrst, a FEM is established by 
integrating the special design documentation for the high formwork system with the boundary conditions of the construction site; then, construction-stage design loads are applied to analyze the stress and deformation of the high formwork structure, 
and structural buckling failure analysis is performed to determine the initial alarm thresholds, which are used to guide on-site monitoring. As construction progresses, 
the structural state may change; therefore, accumulated measured data are used to periodically update the FEM. The updated model can more accurately reﬂect the actual stress state and deformation of the high formwork structure, allowing 
structural buckling failure analysis to be re-performed and alarm thresholds to be updated to continue guiding on-site monitoring. In addition, under extreme condi-tions where on-site monitoring may be infeasible due to safety or other constraints, 
data provided by the FEM can serve as a supplement to measured data, supplying sufﬁcient training samples for the subsequent prediction module. The third module primarily employs the CNN-BiLSTM-AdaBoost algorithm for structural response 
prediction. This algorithm enables advanced prediction of displacement trends of the high formwork structure and issues early warning signals, facilitating timely and effective emergency measures.
5.1 Determination and Updating of Monitoring Alarm 
Thresholds 
5.1.1 Initial Alarm Threshold Determination 
(1) Model establishment In this project, the high formwork support system adopts a cuplock-type steel 
pipe support frame. Adjustable screw jacks are used for both beam-bottom and slab-bottom vertical posts to enhance vertical load-bearing capacity. The 
material properties and cross-sectional information of the members are listed in Table 
5.1.

## p117
Chapter 6 
Conclusions and Future Perspectives 
6.1 Key Innovations and Contributions 
This study adopts a hybrid data-model-driven approach with a focus on structural 
safety monitoring and early warning for hazard-prone construction projects. For 
tower cranes, research was conducted on Internet of Things (IoT)-based monitoring, 
structural dynamic response analysis, and response prediction for early warning. For 
high-formwork support systems, studies were carried out on computer vision-based 
monitoring, dynamic updating of monitoring and warning thresholds, and short-term 
response prediction. The main innovations are summarized as follows: 
(1) Tower crane structures 
A hybrid data-model-driven dynamic response prediction framework for tower 
cranes under extreme typhoon conditions is proposed. This framework effectively 
addresses the shortage of extreme-event samples in measured data and signiﬁcantly 
improves the accuracy and reliability of predicting “gray swan” typhoon events. 
Furthermore, a wind-induced dynamic response prediction method for tower 
cranes based on a CNN-BiLSTM-AdaBoost ML model is developed, enabling 
accurate capture of response trends and providing early warning capability. 
(2) High-formwork support structures 
A hybrid data-model-driven framework for determining and dynamically updating 
monitoring and warning thresholds of high-formwork support structures is proposed, 
allowing continuous iteration of alarm thresholds and improving early warning 
accuracy. 
A visual displacement monitoring system for high-formwork structures is estab-
lished, enabling real-time perception of structural responses and timely data feedback, which lays a solid foundation for warning threshold updating. 
In addition, a CNN-BiLSTM-AdaBoost-based method for short-term displace-
ment prediction and rapid inversion of upper construction loads is proposed, providing effective early warning for high-formwork support structures。
© The Author(s) 2026 
Q. Li et al., A Hybrid Data-Model and AI-Driven Approach for Structural Monitoring in 
Hazardous Construction, https://doi.org/10.1007/978-981-95-8688-2_6 111

## p118
112 6 Conclusions and Future Perspectives
6.2 Main Conclusions 
This study proposes a hybrid data-model-driven method to predict tower crane 
displacement responses under extreme typhoon conditions and to realize the updating of monitoring and warning thresholds as well as short-term response prediction for 
high-formwork support structures. In the tower crane study, an actual construction project tower crane was taken as an example, and an IoT-based real-time displace-ment monitoring system was developed to obtain load-response data of the tower 
crane during construction. Meanwhile, a FEM was established to simulate tower crane displacements under various extreme wind loads, compensating for the lack of extreme-event samples in the monitoring data. Then, based on the CNN-BiLSTM-
AdaBoost algorithm, both data-driven and hybrid data-model-driven methods were adopted to predict the top displacement of the tower crane under normal wind and 
typhoon conditions. In the high-formwork structure study, the inﬂuences of different external factors on the visual system were ﬁrst investigated. Then, taking an actual high-formwork structure as an example, a visual monitoring system and a FEM were 
established, forming a closed-loop framework for real-time perception and feedback updating of structural responses, which enables the determination and continuous iterative updating of alarm thresholds. Finally, the CNN-BiLSTM-AdaBoost algo-
rithm was used to conduct short-term structural displacement prediction and rapid inversion of construction loads, providing early warning for high-formwork support structures. Based on the research results, the main conclusions are as follows: 
Based on the research results, the main conclusions are as follows: 
(1) Purely data-driven methods show obvious limitations in predicting tower crane 
displacements under extreme typhoon conditions and tend to underestimate the 
structural responses of tower cranes. 
(2) The hybrid data-model-driven method integrates real-time monitoring data 
with extreme typhoon simulation results, signiﬁcantly improving the accuracy 
and robustness of tower crane displacement prediction under extreme typhoon conditions. 
Computer vision-based real-time displacement monitoring of high-formwork 
support structures: 
(1) Illumination intensity: M-DA VIM achieves optimal accuracy within the range of 200–400 lx. Under low illumination or extreme lighting conditions, errors increase signiﬁcantly but remain within acceptable engineering tolerances. 
Fog concentration: A GAN-based integrated image restoration module can effectively compensate for image blurring caused by fog and maintains sub-
millimeter accuracy even under dense fog conditions. Camera elevation angle: The visual system maintains high accuracy when the elevation angle is within 30°. Target size: When the target size is smaller than 18 pixels, measurement 
errors increase; therefore, when the M-DA VIM system is used outdoors, the marker size should be greater than 18 pixels. Camera vibration: M-DA VIM can