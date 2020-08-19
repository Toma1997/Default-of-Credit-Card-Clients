# Helper function
def eq(x, y):
    if x == 'nisam siguran':
        return False
    return x == y

# EXPERT SYSTEM DEFINITION

# Decision context
def define_ctxs(sh):
    #sh.define_ctx(Ctx('client', ['sex', 'marriage','education']))
    sh.define_ctx(Ctx('client', goals=['preporuka']))

# Parameters (attributes)
def define_params(sh):
    
    # Client parameters
    sh.define_param(Param('sex', 'client', enum=['male', 'female'], ask_first=True))
    sh.define_param(Param('marriage', 'client', enum=['married', 'single', 'others'], ask_first=True))
    sh.define_param(Param('education', 'client', enum=['graduate school', 'university', 'high school', 'others'], ask_first=True))

    # Class paramters (decisios) - default payment next month prediciton 
    sh.define_param(Param('default_payment_next_month', 'client', enum=['yes', 'no']))

# Production rules
def define_rules(sh):
    # Rules
    sh.define_rule(Rule(1,
                        [('sex', 'client', eq, 'male')],
                        [('default_payment_next_month', 'client', eq, 'yes')],
			1.0))
    sh.define_rule(Rule(2,
                        [('marriage', 'client', eq, 'yes')],
                        [('default_payment_next_month', 'client', eq, 'no')],
			0.86))
    sh.define_rule(Rule(3,
                        [('education', 'client', eq, 'university')],
                        [('default_payment_next_month', 'client', eq, 'no')],
			1.0))
    # Default rule
    sh.define_rule(Rule(4,
                        [],
                        [('default_payment_next_month', 'client', eq, 'no')],
			0.75))
    
# System execution
from expert_shell import Param, Ctx, Rule, Shell

def report_findings(findings):
    for inst, result in findings.items():
        print('\nDecision for %s-%d:' % (inst[0], inst[1]))
        for param, vals in result.items():
            possibilities = ['%s %f' % (val[0], val[1]) for val in vals.items()]
            print('%s: %s' % (param, ', '.join(possibilities)))
        
def main():
    sh = Shell()
    define_ctxs(sh)
    define_params(sh)
    define_rules(sh)
    report_findings(sh.execute(['client']))

main()