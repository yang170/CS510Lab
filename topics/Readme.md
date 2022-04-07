# SimpleText 2022 topics

## Description

### Topic definition

Each topic is defined as a short article published in:

* the [tech section of The Guardian](https://www.theguardian.com/uk/technology) newspaper (topics G01 to G20)
* [Tech Xplore](https://techxplore.com/) website (topics T01 to T20)

URLs to original articles and textual content of each topic are provided to participants. **All passages retrieved from DBLP by participants are expected to have some overlap (lexical or semantic) with the article content.**

### Queries as facets

Queries are provided with each topics. It has been manually checked that each query allows to retrieve some relevant passages that could be inserted as citations in the press article.

For each query we provide the URL to retrieve a maximum of 1000 documents from the corpus in json format. More complex queries can be formulated ([see the documentation here](../corpus/src/documentation_GUI_API.md?fileId=921300)). The connection to the server requires the following credentials:

* login: inex
* password: qatc2011

### Expected results

#### Ad-hoc passage retrieval

Participants should retrieve for each topic and each query, all passages from DBLP abstracts, about the query and that would be relevant to be inserted as citation in the paper associated with the topic. Some passages could require simplification

#### Open passage retrieval (optional)

Participants are encouraged to extract supplementary relevant queries from titles and/or content articles and to provide results based on these supplementary queries.

#### Format of the results

Results should be provided in a TREC style tabulated format:

1. *run_id:* Run ID starting with *teamid*
2. *manual:* Whether the run is manual {0,1}
3. *topic_id:* Topic ID
4. query_id: Query ID used to retrieve the document (if one of the queries provided for the topic was used; 0 otherwise)
5. *doc_id:* ID of the retrieved document (to be extracted from the json output)
6. *passage:* Text of the selected passage

**For each topic, the maximum number of distinct DBLP references (_id json field) is 100 and the total length of passages should not exceed 1000 tokens.**

Here is an output format example:

```
run_id	manual	topic_id	query_id	doc_id	passage
ST1_1	0	G01	G01.1	1564531496	A CDA is a mobile user device, similar to a Personal Digital Assistant (PDA). It supports the citizen when dealing with public authorities and proves his rights - if desired, even without revealing his identity.
ST1_1	0	G01	G01.1	3000234933	People are becoming increasingly comfortable using Digital Assistants (DAs) to interact with services or connected objects
ST1_1	0	G01	G01.2	1448624402	As extensive experimental research has shown individuals suffer from diverse biases in decision-making.
```

### Evaluation

Passage relevance will be assessed based on:

1. lexical and semantic overlap of extracted passages with topic article content
2. manual assessment of a pool of passages

### Folder content

* folder query related content provides the text content of press articles.
* SP12022tocs.xxx files provide the set of topics introduced here in csv format or json.

---

## Topic G01: Digital assistants like Siri and Alexa entrench gender biases, says UN

<https://www.theguardian.com/technology/2019/may/22/digital-voice-assistants-siri-alexa-gender-biases-unesco-says>

### Query G01.1: Digital assistant

[https://guacamole.univ-avignon.fr/dblp1/_search?q="Digital assistant"&size=1000](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22Digital%20assistant%22&size=1000)

### Query G01.2: Biases

<https://guacamole.univ-avignon.fr/dblp1/_search?q=biases&size=1000>

## Topic G02: Apple contractors 'regularly hear confidential details' on Siri recordings

<https://www.theguardian.com/technology/2019/jul/26/apple-contractors-regularly-hear-confidential-details-on-siri-recordings>

### Query G02.1: Confidential

<https://guacamole.univ-avignon.fr/dblp1/_search?q=confidential&size=1000>

### Query G02.2: Privacy

<https://guacamole.univ-avignon.fr/dblp1/_search?q=privacy&size=1000>

## Topic G03: Alexa, Siri... Elsa? Children drive boom in smart speakers

<https://www.theguardian.com/technology/2020/oct/18/alexa-siri-elsa-children-drive-boom-in-smart-speakers>

### Query G03.1: smart speaker

[https://guacamole.univ-avignon.fr/dblp1/_search?q="smart speaker"&size=1000](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22smart%20speaker%22&size=1000)

### Query G03.2: surveillance

<https://guacamole.univ-avignon.fr/dblp1/_search?q=surveillance&size=1000>

## Topic G04: Drug companies look to AI to end 'hit and miss' research

<https://www.theguardian.com/business/2021/feb/20/drug-companies-look-to-ai-to-end-hit-and-miss-research>

### Query G04.1: drug discovery

[https://guacamole.univ-avignon.fr/dblp1/_search?q="drug discovery"&size=1000](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22drug%20discovery%22&size=1000)

### Query G04.2: functional genomics

[https://guacamole.univ-avignon.fr/dblp1/_search?q="Functional genomics"&size=1000](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22Functional%20genomics%22&size=1000)

### Query G04.3: infectious diseases

[https://guacamole.univ-avignon.fr/dblp1/_search?q="infectious diseases"&size=1000](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22infectious%20diseases%22&size=1000)

## Topic G05: After the Nobel, what next for Crispr gene-editing therapies?

<https://www.theguardian.com/science/2021/feb/21/after-the-nobel-what-next-for-crispr-gene-editing-therapies>

### Query G05.1: gene editing

[https://guacamole.univ-avignon.fr/dblp1/_search?q="gene editing"&size=1000](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22gene%20editing%22&size=1000)

### Query G05.2: crispr

<https://guacamole.univ-avignon.fr/dblp1/_search?q=Crispr&size=1000>

## Topic G06: Elon Musk: regulate AI to combat 'existential threat' before it's too late

<https://www.theguardian.com/technology/2017/jul/17/elon-musk-regulation-ai-combat-existential-threat-tesla-spacex-ceo>

### Query G06.1: ubiquity

<https://guacamole.univ-avignon.fr/dblp1/_search?q=ubiquity&size=1000>

### Query G06.2: self driving

[https://guacamole.univ-avignon.fr/dblp1/_search?q="self driving"&size=1000](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22self%20driving%22&size=1000)

## Topic G07: Misinformation runs rampant as Facebook says it may take a week before it unblocks some pages

<https://www.theguardian.com/technology/2021/feb/19/misinformation-runs-rampant-as-facebook-says-it-may-take-a-week-before-it-unblocks-some-pages>

### Query G07.1: misinformation

<https://guacamole.univ-avignon.fr/dblp1/_search?q=Misinformation&size=1000>

### Query G07.2: conspiracy theories

[https://guacamole.univ-avignon.fr/dblp1/_search?q="conspiracy theories"&size=1000](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22conspiracy%20theories%22&size=1000)

## Topic G08: Bitcoin's market value exceeds $1tn after price soars

<https://www.theguardian.com/technology/2021/feb/19/bitcoins-market-value-exceeds-1tn-after-price-soars-to-above-54000>

### Query G08.1: cryptocurrency

<https://guacamole.univ-avignon.fr/dblp1/_search?q=Cryptocurrency&size=1000>

### Query G08.2: financial markets

[https://guacamole.univ-avignon.fr/dblp1/_search?q="Financial markets"&size=1000](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22Financial%20markets%22&size=1000)

## Topic G09: Forensic Architecture: detail behind the devilry

<https://www.theguardian.com/artanddesign/2018/feb/25/forensic-architects-eyal-weizman>

### Query G09.1: forensics

[https://guacamole.univ-avignon.fr/dblp1/_search?q=forensics)&size=1000](https://guacamole.univ-avignon.fr/dblp1/_search?q=forensics&size=1000)

## Topic G10: Robots on the rise as Americans experience record job losses amid pandemic

<https://www.theguardian.com/technology/2020/nov/27/robots-replacing-jobs-automation-unemployment-us>

### Query G10.1: humanoid robots

[https://guacamole.univ-avignon.fr/dblp1/_search?q="Humanoid robots"&size=1000](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22Humanoid%20robots%22&size=1000)

### Query G10.2: disrupting

<https://guacamole.univ-avignon.fr/dblp1/_search?q=disrupting&size=1000>

## Topic G11: UK wants new drones in wake of Azerbaijan military success

<https://www.theguardian.com/world/2020/dec/29/uk-defence-secretary-hails-azerbaijans-use-of-drones-in-conflict>

### Query G11.1: drones

[https://guacamole.univ-avignon.fr/dblp1/_search?q= "drones"&size=1000](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22drones%22&size=1000)

## Topic G12: Patient data from GP surgeries sold to US companies

<https://www.theguardian.com/politics/2019/dec/07/nhs-medical-data-sales-american-pharma-lack-transparency>

### Query G12.1: patient data

[https://guacamole.univ-avignon.fr/dblp1/_search?q="patient data"&size=1000](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22patient%20data%22&size=1000)

## Topic G13: Baffled by digital marketing? Find your way out of the maze

<https://www.theguardian.com/small-business-network/2016/apr/22/baffled-digital-marketing-seo-content>

### Query G13.1: digital marketing

[https://guacamole.univ-avignon.fr/dblp1/_search?q="digital marketing"&size=1000](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22digital%20marketing%22&size=1000)

### Query G13.2: advertising

<https://guacamole.univ-avignon.fr/dblp1/_search?q=advertising&size=1000>

## Topic G14: End-to-end encryption protects children, says UK information watchdog

<https://www.theguardian.com/technology/2022/jan/21/end-to-end-encryption-protects-children-says-uk-information-watchdog>

### Query G14.1: online safety for children

[https://guacamole.univ-avignon.fr/dblp1/_search?q=online safety for children](https://guacamole.univ-avignon.fr/dblp1/_search?q=online%20safety%20for%20children)

### Query G14.2: end to end encryption

[https://guacamole.univ-avignon.fr/dblp1/_search?q="end to end encryption"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22end%20to%20end%20encryption%22)

## Topic G15: What is GDPR and why does the UK want to reshape its data laws?

<https://www.theguardian.com/technology/2021/aug/26/what-gdpr-why-does-uk-want-reshape-data-laws>

### Query G15.1: Snowden

[ht](https://guacamole.univ-avignon.fr/dblp1/_search?q=online%20safety%20for%20children)[tps://guacamole.univ-avignon.fr/dblp1/_search?q=snowden](https://guacamole.univ-avignon.fr/dblp1/_search?q=snowden)

### Query G15.2: cookies

<https://guacamole.univ-avignon.fr/dblp1/_search?q=cookies>

### Query G15.3: GDPR

[https://guacamole.univ-avignon.fr/dblp1/_search?q= GDPR](https://guacamole.univ-avignon.fr/dblp1/_search?q=GDPR)

### Query G15.4: ePrivacy

<https://guacamole.univ-avignon.fr/dblp1/_search?q=ePrivacy>

## Topic G16: Algorithms are more like puppies than monsters, they want to please you

<https://www.theguardian.com/media-network/2016/jun/06/algorithms-more-puppies-than-monsters-please-you-natural-language-processing>

### Query G16.1: algorithm

<https://guacamole.univ-avignon.fr/dblp1/_search?q=algorithm>

### Query G16.2: NLP applications

https://guacamole.univ-avignon.fr/dblp1/_search?q="NLP applications"

### Query G16.3: accountability

<https://guacamole.univ-avignon.fr/dblp1/_search?q=accountability>

### Query G16.4: OpenNLP

<https://guacamole.univ-avignon.fr/dblp1/_search?q=opennlp>

## Topic G17: The next giant leap: why Boris Johnson wants to ‘go big’ on quantum computing

<https://www.theguardian.com/technology/2021/nov/21/next-giant-leap-boris-johnson-go-big-on-quantum-computing>

### Query G17.1: quantum computing

[https://guacamole.univ-avignon.fr/dblp1/_search?q=quantum computing](https://guacamole.univ-avignon.fr/dblp1/_search?q=quantum%20computing)

### Query G17.2: qbit

<https://guacamole.univ-avignon.fr/dblp1/_search?q=qubit>

### Query G17.3: Jay Gambetta

[https://guacamole.univ-avignon.fr/dblp1/_search?q="Jay Gambetta"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22Jay%20Gambetta%22)

### Query G17.4: quantum applications

[https://guacamole.univ-avignon.fr/dblp1/_search?q=quantum applications](https://guacamole.univ-avignon.fr/dblp1/_search?q=quantum%20applications)

## Topic G18: New crowdsourced recruitment tool aims to get more women into tech

<https://www.theguardian.com/careers/2018/nov/12/new-crowdsourced-recruitment-tool-aims-to-get-more-women-into-tech>

### Query G18.1: Peer recommendations

[https://guacamole.univ-avignon.fr/dblp1/_search?q="peer recommendations"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22peer%20recommendations%22)

### Query G18.2: Crowdsourcing

<https://guacamole.univ-avignon.fr/dblp1/_search?q=crowsourcing>

### Query G18.3: tech job search

[https://guacamole.univ-avignon.fr/dblp1/_search?q=tech job search](https://guacamole.univ-avignon.fr/dblp1/_search?q=tech%20job%20search)

### Query G18.4: +women +computer -games

[https://guacamole.univ-avignon.fr/dblp1/_search?q=+women +computer -games](https://guacamole.univ-avignon.fr/dblp1/_search?q=+women%20+computer%20-games)

## Topic G19: International Space Station attacked by ‘virus epidemics’

<Https://www.theguardian.com/technology/2013/nov/12/international-space-station-virus-epidemics-malware>

### Query G19.1: International Space Station Linux

[https://guacamole.univ-avignon.fr/dblp1/_search?q=international space station Linux](https://guacamole.univ-avignon.fr/dblp1/_search?q=international%20space%20station%20Linux)

### Query G19.2: Kaspersky Linux

<https://guacamole.univ-avignon.fr/dblp1/_search?q=kaspersky> linux

### Query G19.3: malicious password swiping malware

[https://guacamole.univ-avignon.fr/dblp1/_search?q=malicious password swiping malware](https://guacamole.univ-avignon.fr/dblp1/_search?q=malicious%20password%20swiping%20malware)

## Topic G20: Open data is a force for good, but not without risks

<https://www.theguardian.com/society/2012/jul/10/open-data-force-for-good-risks>

### Query G20.1 : "open data" risk

[https://guacamole.univ-avignon.fr/dblp1/_search?q="open data" risk](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22open%20data%22%20risk)

### Query G20.2 : "open data" "impact of policies"

[https://guacamole.univ-avignon.fr/dblp1/_search?q= "open data" "impact of policies"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%20%22open%20data%22%20%22impact%20of%20policies%22)

---

## Topic T01: Curve Light: A highly performing indoor positioning system

<https://techxplore.com/news/2021-12-highly-indoor-positioning.html>

### Query T01.1: indoor positioning system

https://guacamole.univ-avignon.fr/dblp1/_search?q="indoor positioning system"

### Query T01.2: light positioning

https://guacamole.univ-avignon.fr/dblp1/_search?q="light positioning"

### Query T01.3: LED lamp

https://guacamole.univ-avignon.fr/dblp1/_search?q="LED lamp"

## Topic T02: Studying RISC-V architecture to create customized systems for space computing

<https://techxplore.com/news/2021-09-risc-v-architecture-customized-space.html>

### Query T02.1: spacecraft

[https://guacamole.univ-avignon.fr/dblp1/_search?q="spacecraft"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22spacecraft%22)

### Query T02.2: RISC-V

[https://guacamole.univ-avignon.fr/dblp1/_search?q="RISC-V"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22RISC-V%22)

### Query T02.3: architecture modularity

https://guacamole.univ-avignon.fr/dblp1/_search?q="architecture modularity"

## Topic T03: RoboTurk: A crowdsourcing platform for imitation learning in robotics

<https://techxplore.com/news/2018-11-roboturk-crowdsourcing-platform-imitation-robotics.html>

### Query T03.1: imitation learning

https://guacamole.univ-avignon.fr/dblp1/_search?q="imitation learning"

### Query T03.2: crowdsourcing

[https://guacamole.univ-avignon.fr/dblp1/_search?q="crowdsourcing"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22crowdsourcing%22)

### Query T03.3: robot learning

https://guacamole.univ-avignon.fr/dblp1/_search?q="robot learning"

## Topic T04: Artificial intelligence—parking a car with only 12 neurons

<https://techxplore.com/news/2018-10-artificial-intelligenceparking-car-neurons.html>

### Query T04.1: intelligent parking

https://guacamole.univ-avignon.fr/dblp1/_search?q="intelligent parking"

### Query T04.2: RNN

[https://guacamole.univ-avignon.fr/dblp1/_search?q="RNN"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22RNN%22)

### Query T04.3: nematode

[https://guacamole.univ-avignon.fr/dblp1/_search?q="nematode"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22nematode%22)

### Query T04.4: small neural network

https://guacamole.univ-avignon.fr/dblp1/_search?q="small neural network"

## Topic T05: New ‘emotional’ robots aim to read human feelings

<https://techxplore.com/news/2018-01-emotional-robots-aim-human.html>

### Query T05.1: emotional robot

https://guacamole.univ-avignon.fr/dblp1/_search?q="emotional robot"

### Query T05.2: emotion detection

https://guacamole.univ-avignon.fr/dblp1/_search?q="emotion detection"

### Query T05.3: emotion synthesis

https://guacamole.univ-avignon.fr/dblp1/_search?q="emotion synthesis"

### Query T05.4: empathy

[https://guacamole.univ-avignon.fr/dblp1/_search?q="empathy"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22empathy%22)

## Topic T06: AI system-on-chip runs on solar power

<https://techxplore.com/news/2021-06-ai-system-on-chip-solar-power.html>

### Query T06.1: system-on-chip

[https://guacamole.univ-avignon.fr/dblp1/_search?q="system-on-chip"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22system-on-chip%22)

### Query T06.2: energy efficiency

https://guacamole.univ-avignon.fr/dblp1/_search?q="energy efficiency"

### Query T06.3: neural network accelerator

https://guacamole.univ-avignon.fr/dblp1/_search?q="neural network accelerator"

## Topic T07: Transfer learning offers new insight into machine-learning error estimation

<https://techxplore.com/news/2022-03-insight-machine-learning-error.html>

### Query T07.1: transfer learning

<https://guacamole.univ-avignon.fr/dblp1/_search?q="transfer learning">

### Query T07.2: Bayesian approach

https://guacamole.univ-avignon.fr/dblp1/_search?q="Bayesian approach"

### Query T07.3: classification

[https://guacamole.univ-avignon.fr/dblp1/_search?q="classification"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22classification%22)

### Query T07.4: error estimator

<https://guacamole.univ-avignon.fr/dblp1/_search?q=>["error estimator"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22classification%22)

## Topic T08: What is 3G and why is it being shut down? An electrical engineer explains

<https://techxplore.com/news/2022-02-3g-electrical.html>

### Query T08.1: 3G

[https://guacamole.univ-avignon.fr/dblp1/_search?q="3G"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%223G%22)

### Query T08.2: CDMA

[https://guacamole.univ-avignon.fr/dblp1/_search?q="CDMA"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22CDMA%22)

### Query T08.3: OFDMA

[https://guacamole.univ-avignon.fr/dblp1/_search?q="OFDMA"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22OFDMA%22)

## Topic T09: Using AI to fill in the missing gaps in ancient texts

<https://techxplore.com/news/2022-03-ai-gaps-ancient-texts.html>

### Query T09.1: ancient text

https://guacamole.univ-avignon.fr/dblp1/_search?q="ancient text"

### Query T09.2: text reconstruction

https://guacamole.univ-avignon.fr/dblp1/_search?q="text reconstruction"

### Query T09.3: text classification

<https://guacamole.univ-avignon.fr/dblp1/_search?q="text classification">

## Topic T10: Retina-inspired sensors for more adaptive visual perception

<https://techxplore.com/news/2022-03-retina-inspired-sensors-visual-perception.html>

### Query T10.1: optoelectronic

[https://guacamole.univ-avignon.fr/dblp1/_search?q="optoelectronic"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22optoelectronic%22)

### Query T10.2: visual adaptation

https://guacamole.univ-avignon.fr/dblp1/_search?q="visual adaptation"

### Query T10.3: phototransistor

https://guacamole.univ-avignon.fr/dblp1/_search?q="text phototransistor"

### Query T10.4: vision sensor

https://guacamole.univ-avignon.fr/dblp1/_search?q="vision sensor"

## Topic T11: Data scientist builds a detailed network map of 'The Witcher'

<https://techxplore.com/news/2022-02-scientist-network-witcher.html>

### Query T11.1: character relationship

https://guacamole.univ-avignon.fr/dblp1/_search?q="character relationship"

### Query T11.2: storyline visualization

https://guacamole.univ-avignon.fr/dblp1/_search?q="storyline visualization"

### Query T11.3: social map

https://guacamole.univ-avignon.fr/dblp1/_search?q="social map"

## Topic T12: Deep-learning diagnoses: AI detects COVID-19 from smartwatch sensors

<https://techxplore.com/news/2022-03-deep-learning-ai-covid-smartwatch-sensors.html>

### Query T12.1: deep learning

https://guacamole.univ-avignon.fr/dblp1/_search?q="deep learning"

### Query T12.2: smartwatch

[https://guacamole.univ-avignon.fr/dblp1/_search?q="smartwatch"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22smartwatch%22)

### Query T12.3: diagnosis

[https://guacamole.univ-avignon.fr/dblp1/_search?q="diagnosis"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22diagnosis%22)

### Query T12.4: healthcare

[https://guacamole.univ-avignon.fr/dblp1/_search?q="healthcare"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22healthcare%22)

## Topic T13: Injecting fairness into machine-learning models

<https://techxplore.com/news/2022-03-fairness-machine-learning.html>

### Query T13.1: fairness

[https://guacamole.univ-avignon.fr/dblp1/_search?q="fairness"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22fairness%22)

### Query T13.2: bias

[https://guacamole.univ-avignon.fr/dblp1/_search?q="bias"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22bias%22)

### Query T13.3: imbalanced data

https://guacamole.univ-avignon.fr/dblp1/_search?q="imbalanced data"

### Query T13.4: sensitive attribute

https://guacamole.univ-avignon.fr/dblp1/_search?q="sensitive attribute"

## Topic T14: Aqua-Fi: Underwater WiFi developed using LEDs and lasers

<https://techxplore.com/news/2020-06-aqua-fi-underwater-wifi-lasers.html>

### Query T14.1: wifi

[https://guacamole.univ-avignon.fr/dblp1/_search?q="wifi"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22wifi%22)

### Query T14.2: underwater wireless

https://guacamole.univ-avignon.fr/dblp1/_search?q="underwater wireless"

### Query T14.3: light beam

https://guacamole.univ-avignon.fr/dblp1/_search?q="light beam"

## Topic T15: Cyberattack can steal data via cooling fan vibrations

<https://techxplore.com/news/2020-04-cyberattack-cooling-fan-vibrations.html>

### Query T15.1: cyber-security

[https://guacamole.univ-avignon.fr/dblp1/_search?q="cyber-security"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22cyber-security%22)

### Query T15.2: side-channel attack

https://guacamole.univ-avignon.fr/dblp1/_search?q="side-channel attack"

### Query T15.3: accelerometer

[https://guacamole.univ-avignon.fr/dblp1/_search?q="accelerometer"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22accelerometer%22)

## Topic T16: How it takes just six seconds to hack a credit card

<https://techxplore.com/news/2016-12-seconds-hack-credit-card.html>

### Query T16.1: credit card fraud

https://guacamole.univ-avignon.fr/dblp1/_search?q="credit card fraud"

### Query T16.2: guessing attack

https://guacamole.univ-avignon.fr/dblp1/_search?q="guessing attack"

### Query T16.3: distributed attack

<https://guacamole.univ-avignon.fr/dblp1/_search?q="distributed attack">

## Topic T17: Unfixable security flaw found in Intel chipset

<https://techxplore.com/news/2020-03-unfixable-flaw-intel-chipset.html>

### Query T17.1: chipset

[https://guacamole.univ-avignon.fr/dblp1/_search?q="chipset"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22chipset%22)

### Query T17.2: OTP memory

<https://guacamole.univ-avignon.fr/dblp1/_search?q="OTP memory">

### Query T17.3: vulnerability

[https://guacamole.univ-avignon.fr/dblp1/_search?q="vulnerability"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22vulnerability%22)

### Query T17.4: key generation

<https://guacamole.univ-avignon.fr/dblp1/_search?q="key generation">

## Topic T18: Backscatter breakthrough runs near-zero-power IoT communicators at 5G speeds everywhere

<https://techxplore.com/news/2021-06-backscatter-breakthrough-near-zero-power-iot-5g.html>

### Query T18.1: backscatter

[https://guacamole.univ-avignon.fr/dblp1/_search?q="backscatter"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22backscatter%22)

### Query T18.2: low power IoT

<https://guacamole.univ-avignon.fr/dblp1/_search?q="low power IoT">

### Query T18.3: passive device

<https://guacamole.univ-avignon.fr/dblp1/_search?q="passive device">

### Query T18.4: mmWave

[https://guacamole.univ-avignon.fr/dblp1/_search?q="mmWave"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22mmWave%22)

## Topic T19: A new genetic algorithm for traffic control optimization

<https://techxplore.com/news/2019-07-genetic-algorithm-traffic-optimization.html>

### Query T19.1: traffic optimization

https://guacamole.univ-avignon.fr/dblp1/_search?q="traffic optimization"

### Query T19.2: genetic algorithm

https://guacamole.univ-avignon.fr/dblp1/_search?q="genetic algorithm"

### Query T19.3: road accident

https://guacamole.univ-avignon.fr/dblp1/_search?q="road accident"

## Topic T20: Software developed to help programmers prototype graphic user interfaces

<https://techxplore.com/news/2020-11-software-programmers-prototype-graphic-user.html>

### Query T20.1: user-friendly

[https://guacamole.univ-avignon.fr/dblp1/_search?q="user-friendly"](https://guacamole.univ-avignon.fr/dblp1/_search?q=%22user-friendly%22)

### Query T20.2: graphical user interface

<https://guacamole.univ-avignon.fr/dblp1/_search?q="graphical user interface">

### Query T20.3: deep learning

<https://guacamole.univ-avignon.fr/dblp1/_search?q="deep learning">