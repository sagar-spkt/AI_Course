# AI_Course
This repo has algorithms I learned during AI Course

## Algorithms Included
### Uninformed Search Algorithms
Uses iterative state formulation
* **[Breadth First Search](https://github.com/sagar-spkt/AI_Course/blob/1414ac985993e1256028754fdd3b1c6d42cb8e52/algorithms/uninformed_search.py#L1-L27)** 
* **[Depth First Search](https://github.com/sagar-spkt/AI_Course/blob/1414ac985993e1256028754fdd3b1c6d42cb8e52/algorithms/uninformed_search.py#L30-L60)**
* **[Depth Limit Search](https://github.com/sagar-spkt/AI_Course/blob/1414ac985993e1256028754fdd3b1c6d42cb8e52/algorithms/uninformed_search.py#L63-L96)**
* **[Uniform Cost Search](https://github.com/sagar-spkt/AI_Course/blob/1414ac985993e1256028754fdd3b1c6d42cb8e52/algorithms/uninformed_search.py#L99-L140)**

### Informed Search Algorithms
Uses complete state formulation
* **[A* Search](https://github.com/sagar-spkt/AI_Course/blob/1414ac985993e1256028754fdd3b1c6d42cb8e52/algorithms/informed_search.py#L8-L15)** - *Using f(n) = g(n) + h(n) as evaluation function in [Uniform Cost Search](https://github.com/sagar-spkt/AI_Course/blob/1414ac985993e1256028754fdd3b1c6d42cb8e52/algorithms/uninformed_search.py#L99-L140)*

### Beyond Classical Search Algorithms
Uses complete state formulation
* **[Hill Climbing](https://github.com/sagar-spkt/AI_Course/blob/1414ac985993e1256028754fdd3b1c6d42cb8e52/algorithms/informed_search.py#L18-L47)** - *Greedy local search optimization algorithm*
* **[Simulated Annealing](https://github.com/sagar-spkt/AI_Course/blob/1414ac985993e1256028754fdd3b1c6d42cb8e52/algorithms/informed_search.py#L63-L84)**
* **[Genetic Algorithm](https://github.com/sagar-spkt/AI_Course/blob/1414ac985993e1256028754fdd3b1c6d42cb8e52/algorithms/informed_search.py#L125-L142)**

### Adversarial Search
Reference - [tonypoer.io](https://tonypoer.io/2016/10/28/implementing-minimax-and-alpha-beta-pruning-using-python/)
* **[Minimax Algorithm](https://github.com/sagar-spkt/AI_Course/blob/1414ac985993e1256028754fdd3b1c6d42cb8e52/algorithms/adversarial_search/minimax.py#L19-L53)**
* **[AlphaBeta Pruning](https://github.com/sagar-spkt/AI_Course/blob/1414ac985993e1256028754fdd3b1c6d42cb8e52/algorithms/adversarial_search/minimax_improve.py#L31-L51)**

## AI Problems Coded
Some of the popular AI Problems are coded to instantiate Above mentioned algorithms
* **[NQueen Problem](https://github.com/sagar-spkt/AI_Course/blob/1414ac985993e1256028754fdd3b1c6d42cb8e52/ai_problems/search_problems.py#L6)** - *[NQueen](https://github.com/sagar-spkt/AI_Course/blob/1414ac985993e1256028754fdd3b1c6d42cb8e52/ai_problems/genetic_nqueen.py#L6) for Genetic Algorithm*
* **[Problem Of Romania](https://github.com/sagar-spkt/AI_Course/blob/1414ac985993e1256028754fdd3b1c6d42cb8e52/ai_problems/search_problems.py#L102)** - *Coming soon*
* **[Tic-Tac-Toe](https://github.com/sagar-spkt/AI_Course/blob/1414ac985993e1256028754fdd3b1c6d42cb8e52/ai_problems/game.py#L4)** - *Used as problems including multiple agent: Minimax & AlphaBeta Pruning*

## How To Use
**Coming Soon!!!**


## Extra
##### Facebook Chat Bot Using DialoFlow API
Create a DialogFlow API Access token and place it in the [code](https://github.com/sagar-spkt/AI_Course/blob/e6ab5561b68dbd192e7e57e58e06aa0b419adfef/fbchat_bot_dialogflow.py#L8)

And use your facebook credential [here](https://github.com/sagar-spkt/AI_Course/blob/e6ab5561b68dbd192e7e57e58e06aa0b419adfef/fbchat_bot_dialogflow.py#L28)