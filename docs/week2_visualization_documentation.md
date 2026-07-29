\# Week 2 Visualization Documentation



\## Project



\*\*Travel \& Hospitality – Reinforcement Learning for Dynamic Pricing\*\*



\---



\# Objective



The objective of Week 2 was to prepare visualizations and workflow diagrams that explain the key concepts behind dynamic pricing in the travel and hospitality industry.



The visualizations demonstrate the relationships between ticket price, customer demand, revenue, booking probability, and pricing behaviour over time. These graphical representations support the Reinforcement Learning model being developed by the team.



The data used in these visualizations is simulated for demonstration purposes and can later be replaced with the processed booking demand dataset.



\---



\# Deliverables



The following deliverables were completed during Week 2:



\- Demand vs Price visualization

\- Revenue vs Price visualization

\- Booking Probability vs Price chart

\- Demand Heatmap

\- Dynamic Price Trend graph

\- Reinforcement Learning workflow diagram

\- Q-Learning workflow diagram

\- Updated Google Colab notebook

\- Visualization documentation



\---



\# Visualization 1 – Demand vs Price



\## Purpose



This graph illustrates how customer demand changes with ticket price.



\## Description



As ticket prices increase, customer demand generally decreases because fewer customers are willing to purchase expensive tickets.



This inverse relationship is one of the fundamental concepts behind dynamic pricing.



\## Observation



\- Lower ticket prices attract more customers.

\- Higher ticket prices reduce booking demand.

\- Dynamic pricing algorithms continuously adjust prices to maintain an optimal balance.



\---



\# Visualization 2 – Revenue vs Price



\## Purpose



To demonstrate how revenue varies with ticket price.



\## Description



Revenue initially increases as ticket prices increase because each booking generates more income.



However, after reaching an optimal price, customer demand decreases rapidly, causing total revenue to decline.



\## Observation



\- Revenue is not maximized at the highest price.

\- There exists an optimal ticket price.

\- Reinforcement Learning aims to discover this optimal pricing strategy automatically.



\---



\# Visualization 3 – Booking Probability vs Price



\## Purpose



To illustrate how ticket price influences the probability of customers making a booking.



\## Description



As prices increase, the probability of customers completing a booking decreases.



This information is useful for understanding customer behaviour in dynamic pricing systems.



\## Observation



\- Lower prices lead to higher booking probability.

\- Higher prices reduce customer conversion.

\- Booking probability is an important factor when determining pricing decisions.



\---



\# Visualization 4 – Demand Heatmap



\## Purpose



To visualize customer demand across different ticket prices and booking periods.



\## Description



The heatmap provides an overview of demand intensity using colour variation.



Higher demand appears at lower prices and earlier booking periods.



\## Observation



\- Demand decreases as ticket prices increase.

\- Demand also changes depending on the remaining booking period.

\- Heatmaps provide a quick visual understanding of customer behaviour.



\---



\# Visualization 5 – Dynamic Price Trend



\## Purpose



To demonstrate how ticket prices change as the departure date approaches.



\## Description



Dynamic pricing systems continuously adjust prices according to demand, inventory, and remaining time.



The graph illustrates a typical pricing strategy where prices increase closer to departure.



\## Observation



\- Prices generally increase as departure approaches.

\- Real-world pricing strategies may also decrease prices near departure if many seats remain unsold.

\- Reinforcement Learning can learn these strategies automatically instead of relying on fixed rules.



\---



\# Reinforcement Learning Workflow



\## Purpose



To explain how the Reinforcement Learning agent interacts with the market environment.



\## Workflow



1\. Observe the current state.

2\. Select a pricing action.

3\. Apply the selected ticket price.

4\. Customers respond to the offered price.

5\. Revenue is generated.

6\. The environment transitions to the next state.

7\. The learning process repeats.



\## Outcome



The agent gradually learns which pricing decisions maximize long-term revenue.



\---



\# Q-Learning Workflow



\## Purpose



To explain the learning cycle of the Q-Learning algorithm.



\## Workflow



1\. Observe the current state.

2\. Choose a pricing action.

3\. Execute the action.

4\. Receive a reward.

5\. Update the Q-value.

6\. Move to the next state.

7\. Repeat until the episode ends.



\## Outcome



Over multiple training episodes, the Q-table stores increasingly accurate estimates of the expected reward for each state-action pair.



\---



\# Tools Used



\- Python

\- Google Colab

\- Matplotlib

\- NumPy

\- Pandas

\- PowerPoint / draw.io (Workflow Diagrams)

\- GitHub

\- GitHub Desktop



\---



\# Files Created



\## Notebook



\- Week2\_Visualizations.ipynb



\## Reports



\- demand\_vs\_price.png

\- revenue\_vs\_price.png

\- booking\_probability.png

\- demand\_heatmap.png

\- price\_trend.png

\- rl\_workflow.png

\- qlearning\_workflow.png



\## Documentation



\- week2\_visualization\_documentation.md



\---



\# Conclusion



The visualizations prepared during Week 2 provide a clear understanding of the relationships between pricing, customer demand, booking probability, and revenue generation in a dynamic pricing system.



The workflow diagrams explain how Reinforcement Learning and Q-Learning operate within the pricing environment.



These deliverables support the implementation phase of the project by providing visual references and technical documentation for the development team.

