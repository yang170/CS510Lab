[techxplore.com](https://techxplore.com/news/2018-10-artificial-intelligenceparking-car-neurons.html)

# Artificial intelligence—parking a car with only 12 neurons

Florian Aigner

---

Computer scientists at TU Wien (Vienna) are improving artificial intelligence by drawing inspiration from biology. The new approaches achieve amazing results with surprisingly little effort.

A naturally grown brain works quite differently than an ordinary computer program. It does not use code consisting of clear logical instructions, it is a network of cells that communicate with each other. Simulating such networks on a computer can help to solve problems which are difficult to break down into logical operations.

At TU Wien (Vienna), in collaboration with researchers at Massachusetts Institute of Technology (MIT), a new approach for programming such neural networks has now been developed, which models the time evolution of the nerve signals in a completely different way. It was inspired by a particularly simple and well-researched creature, the roundworm C. elegans. Neural circuits from its nervous system were simulated on the computer, and then the model was adapted with machine learning algorithms. This way, it was possible to solve remarkable tasks with an extremely low number of simulated nerve cells – for example parking a car. Even though the worm-inspired network only consists of 12 neurons, it can be trained to steer a rover robot to a given spot. Ramin Hasani from the Institute of Computer Engineering at TU Wien has now presented his work at the TEDx conference in Vienna on October 20.

It can be shown that these novel neural networks are extremely versatile. Another advantage is that their internal dynamics can be understood - in contrast to standard artificial neural networks, which are often regarded as a useful but inscrutable "black box".
 Signals in branched networks

"Neural networks have to be trained" says Ramin Hasani. "You provide a specific input and adjust the connections between the neurons so that the desired output is delivered."

The input, for example, can be a photograph, and the output can be the name of the person in the picture. "Time usually does no play an important role in this process," says Radu Grosu from the Institute of Computer Engineering of TU Wien. For most neural networks, all the input is delivered at once, immediately resulting in a certain output. But in nature things are very different.

Speech recognition, for example, is always time-dependent, as are simultaneous translations or sequences of movements reacting to a changing environment. "Such tasks can be handled better using what we call RNN, or recurrent neural networks", says Ramin Hasani. "This is an architecture that can capture sequences, because it makes neurons remember what happened previously."

Hasani and his colleagues propose a novel RNN-architecture based on a biophysical neuron and synapse model that allows time-varying dynamics. "In a standard RNN-model, there is a constant link between neuron one and neuron two, defining how strongly the activity of neuron one influences the activity of neuron two", says Ramin Hasani. "In our novel RNN architecture, this link is a nonlinear function of time."

## The worm brain that can park a car

Allowing cell activities and links between cells to vary over time opens up completely new possibilities. Ramin Hasani, Mathias Lechner and their coworkers showed theoretically that their architecture can, in principle, approximate arbitrary dynamics. To demonstrate the versatility of the new approach, they developed and trained a small neural network: "We re-purposed a neural circuit from the nervous system of the nematode C. elegans. It is responsible for generating a simple reflexive behavior - the touch-withdrawal," says Mathias Lechner, who is now working at the Institute of Science and Technology (IST) Austria. "This neural network was simulated and trained to control real-life applications."

The success is remarkable: the small, simple network with only 12 neurons can (after appropriate training) solve challenging tasks. For instance, it was trained to manoeuvre a vehicle into a parking space along a pre-defined path. "The output of the neural network, which in nature would control the movement of nematode worms, is used in our case to steer and accelerate a vehicle", says Hasani. "We theoretically and experimentally demonstrated that our novel neural networks can solve complex tasks in real-life and in simulated physical environments."

The new approach has another important advantage: it provides a better insight into the inner workings of the neural network. Previous neural networks, which often consisted of many thousands of nodes, have been so complex that only the final results could be analysed. Obtaining a deeper understanding of what is going on inside was hardly possible. The smaller but extremely powerful network of the Vienna team is easier to analyse, and so scientists can at least partially understand, which nerve cells cause which effects. "This is a great advantage which encourages us to further research their properties", says Hasani.

Of course, this does not mean that cars will be parked by artificial worms in the future, but it shows that artificial intelligence with a more brain-like architecture can be far more powerful than previously thought. 
