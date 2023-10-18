# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from asyncio import sleep, wait
from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        
        legalMoves = gameState.getLegalActions()
        
        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        #ghost_X, ghost_Y = newGhostStates[0].getPosition()
        #pacman_X, pacman_Y = newPos 
        #newFood.asList()
        #newPos
        #
        "*** TEST ***"
        #print(type(successorGameState))
        #print(successorGameState.getWalls())
        #a = newGhostStates[0]
        # a.getPostion()
        
        # pac_X, pac_Y = 
        # print (a)
        #print(newFood.asList())
        #print(action)
        #print(successorGameState.getScore())

        # check corner
        
        #print(len(successorGameState.getWalls()))     
        # insert a* 

        foods = newFood.asList()
        min = 999999
        for food in foods:
            temp = manhattanDistance(newPos, food)
            if temp < min:
                min = temp
        
        # max = 0.001
        # for newGhostPos in newGhostStates:
            
        #     temp = ((newPos[0] - newGhostPos.getPosition()[0]) ** 2 + (newPos[1] - newGhostPos.getPosition()[1])) ** 0.5
        #     if (temp > max):
        #         if temp <= 1.5:
        #             max = temp
            
        # insert a* 
       

        #print (min)
        return successorGameState.getScore() + 1/min

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """

        "*** TESTING CODE ***"
        #print(self.depth)
        #print(self.evaluationFunction)
        # legalMoves = gameState.getLegalActions()
        # newGhostStates = gameState.getGhostStates()
        # print (newGhostStates[0])
        # a, b = newGhostStates[0].getPosition()
        # print (a, b)
        # print(gameState.getNumAgents())
        "*** YOUR CODE HERE ***"
        # from util import Queue
        # q = Queue()
        # q.push((gameState, 0, []))
        #iterative method
        # while q.isEmpty is False:
        #     tempGameState, level, path = q.pop()
        #     listGhostMoves = MinimaxAgent.getListGhostMoves(tempGameState)
        #     for moves in listGhostMoves:
        #         for i in range(gameState.getNumAgents() + 1):
        #             tempGameState.generateSuccessor(i, moves[i])

        #         if level != self.depth:
        #             # if tempGameState.isWin() == True:
        #             #     # add 

        #             if tempGameState.isLose() != False:
        #                 q.push((tempGameState, level + 1))
                    
        #         else:
        #             temp.append()
        
        # for moves in legalMoves:
        # def getListGhostMoves(gameState):
        #     import itertools
        #     # newGhostStates = gameState.getGhostStates()
        #     listMoves = []
        #     for i in range (1, gameState.getNumAgents() + 1):
                
        #         listMoves.append(gameState.getLegalActions(i))

        #     return list(itertools.product(*listMoves))

        def minValue(gameState, level, ghostIndex):
            legalMoves = gameState.getLegalActions(ghostIndex)

            if len(legalMoves) == 0:
                return self.evaluationFunction(gameState)
            
            v = 999999
            if ghostIndex == gameState.getNumAgents() - 1:
                for move in legalMoves:
                    v = min(v, maxValue(gameState.generateSuccessor(ghostIndex, move), level))
                return v
            else:
                for move in legalMoves:
                    v = min(v, minValue(gameState.generateSuccessor(ghostIndex, move), level, ghostIndex + 1))
                return v

        def maxValue(gameState, level):
            legalMoves = gameState.getLegalActions(0)

            if len(legalMoves) == 0 or level == self.depth:
                return self.evaluationFunction(gameState)
            v = -999999
            for move in legalMoves:
                v = max(v, minValue(gameState.generateSuccessor(0, move), level + 1, 1))

            return v

        maxTemp = -999999
        tempmove = ""
        for move in gameState.getLegalActions(0):
            temp = minValue(gameState.generateSuccessor(0, move), 1, 1)
            if maxTemp < temp:
                maxTemp = temp
                tempmove = move

        return tempmove
        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        def minValue(gameState, level, ghostIndex, alpha, beta):
            legalMoves = gameState.getLegalActions(ghostIndex)

            if len(legalMoves) == 0:
                return self.evaluationFunction(gameState)
            
            v = 999999
            for move in legalMoves:
                if ghostIndex == gameState.getNumAgents() - 1:
                    tempMaxValue = min(v, maxValue(gameState.generateSuccessor(ghostIndex, move), level, alpha, beta))
                else:
                    tempMaxValue = min(v, minValue(gameState.generateSuccessor(ghostIndex, move), level, ghostIndex + 1, alpha, beta))

                v = min(v, tempMaxValue)
                if v < alpha:
                    return v 
                beta = min(beta, v)
            return v

        def maxValue(gameState, level, alpha, beta):
            legalMoves = gameState.getLegalActions(0)

            if len(legalMoves) == 0 or level == self.depth:
                return self.evaluationFunction(gameState)
            v = -999999
        
            for move in legalMoves:
                tempMinValue = minValue(gameState.generateSuccessor(0, move), level + 1, 1, alpha, beta)
                v = max(v, tempMinValue)
                if v > beta:
                    return v 
                alpha = max(alpha, v)

                if level == 0 and v == tempMinValue:
                    m = move
            if level == 0: 
                return m
            return v
        

        return maxValue(gameState, 0, -999999, 999999)

        util.raiseNotDefined()
        
class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        def expValue(gameState, level, ghostIndex):
            legalMoves = gameState.getLegalActions(ghostIndex)

            if len(legalMoves) == 0:
                return self.evaluationFunction(gameState)
            
            v = 0
            prob = 1 / len(legalMoves)
            if ghostIndex == gameState.getNumAgents() - 1:
                for move in legalMoves:
                    v += prob * maxValue(gameState.generateSuccessor(ghostIndex, move), level)
                return v
            else:
                for move in legalMoves:
                    v += prob * expValue(gameState.generateSuccessor(ghostIndex, move), level, ghostIndex + 1)
                return v
        

        def maxValue(gameState, level):
            legalMoves = gameState.getLegalActions(0)

            if len(legalMoves) == 0 or level == self.depth:
                return self.evaluationFunction(gameState)
            v = -999999
            for move in legalMoves:
                v = max(v, expValue(gameState.generateSuccessor(0, move), level + 1, 1))

            return v
        
        maxTemp = -999999
        tempmove = ""
        for move in gameState.getLegalActions(0):
            temp = expValue(gameState.generateSuccessor(0, move), 1, 1)
            if maxTemp < temp:
                maxTemp = temp
                tempmove = move

        return tempmove
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    # newGhostStates = currentGameState.getGhostStates()
    # newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    # minA = 999999
    # for food in foods:
    #     temp = manhattanDistance(newPos, food)
    #     if temp < minA:
    #         minA = temp
    
    # minB = 999999
    # for newGhostPos in newGhostStates:
    #     temp = abs(manhattanDistance(newPos, newGhostPos.getPosition()))
    #     if (temp < minB):
    #         minB = temp
        
    # #print (min)
    # #return currentGameState.getScore()  + 1/min
    # if (minB <= 2):
    #     return currentGameState.getScore()  - 1000 * minB
    # elif (temp >= 1 for temp in newScaredTimes):
    #     return currentGameState.getScore()  + 1 / minA
    # else:
    #     return currentGameState.getScore()+ 1 / minA  - 1/minB


    "*** YOUR CODE HERE - 2nd TRY ***"
    #each food is 10 pts
    #each step -1
    #grid 3x3
    gridLen = 2

    # make every movement is estimate with expectimax. Get the priority as which should be closer to food

    def expValue(gameState, level, maxDepth, ghostIndex):
        legalMoves = gameState.getLegalActions(ghostIndex)

        if len(legalMoves) == 0:
            return gameState.getScore() + 9/ getmin(gameState)
        
        v = 0
        prob = 1 / (len(legalMoves) ) 
        if ghostIndex == gameState.getNumAgents() - 1:
            for move in legalMoves:
                
                v += prob * (maxValue(gameState.generateSuccessor(ghostIndex, move), level, maxDepth) + 9/ getmin(gameState.generateSuccessor(ghostIndex, move)) )
            return v
        else:
            for move in legalMoves:
                
                v += prob * (expValue(gameState.generateSuccessor(ghostIndex, move), level, maxDepth, ghostIndex + 1))
            return v
    

    def maxValue(gameState, level, maxDepth):
        legalMoves = gameState.getLegalActions(0)
        #print(legalMoves)
        if len(legalMoves) == 0 or level == maxDepth:
            return gameState.getScore() 
        v = -999999
        for move in legalMoves:
            v = max(v, expValue(gameState.generateSuccessor(0, move), level + 1, maxDepth, 1)) 
        return v
    
    return maxValue(currentGameState, 1, gridLen)


    util.raiseNotDefined()

def getmin(gameState):
    foods = gameState.getFood().asList()
    newPos = gameState.getPacmanPosition()
    minA = 999999
    for food in foods:
        temp = manhattanDistance(newPos, food)
        if temp < minA:
            minA = temp
    return minA
# Abbreviation
better = betterEvaluationFunction
