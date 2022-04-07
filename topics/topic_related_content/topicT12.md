[techxplore.com](https://techxplore.com/news/2022-03-deep-learning-ai-covid-smartwatch-sensors.html)

# Deep-learning diagnoses: AI detects COVID-19 from smartwatch sensors

Molly Sharlach, Princeton University

---

Combining questions about a person's health with data from smartwatch sensors, a new app developed using research at Princeton University can predict within minutes whether someone is infected with COVID-19.

This new breed of diagnostic tool stems from research led by Niraj Jha, a professor of electrical and computer engineering at Princeton University. His team is developing artificial intelligence (AI) technology for COVID-19 detection, as well as diagnosis and monitoring of chronic conditions including depression, bipolar disorder, schizophrenia, diabetes and sickle cell disease.

NeuTigers, a company founded to commercialize Jha's work, applied to the U.S. FDA, under the agency's provision for "software as a medical device," for clearance for its COVIDDeep product. Shayan Hassantabar, a Ph.D. student in Jha's group, is the lead author of a paper in IEEE Transactions on Consumer Electronics describing the development and testing of COVIDDeep. The software integrates smartwatch sensor readings of heart rate, skin temperature and galvanic skin response with blood pressure and oxygen saturation levels, as well as a questionnaire on COVID symptoms.

Jha's research group at Princeton has long focused on adapting a type of AI called deep learning, which is typically energy-intensive, to function on low-power electronic devices such as phones and watches instead of centralized cloud computing centers. This approach, known as edge AI, has the added benefit of helping to preserve users' privacy and increase security. A key innovation is pared-down neural networks (the "neu" of NeuTigers) that mimic human brain development.

"It's a very generalizable framework," said Jha. "Smart health care is just one application. We are also applying it to cybersecurity and other internet-of-things applications." Similar to preventive medical interventions, machine learning models could spot aberrant patterns and help fix software vulnerabilities before a cyberattack ever occurs, he said.

In recent years, Jha's team has explored edge AI for health care applications such as noninvasive detection of diabetes and mental health disorders from smartwatch and smartphone sensor data.

In fall 2017, former pharmaceutical executive Adel Laoui audited Jha's class on "Machine Learning for Predictive Data Analytics" and was intrigued by the technology. Laoui, who had experience developing and deploying new technologies for disease management, approached Jha after the course ended. After further discussions with Jha's Ph.D. students, they launched NeuTigers in June 2018.

"We saw a lot of intersections in our interests," said Jha. "Smart health care with the help of edge AI was taking off, so it was an opportune moment for a startup in this area. Adel had a lot of connections with angel investors, and so it ramped up very quickly."

Several patented technologies from Jha's lab have been licensed to NeuTigers, including methods for diagnosis of diabetes and mental health conditions, and for security vulnerability detection in internet-of-things systems.

When the COVID-19 pandemic was declared in March 2020, Jha wondered whether his team's deep learning approaches could be used to diagnose the virus—especially in people with the potential to spread COVID-19 with no apparent symptoms, a major problem for controlling the disease.

"The hypothesis was that the disease leaves a unique signature on the physiological signals emanating from our body," said Jha. "This hypothesis seems to have been true, at least for the few diseases we had looked at, so my idea was to see if we could diagnose COVID-19 this way."

Jha and Laoui got in touch with Ignazio Marino, a professor of surgery at Thomas Jefferson University in Philadelphia and the executive director of the Jefferson Italy Center.

In May 2020, at the tail end of northern Italy's initial cluster of COVID-19 in Europe, NeuTigers CTO Vishu Ghanakota traveled to Pavia, Italy, to deliver medical-grade smartwatches, software applications and training materials to Marino's colleagues at San Matteo Hospital. The clinical researchers collected data from 87 individuals, 30 of whom had tested negative for COVID by PCR; another 30 tested positive and were symptomatic, and 27 tested positive and were asymptomatic.

The data included 60 minutes of smartwatch sensor readings on heart rate, skin temperature and galvanic skin response (a measure of sweat gland activity), divided into 15-second intervals. Separately, the clinicians measured participants' blood pressure and oxygen saturation levels, and answered a questionnaire indicating whether each participant had shortness of breath, cough, fever or any of eight other symptoms.

The Princeton researchers, led by Ph.D. student Hassantabar, used a subset of this data to train neural network models to predict a patient's COVID-19 status, and another subset to test the resulting models. The team found that their models were 98.1% accurate at detecting COVID-19.

One method Hassantabar used to boost the models' accuracy was the addition of synthetic data obtained based on the probability distribution of the real data—a broadly applicable technique that Jha's group first used for other applications. Another method he used was based on the grow-and-prune neural network synthesis paradigm developed in Jha's group.

The researchers have since validated the method with a larger field trial in France, and health organizations in the United States and Algeria have piloted COVIDDeep among their staff. To enable more widespread adoption of COVIDDeep, NeuTigers is working to make it compatible with some types of Samsung, Fitbit and Apple smartwatches, which will also integrate blood pressure and pulse oximeter measurements.

Manually entering clinical data into a smartphone app could be another useful screening approach in many settings, especially since smartphones are far more common worldwide than smartwatches, said Marino, who oversaw clinical data collection for the study. On the other hand, said Laoui, using a smartwatch alone may be preferable for many users, and the researchers are also working to adapt the neural network models to function with a smartwatch's more limited computing power.

"I think this could be far superior [to rapid antigen tests], because the accuracy of a rapid test that you do by yourself at home is limited," said Marino. "Pushing the swab up in the nose is obviously a discomfort, and I don't know if people are going to do that as accurately as they need to. But if you have a device on your wrist that is not invasive and is totally independent from a physical human maneuver, I think that is much better."

Marino also expressed hope that the technology could improve early diagnosis of widespread conditions such as diabetes. "There are millions of people in the United States that have early diabetes that probably is very treatable, and they don't know," he said. Having new information that leads to early diagnosis could lead to "a very successful treatment," he added.

Laoui is interested in exploring the methods' use for diagnosis and monitoring of other diseases such as cardiovascular disorders and sepsis infections, both increasing problems for the world's aging population.

"We're going to have a library of disease models embedded in the watch, and from time to time we're going to run the sensors' information through these disease models, which will be personalized," said Laoui. "If there is something wrong or something unusual, we are going to inform you in a meaningful way. I believe this new era of smart health care will be powered by edge AI applications and will redefine healthcare delivery and consumer well-being." 
