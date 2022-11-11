from thlr_automata import *

#[Q1]
B=ENFA([0,1,2,3],[0],[2],["a","b"], [(0,"a",1),(0,"b",2),(2,"b",2),(3,"a",2)])

#[/Q1]
#[Q2]
B.add_letter("c")
B.add_edge(2,"c",3)
s=B.add_state()
B.add_edge(4,"a",3)
B.export("B")
#[/Q2]

#[Q3]
def get_accessible_states(automaton, origin):
    visited=set()
    incoming=set()
    incoming.add(origin)
    letters=automaton.alphabet
    for l in letters:
        succ=automaton.get_successors(origin, l)
        for s in succ:
            if not s in incoming:
                incoming.add(s)
    while(len(incoming)!=0):
        aux=incoming.pop()
        visited.add(aux)
        for l in letters:
            succ=automaton.get_successors(aux, l)
            for s in succ:
                if not s in visited:
                    incoming.add(s)
    return visited
    
#[/Q3]

#[Q4]
def is_accessible(automaton, state):
    accessible=set()
    states=automaton.initial_states
    for s in states:
        temp= get_accessible_states(automaton, s)
        for i in temp:
            if (not i in accessible):
                accessible.add(i)
    return state in accessible
#[/Q4]


#[Q5]
def is_co_accessible(automaton, state):
    finals=automaton.final_states
    accessible= get_accessible_states(automaton, state)
    for i in accessible:
        if(i in finals):
            return True
    return False
#[/Q5]

#[Q6]
def is_useful(automaton, state):
    return is_accessible(automaton, state) and is_co_accessible(automaton, state)
#[/Q6]


#[Q7]
def prune(automaton):
    all_states=automaton.all_states
    to_remove=set()
    for i in all_states:
        if(not is_useful(automaton, i)):
            to_remove.add(i)
    for i in to_remove:
        automaton.remove_state(i)

#[/Q7]


############################TESTS####################
B.export("before")
prune(B)
#print(is_useful(B,0))
#B.remove_state(4)
#B.remove_state(1)
B.export("after")
