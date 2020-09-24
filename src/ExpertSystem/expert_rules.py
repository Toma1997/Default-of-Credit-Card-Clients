# Helper function
def eq(x, y):
    if x == 'Not sure':
        return False
    return x == y

# EXPERT SYSTEM DEFINITION

# Decision context
def define_ctxs(shell):                
    shell.define_ctx(Ctx('client', goals=['default_payment_next_month']))

def yes_no_param(shell, param, ask_first = False):
    shell.define_param(Param(param, 'client', enum=['no', 'yes'], ask_first= ask_first))

# Parameters (attributes)
def define_params(shell):
    
    # Client parameters
    yes_no_param(shell, 'PAY_0 <= 1.5', True)
    yes_no_param(shell, 'PAY_2 <= 1.5')
    yes_no_param(shell, 'PAY_AMT3 <= 810.5')
    yes_no_param(shell, 'BILL_AMT1 <= 530')
    yes_no_param(shell, 'PAY_AMT4 <= 999')
    yes_no_param(shell, 'LIMIT_BAL <= 185000')
    yes_no_param(shell, 'PAY_4 <= 0.5')
    yes_no_param(shell, 'LIMIT_BAL <= 75000')
    yes_no_param(shell, 'PAY_AMT2 <= 2187.5')
    yes_no_param(shell, 'PAY_5 <= 1')
    yes_no_param(shell, 'LIMIT_BAL <= 255000')
    yes_no_param(shell, 'PAY_AMT6 <= 7367')
    yes_no_param(shell, 'AGE <= 34.5')
    yes_no_param(shell, 'PAY_AMT5 <= 4.5')
    yes_no_param(shell, 'PAY_AMT3 <= 1435')
    yes_no_param(shell, 'PAY_AMT6 <= 1950')
    yes_no_param(shell, 'PAY_6 <= 1')
    yes_no_param(shell, 'BILL_AMT1 <= 2212')
    yes_no_param(shell, 'PAY_AMT2 <= 1493.5')
    yes_no_param(shell, 'PAY_AMT1 <= 966')
    yes_no_param(shell, 'BILL_AMT1 <= 27839.5')
    yes_no_param(shell, 'LIMIT_BAL <= 15000')
    yes_no_param(shell, 'BILL_AMT6 <= 29585')
    yes_no_param(shell, 'PAY_AMT3 <= 11779')
    yes_no_param(shell, 'PAY_2 <= 3.5')
    yes_no_param(shell, 'BILL_AMT6 <= 894')
    yes_no_param(shell, 'AGE <= 38.5')

    # Class paramters (decisios) - default payment next month prediciton 
    yes_no_param(shell, 'default_payment_next_month')

# Production rules
def define_rules(shell):

    # Rules
    shell.define_rule(Rule(1, [('PAY_0 <= 1.5', 'client', eq, 'yes'), 
                               ('PAY_2 <= 1.5', 'client', eq, 'yes'),
                               ('PAY_AMT3 <= 810.5', 'client', eq, 'yes'),
                               ('BILL_AMT1 <= 530', 'client', eq, 'yes'),
                               ('PAY_AMT4 <= 999', 'client', eq, 'yes')],
                              [('default_payment_next_month', 'client', eq, 'NO')], 1.0))

    shell.define_rule(Rule(2, [('PAY_0 <= 1.5', 'client', eq, 'yes'), 
                               ('PAY_2 <= 1.5', 'client', eq, 'yes'),
                               ('PAY_AMT3 <= 810.5', 'client', eq, 'yes'),
                               ('BILL_AMT1 <= 530', 'client', eq, 'yes'),
                               ('PAY_AMT4 <= 999', 'client', eq, 'no')],
                              [('default_payment_next_month', 'client', eq, 'NO')], 1.0))


    shell.define_rule(Rule(3, [('PAY_0 <= 1.5', 'client', eq, 'yes'), 
                               ('PAY_2 <= 1.5', 'client', eq, 'yes'),
                               ('PAY_AMT3 <= 810.5', 'client', eq, 'yes'),
                               ('BILL_AMT1 <= 530', 'client', eq, 'no'),
                               ('LIMIT_BAL <= 185000', 'client', eq, 'yes')],
                              [('default_payment_next_month', 'client', eq, 'NO')], 1.0))

    shell.define_rule(Rule(4, [('PAY_0 <= 1.5', 'client', eq, 'yes'), 
                               ('PAY_2 <= 1.5', 'client', eq, 'yes'),
                               ('PAY_AMT3 <= 810.5', 'client', eq, 'yes'),
                               ('BILL_AMT1 <= 530', 'client', eq, 'no'),
                               ('LIMIT_BAL <= 185000', 'client', eq, 'no')],
                              [('default_payment_next_month', 'client', eq, 'NO')], 1.0))

    shell.define_rule(Rule(5, [('PAY_0 <= 1.5', 'client', eq, 'yes'), 
                               ('PAY_2 <= 1.5', 'client', eq, 'yes'),
                               ('PAY_AMT3 <= 810.5', 'client', eq, 'no'),
                               ('PAY_4 <= 0.5', 'client', eq, 'yes'),
                               ('LIMIT_BAL <= 75000', 'client', eq, 'yes')],
                              [('default_payment_next_month', 'client', eq, 'NO')], 1.0))

    shell.define_rule(Rule(6, [('PAY_0 <= 1.5', 'client', eq, 'yes'), 
                               ('PAY_2 <= 1.5', 'client', eq, 'yes'),
                               ('PAY_AMT3 <= 810.5', 'client', eq, 'no'),
                               ('PAY_4 <= 0.5', 'client', eq, 'yes'),
                               ('LIMIT_BAL <= 75000', 'client', eq, 'no')],
                              [('default_payment_next_month', 'client', eq, 'NO')], 1.0))

    shell.define_rule(Rule(7, [('PAY_0 <= 1.5', 'client', eq, 'yes'), 
                               ('PAY_2 <= 1.5', 'client', eq, 'yes'),
                               ('PAY_AMT3 <= 810.5', 'client', eq, 'no'),
                               ('PAY_4 <= 0.5', 'client', eq, 'no'),
                               ('PAY_AMT2 <= 2187.5', 'client', eq, 'yes')],
                              [('default_payment_next_month', 'client', eq, 'YES')], 1.0))

    shell.define_rule(Rule(8, [('PAY_0 <= 1.5', 'client', eq, 'yes'), 
                               ('PAY_2 <= 1.5', 'client', eq, 'yes'),
                               ('PAY_AMT3 <= 810.5', 'client', eq, 'no'),
                               ('PAY_4 <= 0.5', 'client', eq, 'no'),
                               ('PAY_AMT2 <= 2187.5', 'client', eq, 'no')],
                              [('default_payment_next_month', 'client', eq, 'NO')], 1.0))


    shell.define_rule(Rule(9, [('PAY_0 <= 1.5', 'client', eq, 'yes'), 
                               ('PAY_2 <= 1.5', 'client', eq, 'no'),
                               ('PAY_5 <= 1', 'client', eq, 'yes'),
                               ('LIMIT_BAL <= 255000', 'client', eq, 'yes'),
                               ('PAY_AMT6 <= 7367', 'client', eq, 'yes')],
                              [('default_payment_next_month', 'client', eq, 'NO')], 1.0))

    shell.define_rule(Rule(10, [('PAY_0 <= 1.5', 'client', eq, 'yes'), 
                               ('PAY_2 <= 1.5', 'client', eq, 'no'),
                               ('PAY_5 <= 1', 'client', eq, 'yes'),
                               ('LIMIT_BAL <= 255000', 'client', eq, 'yes'),
                               ('PAY_AMT6 <= 7367', 'client', eq, 'no')],
                              [('default_payment_next_month', 'client', eq, 'NO')], 1.0))

    shell.define_rule(Rule(11, [('PAY_0 <= 1.5', 'client', eq, 'yes'), 
                               ('PAY_2 <= 1.5', 'client', eq, 'no'),
                               ('PAY_5 <= 1', 'client', eq, 'yes'),
                               ('LIMIT_BAL <= 255000', 'client', eq, 'no'),
                               ('AGE <= 34.5', 'client', eq, 'yes')],
                              [('default_payment_next_month', 'client', eq, 'NO')], 1.0))

    shell.define_rule(Rule(12, [('PAY_0 <= 1.5', 'client', eq, 'yes'), 
                               ('PAY_2 <= 1.5', 'client', eq, 'no'),
                               ('PAY_5 <= 1', 'client', eq, 'yes'),
                               ('LIMIT_BAL <= 255000', 'client', eq, 'no'),
                               ('AGE <= 34.5', 'client', eq, 'no')],
                              [('default_payment_next_month', 'client', eq, 'NO')], 1.0))

    shell.define_rule(Rule(13, [('PAY_0 <= 1.5', 'client', eq, 'yes'), 
                               ('PAY_2 <= 1.5', 'client', eq, 'no'),
                               ('PAY_5 <= 1', 'client', eq, 'no'),
                               ('PAY_AMT5 <= 4.5', 'client', eq, 'yes'),
                               ('PAY_AMT3 <= 1435', 'client', eq, 'yes')],
                              [('default_payment_next_month', 'client', eq, 'YES')], 1.0))

    shell.define_rule(Rule(14, [('PAY_0 <= 1.5', 'client', eq, 'yes'), 
                               ('PAY_2 <= 1.5', 'client', eq, 'no'),
                               ('PAY_5 <= 1', 'client', eq, 'no'),
                               ('PAY_AMT5 <= 4.5', 'client', eq, 'yes'),
                               ('PAY_AMT3 <= 1435', 'client', eq, 'no')],
                              [('default_payment_next_month', 'client', eq, 'YES')], 1.0))

    shell.define_rule(Rule(15, [('PAY_0 <= 1.5', 'client', eq, 'yes'), 
                               ('PAY_2 <= 1.5', 'client', eq, 'no'),
                               ('PAY_5 <= 1', 'client', eq, 'no'),
                               ('PAY_AMT5 <= 4.5', 'client', eq, 'no'),
                               ('PAY_AMT6 <= 1435', 'client', eq, 'yes')],
                              [('default_payment_next_month', 'client', eq, 'YES')], 1.0))

    shell.define_rule(Rule(16, [('PAY_0 <= 1.5', 'client', eq, 'yes'), 
                               ('PAY_2 <= 1.5', 'client', eq, 'no'),
                               ('PAY_5 <= 1', 'client', eq, 'no'),
                               ('PAY_AMT5 <= 4.5', 'client', eq, 'no'),
                               ('PAY_AMT6 <= 1435', 'client', eq, 'no')],
                              [('default_payment_next_month', 'client', eq, 'NO')], 1.0))

    shell.define_rule(Rule(17, [('PAY_0 <= 1.5', 'client', eq, 'no'), 
                               ('PAY_6 <= 1', 'client', eq, 'yes'),
                               ('BILL_AMT1 <= 2212', 'client', eq, 'yes'),
                               ('PAY_AMT2 <= 1493.5', 'client', eq, 'yes'),
                               ('PAY_AMT1 <= 966', 'client', eq, 'yes')],
                              [('default_payment_next_month', 'client', eq, 'NO')], 1.0))

    shell.define_rule(Rule(18, [('PAY_0 <= 1.5', 'client', eq, 'no'), 
                               ('PAY_6 <= 1', 'client', eq, 'yes'),
                               ('BILL_AMT1 <= 2212', 'client', eq, 'yes'),
                               ('PAY_AMT2 <= 1493.5', 'client', eq, 'yes'),
                               ('PAY_AMT1 <= 966', 'client', eq, 'no')],
                              [('default_payment_next_month', 'client', eq, 'YES')], 1.0))

    shell.define_rule(Rule(19, [('PAY_0 <= 1.5', 'client', eq, 'no'), 
                               ('PAY_6 <= 1', 'client', eq, 'yes'),
                               ('BILL_AMT1 <= 2212', 'client', eq, 'yes'),
                               ('PAY_AMT2 <= 1493.5', 'client', eq, 'no')],
                              [('default_payment_next_month', 'client', eq, 'NO')], 1.0))

    shell.define_rule(Rule(20, [('PAY_0 <= 1.5', 'client', eq, 'no'), 
                               ('PAY_6 <= 1', 'client', eq, 'yes'),
                               ('BILL_AMT1 <= 2212', 'client', eq, 'no'),
                               ('BILL_AMT1 <= 27839.5', 'client', eq, 'yes'),
                               ('LIMIT_BAL <= 15000', 'client', eq, 'yes')],
                              [('default_payment_next_month', 'client', eq, 'NO')], 1.0))

    shell.define_rule(Rule(21, [('PAY_0 <= 1.5', 'client', eq, 'no'), 
                               ('PAY_6 <= 1', 'client', eq, 'yes'),
                               ('BILL_AMT1 <= 2212', 'client', eq, 'no'),
                               ('BILL_AMT1 <= 27839.5', 'client', eq, 'yes'),
                               ('LIMIT_BAL <= 15000', 'client', eq, 'no')],
                              [('default_payment_next_month', 'client', eq, 'YES')], 1.0))

    shell.define_rule(Rule(22, [('PAY_0 <= 1.5', 'client', eq, 'no'), 
                               ('PAY_6 <= 1', 'client', eq, 'yes'),
                               ('BILL_AMT1 <= 2212', 'client', eq, 'no'),
                               ('BILL_AMT1 <= 27839.5', 'client', eq, 'no'),
                               ('BILL_AMT6 <= 29585', 'client', eq, 'yes')],
                              [('default_payment_next_month', 'client', eq, 'YES')], 1.0))

    shell.define_rule(Rule(23, [('PAY_0 <= 1.5', 'client', eq, 'no'), 
                               ('PAY_6 <= 1', 'client', eq, 'yes'),
                               ('BILL_AMT1 <= 2212', 'client', eq, 'no'),
                               ('BILL_AMT1 <= 27839.5', 'client', eq, 'no'),
                               ('BILL_AMT6 <= 29585', 'client', eq, 'no')],
                              [('default_payment_next_month', 'client', eq, 'YES')], 1.0))

    shell.define_rule(Rule(24, [('PAY_0 <= 1.5', 'client', eq, 'no'), 
                               ('PAY_6 <= 1', 'client', eq, 'no'),
                               ('PAY_AMT3 <= 11779', 'client', eq, 'yes'),
                               ('PAY_2 <= 3.5', 'client', eq, 'yes'),
                               ('BILL_AMT6 <= 894', 'client', eq, 'yes')],
                              [('default_payment_next_month', 'client', eq, 'YES')], 1.0))

    shell.define_rule(Rule(25, [('PAY_0 <= 1.5', 'client', eq, 'no'), 
                               ('PAY_6 <= 1', 'client', eq, 'no'),
                               ('PAY_AMT3 <= 11779', 'client', eq, 'yes'),
                               ('PAY_2 <= 3.5', 'client', eq, 'yes'),
                               ('BILL_AMT6 <= 894', 'client', eq, 'no')],
                              [('default_payment_next_month', 'client', eq, 'YES')], 1.0))

    shell.define_rule(Rule(26, [('PAY_0 <= 1.5', 'client', eq, 'no'), 
                               ('PAY_6 <= 1', 'client', eq, 'no'),
                               ('PAY_AMT3 <= 11779', 'client', eq, 'yes'),
                               ('PAY_2 <= 3.5', 'client', eq, 'no'),
                               ('AGE <= 38.5', 'client', eq, 'yes')],
                              [('default_payment_next_month', 'client', eq, 'NO')], 1.0))

    shell.define_rule(Rule(27, [('PAY_0 <= 1.5', 'client', eq, 'no'), 
                               ('PAY_6 <= 1', 'client', eq, 'no'),
                               ('PAY_AMT3 <= 11779', 'client', eq, 'yes'),
                               ('PAY_2 <= 3.5', 'client', eq, 'no'),
                               ('AGE <= 38.5', 'client', eq, 'no')],
                              [('default_payment_next_month', 'client', eq, 'YES')], 1.0))

    shell.define_rule(Rule(28, [('PAY_0 <= 1.5', 'client', eq, 'no'), 
                               ('PAY_6 <= 1', 'client', eq, 'no'),
                               ('PAY_AMT3 <= 11779', 'client', eq, 'no')],
                              [('default_payment_next_month', 'client', eq, 'NO')], 1.0))
    
    # Default rule
    shell.define_rule(Rule(29, [], [('default_payment_next_month', 'client', eq, 'NO')], 0.0))
    
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