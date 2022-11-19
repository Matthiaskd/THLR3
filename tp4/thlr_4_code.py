from thlr_automata import *
from thlr_regex import *

#[Q1]
r1=new_regex("a*")
r2=new_regex("a*.b+c")
r3=new_regex("(a+ε)*")
#[/Q1]

#[Q2]
def convert_regex(enfa, origin, destination, regex):
    op=regex.root
    if(op=="."):
        a=enfa.add_state()
        b=enfa.add_state()
        enfa.add_edge(a,"",b)
        convert_regex(enfa,origin,a,regex.children[0])
        convert_regex(enfa, b, destination, regex.children[1])

    elif(op=="+"):
        a=enfa.add_state()
        b=enfa.add_state()
        c=enfa.add_state()
        d=enfa.add_state()

        enfa.add_edge(origin,"",a)
        enfa.add_edge(origin,"",c)
        enfa.add_edge(b,"",destination)
        enfa.add_edge(d,"",destination)

        convert_regex(enfa, a, b, regex.children[0])
        convert_regex(enfa, c, d, regex.children[1])

    elif(op=="*"):
        a=enfa.add_state()
        b=enfa.add_state()
        enfa.add_edge(origin,"",a)
        enfa.add_edge(origin, "",destination)
        enfa.add_edge(b,"",destination)
        enfa.add_edge(b,"",a)
        convert_regex(enfa, a, b, regex.children[0])
    else:
        enfa.add_letter(op)
        enfa.add_edge(origin, op,destination)
#[/Q2]

#[Q3]
def to_enfa(regex):
    NFA=ENFA([0,1], [0],[1],[],[])
    convert_regex(NFA, 0, 1, regex)
    return NFA
#[/Q3]

#[Q4]
def get_epsilon_closure(enfa, origin):
    visited=set()
    incoming=set()
    incoming.add(origin)
    while(len(incoming)!=0):
        aux=incoming.pop()
        visited.add(aux)
        e_forward=enfa.get_successors(aux,"")
        for s in e_forward:
            if not s in visited:
                incoming.add(s)
    return visited
#[/Q4]

#[Q5]
def to_nfa(enfa):
    alphabet=enfa.alphabet
    states=enfa.all_states
    for p in states:
        e_fwd=get_epsilon_closure(enfa, p)
        for q in e_fwd:
            for a in alphabet:
                succ=enfa.get_successors(q, a)
                for q2 in succ:
                    enfa.add_edge(p, a, q2)
                    if(q2 in e_fwd and q2 in enfa.final_states):
                        enfa.final_states.add(q)
    enfa.alphabet.remove("")

#[/Q5]
