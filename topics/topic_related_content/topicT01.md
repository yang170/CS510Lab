[techxplore.com](https://techxplore.com/news/2021-12-highly-indoor-positioning.html)

# Curve Light: A highly performing indoor positioning system

Ingrid Fadelli

---

In recent years, engineers have been trying to develop more effective sensors and tools to monitor indoor environments. Serving as the foundation of these tools, indoor positioning systems automatically determine the position of objects with high accuracy and low latency, enabling emerging Internet-of-Things (IoT) applications, such as robots, autonomous driving, VR/AR, etc.

A team of researchers recently created CurveLight, an accurate and efficient light positioning system. Their technology, described in a paper presented at ACM's SenSys 2021 Conference on Embedded Networked Sensor Systems, could be used to enhance the performance of autonomous vehicles, robots and other advanced technologies.

"In CurveLight, the signal transmitter includes an infrared LED, covered by a hemispherical and rotatable shade," Zhimeng Yin, one of the researchers who developed the system at City University of Hong Kong, told TechXplore. "The receiver detects the light signals with a photosensitive diode. When the shade is rotating, the transmitter generates a unique sequence of light signals for each point in the covered space."

Recently developed positioning systems can detect the position of objects using LED lamps as landmarks (i.e., by analyzing their unique light-related characteristics). To make them easier to deploy in real-world settings, some developers did not limit their use to LED lamps, but instead designed the systems so that they collect lamp-specific information and use it as a fingerprint.

While some of these systems achieved promising performances, they often require extensive sensing and computational resources. In addition, to work well, these systems need to continuously capture and analyze images, which could be a privacy concern for users.

"Existing solutions measure the received light intensity, compute the distances from the receiver to LED transmitters, based on the Lambertian model, and further adopt multilateral positioning for localization," Yin said. "Typically, this type of positioning methods suffers from model inaccuracy, environmental noises and sensitivity to receiver's orientation."

To overcome the limitations of existing positioning systems, some researchers suggested substituting LED lamps with other light sources, such as projectors. Compared to LED lamps, however, projectors could be harder to deploy in the real-world.

"For example, SpotLight and SmartLight exploit projectors to project dynamically changing images into the space. By detecting the changing light patterns, the receiver can compute its location," Yin said. "SmartLight reports an error of 0.1 m, but the system is not easy to deploy due to the requirement of projectors. In addition, the localization latency is fairly high, making it unsuitable for real-time applications."

Instead of using light, some positioning systems use other wireless signals, such as wi-fi, UWB, sound waves, geomagnetic signals and radiofrequency identification (RFID). Wi-fi signals are easier to access in real-time settings, but when used to predict the position of objects they often result in poorer accuracy and stability. On the other hand, positioning systems that use RFID technology are often very accurate, but they can be more expensive to implement.

The new positioning system created by Yin and his colleagues uses light to detect objects and determine their position. Its components include a transmitter based on an infrared (IR) chip, which is fixed on the ceiling, with its base placed horizontally.

"The LED bead is very small in size (around 2 mm × 2 mm), so can be approximately treated as a point light source," Yin explained. "To distinguish the emitted light signals from ambient light, a microcontroller (MCU) in the transmitter lets the LED flashes at a certain rate."

The transmitter used by the researchers also includes a hemispherical shade that covers the LED lamp, as well as a motor that allows the shade to spin around the lamp at a fixed rate. In the initial prototype of the team's system, the shade spins at a rate of 1200 revolutions per minute (RPM).

"The shade consists of two types of regions: transparent regions and translucent regions," Yin said. "When the LED is on, the transparent regions allow the light to pass through and result in bright regions on the ground, while the translucent regions absorb part of the light energy and create gray regions on the ground. When the shade rotates, the shade's projected image also rotates with the same rotational speed on the ground. As a result, the receiver detects a sequence of light signals with two levels of intensity for uniquely determining its location."

The light positioning system created by Yin and his colleagues has numerous advantages over other systems created in the past. Firstly, it is highly accurate, with an average accuracy of 2–3cm across in typical indoor environments. Secondly, it has a low-latency, achieving an update rate of 36 Hz using a single transmitter.

The system is also practical and very easy to implement. As part of their study, the researchers evaluated it in a series of tests and implemented it in several real-world environments, demonstrating its value for enhancing both autonomous driving and robotic navigation.

"Other than typical lab settings, we have also deployed our system in more than ten real-world environments, including autonomous driving, industrial robots in smart factories, warehouses, mines, etc.," Yin said. "In the paper, we report two use cases, in which CurveLight was accepted as a key part of the customer's full navigation solution."

In the future, CurveLight could be used by a growing number of roboticists and developers to enhance the performance of robots, self-driving cars and other autonomous systems. Meanwhile, Yin and his colleagues will continue working on their system and evaluating its applicability in other settings.

"We now plan to develop accurate and scalable 3D positioning systems to serve numerous IoT applications," Yin added.