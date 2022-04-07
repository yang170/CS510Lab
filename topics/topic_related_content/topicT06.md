[techxplore.com](https://techxplore.com/news/2021-06-ai-system-on-chip-solar-power.html)

# AI system-on-chip runs on solar power

Swiss Center for Electronics and Microtechnology - CSEM

---

AI is used in an array of useful applications, such as predicting a machine's lifetime through its vibrations, monitoring the cardiac activity of patients and incorporating facial recognition capabilities into video surveillance systems. The downside is that AI-based technology generally requires a lot of power and, in most cases, must be permanently connected to the cloud, raising issues related to data protection, IT security and energy use.

CSEM engineers may have found a way to get around those issues, thanks to a new system-on-chip they have developed. It runs on a tiny battery or a small solar cell and executes AI operations at the edge—i.e., locally on the chip rather than in the cloud. What's more, their system is fully modular and can be tailored to any application where real-time signal and image processing is required, especially when sensitive data are involved. The engineers will present their device at the prestigious 2021 VLSI Circuits Symposium in Kyoto this June.

The CSEM system-on-chip works through an entirely new signal processing architecture that minimizes the amount of power needed. It consists of an ASIC chip with a RISC-V processor (also developed at CSEM) and two tightly coupled machine-learning accelerators: one for face detection, for example, and one for classification. The first is a binary decision tree (BDT) engine that can perform simple tasks but cannot carry out recognition operations.

"When our system is used in facial recognition applications, for example, the first accelerator will answer preliminary questions like: Are there people in the images? And if so, are their faces visible?" says Stéphane Emery, head of system-on-chip research at CSEM. "If our system is used in voice recognition, the first accelerator will determine whether noise is present and if that noise corresponds to human voices. But it can't make out specific voices or words—that's where the second accelerator comes in."

The second accelerator is a convolutional neural network (CNN) engine that can perform these more complicated tasks—recognizing individual faces and detecting specific words—but it also consumes more energy. This two-tiered data processing approach drastically reduces the system's power requirement, since most of the time only the first accelerator is running. The integrated circuit can carry out complicated artificial-intelligence operations like face, voice and gesture recognition and cardiac monitoring. Credit: CSEM

As part of their research, the engineers enhanced the performance of the accelerators themselves, making them adaptable to any application where time-based signal and image processing is needed. "Our system works in basically the same way regardless of the application," says Emery. "We just have to reconfigure the various layers of our CNN engine."

The CSEM innovation opens the door to an entirely new generation of devices with processors that can run independently for over a year. It also sharply reduces the installation and maintenance costs for such devices, and enables them to be used in places where it would be hard to change the battery.