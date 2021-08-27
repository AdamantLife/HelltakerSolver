import json
from Helltaker import GameplaySequence

def BruteForceSolver(gameplay):
    """ Brute forces the puzzle by checking all possible paths """
    MEMO = {}
    def recursion(gamestate: GameplaySequence):
        ## print('recurse')
        allresults = []
        ## print(">>>",gamestate.character.haskey)
        for move in gamestate.character.available_actions():
            ## print(gamestate.remaining_actions(), move)
            newstate = gamestate.copy()
            try:
                moveresult = newstate.move(move)
                ## print("moved")
            except GameplaySequence.Victory:
                allresults.append(newstate)
                continue
            except GameplaySequence.GameOver:
                ## print("gameover")
                continue
            else:
                ## move was illegal
                if moveresult is None:
                    ## print("> Illegal")
                    continue
                ## After this move, character does not have
                ## enough stamina to move to the Target (naive)
                if newstate.unwinnable():
                    ## print("> Unwinnable")
                    continue
                ## Already recursed through this map position
                grid = "\n".join(",".join(row) for row in newstate.map.cleangrid(newstate.map.grid))
                if grid in MEMO:
                    if len(MEMO[grid])<= len(newstate.actions):
                        ## print("> Duplicate State")
                        continue
                MEMO[grid] = newstate.actions
                results = recursion(newstate)
                allresults.extend(results)
        return allresults    
    _all = recursion(gameplay)
    # with open("output.json",'w') as f:
    #     json.dump(MEMO, f)
    return _all

def load_bruteforce(jsonfile):
    """ Uses a json file to start a BruteForceSolver. """
    gameplay = GameplaySequence.loadfromjson(jsonfile)
    return BruteForceSolver(gameplay)
