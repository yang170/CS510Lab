[techxplore.com](https://techxplore.com/news/2019-07-genetic-algorithm-traffic-optimization.html)

# A new genetic algorithm for traffic control optimization

Ingrid Fadelli , Tech Xplore

---

Researchers at the University of Technology Sydney and DATA61 have recently developed a new method for optimizing the timing of signals in urban environments under severe traffic conditions. Their approach, presented in a paper pre-published on arXiv, entails the use of genetic algorithms (GAs), a popular computer science technique for solving optimization problems.

"The idea of this research work came from various drives with my car in the city of Sydney, which is often affected by traffic incidents, causing a large amount of delay and increased road congestion," Tuo Mao, one of the researchers who carried out the study, told TechXplore. "This made me wonder: How can we solve this problem with the aid of advanced computer science techniques?"

Traffic control signals are the most widespread tools to control and manage road traffic in densely populated urban environments. A traffic signal's settings, also known as signal control plan, can affect road traffic significantly, particularly when disruptions first arise.

So far, the majority of proposed solutions for traffic control optimization are designed to work under normal traffic conditions. This is because optimizing a traffic light's control plans after an incident has occurred or when traffic is at a peak is a particularly challenging task, especially if multiple lanes or an entire road section are affected.

Contrarily to most previous works, Mao and his colleagues set out to achieve traffic signal control optimization under severe traffic conditions using GAs. GAs are a computer science technique inspired by the biological evolution observed in humans, which is designed to naturally select the most optimal solutions among an initial set of possibilities.

"GAs are commonly used in optimization problems (e.g., finding the best phase duration that would minimise travel time in an intersection) by using bio-inspired functions such as individual mutation, crossover, and selection of best individuals to carry on the best genes of a population—in our case, best signal phases," Mao said. "We thought that GAs would be a fantastic solution to solve this problem and decided to use them to generate the optimized traffic signal plans for the incident affected area."

The GA developed by Mao and his colleagues essentially explores all possible traffic signal control plans for a given intersection (e.g. the green time for "right turn" signals, "go straight' signals, etc.). Its key objective is to minimize the total travel time in an area affected by a road accident by identifying the best combination of signal phases across all intersections within that area.

"We first generate a large number of traffic control plans, including different phase durations evenly distributed in a large numerical space, which constitute the first generation of individuals from the entire population," Mao explained. "Then we apply selection, crossover and mutation in order to introduce more randomness in exploring the space of all possibilities, and select only the best candidates to carry on the optimization in a next generation."
 
Subsequently, the approach devised by Mao and his colleagues evolves the original population for a specific number of generations until the majority of individuals within that population are similar, and it has reached an optimal solution. The GA's final outcome is an optimized traffic signal control plan for all traffic lights in areas affected by road accidents.

While past studies have proposed several other traffic signal control optimization techniques, most of these are based on traffic modeling and knowledge-based expert (i.e., heuristic) systems. These systems passively react to observed traffic conditions and are hence unable to actively propose solutions for reducing congestion caused by road accidents.

"Our method has three key advantages," Mao explained. Firstly, it considers non-recurrent traffic incidents, as we input the incident to the model actively after someone reported it, therefore the traffic signal control plan is aware of the incident and can respond faster. Secondly, it considers the rerouting behavior of drivers by applying a dynamic traffic assignment, which considers the road capacity drop caused by the traffic incidents. Finally, our method is efficient for exploring many possibilities of signal control plans."

The researchers evaluated their technique using a four-intersection network designed in AIMSUN, a renowned traffic modeling platform. They constructed three different scenarios in which the GA had to optimize traffic signal timings under both normal conditions and with severe traffic. In these tests, they observed that when traffic signal control plans can be adapted to a change of route by drivers after a traffic accident has occurred, congestion tends to dissipate faster.

"When using our method, we improved drivers' total travel time by 40.76% compared to applying no response at all (i.e. no control over the signal phasing)," Mao said. " Our research could provide suggestions for traffic management centres on how to act when a fresh incident happens, as a part of a routine for managing a better traffic response."

In the future, the GA developed by Mao and his colleagues could aid the development of more effective traffic control systems. According to the researchers, by advancing their technique's data streaming capabilities and computational performance they could ultimately allow it to automatically optimize traffic signals, actively responding to live road incidents.

"We are currently applying the method to a more complicated network and even a larger network from the city of Sydney," Mao said. "We are also researching to further shorten the computation time and further increase efficiency by coupling the GA with machine learning, which could speed-up the convergence rate towards the best solutions."
