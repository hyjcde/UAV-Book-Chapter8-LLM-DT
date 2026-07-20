## PDF page 1/187
PALGRAVE STUDIES IN DIGITAL BUSINESS 
& ENABLING TECHNOLOGIES
SERIES EDITORS : THEO LYNN · PIERANGELO ROSATI
Disrupting 
Buildings
Digitalisation and the 
Transformation of Deep Renovation
Edited by
Theo Lynn · Pierangelo Rosati
Mohamad Kassem · Stelios Krinidis
Jennifer Kennedy

## PDF page 2/187
Palgrave Studies in Digital Business & Enabling 
Technologies
Series Editors
Theo Lynn  
Irish Institute of Digital Business
DCU Business School
Dublin, Ireland
Pierangelo Rosati  
J.E. Cairnes School of Business and Economics
University of Galway
Galway, Ireland

## PDF page 3/187
This multi-disciplinary series will provide a comprehensive and coherent 
account of cloud computing, social media, mobile, big data, and other 
enabling technologies that are transforming how society operates and how 
people interact with each other. Each publication in the series will focus on 
a discrete but critical topic within business and computer science, covering 
existing research alongside cutting edge ideas. Volumes will be written by 
field experts on topics such as cloud migration, measuring the business 
value of the cloud, trust and data protection, fintech, and the Internet of 
Things. Each book has global reach and is relevant to faculty, researchers 
and students in digital business and computer science with an interest in 
the decisions and enabling technologies shaping society. More information 
about this series at http://www.palgrave.com/gp/series/16004 .

## PDF page 4/187
Theo Lynn  
Pierangelo Rosati  
Mohamad Kassem  
Stelios Krinidis  • Jennifer Kennedy
Editors
Disrupting Buildings
Digitalisation and the Transformation of Deep 
Renovation

## PDF page 5/187
ISSN 2662-1282      ISSN 2662-1290  (electronic)
Palgrave Studies in Digital Business & Enabling Technologies
ISBN 978-3-031-32308-9     ISBN 978-3-031-32309-6  (eBook)
https://doi.org/10.1007/978-3-031-32309-6
© The Editor(s) (if applicable) and The Author(s) 2023. This book is an open access 
publication.
Open Access   This book is licensed under the terms of the Creative Commons Attribution 
4.0 International License ( http://creativecommons.org/licenses/by/4.0/ ), which permits 
use, sharing, adaptation, distribution and reproduction in any medium or format, as long as 
you give appropriate credit to the original author(s) and the source, provide a link to the 
Creative Commons licence and indicate if changes were made.
The images or other third party material in this book are included in the book’s Creative 
Commons licence, unless indicated otherwise in a credit line to the material. If material is not 
included in the book’s Creative Commons licence and your intended use is not permitted by 
statutory regulation or exceeds the permitted use, you will need to obtain permission directly 
from the copyright holder.
The use of general descriptive names, registered names, trademarks, service marks, etc. in this 
publication does not imply, even in the absence of a specific statement, that such names are 
exempt from the relevant protective laws and regulations and therefore free for general use.
The publisher, the authors, and the editors are safe to assume that the advice and information 
in this book are believed to be true and accurate at the date of publication. Neither the 
 publisher nor the authors or the editors give a warranty, expressed or implied, with respect to 
the material contained herein or for any errors or omissions that may have been made. The 
publisher remains neutral with regard to jurisdictional claims in published maps and 
 institutional affiliations.
This Palgrave Macmillan imprint is published by the registered company Springer Nature 
Switzerland AG.
The registered company address is: Gewerbestrasse 11, 6330 Cham, SwitzerlandEditors
Theo Lynn
Irish Institute of Digital Business 
DCU Business School
Dublin City University
Dublin, Ireland
Mohamad Kassem
School of Engineering
Newcastle University
Newcastle upon Tyne, UK
Jennifer Kennedy
Irish Institute of Digital Business 
DCU Business School
Dublin City University
Dublin, IrelandPierangelo Rosati
J.E. Cairnes School of Business and 
Economics
University of Galway
Galway, Irelan

## PDF page 6/187
vThis book was partially funded by the European Union’s Horizon 2020 
Research and Innovation Programme through the RINNO project 
(https://rinno-  h2020.eu/ ) under Grant Agreement 892071, and the 
Irish Institute of Digital Business.Acknowledgements

## PDF page 7/187
The world’s extant building stock accounts for a significant portion of 
worldwide energy consumption and greenhouse gas emissions. In 2020, 
buildings and construction accounted for 36% of global final energy con -
sumption and 37% of energy-related CO 2 emissions. The European Union 
(EU) estimates that up to 75% of the EU’s existing building stock has 
poor energy performance, 85–95% of which will still be in use in 2050.
To meet the goals of the Paris Agreement on Climate Change will require 
a transformation of construction processes and deep renovation of the 
extant building stock. The World Economic Forum, World Business Council 
for Sustainable Development, and the European Commission are amongst 
the many global organisations that recognise the important role ICTs can 
play in construction, renovation, and maintenance, as well as supporting the 
incentivisation and financing of deep renovation. Technologies such as sen -
sors, big data analytics and machine learning, building information model -
ling (BIM), digital twinning, simulation, robots, cobots and unmanned 
autonomous vehicles (UAVs), additive manufacturing, smart contracts, and 
the Internet of Things are transforming the deep renovation process, 
improving sustainability performance, and developing new services and 
markets.
This book defines a deep renovation digital ecosystem for the twenty-
first century, providing a state-of-the art review of current literature, sug -
gesting avenues for new research, and offering perspectives from business, 
technology, and industry.Book description

## PDF page 8/187
ix 1   Deep Renovation: Definitions, Drivers and Barriers    1
Theo Lynn, Pierangelo Rosati, and Antonia Egli
 2   Embedded Sensors, Ubiquitous Connectivity and Tracking   23
Marco Arnesano and Silvia Angela Mansi
 3   Building Information Modelling   39
Omar Doukari, Mohamad Kassem, and David Greenwood
 4   Building Performance Simulation   53
Asimina Dimara, Stelios Krinidis, Dimosthenis Ioannidis, and 
Dimitrios Tzovaras
 5   Big Data and Analytics in the Deep Renovation Life Cycle   69
Paraskevas Koukaras, Stelios Krinidis, Dimosthenis Ioannidis, 
Christos Tjortjis, and Dimitrios Tzovaras
 6   Digital Twins and Their Roles in Building Deep 
Renovation Life Cycle   83
Yuandong Pan, Zhiqi Hu, and Ioannis Brilakiscontents

## PDF page 9/187
x CONTENTS
 7   Additive Manufacturing and the Construction Industry   97
Mehdi Chougan, Mazen J. Al-Kheetan, and  
Seyed Hamidreza Ghaffar
 8   Intelligent Construction Equipment and Robotics  111
Alessandro Pracucci, Laura Vandi, and SeyedReza RazaviAlavi
 9   Cybersecurity Considerations for Deep Renovation  135
Muammer Semih Sonkor and Borja García de Soto
 10   Financing Building Renovation: Financial Technology as 
an Alternative Channel to Mobilise Private Financing  153
Mark Cummins, Theo Lynn, and Pierangelo Rosati
  Index  173

## PDF page 10/187
xiMazen  J. Al-Kheetan  is an Assistant Professor in the Department of Civil 
and Environmental Engineering at Mutah University, Jordan. He is also 
an associate editor at the Proceedings of the Institution of Civil Engineers—
Transport, UK. He previously served as the head of the Department of 
Civil and Environmental Engineering at Mutah University, Jordan.
Marco  Arnesano  is Associate Professor of Mechanical and Thermal 
Measurements and coordinator of Industrial Engineering at eCampus 
University, Italy. He is also the co-founder of LIS (Live Information 
System), a startup company developing BIM-based solutions for build -
ings’ digitalisation.
Ioannis  Brilakis  is Laing O’Rourke Professor of Construction 
Engineering and the director of the Construction Information Technology 
Laboratory in the Department of Engineering at the Division of Civil 
Engineering, University of Cambridge, UK.
Mehdi Chougan  is a Marie Sk łodowska-Curie Research Fellow in the 
Department of Civil and Environmental Engineering at Brunel University 
London, UK. His research focuses on cementitious composite materials, 
especially in graphene-  engineered cementitious composites, and additive 
manufacturing of alkali-  activated cementitious composites.
Mark Cummins  is Professor of Financial Technology at the University of 
Strathclyde, UK.  His research interests include financial technology notes on contri Butors

## PDF page 21/187
3
discuss how these barriers may surface across the life cycle of a deep reno -
vation project. Advances in technologies, not least information and com -
munications technologies (ICTs), are central to accelerating the renovation 
life cycle and overcoming the existing barriers to deep renovation. We 
conclude with a summary of the remainder of this book which looks at the 
main digital innovations disrupting and transforming the construc -
tion sector.
1.2  d eep renovat Ion
“Deep renovation” has become somewhat of a buzzword in recent years, 
albeit an obscure one. There remains little consensus on the term’s defini -
tion and, although widely adopted in academia, industry and legislation, 
definitions vary significantly on local, regional and international levels 
(Shnapp et al., 2013 ). While deep renovation (sometimes referred to as 
deep energy renovation, deep retrofit or deep refurbishment) may be 
defined simply as renovation efforts which capture the “full economic 
energy efficiency potential of improvement works […] of existing build -
ings” and lead to high energy performance levels (Shnapp et al., 2013 ), 
the core concept of deep renovation is categorised into broad  and narrow  
definitions:
• Broad , referring to the use of different simultaneous building enve -
lope and installation system renovation measures into one integrated 
strategy across the entire building life cycle (Agliardi et al., 2018 );
• Narrow , relating to performance levels of refurbishments that reduce 
building energy consumption by a significant proportion to energy 
levels observed before renovation works began (Sibileau et al., 2021 ).
D’agostino et al. ( 2017 ) take a more quantitative approach, categoris -
ing deep renovation efforts by performance impact as presented in 
Table  1.1. This offers a relative numeric classification of deep renovation 
efforts, although an exact quantitative reference value for deep renovation 
energy reductions remains unavailable (D’Oca et al., 2018 ).
Deep renovation involves the use of multiple energy-saving measures. 
Bruel et al. ( 2013 ) summarise these measures as (1) energy-efficient build -
ing elements such as windows, heating, ventilation and air conditioning 
(HVAC), air filtration, lighting and appliances; (2) renewable energy 
sources like solar hot water, solar photovoltaic (PV) panels, passive solar 
energy, shading, wind, heat pumps, biomass and biogas; and (3) 1 DEEP RENOV ATION: DEFINITIONS, DRIVERS AND BARRIERS  

## PDF page 41/187
23CHAPTER 2
Embedded Sensors, Ubiquitous Connectivity 
and Tracking
Marco Arnesano and Silvia Angela Mansi
Abstract  The digitalisation of the deep renovation process and built envi -
ronment is enabled by ubiquitous connectivity and monitoring of the envi -
ronment itself, the artefacts and actors within it, and events that occur. Such 
monitoring is important for efficient construction management, dynamic 
peak demand reduction, affordability, and occupants’ well-being. Sensor 
networks based on Internet of Things (IoT) technologies represent an 
important prerequisite for both optimising and redefining the stages of the 
building process to meet environmental challenges. This chapter provides 
an overview of how computation capabilities are being integrated into the 
physical environment and the role of sensor networks in the context of deep 
renovation. The key advantages and benefits of these technologies at the 
pre, during and post-renovation stages are discussed together with different 
use cases. The value of sensor network infrastructures and the legal and ethi -
cal implications of the use of such sensor infrastructures is also discussed.
Keywords  Sensing networks • IoT • Smart Buildings
M. Arnesano ( *) • S. A. Mansi 
Università Telematica eCampus, Novedrate, Italy
e-mail:  marco.arnesano@uniecampus.it ; silviaangela.mansi@uniecampus.it
© The Author(s) 2023
T. Lynn et al. (eds.), Disrupting Buildings , Palgrave Studies in 
Digital Business & Enabling Technologies, 
https://doi.org/10.1007/978-3-031-32309-6_2