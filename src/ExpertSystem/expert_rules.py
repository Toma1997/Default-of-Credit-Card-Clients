# Helper function
def eq(x, y):
    if x == 'Not sure':
        return False
    return x == y

# EXPERT SYSTEM DEFINITION

# Decision context
def define_ctxs(shell):
    #sh.define_ctx(Ctx('client', ['sex', 'marriage','education']))
    shell.define_ctx(Ctx('client', goals=['default_payment_next_month']))

# Parameters (attributes)
def define_params(shell):
    
    # Client parameters
    shell.define_param(Param('sex', 'client', enum=['male', 'female'], ask_first=True))
    shell.define_param(Param('marriage', 'client', enum=['married', 'single', 'others'], ask_first=True))
    shell.define_param(Param('education', 'client', enum=['graduate school', 'university', 'high school', 'others'], ask_first=True))

    # Class paramters (decisios) - default payment next month prediciton 
    shell.define_param(Param('default_payment_next_month', 'client', enum=['yes', 'no']))

# Production rules
def define_rules(shell):
    # Rules
    shell.define_rule(Rule(1,
                        [('sex', 'client', eq, 'male')],
                        [('default_payment_next_month', 'client', eq, 'yes')],
			0.65))
    shell.define_rule(Rule(2,
                        [('marriage', 'client', eq, 'yes')],
                        [('default_payment_next_month', 'client', eq, 'no')],
			0.79))
    shell.define_rule(Rule(3,
                        [('education', 'client', eq, 'high school')],
                        [('default_payment_next_month', 'client', eq, 'yes')],
			0.75))
    # Default rule
    shell.define_rule(Rule(4,
                        [],
                        [('default_payment_next_month', 'client', eq, 'no')],
			0.50))
    
# System execution
from expert_shell import Param, Ctx, Rule, Shell

def report_findings(findings):
    for inst, result in findings.items():
        print('\nDecision for %s-%d:' % (inst[0], inst[1]))
        for param, vals in result.items():
            possibilities = ['%s %f' % (val[0], val[1]) for val in vals.items()]
            print('%s: %s' % (param, ', '.join(possibilities)))
        
def main():
    shell = Shell()
    define_ctxs(shell)
    define_params(shell)
    define_rules(shell)
    report_findings(shell.execute(['client']))

main()