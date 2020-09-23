# Helper function
def eq(x, y):
    if x == 'Not sure':
        return False
    return x == y

# EXPERT SYSTEM DEFINITION

# Decision context
def define_ctxs(shell):
    shell.define_ctx(Ctx('client', ['LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_0', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 
                                'BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']))
    shell.define_ctx(Ctx('target', goals=['default_payment_next_month']))

def yes_no_param(shell, param, ask_first = False):
    shell.define_param(Param(param, 'client', enum=['no', 'yes']), ask_first = ask_first)

# Parameters (attributes)
def define_params(shell):
    
    # Client parameters

    yes_no_param(shell, 'LIMIT_BAL', True)
    yes_no_param(shell, 'SEX', True)
    yes_no_param(shell, 'EDUCATION', True)
    yes_no_param(shell, 'MARRIAGE', True)
    yes_no_param(shell, 'AGE', True)
    yes_no_param(shell, 'PAY_0')
    yes_no_param(shell, 'PAY_2')
    yes_no_param(shell, 'PAY_3')
    yes_no_param(shell, 'PAY_4')
    yes_no_param(shell, 'PAY_5')
    yes_no_param(shell, 'PAY_6')

    # Class paramters (decisios) - default payment next month prediciton 
    yes_no_param(shell, 'default_payment_next_month')

# Production rules
def define_rules(shell):
    # Rules
    shell.define_rule(Rule(1, [('sex', 'client', eq, 'male')], [('default_payment_next_month', 'client', eq, 'yes')], 0.65))
    shell.define_rule(Rule(2, [('marriage', 'client', eq, 'yes')], [('default_payment_next_month', 'client', eq, 'no')], 0.79))
    shell.define_rule(Rule(3, [('education', 'client', eq, 'high school')], [('default_payment_next_month', 'client', eq, 'yes')], 0.75))
    
    # Default rule
    shell.define_rule(Rule(4, [], [('default_payment_next_month', 'client', eq, 'no')], 0.0))
    
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